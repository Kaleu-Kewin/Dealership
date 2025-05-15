from src.database import Database
from dotenv import load_dotenv
import hashlib
import os

def criar_tabelas():
    load_dotenv()

    nome  = os.getenv("NOME")
    senha = hashlib.sha256(os.getenv("SENHA").encode()).hexdigest()

    db = Database(
        os.getenv("DB_HOST"),
        os.getenv("DB_NAME"),
        os.getenv("DB_USER"),
        os.getenv("DB_PASSWORD"),
        os.getenv("DB_PORT")
    )

    db.conectar()
    try:
        db.criar_tabela(
            "CLIENTES",
            {
                "CLI_CODIGO"          : "SERIAL PRIMARY KEY",
                "CLI_NOME"            : "VARCHAR(100) NOT NULL",
                "CLI_CPF"             : "VARCHAR(14) NOT NULL UNIQUE",
                "CLI_EMAIL"           : "VARCHAR(100) NOT NULL UNIQUE",
                "CLI_TELEFONE"        : "VARCHAR(18) NOT NULL",
                "CLI_DATA_NASCIMENTO" : "DATE NOT NULL",
                "CLI_CEP"             : "VARCHAR(10) NOT NULL",
                "CLI_STATUS"          : "VARCHAR(10) NOT NULL CHECK (CLI_STATUS IN ('ATIVO', 'INATIVO'))",
            }
        )

        db.criar_tabela(
            "VEICULOS",
            {
                "VEI_CODIGO"     : "SERIAL PRIMARY KEY",
                "VEI_MODELO"     : "VARCHAR(50) NOT NULL",
                "VEI_MARCA"      : "VARCHAR(50) NOT NULL",
                "VEI_ANO"        : "VARCHAR(4) NOT NULL",
                "VEI_PRECO"      : "DECIMAL(10, 2) NOT NULL",
                "VEI_COR"        : "VARCHAR(20) NOT NULL",
                "VEI_QUANTIDADE" : "INTEGER NOT NULL",
                "VEI_PLACA"      : "VARCHAR(7) NOT NULL UNIQUE",
                "TIPO_VEICULO"   : "VARCHAR(20) NOT NULL CHECK (TIPO_VEICULO IN ('CARRO', 'MOTO'))"
            }
        )

        db.criar_tabela(
            "CLIENTES_VEICULOS",
            {
                "CLI_CODIGO"  : "INTEGER REFERENCES CLIENTES(CLI_CODIGO) ON DELETE CASCADE",
                "VEI_CODIGO"  : "INTEGER REFERENCES VEICULOS(VEI_CODIGO) ON DELETE CASCADE",
                "PRIMARY KEY" : "(CLI_CODIGO, VEI_CODIGO)"
            }
        )

        db.criar_tabela(
            "USUARIOS",
            {
                "USU_CODIGO" : "SERIAL PRIMARY KEY",
                "USU_NOME"   : "VARCHAR(25) NOT NULL UNIQUE",
                "USU_SENHA"  : "VARCHAR(255) NOT NULL"
            }
        )

        db.insert(
            "USUARIOS",
            {
                "USU_NOME"  : nome,
                "USU_SENHA" : senha
            }
        )

    finally:
        db.desconectar()
