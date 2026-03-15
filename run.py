from app import create_app, db

app=create_app()

with app.app_context():
    db.create_all()
# this allows automatic updates to be displayed in the website (real-time updation)
if __name__=="__main__":
    app.run(debug=True)