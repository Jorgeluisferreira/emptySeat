import asyncio
from services.scrappers.linkedin_scrapper import linkedin_scrapper
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from database.entitys.job import Job

DATABASE_URL = "sqlite:///./database/dados.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


async def main():
    scraper = linkedin_scrapper()
    vagas = await scraper.get_vagas()
    for v in vagas:
        with SessionLocal() as session:
            job = Job(titulo=v['titulo'], empresa=v['empresa'], link=v['Link'])
            session.add(job)
            session.commit()
            session.refresh(job)
            print(f"Vaga adicionada: {job.titulo} na empresa {job.empresa}")

asyncio.run(main())
