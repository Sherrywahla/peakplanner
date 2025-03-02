# PeakPlanner – Your Personal Productivity Hub  

**PeakPlanner** is a powerful, web-based task management system designed to help users streamline their workflow, manage tasks effectively, take notes, and set reminders all in one place! Whether you're a freelancer, student, or professional, PeakPlanner keeps you organized and focused.  

## Features  

- **User Authentication** – Secure login and registration with custom user models  
- **Task Management** – Create, edit, update, and delete tasks with due dates & status tracking  
- **Notes** – Store and organize important notes efficiently  
- **Reminders** – Set timely reminders for crucial tasks  
- **Admin Panel** – Full admin access to manage users and content  
- **Intuitive UI** – Built with **Tailwind CSS** for a sleek, responsive design  
- **Persistent Storage** – Manage files and media securely  



## Project Structure  

```
peakplanner/                # Root project folder
│── .env                    # Environment variables
│── manage.py                # Django management script
│── db.sqlite3               # SQLite database (default)
│── staticfiles/             # Collected static files
│
├── settings/                # Django project settings
│   │── settings.py          # Core settings file
│   │── urls.py              # URL configurations
│
├── ui/                      # Frontend with Tailwind CSS
│   │── static/              # Compiled static files
│   │── templates/           # HTML templates for all features
│
├── accounts/                # Custom authentication app
│   │── models.py            # CustomUser model
│   │── views.py             # Login/Register functionality
│
├── tasks/                   # Task management system
│   │── models.py            # Task structure
│   │── views.py             # Task CRUD operations
│
├── notes/                   # Notes management
│   │── models.py
│   │── views.py
│
├── reminders/               # Reminder system
│   │── models.py
│   │── views.py
│
├── dashboard/               # User dashboard logic
│
└── requirements.txt         # Dependencies for the project
```



## Installation  

### **Clone the repository**
```bash
git clone https://github.com/Sherrywahla/peakplanner.git
cd peakplanner
```

### **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### **Install dependencies**
```bash
pip install -r requirements.txt
```

### **Apply database migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

### **Run the server**
```bash
python manage.py runserver
```



## Deployment with Docker  

For containerized deployment, use the provided **Dockerfile**:  

```bash
docker build -t peakplanner .
docker run -p 8000:8000 peakplanner
```



## Admin Access  
To access the **Django Admin Panel**, create a superuser:  
```bash
python manage.py createsuperuser
```

Then log in at:  
[http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)



## Future Enhancements  

- Dark Mode
- Advanced Task Filtering
- Calendar Integration
- Mobile App Companion  



## License  

PeakPlanner is open-source and available under the **MIT License**.  



### Contribute & Star
If you find **PeakPlanner** useful, consider giving it a ⭐️ on GitHub and contributing!  