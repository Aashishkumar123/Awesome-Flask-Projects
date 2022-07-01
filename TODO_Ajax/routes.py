from flask import Blueprint, render_template,jsonify, request
from datetime import datetime

todo_blueprint = Blueprint('todo',__name__)
from .models import List
from TODO_Ajax.__init__ import db


@todo_blueprint.route('/')
def show_list():
    lists = List.query.all()
    return render_template('todo.html',date=datetime.now().strftime('%Y-%m-%d'),lists=lists)


@todo_blueprint.route('/submit-list',methods=['POST'])
def submit_list():
    title = request.form.get('title')
    add_list = List(
        title=title
    )
    db.session.add(add_list)
    db.session.commit()
    data = {'id':add_list.id,'title':add_list.title}
    return jsonify(data)


@todo_blueprint.route('/edit-list/<int:id>',methods=['POST'])
def edit_list(id):
    update_list = List.query.get(id)
    update_list.title = request.form.get('title')
    db.session.commit()
    return jsonify({'title':update_list.title})


@todo_blueprint.route('/delete-list/<int:id>/',methods=['POST'])
def delete_list(id):
    destroy_list = List.query.get(id)
    db.session.delete(destroy_list)
    db.session.commit()
    return jsonify({'ok':True})
