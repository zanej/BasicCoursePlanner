from course_planner.models import db, Course
from app import app

with app.app_context():
    db.drop_all()
    db.create_all()

    sample_courses = [
        Course(code='CSCE121', title='Intro to Programming', credits=4, category='Core'),
        Course(code='MATH151', title='Engineering Math I', credits=4, category='Math'),
        Course(code='PHYS206', title='Physics Mechanics', credits=4, category='Science'),
        Course(code='ENGL104', title='Composition and Rhetoric', credits=3, category='Communication')
    ]

    db.session.bulk_save_objects(sample_courses)
    db.session.commit()
    print("Database initialized with sample courses.")
