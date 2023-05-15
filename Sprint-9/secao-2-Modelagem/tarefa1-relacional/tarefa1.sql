-- Criar tabela tb_cliente
CREATE TABLE tb_cliente (
  idCliente INTEGER,
  nomeCliente VARCHAR(100),
  cidadeCliente VARCHAR(40),
  estadoCliente VARCHAR(40),
  paisCliente VARCHAR(40),
  PRIMARY KEY (idCliente)
);

-- Inserir dados da tabela tb_locacao na tabela tb_cliente
INSERT INTO tb_cliente (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente)
SELECT DISTINCT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM tb_locacao;



-- Criação da tabela tb_vendedor
CREATE TABLE tb_vendedor (
  idVendedor INTEGER PRIMARY KEY,
  nomeVendedor VARCHAR(15),
  sexoVendedor SMALLINT,
  estadoVendedor VARCHAR(40)
);

-- Copiar dados da tabela original para a tabela tb_vendedor
INSERT INTO tb_vendedor (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor)
SELECT DISTINCT idVendedor, nomeVendedor, sexoVendedor, estadoVendedor
FROM tb_locacao;


-- Criação da tabela tb_carro
CREATE TABLE tb_carro (
  idCarro INTEGER PRIMARY KEY,
  marcaCarro VARCHAR(80),
  modeloCarro VARCHAR(80),
  anoCarro INT,
  classiCarro VARCHAR(50)

);

-- Copiar dados da tabela original para a tabela tb_carro
INSERT INTO tb_carro (idCarro, marcaCarro, modeloCarro, anoCarro, classiCarro)
SELECT DISTINCT idCarro, marcaCarro, modeloCarro, anoCarro, classiCarro
FROM tb_locacao;

-- Criação da tabela tb_combustivel
CREATE TABLE tb_combustivel (
  idCombustivel INTEGER PRIMARY KEY,
  tipoCombustivel VARCHAR(20)
);

-- Copiar dados únicos da coluna idCombustivel e tipoCombustivel para a tabela tb_combustivel
INSERT INTO tb_combustivel (idCombustivel, tipoCombustivel)
SELECT DISTINCT idCombustivel, tipoCombustivel
FROM tb_locacao;



-- Criação da tabela tb_locacao_normalizada
CREATE TABLE tb_locacao_normalizada (
  idLocacao INTEGER PRIMARY KEY,
  idCliente INTEGER,
  idVendedor INTEGER,
  idCombustivel INTEGER,
  idCarro INTEGER,
  kmCarro INT,
  dataLocacao DATETIME,
  horaLocacao TIME,
  qtdDiaria INT,
  vlrDiaria DECIMAL(18, 2),
  dataEntrega DATE,
  horaEntrega TIME,
  FOREIGN KEY (idCliente) REFERENCES tb_cliente(idCliente),
  FOREIGN KEY (idVendedor) REFERENCES tb_vendedor(idVendedor),
  FOREIGN KEY (idCarro) REFERENCES tb_carro(idCarro),
  FOREIGN KEY (idCombustivel) REFERENCES tb_combustivel(idCombustivel)

); 

-- Copiar dados da tabela original para a tabela tb_locacao_normalizada
INSERT INTO tb_locacao_normalizada (idLocacao, idCliente, idVendedor, idCarro, kmCarro, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, idCombustivel )
SELECT idLocacao, idCliente, idVendedor, idCarro, kmCarro, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, idCombustivel
FROM tb_locacao;
