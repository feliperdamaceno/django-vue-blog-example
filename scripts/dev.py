import os
import subprocess


def start_server():
    backend_path = os.path.join(os.path.dirname(__file__), "..", "backend")
    start_command = "python manage.py runserver"
    subprocess.run(start_command, shell=True, cwd=backend_path)


if __name__ == "__main__":
    start_server()
