# Nama Aplikasi
ShiftMaster - Pengelolaan Data Shift Karyawan

# Tech Stack
Backend: Python, Flask
Frontend: CSS, JavaScript, Bootstrap 5
Database: JSON files (migrasi ke Firebase)
Hosting: Vercel

# Rules
- Max 50 baris per file — split kode secara agresif
- Nama function harus sesuai dengan fungsi utamanya
- Frontend berstruktur component bersifat reusable
- Logic inti → controller/, model database → models/, template → templates/

# Struktur Project
```
main.py              # Entry point
controller/
  auth.py            # Login/logout
  auth_store.py      # User storage
  page.py            # Dashboard & register
  module.py          # Route handler untuk 4 modul
  roster.py          # API CRUD roster
  tukar_shift.py     # API CRUD tukar shift
  master_shift.py    # API CRUD master shift
  rekap.py           # API CRUD rekap presensi
models/
  user.py            # Model user
  employee.py        # Model karyawan
  shift.py           # Model shift type & assignment
  swap.py            # Model tukar shift
  attendance.py      # Model presensi & lembur
templates/           # HTML templates (Bootstrap)
static/              # CSS, JS, assets
seed.py              # Seed data untuk testing
```

# Modul Aplikasi

## 1. Master Roster Jadwal Shift (`/roster`)
- Tampilan matriks jadwal shift mingguan
- Filter berdasarkan nama, unit kerja, shift
- Tambah/edit/hapus penugasan shift
- Navigasi minggu (prev/next)
- KPI: personil aktif, keterisian, kurang staf, review tukar
- Monitoring kuota shift per hari (min personil)
- Export ke Excel/PDF

## 2. Pengajuan Tukar Shift (`/tukar-shift`)
- Daftar pengajuan tukar dengan status (menunggu, disetujui, ditolak)
- Detail perbandingan shift kedua belah pihak
- Validasi otomatis (jam istirabat minimum, deteksi lembur)
- Approve/reject dengan catatan
- Upload dokumen pendukung
- Form pengajuan mandiri oleh karyawan

## 3. Pengaturan Master Shift (`/master-shift`)
- Template shift (Pagi, Siang, Malam, Off)
- Konfigurasi jam kerja, durasi, toleransi
- Aturan bisnis (jam istirabat minimum, max hari berturut, batas lembur)
- Riwayat perubahan konfigurasi
- Validasi rasio medis per unit kerja

## 4. Rekap Presensi & Lembur (`/rekap`)
- Tabel presensi lengkap (check-in/out, status kepatuhan)
- Tracking jam lembur per karyawan
- Filter nama, unit kerja, status, tanggal
- Distribusi lembur per unit kerja
- Export rekap untuk payroll

# Data Models

## Employee
- id, nama, nip, nik, department, position, status_aktif

## ShiftType
- code, name, start_time, end_time, duration, color

## ShiftAssignment
- employee_id, date, shift_code

## SwapRequest
- id, requester_id, replacement_id, requester_shift_date, replacement_shift_date, reason, document, status, approved_by, created_at

## Attendance
- employee_id, date, shift_code, check_in, check_out, status, overtime_hours

# Seed Data
- 1 admin user (admin@company.com / admin123)
- 10 sample karyawan dari berbagai unit kerja
- 4 shift types (Pagi, Siang, Malam, Off)
- Sample roster untuk 1 minggu
- Sample pengajuan tukar shift

# Development Phases

## Phase 1: Foundation (Saat Ini)
- [x] Setup project structure
- [x] Implementasi auth (login, register, session)
- [x] Buat model User
- [x] Buat seed data admin
- [ ] Buat model Employee, ShiftType
- [ ] Buat requirements.txt

## Phase 2: Core Models & CRUD
- [ ] Buat model ShiftAssignment, SwapRequest, Attendance
- [ ] Buat API controller untuk roster
- [ ] Buat API controller untuk tukar shift
- [ ] Buat API controller untuk master shift
- [ ] Buat API controller untuk rekap

## Phase 3: Frontend Integration
- [ ] Wire up roster template dengan data real
- [ ] Wire up tukar-shift template dengan data real
- [ ] Wire up master-shift template dengan data real
- [ ] Wire up rekap template dengan data real
- [ ] Tambah JavaScript untuk interaksi (filter, search, pagination)

## Phase 4: Advanced Features
- [ ] Export Excel/PDF
- [ ] Validasi otomatis aturan shift
- [ ] Dashboard analytics
- [ ] Role-based access control (admin vs staff)

## Phase 5: Deployment
- [ ] Setup Firebase
- [ ] Konfigurasi Vercel
- [ ] Environment variables
- [ ] Testing & bug fixing
