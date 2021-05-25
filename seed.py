# seed file sample for db

from models import db
from app import app

# create all tables
db.drop_all()
db.create_all()