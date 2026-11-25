from pathlib import Path
import base64
import html
import streamlit as st

# ============================================================
# ANDANI KUSUMA DEWI — PORTFOLIO
# Responsive, full-width portfolio inspired by idePorto.pdf.
# Original wording is retained; assets are loaded from /assets.
# ============================================================

st.set_page_config(
    page_title="Andani Kusuma Dewi | Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

ROOT = Path(__file__).parent
ASSETS = ROOT / "assets"

NAVY = "#0D1C42"
WHITE = "#FFFFFF"

LINKEDIN = "https://linkedin.com/in/andani-kusuma-dewi-660441324"
EMAIL = "mailto:andanikd754@gmail.com?subject=Portofolio%20Andani%20Kusuma%20Dewi"
WHATSAPP = "https://wa.me/6281270052004"

URL = {
    "bnsp_dashboard": "https://datastudio.google.com/reporting/8879aca4-37ec-4f78-a8db-bc3ce7c74197",
    "bnsp_colab": "https://colab.research.google.com/drive/10c5SLmhYozUxTug0a_TGbIJpymHd8Yuf?usp=sharing",
    "education": "https://datastudio.google.com/reporting/54d49033-80d8-4006-8635-279ec0f0842f",
    "stress": "https://datastudio.google.com/reporting/82787c28-82b4-4451-8bb2-77becf1ca070",
    "pilgrimage": "https://datastudio.google.com/reporting/25f2a4d6-e8b3-4078-8fb4-297f915cc810",
    "ewallet": "https://skripsisentimen.streamlit.app",
    "student_connect": "https://www.figma.com/proto/E4wcdZogSWRF1eDzpngJ4M?node-id=157-2&t=OQWxTboJfkqaujwa-6",
}

def image_data(filename: str) -> str:
    """Load an image from assets and return an embeddable data URI."""
    path = ASSETS / filename
    if not path.is_file():
        return ""
    ext = path.suffix.lower()
    mime = "jpeg" if ext in (".jpg", ".jpeg") else ext.lstrip(".")
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:image/{mime};base64,{encoded}"

def image(filename: str, alt: str, css_class: str = "") -> str:
    src = image_data(filename)
    if not src:
        return f'<div class="missing">{html.escape(filename)} belum ada di folder assets</div>'
    return (
        f'<img class="{css_class}" src="{src}" '
        f'alt="{html.escape(alt)}" loading="lazy">'
    )

def band(content: str, theme: str = "white", extra: str = "") -> str:
    return f'<section class="band {theme} {extra}"><div class="inner">{content}</div></section>'

def heading(kicker: str, title: str, subtitle: str = "") -> str:
    sub = f'<p class="subtitle">{subtitle}</p>' if subtitle else ""
    return (
        f'<div class="heading"><div class="kicker">{kicker}</div>'
        f'<h2>{title}</h2>{sub}</div>'
    )

def bubble(text: str) -> str:
    return f'<span class="bubble">{text}</span>'

def linked_image(filename: str, alt: str, url: str, label: str, css_class: str = "") -> str:
    return (
        f'<a class="image-link {css_class}" href="{url}" target="_blank" '
        f'rel="noopener noreferrer" aria-label="{label}">'
        f'<div class="image-wrap">{image(filename, alt)}'
        f'<span class="hover-label">{label}</span></div></a>'
    )

def project_card(filename: str, category: str, title: str, description: str,
                 url: str, label: str = "Lihat Dashboard", tools: tuple = ()) -> str:
    tags = "".join(bubble(t) for t in tools)
    return f"""
    <a class="project-card" href="{url}" target="_blank" rel="noopener noreferrer">
      <div class="image-wrap">
        {image(filename, title)}
        <span class="hover-label">{label}</span>
      </div>
      <div class="project-copy">
        <div class="card-kicker">{category}</div>
        <h3>{title}</h3>
        <p>{description}</p>
        <div class="tag-row">{tags}</div>
      </div>
    </a>"""

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Playfair+Display:wght@500;600;700&display=swap');

:root { --navy:#0D1C42; --white:#FFFFFF; }
html { scroll-behavior:smooth; }
#MainMenu, footer, header, [data-testid="stSidebar"] {display:none !important;}
.stApp {background:var(--white); color:var(--navy);}
.block-container {
  max-width:none !important; width:100% !important;
  padding:0 !important; margin:0 !important;
}
div[data-testid="stVerticalBlock"] {gap:0;}
.portfolio {font-family:'DM Sans',Arial,sans-serif;color:var(--navy);}
.band {
  width:100%; margin:0; padding:clamp(2.6rem,5.5vw,5.5rem) 0;
  box-sizing:border-box;
}
.band.white {background:var(--white);color:var(--navy);}
.band.navy {background:var(--navy);color:var(--white);}
.inner {width:min(1320px, calc(100% - clamp(2rem,8vw,9rem)));margin:0 auto;}
.heading {margin:0 0 1.8rem;}
.kicker {
  font-size:.75rem; font-weight:800; letter-spacing:.18em;
  text-transform:uppercase; margin-bottom:.5rem;
}
.white .kicker {color:var(--navy);}
.navy .kicker {color:var(--white);}
.heading h2 {
  margin:0; font-family:'DM Sans',Arial,sans-serif; font-size:clamp(1.8rem,3.2vw,3rem);
  font-weight:800; line-height:1.12; letter-spacing:-.035em;
}
.subtitle {margin:.65rem 0 0;max-width:900px;font-size:1rem;line-height:1.7;}
.white .subtitle {color:var(--navy);}
.navy .subtitle {color:var(--white);}

/* COVER — large serif lettering, skewed name plaque, arched portrait. */
.cover {background:var(--white);padding:clamp(2rem,4.5vw,4.7rem) 0;}
.cover-grid {display:grid;grid-template-columns:1.15fr .85fr;gap:clamp(2rem,5vw,5.5rem);align-items:center;}
.cover-left {min-width:0;}
.cover-title {
  display:inline-block; position:relative; z-index:1;
  background:var(--navy); color:var(--white);
  font-family:'Playfair Display',Georgia,serif;
  font-size:clamp(4.2rem,10.5vw,9rem);line-height:.95;letter-spacing:-.055em;
  padding:.04em .16em .10em; border-radius:10px 18px 8px 16px;
  transform:rotate(-2deg); box-shadow:12px 13px 0 var(--white);
}
.name-plaque {
  position:relative; z-index:2; width:max-content; max-width:90%;
  margin:-.05rem 0 2.1rem clamp(7rem,24vw,23rem);
  padding:1rem 1.7rem;background:var(--navy);color:var(--white);
  font-family:'Playfair Display',Georgia,serif;
  font-size:clamp(1.4rem,3vw,2.5rem);white-space:nowrap;
  border-radius:8px 14px 8px 14px;transform:rotate(1.5deg);
}
.cover-pills {display:flex;flex-wrap:wrap;gap:.55rem;margin:1.3rem 0 1.5rem;}
.cover-pill {
  display:inline-flex;align-items:center;justify-content:center;
  padding:.55rem 1rem;border-radius:999px;background:var(--navy);
  color:var(--white);font-size:clamp(.8rem,1.2vw,1.05rem);font-weight:500;
}
.logo-strip {
  display:flex;align-items:center;justify-content:center;
  width:min(100%,560px);min-height:76px;padding:.6rem 1rem;
  background:var(--navy);border-radius:24px;margin:1.2rem 0;
}
.logo-strip img {display:block;width:100%;max-height:66px;object-fit:contain;}
.logo-missing {font-size:.85rem;color:var(--white);}
.contact-list {display:flex;flex-direction:column;align-items:flex-start;gap:.55rem;margin-top:1rem;}
.contact {
  display:inline-flex;align-items:center;gap:.55rem;max-width:100%;
  background:var(--navy);color:var(--white)!important;
  border-radius:8px;padding:.4rem .7rem;font-size:clamp(.78rem,1.25vw,1rem);
  text-decoration:underline!important;transition:transform .2s ease;
}
.contact:hover {transform:translateX(7px);}
.cover-right {display:flex;flex-direction:column;align-items:center;justify-content:center;}
.portrait-arch {
  width:min(340px,76%);aspect-ratio: .78;overflow:hidden;
  border:13px solid var(--navy);border-bottom:0;
  border-radius:180px 180px 0 0;padding:0;background:var(--white);
}
.portrait-arch img {width:100%;height:100%;object-fit:cover;display:block;}
.bio-plaque {
  position:relative;width:100%;margin-top:-.05rem;padding:1.15rem 1.25rem;
  background:var(--navy);color:var(--white);border-radius:18px;
  font-size:clamp(.88rem,1.3vw,1.1rem);line-height:1.8;text-align:justify;
}

/* BUBBLES AND CARDS */
.bubble-row,.tag-row {display:flex;flex-wrap:wrap;gap:.55rem;margin-top:1rem;}
.bubble {
  display:inline-flex;align-items:center;justify-content:center;
  padding:.48rem .85rem;border-radius:999px;
  background:var(--white);color:var(--navy);font-size:.78rem;font-weight:700;
}
.white .bubble {background:var(--navy);color:var(--white);}
.project-grid {display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:1.25rem;}
.project-card {
  display:flex;flex-direction:column;min-width:0;overflow:hidden;
  background:var(--white);color:var(--navy)!important;
  border:2px solid var(--white);border-radius:22px;
  text-decoration:none!important;transition:transform .24s ease,box-shadow .24s ease;
}
.project-card:hover {transform:translateY(-9px);box-shadow:0 18px 0 rgba(255,255,255,.16);}
.image-link {display:block;color:var(--white)!important;text-decoration:none!important;}
.image-wrap {position:relative;overflow:hidden;aspect-ratio:16/10;background:var(--navy);}
.image-wrap img {display:block;width:100%;height:100%;object-fit:cover;transition:transform .35s ease;}
.image-wrap:after {
  content:"";position:absolute;inset:0;background:var(--navy);opacity:0;
  transition:opacity .22s ease;
}
.hover-label {
  position:absolute;z-index:2;left:50%;top:50%;transform:translate(-50%,-35%);
  padding:.65rem 1rem;border:2px solid var(--white);border-radius:999px;
  color:var(--white);background:var(--navy);font-size:.84rem;font-weight:800;
  white-space:nowrap;opacity:0;transition:opacity .22s ease,transform .22s ease;
}
.project-card:hover .image-wrap img, .image-link:hover .image-wrap img {transform:scale(1.06);}
.project-card:hover .image-wrap:after, .image-link:hover .image-wrap:after {opacity:.55;}
.project-card:hover .hover-label, .image-link:hover .hover-label {opacity:1;transform:translate(-50%,-50%);}
.project-copy {padding:1.05rem 1.1rem 1.2rem;display:flex;flex-direction:column;flex:1;}
.card-kicker {font-size:.68rem;font-weight:800;letter-spacing:.15em;text-transform:uppercase;}
.project-copy h3 {font-size:1.03rem;line-height:1.42;margin:.45rem 0 .55rem;font-weight:800;}
.project-copy p {font-size:.88rem;line-height:1.7;margin:0;}
.project-copy .bubble {background:var(--navy);color:var(--white);font-size:.68rem;padding:.35rem .65rem;}
/* BNSP three visual elements, each with the same hover behaviour. */
.bnsp-layout {display:grid;grid-template-columns:1fr 1.05fr 1.05fr .9fr;gap:1rem;align-items:center;}
.bnsp-copy h3 {font-family:'Playfair Display',Georgia,serif;font-size:clamp(1.4rem,2.2vw,2rem);line-height:1.25;margin:0 0 .8rem;}
.bnsp-copy p {font-size:.92rem;line-height:1.75;margin:0 0 1rem;}
.bnsp-tasks {margin:.5rem 0 0;padding-left:1.2rem;font-size:.84rem;line-height:1.65;}
.bnsp-layout .image-wrap {aspect-ratio:1.2;}
.bnsp-layout .certificate .image-wrap {aspect-ratio:.72;}
.bnsp-layout .certificate img {width:100%;height:auto;max-height:310px;object-fit:contain;background:var(--white);border-radius:14px;}
.bnsp-activities {margin-top:.8rem;font-size:.76rem;line-height:1.55;}
.bnsp-activities h4 {font-size:.9rem;margin:0 0 .4rem;}
.bnsp-activities ol {margin:0;padding-left:1.15rem;}
.bnsp-tags {margin-top:1.4rem;}
/* Experiences */
.experience-grid {display:grid;grid-template-columns:.95fr 1.05fr;gap:1.3rem;align-items:center;}
.experience-photo {width:100%;height:100%;max-height:450px;min-height:260px;object-fit:cover;border:3px solid var(--white);border-radius:18px;}
.experience-copy {background:var(--white);color:var(--navy);border-radius:18px;padding:1.2rem 1.35rem;}
.experience-copy h3 {font-family:'Playfair Display',Georgia,serif;font-size:1.3rem;line-height:1.3;margin:0 0 .55rem;}
.experience-copy p {font-size:.9rem;line-height:1.75;margin:0;}
.experience-copy + .experience-copy {margin-top:.8rem;}
.experience-white {display:grid;grid-template-columns:.9fr 1.1fr;gap:1.2rem;align-items:center;}
.pkkmb-layout {display:grid;grid-template-columns:.8fr 1.45fr;gap:1rem;align-items:stretch;}
.pkkmb-layout img {width:100%;height:100%;min-height:190px;object-fit:cover;border:3px solid var(--navy);border-radius:16px;}
.pkkmb-bottom {display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin-top:1rem;align-items:stretch;}
.pkkmb-bottom img {width:100%;height:100%;min-height:170px;object-fit:cover;border:3px solid var(--navy);border-radius:16px;}
.pkkmb-text {background:var(--navy);color:var(--white);border-radius:16px;padding:1.1rem;line-height:1.8;}
/* Certificates */
.certificate-grid {display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:1rem;}
.certificate-item {background:var(--white);color:var(--navy);border-radius:16px;padding:.65rem;transition:transform .22s ease;}
.certificate-item:hover {transform:translateY(-7px);}
.certificate-item img {width:100%;height:220px;object-fit:contain;display:block;background:var(--white);}
.certificate-item p {font-size:.82rem;font-weight:800;line-height:1.4;text-align:center;margin:.65rem .2rem .25rem;}
/* footer */
.footer {text-align:center;padding:2.5rem 1rem 0;}
.footer h2 {font-family:'Playfair Display',Georgia,serif;font-size:2.1rem;margin:0 0 .5rem;}
.footer p {font-size:.9rem;line-height:1.7;margin:.3rem 0 1rem;}
.footer-links {display:flex;justify-content:center;flex-wrap:wrap;gap:.65rem;}
.footer-links a {background:var(--white);color:var(--navy)!important;border-radius:999px;padding:.65rem 1rem;font-weight:800;}
.missing {padding:1rem;background:var(--white);color:var(--navy);border:2px dashed var(--navy);font-size:.8rem;text-align:center;}
@media(max-width:980px) {
 .cover-grid {grid-template-columns:1fr;gap:2rem;}
 .cover-right {grid-row:1;}
 .cover-left {text-align:center;}
 .name-plaque {margin:.4rem auto 1.5rem;white-space:normal;}
 .cover-pills,.contact-list {justify-content:center;align-items:center;}
 .logo-strip {margin:1.2rem auto;}
 .project-grid {grid-template-columns:repeat(2,minmax(0,1fr));}
 .bnsp-layout {grid-template-columns:1fr 1fr;}
 .bnsp-copy {grid-column:1/-1;}
 .certificate-grid {grid-template-columns:repeat(3,minmax(0,1fr));}
}
@media(max-width:620px) {
 .inner {width:calc(100% - 1.5rem);}
 .band {padding:2.3rem 0;}
 .cover {padding:2rem 0;}
 .cover-title {font-size:clamp(3.4rem,17vw,5rem);}
 .portrait-arch {width:min(260px,72%);}
 .bio-plaque {text-align:left;}
 .project-grid,.bnsp-layout,.experience-grid,.experience-white,.pkkmb-layout,.pkkmb-bottom {grid-template-columns:1fr;}
 .bnsp-copy {grid-column:auto;}
 .certificate-grid {grid-template-columns:repeat(2,minmax(0,1fr));}
 .certificate-item img {height:180px;}
}
</style>
""", unsafe_allow_html=True)

# Batik putih sebagai latar penuh pada semua section putih.
# Pastikan file batik.png tersedia di folder assets pada repository.
_batik_bg = image_data("batik.png")
if _batik_bg:
    st.markdown(f"""
    <style>
    .band.white, .cover {{
        background-color: #FFFFFF !important;
        background-image: url("{_batik_bg}") !important;
        background-repeat: repeat !important;
        background-size: 420px auto !important;
        background-position: top left !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# ------------------------------- COVER -------------------------------
logo_src = image_data("logo.png")
logo_html = (
    f'<img src="{logo_src}" alt="Logo tools yang digunakan">'
    if logo_src else
    '<span class="logo-missing">Tambahkan file assets/logo.png untuk menampilkan logo tools</span>'
)
cover = f"""
<div class="portfolio">
<section class="band white cover" id="top">
 <div class="inner cover-grid">
  <div class="cover-left">
   <div class="cover-title">Portofolio</div>
   <div class="name-plaque">Andani Kusuma Dewi</div>
   <div class="cover-pills">
    <span class="cover-pill">Data Analyst</span>
    <span class="cover-pill">Data Prepocessing</span>
    <span class="cover-pill">Bussines Intelligence</span>
   </div>
   <div class="logo-strip">{logo_html}</div>
   <div class="contact-list">
    <a class="contact" href="{LINKEDIN}" target="_blank" rel="noopener noreferrer">▣&nbsp; linkedin.com/in/andani-kusuma-dewi-660441324</a>
    <a class="contact" href="{EMAIL}">✉&nbsp; andanikd754@gmail.com</a>
    <a class="contact" href="{WHATSAPP}" target="_blank" rel="noopener noreferrer">☎&nbsp; 081270052004</a>
   </div>
  </div>
  <div class="cover-right">
   <div class="portrait-arch">{image("diriku.png","Andani Kusuma Dewi")}</div>
   <div class="bio-plaque">
    Fresh Graduate S1 Sistem Informasi Universitas Gunadarma dengan IPK
    3,73/4,00 dan tersertifikasi BNSP Okupasi Data Analyst. Memiliki
    pengalaman dalam pengolahan, pembersihan, analisis, dan visualisasi
    data melalui berbagai proyek berbasis Python dan Google Looker Studio.
    Terbiasa mengubah data menjadi informasi, insight, dan rekomendasi yang
    mendukung kebutuhan bisnis. Memiliki pengalaman pendukung dalam
    pengelolaan database, analisis sistem, dan administrasi operasional.
   </div>
  </div>
 </div>
</section>
"""
st.markdown(cover, unsafe_allow_html=True)

# ------------------------------- BNSP --------------------------------
bnsp = f"""
{heading("Badan Nasional Sertifikasi Profesi Okupasi Data Analyst",
         "Badan Nasional Sertifikasi Profesi Okupasi Data Analyst")}
<div class="bnsp-layout">
 <div class="bnsp-copy">
  <h3>Analisis Faktor<br>Kemiskinan</h3>
  <p>Melakukan proses analisis data kemiskinan untuk menghasilkan informasi yang dapat mendukung pengambilan keputusan terkait ketimpangan tingkat kemiskinan antar daerah di Indonesia.</p>
 </div>
 {linked_image("kemiskinan.png","Dashboard analisis faktor kemiskinan",URL["bnsp_dashboard"],"Lihat Dashboard")}
 {linked_image("colabKemiskinan.png","Notebook Google Colab analisis kemiskinan",URL["bnsp_colab"],"Lihat Notebook")}
 <div>
  <div class="certificate">{image("bnsp.png","Sertifikat kompetensi BNSP")}</div>
  <div class="bnsp-activities">
   <h4>Kegiatan:</h4>
   <ol>
    <li>Mengumpulkan dan memahami dataset kemiskinan dari sumber statistik resmi</li>
    <li>Melakukan preprocessing dan validasi data.</li>
    <li>Memeriksa duplikasi, missing value, tipe data, dan outlier.</li>
    <li>Melakukan correlation analysis menggunakan heatmap.</li>
    <li>Menganalisis hubungan antarvariabel.</li>
    <li>Membuat visualisasi dan dashboard.</li>
    <li>Menginterpretasikan temuan menjadi insight.</li>
    <li>Menyusun rekomendasi berbasis data.</li>
   </ol>
  </div>
 </div>
</div>
"""
st.markdown(band(bnsp, "navy"), unsafe_allow_html=True)

# ----------------------- DATA ANALYSIS & VISUALIZATION ----------------
data_projects = [
    project_card(
        "sd.png", "Workshop Kelayakan Pendidikan Sekolah Dasar di Indonesia Tahun 2023",
        "Workshop Kelayakan Pendidikan Sekolah Dasar di Indonesia Tahun 2023",
        "Mengolah dataset pendidikan, membuat visualisasi berdasarkan indikator, membandingkan SD negeri dan swasta, menganalisis pola, mengidentifikasi insight, serta menyusun narasi untuk menjelaskan hasil visualisasi",
        URL["education"], "Lihat Dashboard"
    ),
    project_card(
        "stress.png", "Data Preparation for the Business Process of Analyzing Student Stress Levels",
        "Data Preparation for the Business Process of Analyzing Student Stress Levels",
        "Mengidentifikasi faktor-faktor yang berkaitan dengan tingkat stres pelajar untuk kebutuhan rekomendasi bisnis yang dapat mendukung pengembangan layanan pendampingan akademik oleh perusahaan EdTech",
        URL["stress"], "Lihat Dashboard"
    ),
    project_card(
        "islam.png", "Creating Business Intelligence Case Islamic Pilgrimage",
        "Creating Business Intelligence Case Islamic Pilgrimage",
        "Memahami kebutuhan bisnis, data cleaning, preprocessing, exploratory data analysis, analisis hubungan antarvariabel, pembuatan dashboard visualisasi, interpretasi insight, dan penyusunan rekomendasi untuk sektor pariwisata religi",
        URL["pilgrimage"], "Lihat Dashboard"
    ),
]
data_section = f"""
{heading("Data Analysis & Visualization", "DATA ANALYSIS & VISUALIZATION",
         "Mengolah data melalui proses pembersihan, analisis, visualisasi, dan interpretasi untuk menghasilkan insight serta rekomendasi berbasis data")}
<div class="bubble-row">
 {bubble("Data Cleaning")}{bubble("Preprocessing")}{bubble("EDA")}
 {bubble("Data Interpretation")}{bubble("Dashboard Visualization")}
 {bubble("Correlation & Trend Analysis")}
</div>
<div class="project-grid" style="margin-top:1.5rem">{''.join(data_projects)}</div>
"""
st.markdown(band(data_section, "navy"), unsafe_allow_html=True)

# --------------------------- MAJOR ACADEMIC ---------------------------
academic_cards = [
    project_card(
        "skripsi.png", "Skripsi",
        "Implementasi Dashboard Web Klasifikasi Sentimen E-Wallet Menggunakan Naive Bayes dan Support Vector Machine",
        "Mengumpulkan dan mengolah ulasan Google Play dari DANA, GoPay, dan ShopeePay. Melakukan text preprocessing, klasifikasi sentimen menggunakan Naïve Bayes dan Support Vector, serta evaluasi model. Mengimplementasikan hasil analisis dalam dashboard web interaktif berbasis Streamlit",
        URL["ewallet"], "Lihat Dashboard Streamlit"
    ),
    project_card(
        "UIUX.png", "Penulisan Ilmiah",
        "Perancangan User Interface (UI) dan User Experience (UX) Website Student Connect",
        "Melakukan riset kebutuhan terhadap 100 siswa SMK X melalui kuesioner. Merancang user flow, struktur navigasi, wireframe, UI mockup, dan prototype interaktif menggunakan Figma. Melakukan usability testing dengan hasil System Usability Scale (SUS) sebesar 91,1",
        URL["student_connect"], "Lihat Perancangan"
    ),
]
paudqu = f"""
<div class="project-card">
 <div class="image-wrap">{image("tim.png","Proyek Tim; Laporan Proyek Perangkat Lunak Website PaudQu Al-Ikhlas")}<span class="hover-label">Dokumentasi Proyek</span></div>
 <div class="project-copy">
  <div class="card-kicker">Mata Kuliah Proyek Perancangan Sistem Informasi</div>
  <h3>Proyek Tim; Laporan Proyek Perangkat Lunak Website PaudQu Al-Ikhlas</h3>
  <p>Proyek tim dalam pengembangan perangkat lunak website pendaftaran siswa baru PAUDQu Al-Ikhlas. Menganalisis dan mendokumentasikan kebutuhan klien melalui wawancara dan observasi, menyusun Requirement Document, Software Requirements Specification (SRS), dokumentasi rancangan sistem (SDD), ERD, pengujian sistem, User Acceptance Test (UAT), buku panduan penggunaan, serta berita acara serah terima</p>
 </div>
</div>
"""
academic = f"""
{heading("Skripsi | Penulisan Ilmiah | Mata Kuliah Proyek Perancangan Sistem Informasi",
         "MAJOR ACADEMIC PROJECTS")}
<div class="project-grid">{''.join(academic_cards)}{paudqu}</div>
"""
st.markdown(band(academic, "navy"), unsafe_allow_html=True)

# --------------------------- LABORATORY ASSISTANT --------------------
lab = f"""
{heading("LABORATORY ASSISTANT", "LABORATORY ASSISTANT",
         "Asisten Laboratorium hingga Tutor Praktikum Program Studi Sistem Informasi")}
<div class="experience-grid">
 {image("aslab.png","Dokumentasi Asisten Laboratorium","experience-photo")}
 <div>
  <div class="experience-copy">
   <h3>Asisten Laboratorium (1 Semester)</h3>
   <p>1. Memeriksa dan mengintegrasikan nilai hasil laporan praktikum praktikan ke dalam data nilai<br>
   2. Membantu pelaksanaan praktikum<br>
   3. Mengawasi praktikan serta membantu mengatasi kendala saat praktikum</p>
  </div>
  <div class="experience-copy">
   <h3>Tutor Praktikum Mata Kuliah Sistem Basis Pengetahuan (1 Semester)</h3>
   <p>1. Membimbing proses belajar mahasiswa selama praktikum<br>
   2. Menyampaikan materi praktikum<br>
   3. Menyusun soal Laporan Pendahuluan (LP) dan Laporan Akhir (LA)</p>
  </div>
 </div>
</div>
"""
st.markdown(band(lab, "navy"), unsafe_allow_html=True)

# ---------------------- OPERATIONS ADMIN & DATA MANAGEMENT ----------
swim = f"""
{heading("OPERATIONS ADMIN & DATA MANAGEMENT", "OPERATIONS ADMIN & DATA MANAGEMENT",
         "Admin Operasional & Manajemen Data Swimplash Swimming Club")}
<div class="experience-white">
 <div class="experience-copy">
  <h3>Kontribusi:</h3>
  <p>1. Menambah, merapikan dan memperbarui data murid serta pelatih melalui portal internal<br>
  2. Menangani komunikasi dan follow-up calon murid dari tahap inquiry, trial, hingga keputusan pendaftaran<br>
  3. Mengkoordinasikan kebutuhan murid antara orang tua dan pelatih<br>
  4. Mengatur jadwal serta reschedule pelatih dan murid<br>
  5. Membantu proses perpanjangan paket latihan</p>
 </div>
 {image("swimplash.png","Dokumentasi Operations Admin dan Data Management","experience-photo")}
</div>
<div class="bubble-row">
 {bubble("Administrative & Data Management")}{bubble("Customer Service")}
 {bubble("Lead Handling")}{bubble("Problem Solving")}
</div>
"""
st.markdown(band(swim, "navy"), unsafe_allow_html=True)

# -------------------------- GERAKAN SUKA BACA ------------------------
gsb = f"""
{heading("GERAKAN SUKA BACA VOLUNTEER", "GERAKAN SUKA BACA VOLUNTEER",
         "Divisi Operasional | Sekretaris Database & Presensi Relawan")}
<div class="experience-grid">
 <div class="experience-copy">
  <h3>Peran:</h3>
  <p>1. Mengelola database relawan<br>
  2. Mencatat presensi kegiatan online<br>
  3. Mengirim reminder berdasarkan divisi/kegiatan<br>
  4. Membantu penjadwalan dan koordinasi kegiatan<br>
  5. Memperbarui data tracking presensi</p>
  <div class="bubble-row">{bubble("Tools:")}{bubble("Google Sheets")}</div>
 </div>
 {image("gsb.png","Dokumentasi Gerakan Suka Baca Volunteer","experience-photo")}
</div>
<div class="bubble-row">
 {bubble("Update Data")}{bubble("Identify")}{bubble("Reminder")}{bubble("Attendance")}{bubble("Tracking")}
</div>
"""
st.markdown(band(gsb, "navy"), unsafe_allow_html=True)

# ---------------------------- PKKMB EVENT ----------------------------
# Khusus bagian PKKMB: foto ditampilkan utuh (tanpa crop), sesuai komposisi PDF.
pkkmb = f"""
<style>
.pk-section {{
    width: 100%;
    box-sizing: border-box;
    padding: clamp(18px, 3vw, 42px) 0;
    color: {NAVY};
    background-color: {WHITE};
    background-image: url('{image_data("batik.png")}');
    background-repeat: repeat;
    background-size: 420px auto;
}}
.pk-inner {{
    width: min(1440px, 96%);
    margin: 0 auto;
    display: grid;
    grid-template-columns: .82fr 1.55fr;
    grid-template-rows: auto auto;
    gap: 14px;
    align-items: stretch;
}}
.pk-photo-left, .pk-main, .pk-bottom-left, .pk-contribution {{
    min-width: 0;
    box-sizing: border-box;
    background: {NAVY};
    color: {WHITE};
}}
.pk-photo-left {{
    border-radius: 0 0 28px 28px;
    padding: clamp(12px, 2vw, 24px);
    display: flex;
    align-items: center;
    justify-content: center;
}}
.pk-photo-left img {{
    display: block;
    width: 100%;
    height: auto;
    max-height: 430px;
    object-fit: contain;
    border-radius: 0 0 16px 16px;
}}
.pk-main {{
    border-radius: 0 0 0 28px;
    padding: clamp(18px, 2.6vw, 34px);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    gap: 18px;
}}
.pk-title {{
    margin: 0 0 8px;
    color: {WHITE};
    font-family: 'DM Sans', Arial, sans-serif;
    font-size: clamp(1.45rem, 2.8vw, 2.55rem);
    font-weight: 800;
    line-height: 1.12;
}}
.pk-subtitle {{
    margin: 0;
    color: {WHITE};
    font-size: clamp(.82rem, 1.15vw, 1rem);
    line-height: 1.55;
}}
.pk-tags {{
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin: 18px 0 22px;
}}
.pk-tag {{
    display: inline-flex;
    align-items: center;
    border-radius: 999px;
    padding: 6px 11px;
    background: {WHITE};
    color: {NAVY};
    font-size: clamp(.66rem, .85vw, .78rem);
    font-weight: 800;
}}
.pk-group-photo {{
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    border-radius: 20px;
    background: {NAVY};
}}
.pk-group-photo img {{
    display: block;
    width: 100%;
    height: auto;
    max-height: 460px;
    object-fit: contain;
    object-position: center;
    border-radius: 20px;
}}
.pk-bottom-left {{
    border-radius: 0 28px 0 0;
    padding: clamp(12px, 2vw, 24px);
    display: flex;
    align-items: center;
    justify-content: center;
}}
.pk-bottom-left img {{
    display: block;
    width: 100%;
    height: auto;
    max-height: 350px;
    object-fit: contain;
    border-radius: 16px;
}}
.pk-contribution {{
    border-radius: 0 0 0 28px;
    padding: clamp(20px, 3vw, 42px);
    display: flex;
    flex-direction: column;
    justify-content: center;
}}
.pk-contribution h3 {{
    margin: 0 0 8px;
    color: {WHITE};
    font-size: clamp(1.05rem, 1.6vw, 1.45rem);
    font-weight: 800;
    letter-spacing: .06em;
}}
.pk-contribution p {{
    margin: 0;
    color: {WHITE};
    font-size: clamp(.82rem, 1.1vw, 1rem);
    line-height: 1.65;
}}
@media (max-width: 760px) {{
    .pk-inner {{
        width: 94%;
        grid-template-columns: 1fr;
        grid-template-rows: auto;
        gap: 12px;
    }}
    .pk-photo-left, .pk-main, .pk-bottom-left, .pk-contribution {{
        border-radius: 18px;
    }}
    .pk-photo-left img {{
        width: auto;
        max-width: 100%;
        max-height: 420px;
    }}
    .pk-group-photo img, .pk-bottom-left img {{
        width: 100%;
        max-height: none;
    }}
}}
</style>
<section class="pk-section">
  <div class="pk-inner">
    <div class="pk-photo-left">
      {image("pkkmb1.png", "Dokumentasi panitia PKKMB")}
    </div>
    <div class="pk-main">
      <div>
        <h2 class="pk-title">PKKMB EVENT COMMITTEE</h2>
        <p class="pk-subtitle">Panitia Acara Pengenalan Kehidupan Kampus Mahasiswa Baru (PKKMB)</p>
        <div class="pk-tags">
          <span class="pk-tag">Event Planing &amp; Coordination</span>
          <span class="pk-tag">Team Work</span>
          <span class="pk-tag">Time Mangement</span>
        </div>
      </div>
      <div class="pk-group-photo">
        {image("pkkmb2.png", "Foto seluruh panitia PKKMB")}
      </div>
    </div>
    <div class="pk-bottom-left">
      {image("pkkmb3.png", "Dokumentasi kegiatan PKKMB")}
    </div>
    <div class="pk-contribution">
      <h3>Kontribusi:</h3>
      <p>Perencanaan dan koordinasi rangkaian acara PKKMB, termasuk penyusunan rundown, pengaturan waktu setiap sesi, koordinasi dengan penanggung jawab kegiatan, serta evaluasi pelaksanaan acara</p>
    </div>
  </div>
</section>
"""
st.markdown(pkkmb, unsafe_allow_html=True)
# ---------------------------------------------------------------------

# ------------------------------- CERTIFICATES ------------------------
certificates = [
    ("seminarDA.png", "Seminar Data Analyst"),
    ("mp.png", "MP"),
    ("pengenalanDA.png", "Introduce to Data Analytics"),
    ("excel.png", "Latihan Kasus Microsoft Excel bagi Admin"),
    ("sql.png", "SQL Server Untuk Tingkat Pemula"),
]
cert_items = "".join(
    f'<div class="certificate-item">{image(file,title)}<p>{title}</p></div>'
    for file, title in certificates
)
cert_section = f"""
{heading("SERTIFICATE", "SERTIFICATE")}
<div class="certificate-grid">{cert_items}</div>
<div class="footer">
 <h2>Andani Kusuma Dewi</h2>
 <div class="footer-links">
  <a href="{LINKEDIN}" target="_blank" rel="noopener noreferrer">LinkedIn</a>
  <a href="{EMAIL}">Email</a>
  <a href="{WHATSAPP}" target="_blank" rel="noopener noreferrer">WhatsApp</a>
 </div>
</div>
"""
st.markdown(band(cert_section, "navy"), unsafe_allow_html=True)