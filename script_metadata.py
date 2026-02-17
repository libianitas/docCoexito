
import os
import oracledb

# En GitHub Actions usamos la ruta donde instalamos el client en el paso anterior
lib_dir = os.getenv("ORACLE_HOME")

try:
    # Iniciamos Thick Mode para soportar Wallets fácilmente
    oracledb.init_oracle_client(lib_dir=lib_dir)
    
    conn = oracledb.connect(
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        dsn=os.getenv("DB_SERVICE"),
        config_dir=os.getenv("WALLET_DIR"),
        wallet_password=os.getenv("WALLET_PASSWORD")
    )
    
    print("Conexión exitosa a Oracle Cloud desde el Runner!")
    
    # Aquí irá la lógica de extracción de metadatos que haremos en el siguiente paso
    cur = conn.cursor()
    cur.execute("SELECT table_name FROM user_tables")
    for row in cur:
        print(f"Tabla encontrada: {row[0]}")
        
    conn.close()
except Exception as e:
    print(f"Error conectando a Oracle: {e}")
    exit(1)
