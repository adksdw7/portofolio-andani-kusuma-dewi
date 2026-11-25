# Andani Kusuma Dewi — Streamlit Portfolio

## Struktur folder

```text
andani_portfolio_streamlit/
├── app.py
├── requirements.txt
└── assets/
    ├── slide_01.png
    ├── slide_02.png
    ├── ...
    └── slide_09.png
```

## Menjalankan di komputer

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy ke Streamlit Community Cloud

1. Upload seluruh isi folder ini ke satu repository GitHub.
2. Buka https://share.streamlit.io/
3. Pilih repository dan branch.
4. Set **Main file path** menjadi `app.py`.
5. Deploy.

## Catatan desain dan tautan

- Setiap halaman PDF diekspor menjadi gambar PNG beresolusi tinggi agar desain, tipografi, latar, dan posisi elemen tetap sama dengan PDF.
- Gambar dipasang dalam kanvas responsif 16:9. Semua hotspot menggunakan koordinat persentase, sehingga ikut membesar/mengecil bersama halaman ketika browser di-zoom atau ukuran layar berubah.
- Kontak pada halaman 1: LinkedIn, email (subjek sudah diisi), dan WhatsApp.
- Proyek pada halaman 2–4 memiliki area hover dan tautan sesuai instruksi.
- Proyek PAUDQu dan halaman pengalaman/sertifikat tetap visual karena tidak diberikan tautan publik.
- Bila ingin mengganti tampilan cover di kemudian hari, ganti `assets/slide_01.png` dengan gambar cover baru berukuran 16:9. Jika posisi kontak berubah, sesuaikan tiga `rect` pada bagian PAGE 1 di `app.py`.

## Catatan tautan Islamic Pilgrimage

Pada instruksi awal, tautan yang ditulis untuk Student Stress juga muncul pada item Islamic Pilgrimage berikutnya. Implementasi ini memasangkan:
- Student Stress → tautan `82787c28-82b4-4451-8bb2-77becf1ca070`
- Islamic Pilgrimage → tautan `25f2a4d6-e8b3-4078-8fb4-297f915cc810`

Pastikan pasangan tautan ini memang yang dimaksud sebelum deploy.
