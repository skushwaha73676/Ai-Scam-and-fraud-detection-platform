from app import db
from datetime import datetime
class FraudReport(db.Model):
    __tablename__="fraud_reports"
    id=db.Column(db.Integer,primary_key=True)
    user_id=db.Column(db.Integer,db.ForeignKey("users.id"))
    entity_type=db.Column(db.String(30))
    entity_value=db.Column(db.String(255))
    scam_type=db.Column(db.String(50))
    description=db.Column(db.Text)
    status=db.Column(db.String(20),default="Pending")
    created_at=db.Column(db.DateTime,default=datetime.utcnow)
class Feedback(db.Model):
    __tablename__="feedback"
    id=db.Column(db.Integer,primary_key=True)
    scan_id=db.Column(db.Integer,db.ForeignKey("scan_history.id"))
    user_id=db.Column(db.Integer,db.ForeignKey("users.id"))
    feedback=db.Column(db.String(20))
    comments=db.Column(db.Text)
    created_at=db.Column(db.DateTime,default=datetime.utcnow)
