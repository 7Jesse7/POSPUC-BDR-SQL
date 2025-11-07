import sqlalchemy as sa
import sqlalchemy.orm as orm 

engine = sa.create_engine("sqlite:///BD//ocorrencias.db")  
  
base = orm.declarative_base()

# Tabelas Delegacia de Policia
class dp(base):
    __tablename__ = "tbDP"  

    codDP = sa.Column(sa.INTEGER, primary_key=True, index=True)
    nome = sa.Column(sa.VARCHAR(100), nullable=False)
    endereco = sa.Column(sa.VARCHAR(255), nullable=False)


# Tabela Responsavel Delegacia de Policia
class responsaveldp(base):
    __tablename__ = "tbResponsavelDP" 

    codDP = sa.Column(sa.INTEGER, primary_key=True, index=True)
    delegado = sa.Column(sa.VARCHAR(100), nullable=False)


#Tabela Municipio Delegacia
class municipio(base):
    __tablename__ = "tbMunicipio" 

    codBarras = sa.Column(sa.INTEGER, primary_key=True, index=True)
    codIBGE = sa.Column(sa.INTEGER, primary_key=True, index=True)
    municipio = sa.Column(sa.VARCHAR(100), nullable=False)
    regiao = sa.Column(sa.VARCHAR(25), nullable=False)


#Tabela Ocorrencias criada por último por conter as FK
class ocorrencia(base):
    __tablename__ = "tbOcorrencias" 

    idRegistro = sa.Column(sa.INTEGER, primary_key=True, index=True)
    codDP = sa.Column(sa.INTEGER, sa.ForeignKey("tbDP.codDP", ondelete="NO ACTION", onupdate="CASCADE"), index=True)
    codIBGE = sa.Column(sa.INTEGER, sa.ForeignKey("tbMunicipio.codIBGE", ondelete="NO ACTION", onupdate="CASCADE"), index=True)
    ano = sa.Column(sa.CHAR(4), nullable=False)
    mes = sa.Column(sa.CHAR(2), nullable=False)
    ocorrencias = sa.Column(sa.VARCHAR(100), nullable=False)
    qtde = sa.Column(sa.INTEGER, nullable=False)


#criando a tabela
try:          #tratamento de exceção 
    base.metadata.create_all(engine) # criar todas as classes na estrutura da base declarativa do banco definido na engine
    print("Tabelas criadas com sucesso")
except ValueError:
    ValueError("Não foi possível criar as tabelas!")