import sys
import os

# Добавяме текущата директория в sys.path
sys.path.insert(0, os.path.dirname(__file__))

from app import app as application
