from datetime import datetime, timezone
from werkzeug.security import generate_password_hash, check_password_hash


class User:
    def __init__(self, email, nama, role="staff", user_id=None):
        self.id = user_id
        self.email = email
        self.nama = nama
        self.role = role
        self.created_at = datetime.now(timezone.utc).isoformat()
        self.password_hash = None

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        if not self.password_hash:
            return False
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        return {
            "email": self.email,
            "nama": self.nama,
            "role": self.role,
            "password_hash": self.password_hash,
            "created_at": self.created_at,
        }

    @staticmethod
    def from_dict(data, user_id=None):
        user = User(
            email=data.get("email"),
            nama=data.get("nama"),
            role=data.get("role", "staff"),
            user_id=user_id,
        )
        user.password_hash = data.get("password_hash")
        user.created_at = data.get("created_at", datetime.now(timezone.utc).isoformat())
        return user
