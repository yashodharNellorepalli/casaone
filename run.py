# Initialising and starting Server
from app import app

if __name__ == "main":
    app.run(host='0.0.0.0', port=8081, debug=True, threaded=True)
