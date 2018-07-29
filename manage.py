from app import app
from app.models import BookMark,BookMarkForm
from flask_script import Manager
manager=Manager(app)
@manager.command
def save():
    bookmark=BookMark(url="http://baidu.com")
    bookmark.save()

