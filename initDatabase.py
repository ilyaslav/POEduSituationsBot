from settings import settings
import os

os.system("docker rm -f my_postgres")
os.system(f"docker run --name my_postgres "+\
          f"-p {settings.DB_PORT}:5432 "+\
          f"-e POSTGRES_USER={settings.DB_USER} "+\
          f"-e POSTGRES_PASSWORD={settings.DB_PASS} "+\
          f"-e POSTGRES_DB={settings.DB_NAME} -d postgres")