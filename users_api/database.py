from sqlalchemy import create_engine, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker, session
datebase = 'sqlite:///users.db'
engine = create_engine(datebase, connect_args={"check_same_thread": False})
LocalSession = sessionmaker(bind = engine)
def get_db():
    db = LocalSession()                 # подключение к базе данных
    try:
        yield db
    finally:
        db.close()

