Authors : 

Sai Kumar Reddy Chandupatla

Vaibhav Jajodia

Shruti Savardekar

Sonali Thote

Smart Bidder

295A Project SJSU 

Advisor - Weider Yu

## Tools
+ Python Framework, Cassandra, HTML, CSS, DJango

## About
+ Auctioning application with ML based bot detection for eleminating the suspected bot bidders from the auctioning business.

## Steps to run application:
+ Create a virtual environment
+ Update .pkl pickle file path in the views.py file under predict_human() function
+ set path to auction folder and run below commands:
+ Run ```python manage.py makemigrations auctions``` .
+ For database setup Run ```python manage.py migrate``` .
+ To start server at local system Run ```python manage.py runserver``` .