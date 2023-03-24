#!/usr/bin/env python3

from app import app
from models import db, User, Game, Review



if __name__ == '__main__':
# removed db.init_app(app) as it  
    with app.app_context():
        import ipdb; ipdb.set_trace()
