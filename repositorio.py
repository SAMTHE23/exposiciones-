from sqlalchemy import create_engine, Column, Integer, String, select
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///:memory:", echo=True)
Base = declarative_base()

class Estudiante(Base):
    __tablename__ = "estudiantes"
    id = Column(Integer, primary_key=True)
    nombre = Column(String)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

class EstudianteRepository:
    def __init__(self, session):
        self.session = session

    def guardar(self, nombre):
        self.session.add(Estudiante(nombre=nombre))
        self.session.commit()

    def consultar(self):
        return self.session.scalars(select(Estudiante)).all()

with Session() as session:
    repo = EstudianteRepository(session)
    repo.guardar("Samuel")
    for e in repo.consultar():
        print(e.id, e.nombre)
    