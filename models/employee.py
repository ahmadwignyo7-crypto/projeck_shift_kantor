class Employee:
    def __init__(self, nama, nip, nik, department, position, emp_id=None):
        self.id = emp_id
        self.nama = nama
        self.nip = nip
        self.nik = nik
        self.department = department
        self.position = position
        self.status_aktif = True

    def to_dict(self):
        return {
            "id": self.id,
            "nama": self.nama,
            "nip": self.nip,
            "nik": self.nik,
            "department": self.department,
            "position": self.position,
            "status_aktif": self.status_aktif,
        }

    @staticmethod
    def from_dict(data):
        emp = Employee(
            nama=data.get("nama"),
            nip=data.get("nip"),
            nik=data.get("nik"),
            department=data.get("department"),
            position=data.get("position"),
            emp_id=data.get("id"),
        )
        emp.status_aktif = data.get("status_aktif", True)
        return emp
