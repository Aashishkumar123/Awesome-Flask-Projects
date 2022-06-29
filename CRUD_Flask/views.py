from turtle import update
from flask import Blueprint, render_template, request, flash
from sqlalchemy import delete


crud_blueprint = Blueprint('crud',__name__)
from .models import Student
from CRUD_Flask.__init__ import db

@crud_blueprint.route('/',methods=['GET','POST'])
def index():
    if request.method == "POST" and 'add' in request.form:
        name = request.form.get('name')
        email = request.form.get('email')
        course = request.form.get('course')
        add_stu = Student(
            name=name,
            email=email,
            course=course
        )
        db.session.add(add_stu)
        db.session.commit()
        flash('Student Added !!', 'success')
    
    elif request.method == "POST" and 'delete' in request.form:
        id = request.form.get('id')
        delete_stu = Student.query.get(id)
        db.session.delete(delete_stu)
        db.session.commit()
        flash('Student Deleted !!', 'danger')
    
    if request.method == "POST" and 'update' in request.form:
        id = request.form.get('id')
        name = request.form.get('name')
        email = request.form.get('email')
        course = request.form.get('course')
        update_stu = Student.query.get(id)
        update_stu.name = name
        update_stu.email = email
        update_stu.course = course
        db.session.commit() 
        flash('Student Updated !!', 'success')
    students = Student.query.all()
    return render_template('index.html',students=students)
