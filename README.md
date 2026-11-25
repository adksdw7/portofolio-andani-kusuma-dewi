# Andani Kusuma Dewi — Interactive Portfolio

Portofolio interaktif berbasis Streamlit. Desain dibangun ulang dari elemen HTML/CSS,
bukan menampilkan halaman PDF sebagai gambar. Susunan bagian dan redaksi konten
mengacu pada `idePorto.pdf`.

## Isi folder

```text
andani_portfolio_final/
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
    ├── sql.png
    └── logo.png  # tambahkan file logo tools Anda di sini
```

## Logo tools pada cover

Tambahkan gambar gabungan logo tools bernama **`logo.png`** ke folder `assets`.
Ukuran yang disarankan: lebar 1000–1400 px, tinggi 120–220 px, latar transparan
atau putih. Kode sudah disiapkan untuk menampilkannya. Jika belum ada, area logo
menampilkan pesan pengingat dan aplikasi tetap dapat dijalankan.

## Menjalankan secara lokal

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy ke Streamlit Community Cloud

1. Unggah `app.py`, `requirements.txt`, `README.md`, dan folder `assets/` ke GitHub.
2. Buka https://share.streamlit.io/
3. Pilih repository dan branch.
4. Main file path: `app.py`.
5. Klik Deploy.

## Desain dan interaksi

- Warna teks dan bidang latar utama hanya putih `#FFFFFF` dan biru dongker `#0D1C42`.
- Motif batik tidak digunakan.
- Bidang latar putih/dongker membentang selebar halaman, bergantian mengikuti bagian portofolio.
- Layout menggunakan CSS Grid/Flexbox, persentase, `clamp()`, dan media query agar menyesuaikan zoom dan ukuran layar.
- Cover meniru komposisi cover `idePorto.pdf`: judul serif besar, bidang nama miring, foto berbingkai lengkung, bubble bidang, logo tools, kontak, dan ringkasan profil.
- Kartu proyek menampilkan label saat pointer diarahkan ke gambar.
- BNSP memiliki gambar dashboard, notebook Colab, dan sertifikat; dashboard dan notebook memakai hover label dan tautan masing-masing.
- PAUDQu tidak memiliki tautan eksternal karena proyek belum dipublikasikan.

## Tautan

- LinkedIn: https://linkedin.com/in/andani-kusuma-dewi-660441324
- Email: mailto dengan subjek Portofolio Andani Kusuma Dewi
- WhatsApp: https://wa.me/6281270052004
- BNSP dashboard dan notebook, pendidikan, student stress, Islamic Pilgrimage,
  E-Wallet, dan Student Connect menggunakan URL yang telah diberikan.
