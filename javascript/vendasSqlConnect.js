const { Sequelize, DataTypes } = require('sequelize');

// Conexão com SQLite usando vendasJS.db
const sequelize = new Sequelize({
  dialect: 'sqlite',
  storage: './BD/vendasJS.db'
});

// Tabela Cliente
const Cliente = sequelize.define('cliente', {
  cpf: { type: DataTypes.CHAR(14), primaryKey: true },
  nome: { type: DataTypes.STRING(100), allowNull: false },
  email: { type: DataTypes.STRING(50), allowNull: false },
  genero: { type: DataTypes.CHAR(1) },
  salario: { type: DataTypes.DECIMAL(10, 2) },
  dia_mes_aniversario: { type: DataTypes.STRING(5) },
  bairro: { type: DataTypes.STRING(50) },
  cidade: { type: DataTypes.STRING(50) },
  uf: { type: DataTypes.CHAR(2) }
}, {
  tableName: 'cliente',
  timestamps: false,
  freezeTableName: true
});

// Tabela Fornecedor
const Fornecedor = sequelize.define('fornecedor', {
  registro_fornecedor: { type: DataTypes.INTEGER, primaryKey: true },
  nome_fantasia: { type: DataTypes.STRING(50), allowNull: false },
  razao_social: { type: DataTypes.STRING(100), allowNull: false },
  cidade: { type: DataTypes.STRING(50), allowNull: false },
  uf: { type: DataTypes.CHAR(2), allowNull: false }
}, {
  tableName: 'fornecedor',
  timestamps: false,
  freezeTableName: true
});

// Tabela Produto
const Produto = sequelize.define('produto', {
  codBarras: { type: DataTypes.INTEGER, primaryKey: true },
  dscProduto: { type: DataTypes.STRING(100), allowNull: false },
  genero: { type: DataTypes.CHAR(1) }
}, {
  tableName: 'produto',
  timestamps: false,
  freezeTableName: true
});
Produto.belongsTo(Fornecedor, {
  foreignKey: 'registro_fornecedor',
  onDelete: 'NO ACTION',
  onUpdate: 'CASCADE'
});

// Tabela Vendedor
const Vendedor = sequelize.define('vendedor', {
  registro_vendedor: { type: DataTypes.INTEGER, primaryKey: true },
  cpf: { type: DataTypes.CHAR(14), allowNull: false },
  nome: { type: DataTypes.STRING(100), allowNull: false },
  email: { type: DataTypes.STRING(50), allowNull: false },
  genero: { type: DataTypes.CHAR(1) }
}, {
  tableName: 'vendedor',
  timestamps: false,
  freezeTableName: true
});

// Tabela Vendas
const Vendas = sequelize.define('vendas', {
  idTransacao: { type: DataTypes.INTEGER, primaryKey: true }
}, {
  tableName: 'vendas',
  timestamps: false,
  freezeTableName: true
});
Vendas.belongsTo(Cliente, {
  foreignKey: 'cpf',
  onDelete: 'NO ACTION',
  onUpdate: 'CASCADE'
});
Vendas.belongsTo(Vendedor, {
  foreignKey: 'registro_vendedor',
  onDelete: 'NO ACTION',
  onUpdate: 'CASCADE'
});
Vendas.belongsTo(Produto, {
  foreignKey: 'codBarras',
  onDelete: 'NO ACTION',
  onUpdate: 'CASCADE'
});

// Criação das tabelas
sequelize.sync({ force: false })
  .then(() => {
    console.log("✅ Tabelas criadas com sucesso no banco vendasJS.db!");
  })
  .catch((err) => {
    console.error("❌ Erro ao criar tabelas:", err);
  });

// exportando os modelos e o sequelize
module.exports = {
  sequelize,
  Cliente,
  Fornecedor,
  Produto,
  Vendedor,
  Vendas
};