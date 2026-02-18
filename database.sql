CREATE DATABASE IF NOT EXISTS performance_analytics;
USE performance_analytics;

CREATE TABLE IF NOT EXISTS jogos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS sessoes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    jogo_id INT,
    data_sessao DATE DEFAULT CURRENT_DATE,
    horas_jogadas FLOAT,
    fps_medio INT,
    stutter BOOLEAN,
    config_grafica VARCHAR(50),
    horas_sono FLOAT,
    nivel_foco INT CHECK (nivel_foco BETWEEN 1 AND 3),
    desempenho_percebido INT CHECK (desempenho_percebido BETWEEN 1 AND 3),
    FOREIGN KEY (jogo_id) REFERENCES jogos(id)
);