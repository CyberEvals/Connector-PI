# Project Dashboard API Documentation

## Overview
The Project Dashboard API provides endpoints to manage and track project information. It offers functionality to view projects, get statistics, and search through project data.

## Base URL
```
http://localhost:5000/api
```

## Authentication
All endpoints require authentication. Include your authentication token in the request header:
```
Authorization: Bearer <your_token>
```

## Endpoints

### 1. List All Projects
Retrieve a list of all projects with their details.

**Endpoint:** `GET /projects/`

**Response:**
```json
[
  {
    "id": 1,
    "name": "Project Alpha",
    "status": "Completed",
    "progress": 100,
    "description": "A cutting-edge AI implementation project...",
    "team": [
      {
        "name": "John Doe",
        "role": "Project Lead",
        "email": "john.doe@example.com"
      }
    ],
    "start_date": "2023-01-15",
    "end_date": "2023-06-30",
    "budget": 500000,
    "technologies": ["Python", "TensorFlow", "PyTorch"],
    "milestones": [
      {
        "name": "Research Phase",
        "completed": true,
        "completion_date": "2023-02-28"
      }
    ],
    "risks": [
      {
        "description": "Data privacy concerns",
        "severity": "Medium",
        "mitigation": "Implemented encryption..."
      }
    ]
  }
]
```

### 2. Get Project by ID
Retrieve details of a specific project by its ID.

**Endpoint:** `GET /projects/{id}`

**Parameters:**
- `id` (integer, required): The ID of the project to retrieve

**Response:**
```json
{
  "id": 1,
  "name": "Project Alpha",
  "status": "Completed",
  "progress": 100,
  "description": "A cutting-edge AI implementation project...",
  "team": [...],
  "start_date": "2023-01-15",
  "end_date": "2023-06-30",
  "budget": 500000,
  "technologies": ["Python", "TensorFlow", "PyTorch"],
  "milestones": [...],
  "risks": [...]
}
```

### 3. Get Project Statistics
Retrieve overall project statistics including completion rates and budget information.

**Endpoint:** `GET /projects/stats`

**Response:**
```json
{
  "total_projects": 4,
  "completed": 1,
  "in_progress": 2,
  "not_started": 1,
  "completion_rate": 25.0,
  "budget": {
    "total": 2150000,
    "spent": 1250000,
    "remaining": 900000
  }
}
```

### 4. Search Projects
Search projects by name, description, team member, or technology.

**Endpoint:** `GET /projects/search`

**Parameters:**
- `q` (string, required): Search query

**Response:**
```json
[
  {
    "id": 1,
    "name": "Project Alpha",
    "status": "Completed",
    "progress": 100,
    "description": "A cutting-edge AI implementation project...",
    "team": [...],
    "start_date": "2023-01-15",
    "end_date": "2023-06-30",
    "budget": 500000,
    "technologies": ["Python", "TensorFlow", "PyTorch"],
    "milestones": [...],
    "risks": [...]
  }
]
```

## Data Models

### Project
| Field | Type | Description |
|-------|------|-------------|
| id | integer | Unique identifier for the project |
| name | string | Name of the project |
| status | string | Current status (Completed/In Progress/Not Started) |
| progress | integer | Progress percentage (0-100) |
| description | string | Detailed project description |
| team | array | List of team members |
| start_date | string | Project start date (YYYY-MM-DD) |
| end_date | string | Project end date (YYYY-MM-DD) |
| budget | integer | Project budget in dollars |
| technologies | array | List of technologies used |
| milestones | array | List of project milestones |
| risks | array | List of project risks |

### Team Member
| Field | Type | Description |
|-------|------|-------------|
| name | string | Team member's name |
| role | string | Team member's role |
| email | string | Team member's email |

### Milestone
| Field | Type | Description |
|-------|------|-------------|
| name | string | Name of the milestone |
| completed | boolean | Whether the milestone is completed |
| completion_date | string | Date of completion (YYYY-MM-DD) |

### Risk
| Field | Type | Description |
|-------|------|-------------|
| description | string | Description of the risk |
| severity | string | Risk severity level |
| mitigation | string | Risk mitigation strategy |

## Error Responses

### 404 Not Found
```json
{
  "message": "Project {id} not found"
}
```

### 401 Unauthorized
```json
{
  "message": "Unauthorized access"
}
```

## Example Usage

### Using cURL
```bash
# Get all projects
curl -X GET "http://localhost:5000/api/projects/" \
     -H "Authorization: Bearer <your_token>"

# Get project by ID
curl -X GET "http://localhost:5000/api/projects/1" \
     -H "Authorization: Bearer <your_token>"

# Get project statistics
curl -X GET "http://localhost:5000/api/projects/stats" \
     -H "Authorization: Bearer <your_token>"

# Search projects
curl -X GET "http://localhost:5000/api/projects/search?q=alpha" \
     -H "Authorization: Bearer <your_token>"
```

### Using Python Requests
```python
import requests

base_url = "http://localhost:5000/api"
headers = {"Authorization": "Bearer <your_token>"}

# Get all projects
response = requests.get(f"{base_url}/projects/", headers=headers)
projects = response.json()

# Get project by ID
response = requests.get(f"{base_url}/projects/1", headers=headers)
project = response.json()

# Get project statistics
response = requests.get(f"{base_url}/projects/stats", headers=headers)
stats = response.json()

# Search projects
response = requests.get(f"{base_url}/projects/search", 
                       params={"q": "alpha"}, 
                       headers=headers)
results = response.json()
```

## Interactive Documentation
For interactive API documentation and testing, visit:
```
http://localhost:5000/api/docs
```
This Swagger UI interface allows you to:
- View all available endpoints
- See request/response models
- Test API calls directly from the browser
- View example requests and responses 