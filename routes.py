from flask import Blueprint, render_template, request, redirect, url_for
from .models import db, Course, Schedule

main = Blueprint('main', __name__)

@main.route('/')
def index():
    courses = Course.query.all()
    schedules = Schedule.query.all()
    return render_template('index.html', courses=courses, schedules=schedules)

@main.route('/add_course', methods=['POST'])
def add_course():
    code = request.form['code']
    title = request.form['title']
    credits = int(request.form['credits'])
    category = request.form['category']
    new_course = Course(code=code, title=title, credits=credits, category=category)
    db.session.add(new_course)
    db.session.commit()
    return redirect(url_for('main.index'))

@main.route('/create_schedule', methods=['POST'])
def create_schedule():
    name = request.form['name']
    selected_courses = request.form.getlist('courses')
    schedule = Schedule(name=name)
    for cid in selected_courses:
        course = Course.query.get(int(cid))
        schedule.courses.append(course)
    db.session.add(schedule)
    db.session.commit()
    return redirect(url_for('main.index'))
