from flask import render_template, jsonify, request
from app import create_app
from app.api.routes import sample_data

app = create_app()

@app.route('/')
def index():
    return render_template('index.html', data=sample_data)

@app.route('/project/<int:project_id>')
def project_detail(project_id):
    project = next((p for p in sample_data if p['id'] == project_id), None)
    if project is None:
        return render_template('404.html'), 404
    return render_template('project_detail.html', project=project)

@app.route('/docs')
def api_docs():
    return render_template('docs.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True) 