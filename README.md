# 📚 Flask eLib – Book App

A simple Flask-based e-library application where users can register, log in with Google, search and view book details, and download PDFs securely. Includes support for login, preview, download, and purchase (M-Pesa).

## 🚀 Features

- User registration and login with Google OAuth
- Book search and detailed view
- Download books securely
- Purchase with M-Pesa API
- Admin dashboard and error pages

## 📁 Project Structure
elib/
├── app.py # Main Flask app
├── config.py # App configuration and credentials
├── mpesa.py # M-Pesa integration logic
├── schema.sql # Database schema
├── templates/ # HTML templates
│ ├── index.html
│ ├── login.html
│ ├── dashboard.html
│ └── ...
└── .gitignore

 ⚙️ Installation Guide
 1. Clone the repository

```bash
git clone https://github.com/WeweNaNani/elib.git
cd elib

2. Create and activate a virtual environment
bash

python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate

3. Install the required packages
bash

pip install -r requirements.txt
If requirements.txt doesn’t exist yet, you can generate it with:
pip freeze > requirements.txt

4. Set environment variables
Create a .env file in the root folder:

env

FLASK_APP=app.py
FLASK_ENV=development

GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
MPESA_CONSUMER_KEY=your_mpesa_key
MPESA_CONSUMER_SECRET=your_mpesa_secret

You can load it using python-dotenv. If not added yet, install and configure:

bash
pip install python-dotenv
At the top of app.py:

python
from dotenv import load_dotenv
load_dotenv()

5. Initialize the SQLite database
bash

sqlite3 elib.db < schema.sql

6. Run the Flask app
bash

flask run
Visit: http://localhost:5000

🔐 Notes
Do not commit .env or any sensitive credentials.
.env is already included in .gitignore.

✅ To Do
Add book upload feature for admins
Add download counter per book
Email verification
Pagination and search filters

📄 License
This project is licensed under the MIT License.

yaml

---

Let me know if you want me to generate the `requirements.txt` file too, or include screenshots or a deployment guide (e.g. for Heroku or Render).
