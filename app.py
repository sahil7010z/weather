from flask import Flask, render_template
from routes.dashboard import dashboard_bp
from routes.api_routes import api_bp
import os

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(dashboard_bp)
app.register_blueprint(api_bp)

@app.route('/')
def home():
    return render_template('try_now.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # for Render dynamic port
    app.run(host='0.0.0.0', port=port)
