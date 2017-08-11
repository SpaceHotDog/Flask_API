# manage.py

import os
from flask_script import Manager # Class for handling a set of commands.
from flask_migrate import Migrate, MigrateCommand
from app import db, create_app
# Import the models so that the script can find the models to be migrated.
from app import models

app = create_app(config_name=os.getenv('APP_SETTINGS'))
# The MigrateCommand contains a set of migration commands.
migrate = Migrate(app, db)
# The Manager class keeps track of all the commands and handles how they are called from the command line.
manager = Manager(app) 

# Manager also adds the migration commands and enforces that they start with db.
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
