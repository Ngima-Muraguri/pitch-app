from app import db, create_app
from flask_migrate import Migrate
from flask_script import Manager,Server
from app.models import Pitch, User,Comments
from flask_migrate import Migrate, MigrateCommand


app = create_app('development')
manager = Manager(app)
migrate = Migrate(app,db)


manager.add_command('server',Server)
manager.add_command('db',MigrateCommand)
  
@manager.shell
def make_shell_context():
    return dict(app=app,db=db,User = User, Comments=Comments, Pitch=Pitch)

if __name__ == '__main__':
    manager.run()
