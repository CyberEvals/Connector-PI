from flask_restx import Api, Resource, fields
from app.api.routes import sample_data

api = Api(
    title='Project Dashboard API',
    version='1.0',
    description='A comprehensive API for managing and tracking project information',
    doc='/api/docs',
    prefix='/api'
)

# Namespace for projects
ns = api.namespace('projects', description='Project operations')

# Models for documentation
project_model = api.model('Project', {
    'id': fields.Integer(description='Project ID'),
    'name': fields.String(description='Project name'),
    'status': fields.String(description='Project status'),
    'progress': fields.Integer(description='Project progress percentage'),
    'description': fields.String(description='Project description'),
    'team': fields.List(fields.Nested(api.model('TeamMember', {
        'name': fields.String,
        'role': fields.String,
        'email': fields.String
    }))),
    'start_date': fields.String(description='Project start date'),
    'end_date': fields.String(description='Project end date'),
    'budget': fields.Integer(description='Project budget'),
    'technologies': fields.List(fields.String),
    'milestones': fields.List(fields.Nested(api.model('Milestone', {
        'name': fields.String,
        'completed': fields.Boolean,
        'completion_date': fields.String
    }))),
    'risks': fields.List(fields.Nested(api.model('Risk', {
        'description': fields.String,
        'severity': fields.String,
        'mitigation': fields.String
    })))
})

stats_model = api.model('Stats', {
    'total_projects': fields.Integer,
    'completed': fields.Integer,
    'in_progress': fields.Integer,
    'not_started': fields.Integer,
    'completion_rate': fields.Float,
    'budget': fields.Nested(api.model('Budget', {
        'total': fields.Integer,
        'spent': fields.Integer,
        'remaining': fields.Integer
    }))
})

@ns.route('/')
class ProjectList(Resource):
    @ns.doc('list_projects')
    @ns.marshal_list_with(project_model)
    def get(self):
        """List all projects"""
        return sample_data

@ns.route('/<int:project_id>')
@ns.param('project_id', 'The project identifier')
class Project(Resource):
    @ns.doc('get_project')
    @ns.marshal_with(project_model)
    def get(self, project_id):
        """Fetch a project given its identifier"""
        project = next((p for p in sample_data if p['id'] == project_id), None)
        if project is None:
            api.abort(404, f"Project {project_id} not found")
        return project

@ns.route('/stats')
class ProjectStats(Resource):
    @ns.doc('get_stats')
    @ns.marshal_with(stats_model)
    def get(self):
        """Get project statistics"""
        total_projects = len(sample_data)
        completed = sum(1 for p in sample_data if p['status'] == 'Completed')
        in_progress = sum(1 for p in sample_data if p['status'] == 'In Progress')
        not_started = sum(1 for p in sample_data if p['status'] == 'Not Started')
        
        total_budget = sum(p['budget'] for p in sample_data)
        spent_budget = sum(p['budget'] * (p['progress'] / 100) for p in sample_data)
        
        return {
            "total_projects": total_projects,
            "completed": completed,
            "in_progress": in_progress,
            "not_started": not_started,
            "completion_rate": (completed / total_projects) * 100 if total_projects > 0 else 0,
            "budget": {
                "total": total_budget,
                "spent": spent_budget,
                "remaining": total_budget - spent_budget
            }
        }

@ns.route('/search')
class ProjectSearch(Resource):
    @ns.doc('search_projects')
    @ns.param('q', 'Search query')
    @ns.marshal_list_with(project_model)
    def get(self):
        """Search projects by name, description, team member, or technology"""
        query = ns.payload.get('q', '').lower()
        if not query:
            return []
        
        results = [
            project for project in sample_data 
            if query in project['name'].lower() or 
               query in project['description'].lower() or
               any(query in member['name'].lower() for member in project['team']) or
               any(query in tech.lower() for tech in project['technologies'])
        ]
        return results 