from app import create_app, db
import os

app = create_app()

with app.app_context():
    db.create_all()
port = int(os.environ.get("PORT", 5000))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)