from db_models import Base, admin,riwayat_diagnosa,diagnosa,model_algoritma,dataTrain
from conn import engine

print('create tabless')
Base.metadata.create_all(bind=engine)