from sqlalchemy import create_engine,text,Integer,VARCHAR,String,Float,BLOB,PickleType,ForeignKey,Text
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column,relationship


class Base(DeclarativeBase):
    pass


db=SQLAlchemy(model_class=Base)

class admin(Base):
    __tablename__ = 'admin'
    id_admin:Mapped[str] = mapped_column(VARCHAR(10),primary_key=True)
    username:Mapped[str] = mapped_column(VARCHAR(30), nullable=False)
    password:Mapped[str] = mapped_column(VARCHAR(20),unique=True)

    models:Mapped["model_algoritma"] = relationship(back_populates="admin")
    data_train:Mapped['dataTrain'] = relationship(back_populates='admin')


class model_algoritma(Base):
    __tablename__ = 'model_algoritma'
    id_model:Mapped[str] = mapped_column(VARCHAR(10),primary_key=True)
    id_admin:Mapped[str] = mapped_column(VARCHAR(10),ForeignKey('admin.id_admin'))
    nama_model:Mapped[str] = mapped_column(String(10),nullable=False)
    data_model:Mapped[str] = mapped_column(PickleType,nullable=False)

    admins_model:Mapped['admin'] = relationship(back_populates='models')

class riwayat_diagnosa(Base):
    __tablename__='riwayat_diagnosa'
    id_riwayat:Mapped[str] = mapped_column(VARCHAR(10),primary_key=True)
    id_diagnosa:Mapped[str] = mapped_column(VARCHAR(10),ForeignKey('diagnosa.id_diagnosa'))
    solusi_diagnosa:Mapped[str] = mapped_column(Text)

    hasilDiagnosa:Mapped['diagnosa'] = relationship(back_populates='riwayat')
    riwayatForTrain:Mapped['dataTrain'] = relationship(back_populates='riwayat_diagnosa')
class diagnosa(Base):
    __tablename__= 'diagnosa'
    id_diagnosa:Mapped[str] = mapped_column(VARCHAR(10),primary_key=True)
    Drugs:Mapped[int] = mapped_column(Integer)
    Age:Mapped[int] = mapped_column(Integer)
    Sex:Mapped[int] = mapped_column(Integer)
    Ascites:Mapped[int] = mapped_column(Integer)
    Hepatomegaly:Mapped[int] = mapped_column(Integer)
    Spiders:Mapped[int] = mapped_column(Integer)
    Bilirubin:Mapped[int] = mapped_column(Integer)
    Cholesterol:Mapped[int] = mapped_column(Integer)
    Albumin:Mapped[int] = mapped_column(Integer)
    Copper:Mapped[int] = mapped_column(Integer)
    Alk_Phos:Mapped[int] = mapped_column(Integer)
    SGOT:Mapped[int] = mapped_column(Integer)
    Trysglicerides:Mapped[int] = mapped_column(Integer)
    Platelets:Mapped[int] = mapped_column(Integer)
    Prothrombin:Mapped[int] = mapped_column(Integer)
    Edema:Mapped[int] = mapped_column(Integer)
    Status:Mapped[int] = mapped_column(Integer)
    Stage:Mapped[int] = mapped_column(Integer)

    riwayat:Mapped['riwayat_diagnosa'] = relationship(back_populates='diagnosa')


class dataTrain(Base):
    __tablename__= 'data_train'
    id_diagnosa:Mapped[str] = mapped_column(VARCHAR(10),primary_key=True)
    id_admin:Mapped[str] = mapped_column(VARCHAR(10),ForeignKey('admin.id_admin'))
    id_riwayat:Mapped[str] = mapped_column(VARCHAR(10),ForeignKey('riwayat_diagnosa.id_riwayat'))
    Drugs:Mapped[int] = mapped_column(Integer)
    Age:Mapped[int] = mapped_column(Integer)
    Sex:Mapped[int] = mapped_column(Integer)
    Ascites:Mapped[int] = mapped_column(Integer)
    Hepatomegaly:Mapped[int] = mapped_column(Integer)
    Spiders:Mapped[int] = mapped_column(Integer)
    Bilirubin:Mapped[int] = mapped_column(Integer)
    Cholesterol:Mapped[int] = mapped_column(Integer)
    Albumin:Mapped[int] = mapped_column(Integer)
    Copper:Mapped[int] = mapped_column(Integer)
    Alk_Phos:Mapped[int] = mapped_column(Integer)
    SGOT:Mapped[int] = mapped_column(Integer)
    Trysglicerides:Mapped[int] = mapped_column(Integer)
    Platelets:Mapped[int] = mapped_column(Integer)
    Prothrombin:Mapped[int] = mapped_column(Integer)
    Edema:Mapped[int] = mapped_column(Integer)
    Status:Mapped[int] = mapped_column(Integer)
    Stage:Mapped[int] = mapped_column(Integer)

    admin_dataTrain:Mapped['admin'] = relationship(back_populates='data_train') 
    newTrainData:Mapped['riwayat_diagnosa'] = relationship(back_populates='riwayatForTrain')   
