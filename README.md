# Project Dashboard

A Flask-based project dashboard application with RESTful API endpoints.

## Setup

### Prerequisites
- Python 3.9 or higher
- pip (Python package manager)

### Virtual Environment Setup

#### Windows
```powershell
# Create virtual environment
python -m venv .venv

# Activate virtual environment
.\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

#### Unix/Linux
```bash
# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Running the Application

1. Make sure the virtual environment is activated
2. Run the application:
```bash
python run.py
```

The application will be available at `http://localhost:5000`

### Docker
To build and run the Docker container:
```bash
docker build -t project-dashboard .
docker run -p 5000:5000 project-dashboard
```

## CI/CD
The project includes a GitHub Actions workflow for continuous integration and deployment.