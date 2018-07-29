from app import db
from flask_mongoengine.wtf import model_form
import datetime
class  BookMark(db.Document):
    title = db.StringField(required=True, default="")
    url = db.URLField(required=True, max_length=20, primary_key=True)
    content = db.StringField(required=True, default="",null=True)
    remarks = db.StringField(required=True, default="",null=True)
    time = db.DateTimeField(default=datetime.datetime.now())
    status = db.IntField(default=0)
    userid = db.IntField(default=0)


BookMarkForm = model_form(BookMark)
