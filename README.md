# Boston Tree Finder

## Summary
The Boston Tree Finder is a Django website application that allows users to find and interact with trees throughout Boston. Utilizing the MapBox API, users can find trees around Boston and create journeys that provide directions given a starting location. The application uses an SQLite database along with the Django REST Framework to handle user account creation along with the other backend needs of the application. 

### MapBox API
The MapBox API was used by our team to display maps on the home and journey screens in the application. We also added the directions functionality so that users could select their origin point and get directions to the selected tree via the desired method of transportation, along with receiving the duration and distance information. 

### Django REST Framework
The Django REST Framework provides an out of the box authentication solution with built-in APIs developers can leverage. 

## User Stories
- As a tree enthusiast, I want to find random trees in Boston
- As a tree enthusiast, I want to keep track of my favorite trees in Boston
- As a tree adventurer, I want to keep track of my journeys to trees in Boston
- As a map enthusiast, I want to look at a map with random trees marked in Boston

## Instructions

### Setup
1. Clone this repository
2. Install the necessary dependencies

### How to
1. run `python3 manage.py runserver` in the TreeFinder directory
2. Go to `http://127.0.0.1:8000/home`
3. Create an account
4. Login with the account you created
5. Enjoy the trees in Boston!

## Application

### Login Screen
![Login Screen](https://github.com/ibchand/EC530_Final_Project/blob/main/EC530_Final_Project_Login_Screen.png?raw=true)

### Registration Screen
![Registration Screen](https://github.com/ibchand/EC530_Final_Project/blob/main/EC530_Final_Project_Registration_Screen.png?raw=true)

### Home Screen

#### Guest Home Screen
![Guest Home Screen](https://github.com/ibchand/EC530_Final_Project/blob/main/EC530_Final_Project_Guest_Home_Screen.png?raw=true)

#### Authenticated Home Screen
![Authenticated Home Screen](https://github.com/ibchand/EC530_Final_Project/blob/main/EC530_Final_Project_Authenticated_Home_Screen.png?raw=true)

### Journey Screen
![Journey Screen](https://github.com/ibchand/EC530_Final_Project/blob/main/EC530_Final_Project_Journey_Screen.png?raw=true)

### Past Journey Screen
![Past Journey Screen](https://github.com/ibchand/EC530_Final_Project/blob/main/EC530_Final_Project_Past_Journey_Screen.png?raw=true)

## Database

#### Schema
![Database Schema](https://github.com/ibchand/EC530_Final_Project/blob/main/EC530_Final_Project_Database_Schema.png?raw=true)

## Team
- Benjamin Brewer - bbrewer1@bu.edu
- Ibrahim Chand - ichand@bu.edu
