from project_management import db,app
if __name__=="__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)