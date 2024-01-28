Consumer
Consumer is a Django project designed to receive messages from a producer, process them, and perform specific actions based on the received messages.

Features
Webhook Endpoint: Listens for incoming messages from the producer's webhook.
Getting Started
These instructions will help you set up the project and run it on your local machine.

Prerequisites
Python 3.x
Django
Django Rest Framework
Celery
RabbitMq Brocker

nstallation
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/consumer.git
cd consumer
Install dependencies:
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Apply migrations:
python manage.py migrate
Run the development server:

python manage.py runserver
The project will be available at http://127.0.0.1:8000/consumer/message.

Usage
Set up the producer to send messages to the webhook URL:

Default webhook URL: http://127.0.0.1:8000/consumer/message
When the producer sends a message, the consumer will process it and perform actions based on the content.

Configuration
Customize the message processing logic in views.py to define actions based on the received messages.

Running Tests

Run tests using the following command:
python manage.py test consumer
Contributing
If you'd like to contribute to this project, please follow the Contributing Guidelines.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Thanks to Django and Django Rest Framework for making web development in Python delightful.

don't forget to start celery
celery -A your_project worker --loglevel=info
and
start brocker RabbitMq
