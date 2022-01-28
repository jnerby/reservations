### TECHNOLOGIES
I used a Flask server, Python, a PostgreSQL database, Bootstrap, and Javascript to complete this project. I used Flask due to time constraints, as Flask is lightweight and easy to use. Flask, however, would not scale well; I would consider using Django if I needed to scale. I used Jinja2 templating and Javascript to create an interactive frontend. If I wanted to build a responsive frontend, I would consider using React.

### DATABASE
I used a PostgreSQL database for the small scope of this project. I would need to consider other options if I wanted the project to scale. My database has two tables, users and reservations. The reservations table has a user_id field, which is a foreign key for the users' table's primary key. Since all appointments are the same length, the reservations table simply uses the appointment start date and time. If appointments had multiple length options, I would add a duration or end time field to the reservations table.

### NEXT STEPS
Moving forward, I would add functionality for users to cancel or edit their existing appointments.