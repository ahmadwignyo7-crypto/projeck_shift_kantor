class ShiftType:
    def __init__(self, code, name, start, end, color, shift_id=None):
        self.id = shift_id
        self.code = code
        self.name = name
        self.start_time = start
        self.end_time = end
        self.color = color

    def to_dict(self):
        return {
            "id": self.id,
            "code": self.code,
            "name": self.name,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "color": self.color,
        }

    @staticmethod
    def from_dict(data):
        return ShiftType(
            code=data.get("code"),
            name=data.get("name"),
            start=data.get("start_time"),
            end=data.get("end_time"),
            color=data.get("color"),
            shift_id=data.get("id"),
        )


class ShiftAssignment:
    def __init__(self, employee_id, date, shift_code, assign_id=None):
        self.id = assign_id
        self.employee_id = employee_id
        self.date = date
        self.shift_code = shift_code

    def to_dict(self):
        return {
            "id": self.id,
            "employee_id": self.employee_id,
            "date": self.date,
            "shift_code": self.shift_code,
        }

    @staticmethod
    def from_dict(data):
        return ShiftAssignment(
            employee_id=data.get("employee_id"),
            date=data.get("date"),
            shift_code=data.get("shift_code"),
            assign_id=data.get("id"),
        )
