from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Add custom filter for number formatting
@app.template_filter('number_format')
def number_format(value):
    return "{:,.0f}".format(value)

# Enhanced sample data
sample_data = [
    {
        "id": 1, 
        "name": "Project Alpha", 
        "status": "Completed", 
        "progress": 100,
        "description": "A cutting-edge AI implementation project focusing on natural language processing and machine learning algorithms.",
        "team": [
            {"name": "John Doe", "role": "Project Lead", "email": "john.doe@example.com"},
            {"name": "Jane Smith", "role": "AI Engineer", "email": "jane.smith@example.com"},
            {"name": "Mike Johnson", "role": "Data Scientist", "email": "mike.johnson@example.com"}
        ],
        "start_date": "2023-01-15",
        "end_date": "2023-06-30",
        "budget": 500000,
        "technologies": ["Python", "TensorFlow", "PyTorch", "Docker", "Kubernetes"],
        "milestones": [
            {"name": "Research Phase", "completed": True, "completion_date": "2023-02-28"},
            {"name": "Prototype Development", "completed": True, "completion_date": "2023-04-15"},
            {"name": "Testing Phase", "completed": True, "completion_date": "2023-05-30"},
            {"name": "Deployment", "completed": True, "completion_date": "2023-06-30"}
        ],
        "risks": [
            {"description": "Data privacy concerns", "severity": "Medium", "mitigation": "Implemented encryption and access controls"},
            {"description": "Algorithm accuracy", "severity": "High", "mitigation": "Extended testing phase"}
        ]
    },
    {
        "id": 2, 
        "name": "Project Beta", 
        "status": "In Progress", 
        "progress": 75,
        "description": "Cloud infrastructure migration project to modernize legacy systems and improve scalability.",
        "team": [
            {"name": "Sarah Wilson", "role": "Cloud Architect", "email": "sarah.wilson@example.com"},
            {"name": "David Brown", "role": "DevOps Engineer", "email": "david.brown@example.com"},
            {"name": "Emily Davis", "role": "System Administrator", "email": "emily.davis@example.com"}
        ],
        "start_date": "2023-03-01",
        "end_date": "2023-09-30",
        "budget": 750000,
        "technologies": ["AWS", "Terraform", "Ansible", "Jenkins", "Prometheus"],
        "milestones": [
            {"name": "Infrastructure Assessment", "completed": True, "completion_date": "2023-04-15"},
            {"name": "Migration Planning", "completed": True, "completion_date": "2023-05-30"},
            {"name": "Phase 1 Migration", "completed": True, "completion_date": "2023-07-15"},
            {"name": "Phase 2 Migration", "completed": False, "completion_date": "2023-09-30"}
        ],
        "risks": [
            {"description": "Downtime during migration", "severity": "High", "mitigation": "Scheduled maintenance windows"},
            {"description": "Data integrity", "severity": "High", "mitigation": "Implementing backup and validation procedures"}
        ]
    },
    {
        "id": 3, 
        "name": "Project Gamma", 
        "status": "Not Started", 
        "progress": 0,
        "description": "Mobile application development for customer engagement and service delivery.",
        "team": [
            {"name": "Robert Taylor", "role": "Mobile Developer", "email": "robert.taylor@example.com"},
            {"name": "Lisa Anderson", "role": "UI/UX Designer", "email": "lisa.anderson@example.com"}
        ],
        "start_date": "2023-07-01",
        "end_date": "2023-12-31",
        "budget": 300000,
        "technologies": ["React Native", "Node.js", "MongoDB", "Firebase"],
        "milestones": [
            {"name": "Requirements Gathering", "completed": False, "completion_date": "2023-07-15"},
            {"name": "Design Phase", "completed": False, "completion_date": "2023-08-30"},
            {"name": "Development", "completed": False, "completion_date": "2023-11-15"},
            {"name": "Testing & Launch", "completed": False, "completion_date": "2023-12-31"}
        ],
        "risks": [
            {"description": "App store approval", "severity": "Medium", "mitigation": "Early submission for review"},
            {"description": "User adoption", "severity": "Medium", "mitigation": "User feedback sessions"}
        ]
    },
    {
        "id": 4, 
        "name": "Project Delta", 
        "status": "In Progress", 
        "progress": 50,
        "description": "Data analytics platform for business intelligence and decision making.",
        "team": [
            {"name": "Michael White", "role": "Data Engineer", "email": "michael.white@example.com"},
            {"name": "Jennifer Lee", "role": "Business Analyst", "email": "jennifer.lee@example.com"},
            {"name": "Chris Martin", "role": "Data Scientist", "email": "chris.martin@example.com"}
        ],
        "start_date": "2023-04-15",
        "end_date": "2023-11-30",
        "budget": 600000,
        "technologies": ["Python", "Apache Spark", "Tableau", "Snowflake", "Airflow"],
        "milestones": [
            {"name": "Data Pipeline Setup", "completed": True, "completion_date": "2023-05-30"},
            {"name": "ETL Development", "completed": True, "completion_date": "2023-07-15"},
            {"name": "Dashboard Development", "completed": False, "completion_date": "2023-09-30"},
            {"name": "User Training", "completed": False, "completion_date": "2023-11-30"}
        ],
        "risks": [
            {"description": "Data quality issues", "severity": "High", "mitigation": "Data validation framework"},
            {"description": "Performance optimization", "severity": "Medium", "mitigation": "Load testing and optimization"}
        ]
    }
]

@app.route('/')
def index():
    return render_template('index.html', data=sample_data)

@app.route('/project/<int:project_id>')
def project_detail(project_id):
    project = next((p for p in sample_data if p['id'] == project_id), None)
    if project is None:
        return "Project not found", 404
    return render_template('project_detail.html', project=project)

@app.route('/api/stats')
def project_stats():
    total_projects = len(sample_data)
    completed = sum(1 for p in sample_data if p['status'] == 'Completed')
    in_progress = sum(1 for p in sample_data if p['status'] == 'In Progress')
    not_started = sum(1 for p in sample_data if p['status'] == 'Not Started')
    
    stats = {
        "total_projects": total_projects,
        "completed": completed,
        "in_progress": in_progress,
        "not_started": not_started,
        "completion_rate": (completed / total_projects) * 100 if total_projects > 0 else 0
    }
    return jsonify(stats)

@app.route('/api/search')
def search_projects():
    query = request.args.get('q', '').lower()
    if not query:
        return jsonify([])
    
    results = [
        project for project in sample_data 
        if query in project['name'].lower() or 
           query in project['description'].lower() or
           any(query in member['name'].lower() for member in project['team'])
    ]
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True) 