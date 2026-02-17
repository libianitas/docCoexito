import os
import oracledb
from dotenv import load_dotenv

load_dotenv()

# Detectar si estamos en GitHub o Local para la ruta del cliente
if os.getenv("GITHUB_ACTIONS") == "true":
    # Ruta definida en el YAML arriba
    oracle_path = "/opt/oracle/instantclient_23_0"
else:
    # Tu ruta local de Windows
    oracle_path = r"F:\OCIfunctions\oracle\instantclient_23_0"

try:
    oracledb.init_oracle_client(lib_dir=oracle_path)
    print(f"Thick mode habilitado en: {oracle_path}")
    
    conn = oracledb.connect(
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        dsn=os.getenv("DB_SERVICE"),
        config_dir=os.getenv("WALLET_DIR"),
        wallet_password=os.getenv("WALLET_PASSWORD")
    )
    
    cur = conn.cursor()
    cur.execute("select sysdate from dual")
    print("SYS_DATE =", cur.fetchone()[0])
    
    cur.close()
    conn.close()
    print("Conexion OK en GitHub")
except Exception as e:
    print(f"Error de conexión: {e}")
    exit(1) # Importante para que el pipeline marque fallo si no conecta
