
from pathlib import Path
from email.message import EmailMessage
import os
from dotenv import load_dotenv


load_dotenv
PASSWORD = os.environ.get('PASSWORD')
print(PASSWORD)


