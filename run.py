from app import create_app

app=create_app()

# this allows automatic updates to be displayed in the website (real-time updation)
if __name__=="__main__":
    app.run(debug=True)