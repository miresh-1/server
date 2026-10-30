from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker, session
from sqlalchemy  import create_engine, String
from users_api.database import engine
class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'      #sqlalchemy orm  |  данные об уч

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String, unique=True)
    name: Mapped[str] = mapped_column(String)
    surname: Mapped[str] = mapped_column(String)
    age: Mapped[int] = mapped_column()


Base.metadata.create_all(bind=engine)