from ensurepip import bootstrap
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
db = SQLAlchemy()

def create_app():
    app=Flask(__name__)
    
    bootstrap = Bootstrap(app)

    app.secret_key = 'somerandomvalue'

    app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///Assessment222.sqlite'
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view='auth.login'
    login_manager.init_app(app)

    from .models import User  # importing here to avoid circular references
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


    #add Blueprints
    from . import views
    app.register_blueprint(views.mainbp)
  
    from . import auth
    app.register_blueprint(auth.bp)

    return app