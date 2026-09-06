# AGENTS.md

## Project
ShiftMaster - Aplikasi pengelolaan data shift karyawan. Tech stack: Python/Flask backend, CSS/JS/Bootstrap 5 frontend, JSON file database (akan migrasi ke Firebase).

## Project Rules
- **Max 50 baris per file** — split kode secara agresif
- Nama function harus sesuai dengan fungsi utamanya
- Frontend berstruktur component bersifat reusable
- Logic inti → controller/, model → models/, template → templates/

## Project Structure
```
main.py              # Entry point (Flask app factory)
controller/
  auth.py            # Login/logout routes
  auth_store.py      # User storage (JSON)
  page.py            # Dashboard & register
  module.py          # Route handler untuk 4 modul
  roster.py          # API CRUD roster
  tukar_shift.py     # API CRUD tukar shift
  master_shift.py    # API CRUD master shift
  rekap.py           # API CRUD rekap presensi
models/
  user.py            # Model user (sudah ada)
  employee.py        # Model karyawan
  shift.py           # Model shift type & assignment
  swap.py            # Model tukar shift
  attendance.py      # Model presensi & lembur
templates/           # Jinja2 templates (Bootstrap 5)
static/              # CSS (theme.css), JS (auth.js)
seed.py              # Seed data untuk testing
```

## Setup
```bash
python -m venv env
env\Scripts\activate   # Windows
pip install -r requirements.txt
python seed.py         # Buat sample data
```

## Running
```bash
flask --app main run --debug --port 5000
```

## Current Status

### Implemented
- Auth system (login, register, session, rate limiting, audit log)
- Dashboard dengan navigation ke 4 modul
- Base template dengan sidebar navigation
- Theme CSS (Material Design 3 tokens, dark mode)
- Seed data admin (admin@company.com / admin123)

### In Progress
- 4 module templates (sudah ada tapi hardcoded)
- Models untuk bisnis data

### Not Yet Implemented
- Backend logic untuk 4 modul
- API endpoints untuk CRUD
- Real data integration
- Firebase integration
- Export Excel/PDF
- Role-based access control

## Module Routes
| Route | Page | Status |
|---|---|---|
| `/roster` | Master Roster / Jadwal Shift | Template ready, no backend |
| `/tukar-shift` | Pengajuan Tukar Shift | Template ready, no backend |
| `/master-shift` | Pengaturan Master Shift | Template ready, no backend |
| `/rekap` | Rekap Presensi & Lembur | Template ready, no backend |

## Data Models
- **User** — email, nama, role, password_hash
- **Employee** — id, nama, nip, nik, department, position
- **ShiftType** — code, name, start_time, end_time, color
- **ShiftAssignment** — employee_id, date, shift_code
- **SwapRequest** — id, requester, replacement, reason, status
- **Attendance** — employee_id, date, check_in, check_out, overtime

## Conventions
- Gunakan Flask blueprints untuk menjaga file < 50 baris
- Storage menggunakan JSON files (auth_store.py pattern)
- Setiap model punya to_dict() dan from_dict()
- Template menggunakan Jinja2 + Bootstrap 5
- Route protection: cek session["user_id"]
- ID generated menggunakan UUID atau timestamp

## Template Pattern
```python
# Controller
@bp.route("/endpoint")
def handler():
    err = login_required()
    if err: return err
    data = load_data()
    return render_template("page.html", items=data)

# Template
{% extends "base.html" %}
{% block content %}
<!-- isi konten -->
{% endblock %}
```

## Seed Data
Jalankan `python seed.py` untuk membuat:
- Admin user: admin@company.com / admin123
- 10 sample karyawan (berbagai department)
- 4 shift types (Pagi, Siang, Malam, Off)
- Sample roster 1 minggu
- Sample pengajuan tukar shift
