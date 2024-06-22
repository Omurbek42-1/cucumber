import aiosqlite 
from database.gueries import Queries
 
class Database: 
    def __init__(self, path): 
        self.path = path 
 
    async def create_tables(self): 
        async with aiosqlite.connect(self.path) as conn: 
            async with conn.cursor() as cur: 
                # создание всех таблиц 
                await cur.execute(Queries.CREATE_SURVEY_TABLE)
                # здесь может быть создание других таблиц 
                # которые нам нужны 
                await conn.commit() 
                
    async def execute(self): 
        async with aiosqlite.connect(self, query, params: tuple =()) as conn: 
            await conn.execute(query, params)  
            await conn.commit()  
            
            
from aiogram import create_engine, Column, Integer, String, DateTime
from aiogram import declarative_base
from aiogram import sessionmaker
from datetime import datetime


engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    contact = Column(String, index=True)
    visit_date = Column(String)
    food_quality = Column(String)
    cleanliness = Column(String)
    extra_comments = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

# Создание таблицы при запуске
Base.metadata.create_all(bind=engine)
      