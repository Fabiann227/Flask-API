
# API Autentikasi Pengguna

API ini dibuat menggunakan Flask untuk autentikasi pengguna dengan MySQL sebagai database dan menggunakan Swagger UI untuk dokumentasi.

## Run Locally

Install dependencies

```bash
  pip install -r requirements.txt
```

Create Database (SQL Query)

```bash
  CREATE DATABASE app;
```

Start app

```bash
  python app.py
```

Mengakses Swagger UI

```bash
  http://127.0.0.1:5000/api/docs/
```

## Mengakses Resource yang Dilindungi

### Registrasi Pengguna
- Akses endpoint `POST /api/register` melalui Swagger UI.
- Kirimkan permintaan dengan JSON payload yang berisi `username`, `password`, dan `email`.

### Login Pengguna
- Akses endpoint `POST /api/login` melalui Swagger UI.
- Kirimkan permintaan dengan JSON payload yang berisi `username` dan `password`.
- Jika login berhasil, Anda akan menerima token akses (JWT) dalam respons.

### Mengakses Resource yang Dilindungi
- Akses endpoint `GET /api/protected` melalui Swagger UI.
- Masukkan token akses yang diperoleh sebelumnya dalam header `Authorization` sebagai `Bearer <your_token>`.
   - Contoh header:
     ```
     Authorization: Bearer <your_token>
     ```
- Kirimkan permintaan untuk mengakses resource yang dilindungi.
