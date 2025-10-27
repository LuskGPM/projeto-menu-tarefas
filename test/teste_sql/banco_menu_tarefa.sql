create schema if not exists teste_menu_tarefa;

use menu_tarefa;

CREATE TABLE IF NOT EXISTS usuario(
id INT PRIMARY KEY AUTO_INCREMENT,
nome VARCHAR(60) NOT NULL,
nickname VARCHAR(90) NOT NULL UNIQUE,
senha_hash VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS categoria(
id INT PRIMARY KEY AUTO_INCREMENT,
nome VARCHAR(60) NOT NULL,
cor VARCHAR(7) NOT NULL
);

CREATE TABLE IF NOT EXISTS tarefa(
id INT PRIMARY KEY AUTO_INCREMENT,
titulo VARCHAR(60) NOT NULL,
descricao TEXT,
status ENUM('pendente', 'em_andamento', 'concluida') NOT NULL, 
prioridade ENUM('baixa','media','alta') NOT NULL,
categoria_id INT,
data_criacao DATETIME DEFAULT CURRENT_TIMESTAMP,
data_atualizacao DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
FOREIGN KEY(categoria_id) REFERENCES categoria(id) ON DELETE SET NULL
);
