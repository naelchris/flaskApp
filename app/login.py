from app import app

@app.route("/login")
def login():
    return "login views"