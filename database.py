import os
from urllib.parse import quote_plus

from dotenv import load_dotenv
from sqlalchemy import Float, ForeignKey, String, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, sessionmaker
from sqlalchemy_utils import create_database, database_exists

load_dotenv(".env")

DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = quote_plus(os.getenv("DB_PASSWORD", ""))
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME", "apartment_db")

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL, pool_pre_ping=True)

if not database_exists(engine.url):
    create_database(engine.url)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


class Base(DeclarativeBase):
    pass


class ApartmentType(Base):
    __tablename__ = "apartment_types"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)

    apartments: Mapped[list["Apartment"]] = relationship(back_populates="apartment_type")


class Apartment(Base):
    __tablename__ = "apartments"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    apartment_code: Mapped[str] = mapped_column(String(10), unique=True, nullable=False)
    monthly_rent: Mapped[float] = mapped_column(Float, nullable=False)
    apartment_type_id: Mapped[int] = mapped_column(ForeignKey("apartment_types.id"), nullable=False)

    apartment_type: Mapped["ApartmentType"] = relationship(back_populates="apartments")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()