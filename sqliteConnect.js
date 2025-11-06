const sqlite3 = require('sqlite3').verbose();

// Conecta ou cria o banco
const db = new sqlite3.Database('./BD/tblClienteJS.db');

// Cria a tabela
db.serialize(() => {
  db.run(`
    CREATE TABLE IF NOT EXISTS tbCliente (
      idCliente INTEGER PRIMARY KEY AUTOINCREMENT,
      nmCliente TEXT NOT NULL,
      altura REAL NOT NULL,
      email TEXT NOT NULL,
      mes_aniversario TEXT NOT NULL,
      ano_aniversario TEXT NOT NULL,
      data_cadastro TEXT NOT NULL
    )
  `, (err) => {
    if (err) {
      console.error("Erro ao criar tabela:", err.message);
    } else {
      console.log("✅ Tabela tbCliente criada com sucesso!");
    }
  });
});

// Fecha conexão
db.close();