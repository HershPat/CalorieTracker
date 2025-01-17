# Calorie Tracker

## Dependencies
- Python 3.8+
- PostgreSQL 12+
- psycopg2 (`pip install psycopg2`)

## Database Structure
### Tables
1. User Table
   - userID (Primary Key)
   - firstName
   - lastName 
   - userAge
   - userWeight
   - email
   - phoneNumber
   - isActive
   - createdAt
   - updatedAt

2. Food Table
   - foodID (Primary Key)
   - userID (Foreign Key)
   - foodName
   - calories
   - createdAt
   - updatedAt

3. Food Log Table
   - foodLogID (Primary Key)
   - userID (Foreign Key)
   - foodID (Foreign Key)
   - createdAt
   - updatedAt

## Usage
1. Run `python main.py` to start the application
2. Follow the menu prompts to:
   - Add new food items
   - Log daily food intake
   - View daily calorie summary
   - Set and track calorie goals

## Future Improvements
- Food Picture to Calories using AI
- Create a graphical user interface