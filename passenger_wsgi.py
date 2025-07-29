import sys
import os

# Добави текущата директория в пътищата за import
sys.path.insert(0, os.path.dirname(__file__))

from app import app as application
