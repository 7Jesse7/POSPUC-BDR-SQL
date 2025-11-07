import pandas as pd

endereco = "C:\\Users\\jesse\\OneDrive\\Documentos\\Desenvolvimento Full Stack\\PUCPOS-BDR-SQL\\Dados_Exemplo\\"

vendedor = pd.read_csv(endereco + "vendedor.csv", sep=";")

tbVendedor = pd.DataFrame(vendedor)  # transformando os dados de vendedor em um dataframe

import sqlalchemy as sa

engine = sa.create_engine("sqlite:///BD/vendas.db")

import sqlalchemy.orm as orm

# Conectando ao banco de dados, através da abertura de uma sessão para esse BD
sessao = orm.sessionmaker(bind=engine) # bind significa ligar
sessao = sessao()

# importando as classes do código que contém as tabelas
import vendas as vd

# criando o algoritmo de inserção de dados quando precisa manipular pontualmente cada dado

for i in range (len(tbVendedor)):
    dados_vendedor = vd.vendedor(
                                registro_vendedor = int(tbVendedor['registro_vendedor'][i]),
                                cpf = tbVendedor["cpf"][i],
                                nome = tbVendedor["nome"] [i],
                                genero = tbVendedor["genero"] [i],
                                email = tbVendedor["email"] [i]
                                )
    
    try:                            # inserindo os dados    
        sessao.add(dados_vendedor)  # add na sessao aberta
        sessao.commit()             # confirmando a transação de inserção do dado
    except ValueError:
        ValueError()

print("Dados inseridos na tbVendedor")