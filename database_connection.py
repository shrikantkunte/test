from flask_sqlalchemy import SQLAlchemy
#from _init_ import app



class Create_database_connection:
   def _init_(self, app):
        app.config["SQLALCHEMY_DATABASE_URI"] = "mssql+pyodbc://SK:Tcrn@123@149.171.80.194/test_web_commons?driver=SQL+Server?trusted_connection=yes"
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        db = SQLAlchemy(app)
#        db.create_all()
        return db

    





