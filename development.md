Berikut rencana tugas untuk autentikasi login email/sandi tanpa SSO, dengan fokus mobile-first dan dark mode. Saya buatkan dalam bentuk result.md yang ringkas.
result.md — Rencana Tugas Autentikasi (Tanpa SSO, Mobile-first, Dark Mode)
Tujuan
- Sediakan alur login email/sandi yang sederhana, aman, dan responsif untuk perangkat seluler.
- Aktifkan dark mode dari sisi klien dengan persistensi preferensi pengguna.
- Pastikan keamanan sesi dan privasi data tetap terjaga.
Tiket-tiket Pekerjaan (inklema MVP)
1. Desain dan Prototipe
- Deskripsi: Rancang alur login mobile-first, halaman login, dan komponen terkait (form, tombol, pesan error).
- Keluaran: wireframe/sketsa halaman login, daftar komponen UI (form email, sandi, tombol masuk, tautan lupa sandi).
- Durasi: 1 hari
- Prioritas: Tinggi
2. Backend: Rute Autentikasi
- Deskripsi: Siapkan rute /auth/login, /auth/logout, /auth/session, dan endpoint terkait sesi.
- Detail: Gunakan sesi HTTP-only cookie, issued on login, expired setelah periode tertentu; terapkan CSRF token pada permintaan yang mengubah status autentikasi.
- Durasi: 2 hari
- Prioritas: Tinggi
3. Penyimpanan Sesi dan Keamanan
- Deskripsi: Tentukan penyimpanan sesi (server-side atau cookie terenkripsi), hash sandi di server, dan kebijakan sesi.
- Detail: Terapkan hashing sandi (mis. bcrypt/argon2), sesi aman, token anti-CSRF, dan audit log untuk upaya login.
- Durasi: 2 hari
- Prioritas: Tinggi
4. Frontend: Halaman Login Mobile-first
- Deskripsi: Bangun halaman login responsif dengan form email + sandi, pesan error yang jelas, dan aksi tautan lupa sandi.
- Detail: Gunakan layout fluid, spesifikasi ukuran tap target yang memadai untuk ponsel, serta pengelolaan state form (email, sandi, validasi klien).
- Durasi: 2 hari
- Prioritas: Tinggi
5. Dark Mode
- Deskripsi: Implementasikan tema gelap yang dapat diaktifkan/dinonaktifkan dari UI.
- Detail: Gunakan CSS variabel atau mekanisme tema serupa; simpan preferensi pengguna (localStorage atau cookie) dan terapkan pada seluruh komponen UI; pastikan kontras tetap memadai.
- Durasi: 1–2 hari
- Prioritas: Sedang
6. Integrasi Sesi dan Pengalihan
- Deskripsi: Setelah login berhasil, pengguna dialihkan ke dashboard atau halaman default; pertahankan sesi di seluruh rute yang dilindungi.
- Detail: Terapkan penanganan sesi di sisi klien dan server, serta mekanisme logout yang aman.
- Durasi: 1–2 hari
- Prioritas: Sedang
7. Pengujian dan QA
- Deskripsi: Uji fungsionalitas login di perangkat mobile dan desktop, uji dark mode, dan uji aksesibilitas.
- Detail: Pengujian alur login, pengeluaran pesan error, persistensi sesi, dan kontras warna dalam tema gelap.
- Durasi: 2 hari
- Prioritas: Sedang
8. Keamanan dan Audit
- Deskripsi: Terapkan logging untuk upaya login, serta mekanisme perlindungan terhadap serangan brute-force (misalnya rate limiting).
- Detail: Pastikan transport terenkripsi (HTTPS) dan audit log hanya menyimpan metadata yang diperlukan.
- Durasi: 1 hari
- Prioritas: Sedang
9. Dokumentasi dan Pelatihan
- Deskripsi: Dokumentasikan alur autentikasi, endpoint, serta panduan penggunaan dark mode.
- Detail: Sertakan contoh permintaan/respons, cara mengaktifkan dark mode, dan catatan keamanan sesi.
- Durasi: 1 hari
- Prioritas: Rendah
10. Rilis Bertahap
- Deskripsi: Rencanakan rilis MVP dengan fitur login email/sandi, dark mode dasar, dan perlindungan sesi.
- Detail: Rilis ke environment pengujian lalu produksi, pantau metrik keamanan dan pengalaman pengguna.
- Durasi: 1 hari
- Prioritas: Sedang
Durasi total (estimasi)
- Rangkuman kasar: 10–14 hari kerja untuk MVP (bisa bervariasi tergantung kecepatan iterasi dan panjangnya sesi kerja per hari).
Struktur file yang disarankan untuk pelacakan
- result.md (dokumen ini)
- auth/
- backend: routes/login, logout, session; middleware CSRF; sesi
- frontend: login.html (atau login page komponen), login.css, login.js
- styles/
- theme.css (dark mode), variables.css
- utils/
- auth.js (manajemen sesi, CSRF)
- storage.js (preferensi tema)