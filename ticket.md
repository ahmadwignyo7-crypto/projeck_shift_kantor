# Tiket Lokal — Autentikasi (Tanpa SSO)

## Ringkasan
Login email/sandi, mobile-first, dark mode, sesi aman. Target selesai: 1 hari.

---

## Daftar Tiket

### T-001 | Persiapan Proyek & Struktur File
- **Prioritas:** Tinggi
- **Estimasi:** 1 jam
- **Status:** To Do
- **Deskripsi:**
  - Buat folder `auth/`, `auth/routes/`, `auth/middleware/`
  - Siapkan file konfigurasi sesi
  - Pastikan dependensi terinstal (express/session, bcrypt, dll)

---

### T-002 | Skema Database Pengguna
- **Prioritas:** Tinggi
- **Estimasi:** 1 jam
- **Status:** To Do
- **Deskripsi:**
  - Buat model `User` dengan field: id, email, password_hash, nama, role, created_at
  - Buat migrasi atau inisialisasi collection di Firebase
  - Validasi field wajib

---

### T-003 | Rute Autentikasi Backend
- **Prioritas:** Tinggi
- **Estimasi:** 2 jam
- **Status:** To Do
- **Deskripsi:**
  - `POST /auth/login` — verifikasi email + sandi, terbitkan sesi
  - `POST /auth/logout` — hancurkan sesi
  - `GET /auth/session` — cek status sesi aktif
  - Terapkan CSRF token pada rute yang mengubah status

---

### T-004 | Middleware Sesi & Keamanan
- **Prioritas:** Tinggi
- **Estimasi:** 1 jam
- **Status:** To Do
- **Deskripsi:**
  - Konfigurasi session store (HTTP-only cookie)
  - Hash sandi dengan bcrypt saat registrasi/login
  - Rate limiting pada `/auth/login` (maks 5 percobaan/menit)
  - Audit log sederhana (email, waktu, status login)

---

### T-005 | Halaman Login Frontend (Mobile-first)
- **Prioritas:** Tinggi
- **Estimasi:** 2 jam
- **Status:** To Do
- **Deskripsi:**
  - Form email + sandi dengan layout responsif
  - Tombol "Masuk" berukuran besar untuk tap target
  - Tautan "Lupa Sandi?" (placeholder untuk fase berikutnya)
  - Pesan error yang jelas (email/sandi salah, field kosong)
  - Toggle tampilkan/sembunyikan sandi

---

### T-006 | Dark Mode
- **Prioritas:** Sedang
- **Estimasi:** 1 jam
- **Status:** To Do
- **Deskripsi:**
  - Buat `theme.css` dengan CSS variabel untuk tema terang/gelap
  - Toggle dark mode di halaman login
  - Simpan preferensi di localStorage
  - Pastikan kontras warna memadai (WCAG AA)

---

### T-007 | Integrasi Sesi & Pengalihan
- **Prioritas:** Sedang
- **Estimasi:** 1 jam
- **Status:** To Do
- **Deskripsi:**
  - Setelah login → redirect ke `/dashboard`
  - Cek sesi di rute yang dilindungi
  - Jika tidak ada sesi → redirect ke `/login`
  - Logout bersih (hapus cookie + session)

---

### T-008 | Pengujian
- **Prioritas:** Sedang
- **Estimasi:** 1 jam
- **Status:** To Do
- **Deskripsi:**
  - Uji login berhasil + gagal (email/sandi salah)
  - Uji responsivitas di layar 320px, 768px, 1024px
  - Uji dark mode aktif/nonaktif
  - Uji sesi berakhir otomatis

---

## Total Estimasi: ~10 jam (1 hari kerja)