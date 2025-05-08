import os
from decimal      import Decimal
from src.Models   import Carro, Clientes, Contato, Concessionaria
from src.Enum     import Cores as c
from src.Database import Database
from dotenv       import load_dotenv

load_dotenv()

def main():
    db = Database(
        os.getenv("DB_HOST"),
        os.getenv("DB_NAME"), 
        os.getenv("DB_USER"), 
        os.getenv("DB_PASSWORD"), 
        os.getenv("DB_PORT")
    )
    conexao = db.conectar()

    db.executar_script("""
        CREATE TABLE IF NOT EXISTS teste (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL
        );
    """)
    
    db.adicionar_coluna("teste", "idade", "INTEGER")
    db.remover_coluna("teste", "idade")

    if conexao:
        db.desconectar()

if __name__ == "__main__":
    main()