from sqlalchemy import create_engine
from src.config.db_config import DB_CONFIG

def get_engine():
    url = (
        f"postgresql+psycopg2://{DB_CONFIG['user']}:"
        f"{DB_CONFIG['password']}@"
        f"{DB_CONFIG['host']}:"
        f"{DB_CONFIG['port']}/"
        f"{DB_CONFIG['database']}"
    )
    engine = create_engine(url)
    return engine
