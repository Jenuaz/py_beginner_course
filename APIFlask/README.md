Create quick web API using Flask microframework for Python. We starting from creating a Python file called service.py
We specify an environment variable which tells Flask what file constitutes the starting point of our Flask app, and then 
Tell Flask to run the application using the command flask run:

	FLASK_APP=service.py flask run

Use HTTP request to our root URL to test the app we build:

	curl localhost:5000

For our example with parameter in a route ("/user/<name>") prepared next request:

	curl localhost:5000/user/AnyNameYouWant

!!!When you update service.py file with additional routing you need to rerun service to apply the changes. 
