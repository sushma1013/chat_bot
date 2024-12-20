Project Setup Instructions:
Frontend (ReactJS) Setup:

Ensure you have Node.js installed on your system. You can download it from here.

Navigate to the root directory of the frontend project (where package.json is located).

Run the following command to install the required dependencies:

npm install

After installation is complete, start the React development server:

npm start

The frontend application will be available at http://localhost:3000.


Backend (Flask) Setup:

Ensure you have Python 3.x installed. You can download it from here.

Navigate to the root directory of the backend project (where app.py is located).

Install the required Python dependencies by running:

pip install -r requirements.txt

Create a .env file to store sensitive information like API keys and tokens (make sure to use your OpenAI API key here):
makefile
Copy code
OPENAI_API_KEY=your_openai_api_key
JWT_SECRET_KEY=your_jwt_secret_key
Run the Flask application:

python app.py

The backend API will be available at http://127.0.0.1:5000.
Running the Full Application:

Ensure both the frontend (ReactJS) and backend (Flask) servers are running.
Open the frontend in your browser at http://localhost:3000.
Log in using valid credentials, and you will be able to interact with the chatbot, which fetches data from the backend API.