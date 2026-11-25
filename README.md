# Andani Kusuma Dewi — Interactive Streamlit Portfolio

Website portofolio responsif yang dibangun ulang menggunakan Streamlit + HTML/CSS.
Desain memakai palet biru dongker, kartu proyek interaktif, efek hover, dan gambar asli
dari folder `assets/`. Tidak menggunakan halaman PDF sebagai gambar latar.

## Struktur folder

```text
andani_portfolio_interactive/
├── app.py
├── requirements.txt
├── README.md
└── assets/
    ├── diriku.png
    ├── bnsp.png
    ├── kemiskinan.png
    ├── colabKemiskinan.png
    ├── sd.png
    ├── stress.png
    ├── islam.png
    ├── skripsi.png
    ├── UIUX.png
    ├── tim.png
    ├── aslab.png
    ├── swimplash.png
    ├── gsb.png
    ├── pkkmb1.png
    ├── pkkmb2.png
    ├── pkkmb3.png
    ├── seminarDA.png
    ├── mp.png
    ├── pengenalanDA.png
    ├── excel.png
    └── sql.png
```

## Menjalankan secara lokal

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
streamlit run app.py
```

## Deploy ke Streamlit Community Cloud

1. Buat repository GitHub baru.
2. Upload `app.py`, `requirements.txt`, `README.md`, dan seluruh folder `assets/`.
3. Buka https://share.streamlit.io/
4. Pilih repository dan branch.
5. Isi Main file path: `app.py`.
6. Deploy.

## Interaksi dan responsivitas

- Kartu proyek memiliki efek hover: gambar membesar ringan, kartu terangkat, dan label proyek muncul.
- Klik kartu proyek membuka dashboard atau prototype pada tab baru.
- Kontak LinkedIn, email, dan WhatsApp dapat diklik.
- Layout memakai CSS Grid, Flexbox, `clamp()`, dan media query. Elemen mengalir dan menyesuaikan lebar layar, bukan memakai koordinat tetap, sehingga tetap rapi pada zoom browser dan perangkat berbeda.
- Warna utama biru dongker `#101F46`, dengan putih dan abu-abu terang sebagai warna pendamping.
- Tidak menggunakan motif batik, sesuai arahan terakhir.

## Pemetaan gambar

Nama file gambar sudah mengikuti daftar yang diberikan. Jika nama file diubah, sesuaikan pemanggilan pada `app.py`.

## Catatan tautan

- BNSP Data Analyst: tombol Notebook dan Dashboard dibuat terpisah.
- Student Stress menggunakan tautan `82787c28-82b4-4451-8bb2-77becf1ca070`.
- Islamic Pilgrimage menggunakan tautan `25f2a4d6-e8b3-4078-8fb4-297f915cc810`.
  Instruksi sebelumnya menuliskan tautan Student Stress pada item Islamic Pilgrimage juga; tautan yang berbeda dipakai untuk Islamic Pilgrimage.
- PAUDQu tidak diberi tautan eksternal karena belum dipublikasikan; kartu hanya menampilkan dokumentasi gambar.
- Gambar sertifikat ditampilkan di bagian akhir sesuai arahan.

## Catatan penyesuaian konten

Teks proyek dan pengalaman mengikuti materi portofolio `idePorto.pdf`. Bila ada deskripsi yang ingin dipersingkat atau dikoreksi, ubah bagian teks pada `app.py`; gambar dan tata letak tidak perlu diubah.
