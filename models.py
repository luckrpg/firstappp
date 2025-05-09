from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create the database engine
engine = create_engine('sqlite:///aplicativos.db', echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)


class Profissao(Base):
    __tablename__ = 'profissoes'

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    salario = Column(Float, nullable=False)

    def __repr__(self):
        return f"Profissão: {self.nome} - Salário: R$ {self.salario}"


class Livro(Base):
    __tablename__ = 'livros'

    id = Column(Integer, primary_key=True)
    titulo = Column(String(100), nullable=False)
    autor = Column(String(100), nullable=False)
    ano = Column(String(20))

    def __repr__(self):
        return f"{self.titulo} - {self.autor} ({self.ano})"


def create_tables():
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    create_tables()
