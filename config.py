from dotenv import load_dotenv
import os

# Carga las variables de entorno desde el archivo .env
load_dotenv()

# Ahora puedes acceder a las variables de entorno usando os.environ
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
HOST = os.getenv("HOST")
PORT = int(os.getenv("PORT"))
PASSWORD = os.getenv("PASSWORD")
PRIVATE_CHAT_ID = int(os.getenv("PRIVATE_CHAT_ID"))
COOKIE = os.getenv("COOKIE")
ADMINS = [int(admin_id) for admin_id in os.getenv("ADMINS").split(",")]
