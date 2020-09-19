from dotenv import load_dotenv
import os

load_dotenv()

MESSAGE = os.getenv("PY_MESSAGE")

print(MESSAGE)