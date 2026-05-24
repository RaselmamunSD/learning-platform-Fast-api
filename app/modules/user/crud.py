from sqlalchemy.orm import Session
from app.modules.user.models import User

class CRUDUser:
    def get_user_by_email(self, db: Session, email: str) -> User | None:
        return db.query(User).filter(User.email == email).first()

user = CRUDUser()