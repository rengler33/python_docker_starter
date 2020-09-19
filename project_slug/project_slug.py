import os

from dotenv import load_dotenv

load_dotenv()

MESSAGE = os.getenv("PY_MESSAGE")

print(MESSAGE)
