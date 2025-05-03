# BasicCoursePlanner
Course Planner is a full-stack web application designed to help Texas A&M students organize their class schedules and track their academic progress. With features to add custom courses, categorize them, and build named schedules, it serves as a lightweight academic planning tool for students in any major.

The app allows users to browse and manage all available courses, select which ones to include in a schedule, and save that schedule for future reference. It’s perfect for semester planning, degree audits, or simply staying on top of graduation requirements.

Built with Flask and SQLAlchemy for the backend, the app uses Jinja templates for dynamic rendering. All course and schedule data is stored in a local SQLite database. The frontend is structured using HTML and is fully extendable with CSS or JS for future UI enhancements.

To get started, clone the repository:

git clone https://github.com/your-username/CoursePlanner.git
cd CoursePlanner
Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
Install dependencies:
pip install flask flask_sqlalchemy
Initialize the database:
python init_db.py
Then start the server:
python app.py
Once running, open your browser to http://(localip) to access the application.

Planned improvements include authentication for individual user schedules, drag-and-drop calendar views, API integration with TAMU’s official course catalog, and smarter credit tracking for degree plans. This tool is a practical foundation for students looking to streamline their academic planning in a simple, effective way.
