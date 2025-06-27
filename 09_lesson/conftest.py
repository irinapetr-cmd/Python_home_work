import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Подключение к вашей базе данных QA
DB_URL = "postgresql://postgres:060708@localhost:5432/QA"


@pytest.fixture(scope="function")
def db_session():
    engine = create_engine(DB_URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    yield session

    # После выполнения теста откатываем изменения
    session.rollback()
    session.close()