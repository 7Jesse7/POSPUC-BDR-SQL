import sqlalchemy as sa

engine = sa.create_engine("sqlite:///BD//vendas.db")  # variável para criar engrenagem para criar e conectar ao bd

import sqlalchemy.orm as orm    # para poder utilizar os métodos de orm do sqlalchemy


# Método para declarar o mapeamento dos objetos dentro do banco de dados
# que permite a criação de classe, para criação de tabelas e atributos
base = orm.declarative_base()

#Criando tabela cliente advinda do modelo lógico relacional
class cliente(base):
    __tablename__ = "cliente"  # Nomeando a tabela

    cpf = sa.Column(sa.CHAR(14), primary_key=True, index=True)
    nome = sa.Column(sa.VARCHAR(100), nullable=False)
    email= sa.Column(sa.VARCHAR(50), nullable=False)
    genero = sa.Column(sa.CHAR(1))
    salario = sa.Column(sa.DECIMAL(10,2))
    dia_mes_aniversario = sa.Column(sa.VARCHAR(5))
    bairro = sa.Column(sa.VARCHAR(50))
    cidade = sa.Column(sa.VARCHAR(50))
    uf = sa.Column(sa.CHAR(2))

#Tabela Fornecedor
class fornecedor(base):
    __tablename__ = "fornecedor" 

    registro_fornecedor = sa.Column(sa.INTEGER, primary_key=True, index=True)
    nome_fantasia = sa.Column(sa.VARCHAR(50), nullable=False)
    razao_social = sa.Column(sa.VARCHAR(100), nullable=False)
    cidade = sa.Column(sa.VARCHAR(50), nullable=False)
    uf = sa.Column(sa.CHAR(2), nullable=False)

#Tabela Produto
class produto(base):
    __tablename__ = "produto" 

    codBarras = sa.Column(sa.INTEGER, primary_key=True, index=True)
    registro_fornecedor = sa.Column(sa.INTEGER, sa.ForeignKey("fornecedor.registro_fornecedor", ondelete="NO ACTION", onupdate="CASCADE"), index=True) # chave estrangeira e sua localização no código, bem como a restrição da entidade referencial
    dscProduto = sa.Column(sa.VARCHAR(100), nullable=False)
    genero = sa.Column(sa.CHAR(1))


#Tabela Vendedor
class produto(base):
    __tablename__ = "vendedor" 

    registro_vendedor = sa.Column(sa.INTEGER, primary_key=True, index=True)
    cpf = sa.Column(sa.CHAR(14), nullable=False)
    nome = sa.Column(sa.VARCHAR(100), nullable=False)
    email= sa.Column(sa.VARCHAR(50), nullable=False)
    genero = sa.Column(sa.CHAR(1))

#Tabela Vendas
class produto(base):
    __tablename__ = "vendas" 

    idTransacao = sa.Column(sa.INTEGER, primary_key=True, index=True)
    cpf = sa.Column(sa.CHAR(14), sa.ForeignKey("cliente.cpf", ondelete="NO ACTION", onupdate="CASCADE"), index=True)
    registro_vendedor = sa.Column(sa.INTEGER, sa.ForeignKey("vendedor.registro_vendedor", ondelete="NO ACTION", onupdate="CASCADE"), index=True)
    codBarras = sa.Column(sa.INTEGER, sa.ForeignKey("produto.codBarras", ondelete="NO ACTION", onupdate="CASCADE"), index=True)


try:
    base.metadata.create_all(engine)  # faz a criação das tabelas
    print("Tabelas Criadas com Sucesso!")
except ValueError:
    ValueError()