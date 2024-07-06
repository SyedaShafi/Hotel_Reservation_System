
# WanderStay
The WanderStay is a web application that allows users to make and manage hotel reservations. Users can sign up, log in, make reservations, pay via their account balance, and leave reviews for hotels where they have stayed.

## Features
1. Token-based Authentication: Secure account activation through email.

2. Reservations and Payments: Users can make reservations and pay via their account balance. A dummy section allows users to deposit money (no real transactions).

3. Email Notifications: Users receive email notifications for account and transaction updates.

4. Review System: Users can create, update, and delete reviews/comments for hotels only if they have a reservation at the hotel.

## Technologies Used
1. Backend: Django (MVT architecture)
2. Frontend: HTML, CSS, Bootstrap
3. UI Enhancements: Swiffy Slider
4. Deployment: Render


### Installation
1. Clone the repository:
````bash
git clone https://github.com/SyedaShafi/Hotel_Reservation_System
cd Hotel_Reservation_System
````
2. Create and activate a virtual environment:
````bash
python -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
````
3. Install the dependencies:
````bash
pip install -r requirements.txt
````
4. Apply migrations:
````bash
python manage.py migrate
````

5. Create a superuser:
````bash
python manage.py createsuperuser
````
6. Run the development server:
````bash
python manage.py runserver
````
7. Open your browser and navigate to http://127.0.0.1:8000 to see the application.

## Contact
Your Name -syedashafi4@gmail.com

Project Link: https://hotel-reservation-system.onrender.com/
