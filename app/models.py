from app import app, db


class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jobtitle = db.Column(db.String(100))
    company = db.Column(db.String(200))
    city = db.Column(db.String(200))
    state = db.Column(db.String(2))
    zip = db.Column(db.String(5))
    descr = db.Column(db.String(1000))
    jstatus = db.Column(db.String(200))
    link = db.Column(db.String(1000))
    duties = db.Column(db.Text)
    requi = db.Column(db.Text)
    post_date = db.Column(db.Date)
