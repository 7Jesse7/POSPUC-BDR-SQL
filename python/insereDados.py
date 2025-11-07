from sqlalchemy import create_engine, Column, Integer, String, CHAR, DateTime, Numeric
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

# Conexão com SQLite
engine = create_engine("sqlite:///BD/tbCliente.db")
Session = sessionmaker(bind=engine)
session = Session()

# Modelo
Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'tbCliente'

    idCliente = Column(Integer, primary_key=True)
    nmCliente = Column(String(255), nullable=False)
    altura = Column(Numeric(10, 2), nullable=False)
    email = Column(String(100), nullable=False)
    mes_aniversario = Column(CHAR(2), nullable=False)
    ano_aniversario = Column(CHAR(4), nullable=False)
    data_cadastro = Column(DateTime, nullable=False)

# Loop de inserção
resposta = "S"
while resposta.upper() == "S":
    print("\n=== Cadastro de Cliente ===")
    nome = input("Nome: ")
    altura = float(input("Altura (ex: 1.75): "))
    email = input("E-mail: ")
    nascimento = input("Data de nascimento (dd/mm/aaaa): ")
    cadastro = input("Data de cadastro (dd/mm/aaaa): ")

    try:
        dt_nasc = datetime.strptime(nascimento, "%d/%m/%Y")
        dt_cad = datetime.strptime(cadastro, "%d/%m/%Y")
    except ValueError:
        print("❌ Formato de data inválido. Use dd/mm/aaaa.")
        continue

    cliente = Cliente(
        nmCliente=nome,
        altura=altura,
        email=email,
        mes_aniversario=f"{dt_nasc.month:02}",
        ano_aniversario=str(dt_nasc.year),
        data_cadastro=dt_cad
    )

    session.add(cliente)
    session.commit()
    print("✅ Cliente inserido com sucesso!")

    resposta = input("Deseja inserir outro cliente? (S para sim): ")

# Exibir dados
exibir = input("\nDeseja exibir os dados cadastrados? (S para sim): ")
if exibir.upper() == "S":
    clientes = session.query(Cliente).all()
    print("\n=== Lista de Clientes ===")
    for c in clientes:
        print(f"{c.idCliente} - {c.nmCliente} | {c.email} | Altura: {c.altura} | Cadastro: {c.data_cadastro.strftime('%d/%m/%Y')}")

session.close()
print("\nAplicativo finalizado. Obrigado!")