const sqlite3 = require('sqlite3').verbose();
const readline = require('readline');

// Conecta ao banco
const db = new sqlite3.Database('./BD/tblClienteJS.db');

// Interface para entrada de dados
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function cadastrarCliente() {
  rl.question("Nome: ", (nome) => {
    rl.question("Altura (ex: 1.75): ", (altura) => {
      rl.question("E-mail: ", (email) => {
        rl.question("Data de nascimento (dd/mm/aaaa): ", (nascimento) => {
          rl.question("Data de cadastro (dd/mm/aaaa): ", (cadastro) => {
            const [diaNasc, mesNasc, anoNasc] = nascimento.split("/");
            const dataCadastro = cadastro;

            db.run(`
              INSERT INTO tbCliente (nmCliente, altura, email, mes_aniversario, ano_aniversario, data_cadastro)
              VALUES (?, ?, ?, ?, ?, ?)
            `, [nome, altura, email, mesNasc, anoNasc, dataCadastro], function(err) {
              if (err) {
                console.error("Erro ao inserir cliente:", err.message);
              } else {
                console.log("✅ Cliente inserido com sucesso!");
              }

              rl.question("Deseja inserir outro cliente? (S para sim): ", (resposta) => {
                if (resposta.toUpperCase() === "S") {
                  cadastrarCliente();
                } else {
                  rl.close();
                  db.close();
                  console.log("Aplicativo finalizado. Obrigado!");
                }
              });
            });
          });
        });
      });
    });
  });
}

cadastrarCliente();