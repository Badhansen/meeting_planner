From python:3.6

WORKDIR /meeting_planner/meeting_planner

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /meeting_planner/meeting_planner
EXPOSE 8000
CMD python manage.py runserver 0.0.0.0:8000