class Attendance:
    def __init__(self, employee_id, date, shift_code, att_id=None):
        self.id = att_id
        self.employee_id = employee_id
        self.date = date
        self.shift_code = shift_code
        self.check_in = ""
        self.check_out = ""
        self.status = "Tepat Waktu"
        self.overtime_hours = 0

    def to_dict(self):
        return {
            "id": self.id,
            "employee_id": self.employee_id,
            "date": self.date,
            "shift_code": self.shift_code,
            "check_in": self.check_in,
            "check_out": self.check_out,
            "status": self.status,
            "overtime_hours": self.overtime_hours,
        }

    @staticmethod
    def from_dict(data):
        att = Attendance(
            employee_id=data.get("employee_id"),
            date=data.get("date"),
            shift_code=data.get("shift_code"),
            att_id=data.get("id"),
        )
        att.check_in = data.get("check_in", "")
        att.check_out = data.get("check_out", "")
        att.status = data.get("status", "Tepat Waktu")
        att.overtime_hours = data.get("overtime_hours", 0)
        return att
