from flask import Flask, send_from_directory
import os
from routes import project_bp, task_bp

app = Flask(__name__, static_folder="frontend/build")

# Ensure the database is created
if not os.path.exists('projects.db'):
    from db import create_database
    create_database()
    print("DB created!")

# Register blueprints
app.register_blueprint(project_bp)
app.register_blueprint(task_bp)
# app.register_blueprint(file_bp)


# Route to serve frontend
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_react(path):
    if path and os.path.exists(f"frontend/build/{path}"):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)