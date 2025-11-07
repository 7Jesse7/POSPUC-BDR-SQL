const fs = require('fs');
const path = require('path');
const csv = require('csv-parser');
const xlsx = require('xlsx');
const { sequelize, Produto, Vendedor } = require('./vendasSqlConnect');

const endereco = path.join(__dirname, '../Dados_Exemplo/');

// ✅ Inserção de produtos via Excel
async function inserirProdutos() {
  const workbook = xlsx.readFile(endereco + 'produto1.xlsx');
  const sheet = workbook.Sheets[workbook.SheetNames[0]];
  const rawData = xlsx.utils.sheet_to_json(sheet, { header: 1 });

  const linhas = rawData.slice(1); // Ignora cabeçalhos

  const produtos = linhas.map((linha) => ({
    codBarras: linha[0],
    dscProduto: `Prd${linha[0]}`,
    genero: linha[1]
  }));

  await Produto.bulkCreate(produtos);
  console.log('✅ Produtos inseridos');
}

// ✅ Leitura de vendedores do CSV
function lerVendedoresCSV() {
  return new Promise((resolve, reject) => {
    const vendedores = [];
    fs.createReadStream(endereco + 'vendedor.csv')
      .pipe(csv({ separator: ';' }))
      .on('data', (row) => vendedores.push(row))
      .on('end', () => resolve(vendedores))
      .on('error', (err) => reject(err));
  });
}

// ✅ Inserção de vendedores no banco
async function inserirVendedores() {
  const vendedores = await lerVendedoresCSV();

  await Vendedor.destroy({ where: {}, truncate: true });

  for (const v of vendedores) {
    await Vendedor.create({
      registro_vendedor: parseInt(v.registro_vendedor),
      cpf: v.cpf,
      nome: v.nome,
      email: v.email,
      genero: v.genero
    });
  }

  console.log('✅ Vendedores inseridos');
}

// ✅ Execução sequencial
async function executar() {
  try {
    await sequelize.sync({ force: false });
    console.log('✅ Tabelas sincronizadas');

    await inserirProdutos();
    await inserirVendedores();
  } catch (err) {
    console.error('❌ Erro geral:', err);
  } finally {
    await sequelize.close();
  }
}

executar();