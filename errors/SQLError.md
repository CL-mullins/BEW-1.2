Traceback (most recent call last):
  File "/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/app.py", line 1, in <module>
    from workout_app import app 
  File "/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/workout_app/__init__.py", line 41, in <module>
    db.create_all()
  File "/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/lib/python3.9/site-packages/flask_sqlalchemy/__init__.py", line 1094, in create_all
    self._execute_for_all_tables(app, bind, 'create_all')
  File "/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/lib/python3.9/site-packages/flask_sqlalchemy/__init__.py", line 1086, in _execute_for_all_tables
    op(bind=self.get_engine(app, bind), **extra)
  File "/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/lib/python3.9/site-packages/flask_sqlalchemy/__init__.py", line 1017, in get_engine
    return connector.get_engine()
  File "/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/lib/python3.9/site-packages/flask_sqlalchemy/__init__.py", line 593, in get_engine
    sa_url, options = self.get_options(sa_url, echo)
  File "/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/lib/python3.9/site-packages/flask_sqlalchemy/__init__.py", line 608, in get_options
    sa_url, options = self._sa.apply_driver_hacks(self._app, sa_url, options)
  File "/Users/chrismullins/dev/courses/bew1.2/Assignments/Final Project/venv/lib/python3.9/site-packages/flask_sqlalchemy/__init__.py", line 933, in apply_driver_hacks
    if sa_url.drivername.startswith('mysql'):
AttributeError: 'NoneType' object has no attribute 'drivername'