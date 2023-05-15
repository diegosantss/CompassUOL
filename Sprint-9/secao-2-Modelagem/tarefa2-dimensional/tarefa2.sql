--Criação Tabela dimensão Data 
CREATE TABLE DimData (
  idData INTEGER PRIMARY KEY,
  dataLocacao DATETIME,
  horaLocacao TIME,
  dataEntrega DATE,
  horaEntrega TIME
);

-- População de dados
INSERT INTO DimData (idData, dataLocacao, horaLocacao, dataEntrega, horaEntrega)
SELECT DISTINCT idLocacao, dataLocacao, horaLocacao, dataEntrega, horaEntrega
FROM tb_locacao_normalizada;

--Criação Tabela dimensão Combustivel 
CREATE TABLE DimCombustivel (
  idCombustivel INTEGER PRIMARY KEY,
  tipoCombustivel VARCHAR(20)
);

-- População de dados
INSERT INTO DimCombustivel (idCombustivel, tipoCombustivel)
SELECT DISTINCT idCombustivel, tipoCombustivel
FROM tb_combustivel;

--Criação Tabela dimensão Carro 
CREATE TABLE DimCarro (
  idCarro INTEGER PRIMARY KEY,
  marcaCarro VARCHAR(80),
  modeloCarro VARCHAR(80),
  anoCarro INT,
  classiCarro VARCHAR(50)
);

-- População de dados
INSERT INTO DimCarro (idCarro, marcaCarro, modeloCarro, anoCarro, classiCarro)
SELECT idCarro, marcaCarro, modeloCarro, anoCarro, classiCarro
FROM tb_carro;

--Criação Tabela dimensão Cliente
CREATE TABLE DimCliente (
  idCliente INTEGER PRIMARY KEY,
  nomeCliente VARCHAR(100),
  cidadeCliente VARCHAR(40),
  estadoCliente VARCHAR(40),
  paisCliente VARCHAR(40)
);

-- População de dados
INSERT INTO DimCliente (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente)
SELECT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM tb_cliente;

--Criação Tabela dimensão Vendedor 
CREATE TABLE DimVendedor (
  idVendedor INTEGER PRIMARY KEY,
  nomeVendedor VARCHAR(15),
  sexoVendedor SMALLINT,
  estadoVendedor VARCHAR(40)
);

-- População de dados
INSERT INTO DimVendedor (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor)
SELECT idVendedor, nomeVendedor, sexoVendedor, estadoVendedor
FROM tb_vendedor;

--Criação Tabela Fato Locacao 
CREATE TABLE FatoLocacao (
  idLocacao INTEGER,
  idCliente INTEGER,
  idVendedor INTEGER,
  idCombustivel INTEGER,
  idCarro INTEGER,
  kmCarro INT,
  idData INTEGER,
  qtdDiaria INT,
  vlrDiaria DECIMAL(18, 2),
  PRIMARY KEY (idLocacao),
  FOREIGN KEY (idCliente) REFERENCES DimCliente(idCliente),
  FOREIGN KEY (idVendedor) REFERENCES DimVendedor(idVendedor),
  FOREIGN KEY (idCombustivel) REFERENCES DimCombustivel(idCombustivel),
  FOREIGN KEY (idCarro) REFERENCES DimCarro(idCarro),
  FOREIGN KEY (idData) REFERENCES DimData(idData)
);

-- População de dados
INSERT INTO FatoLocacao (idLocacao, idCliente, idVendedor, idCombustivel, idCarro, kmCarro, idData, qtdDiaria, vlrDiaria)
SELECT idLocacao, idCliente, idVendedor, idCombustivel, idCarro, kmCarro, idLocacao, qtdDiaria, vlrDiaria
FROM tb_locacao_normalizada;
