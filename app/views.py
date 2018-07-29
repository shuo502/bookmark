from app import app
from flask import render_template,request
from app.models import BookMark,BookMarkForm
from datetime import datetime

@app.route("/")
def index():
    form =BookMarkForm()
    bookmarks=BookMark.objects.order_by('-time')
    return render_template("index.html",form=form,bookmarks=bookmarks)
    # return render_template("a.html")

@app.route("/add",methods=['POST',])
def add():
    form=BookMarkForm(request.form)
    if form.validate():
        title=form.title.data
        content=form.content.data
        url=form.url.data
        remarks=form.remarks.data
        print(url,title,content,remarks)
        bookmark=BookMark(url=url,title=title,content=content,remarks=remarks)
        bookmark.save()
    bookmarks=BookMark.objects.order_by('-time')
    return render_template("index.html",form=form,bookmarks=bookmarks)