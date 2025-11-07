import sqlalchemy as sa
from sqlalchemy.orm import declarative_base, sessionmaker

# Corrigido: import moderno do declarative_base
Base = declarative_base()

# Conexão com SQLite
engine = sa.create_engine("sqlite:///BD/tbCliente.db")

# Sessão
Session = sessionmaker(bind=engine)
session = Session()

# Modelo
class User(Base):
    __tablename__ = 'tbCliente'

    idCliente = sa.Column(sa.Integer, primary_key=True)
    nmCliente = sa.Column(sa.String(255), nullable=False)
    altura = sa.Column(sa.Numeric(10, 2), nullable=False)
    email = sa.Column(sa.String(100), nullable=False)
    mes_aniversario = sa.Column(sa.CHAR(2), nullable=False)
    ano_aniversario = sa.Column(sa.CHAR(4), nullable=False)
    data_cadastro = sa.Column(sa.DateTime, nullable=False)

# Criação do banco
Base.metadata.create_all(engine)
print("Banco de Dados criado!")
