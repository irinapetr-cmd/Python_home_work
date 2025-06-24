import pytest
from yougile_api import YougileAPI

API_KEY = "i8uLM8NBeDOdMdNO5NGp-uthx-JuZEjBJYI9-tAXjri59+GntS7e6TXLNNflK3KA"

@pytest.fixture
def api_client():
    """Фикстура для создания клиента API"""
    return YougileAPI(API_KEY)

@pytest.fixture
def test_project(api_client):
    """Фикстура для создания тестового проекта"""
    response = api_client.create_project("Test Project")
    assert response.status_code == 201
    project_id = response.json()["id"]
    yield project_id
    # Удаляем проект после теста
    api_client.delete_project(project_id)

# Позитивные тесты
def test_create_project_positive(api_client):
    """Позитивный тест создания проекта"""
    response = api_client.create_project("New Project")
    assert response.status_code == 201
    assert "id" in response.json()

def test_update_project_positive(api_client, test_project):
    """Позитивный тест обновления проекта"""
    response = api_client.update_project(test_project, title="Updated Title")
    assert response.status_code == 200
    updated_project = api_client.get_project(test_project).json()
    assert updated_project["title"] == "Updated Title"

def test_get_project_positive(api_client, test_project):
    """Позитивный тест получения проекта"""
    response = api_client.get_project(test_project)
    assert response.status_code == 200
    assert response.json()["id"] == test_project

# Негативные тесты
def test_create_project_negative_empty_title(api_client):
    """Негативный тест создания проекта с пустым названием"""
    response = api_client.create_project("")
    assert response.status_code == 400

def test_update_project_negative_nonexistent(api_client):
    """Негативный тест обновления несуществующего проекта"""
    fake_id = api_client.generate_fake_id()
    response = api_client.update_project(fake_id, title="Should Fail")
    assert response.status_code == 404

def test_get_project_negative_nonexistent(api_client):
    """Негативный тест получения несуществующего проекта"""
    fake_id = api_client.generate_fake_id()
    response = api_client.get_project(fake_id)
    assert response.status_code == 404