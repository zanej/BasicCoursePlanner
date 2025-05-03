from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    credits = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(50), nullable=False)

class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    courses = db.relationship('Course', secondary='schedule_courses', backref='schedules')

schedule_courses = db.Table('schedule_courses',
    db.Column('schedule_id', db.Integer, db.ForeignKey('schedule.id')),
    db.Column('course_id', db.Integer, db.ForeignKey('course.id'))
)
