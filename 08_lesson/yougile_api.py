import requests
import uuid

class YougileAPI:
    def __init__(self, api_key):
        self.base_url = "https://ru.yougile.com/api-v2"
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

    def create_project(self, title, users=None):
        """Создание проекта"""
        url = f"{self.base_url}/projects"
        data = {"title": title}
        if users:
            data["users"] = users
        return requests.post(url, json=data, headers=self.headers)

    def update_project(self, project_id, **kwargs):
        """Обновление проекта"""
        url = f"{self.base_url}/projects/{project_id}"
        return requests.put(url, json=kwargs, headers=self.headers)

    def get_project(self, project_id):
        """Получение проекта по ID"""
        url = f"{self.base_url}/projects/{project_id}"
        return requests.get(url, headers=self.headers)

    def delete_project(self, project_id):
        """Удаление проекта (помечаем как deleted)"""
        return self.update_project(project_id, deleted=True)

    def generate_fake_id(self):
        """Генерация случайного UUID для негативных тестов"""
        return str(uuid.uuid4())