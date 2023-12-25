import os
import subprocess


def build_frontend():
    frontend_path = os.path.join(os.path.dirname(__file__), "..", "frontend")
    build_command = "npm run build"
    subprocess.run(build_command, shell=True, cwd=frontend_path)


if __name__ == "__main__":
    build_frontend()
