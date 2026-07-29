# Threat Intelligence Platform

A Flask-based cybersecurity application that collects, analyzes, and visualizes threat intelligence data. The platform provides an interactive dashboard for monitoring threats, managing malicious IP addresses, and generating useful security insights.

---

## Project Overview

The Threat Intelligence Platform helps security analysts and organizations monitor cybersecurity threats efficiently. It stores threat information, analyzes the data, and presents it through a user-friendly dashboard.

---

## Features

- Interactive Threat Intelligence Dashboard
- Threat Data Collection and Analysis
- Malicious IP Monitoring
- Threat Severity Classification
- Database Storage using SQLite
- Security Reports
- Responsive Web Interface

---

## Technologies Used

### Backend
- Python
- Flask
- Flask SQLAlchemy

### Frontend
- HTML
- CSS
- Bootstrap
- JavaScript

### Database
- SQLite

### Version Control
- Git
- GitHub

---

## Project Structure

```text
Threat-Intelligence-Platform/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
│
├── data/
├── database/
├── docs/
│   └── screenshots/
├── models/
├── scripts/
├── services/
├── static/
├── templates/
└── test_services.py
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/Deepak1506-art/Threat-Intelligence-Platform.git
```

### Move into Project

```bash
cd Threat-Intelligence-Platform
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment (Windows)

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Project

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## Workflow

```
Threat Data
      ↓
Data Processing
      ↓
Threat Analysis
      ↓
Database Storage
      ↓
Dashboard Visualization
      ↓
Reports
```

---

## Project Screenshots

### Dashboard

![Dashboard](docs/screenshots/dashboard.png)

### Threat List

![Threat List](docs/screenshots/threat-list.png)

### Threat Details

![Threat Details](docs/screenshots/threat-details.png)

### Reports

![Reports](docs/screenshots/reports.png)

---

## Future Enhancements

- Real-time Threat Intelligence API Integration
- Machine Learning-based Threat Detection
- Email Notifications
- User Authentication and Role Management
- Advanced Analytics Dashboard

---

## Testing

Run the test
