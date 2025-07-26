# locustfile.py
from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 2.5) # Users wait between 1 and 2.5 seconds between tasks

    @task
    def get_users(self):
        self.client.get("/users/") # Simulate getting all users

    @task(3) # This task will be picked 3 times as often as others
    def create_user(self):
        user_data = {
            "name": fake.name(),
            "telefono": fake.telephone(),
            "fecha de nacimiento": fake.date(),
            "email": fake.email(),
            "password": fake.sha256(), # In a real app, hash passwords securely
        }
        self.client.post("/users/", json=user_data)