from pathlib import Path
import base64
import streamlit as st

# ==========================================================
# ANDANI KUSUMA DEWI | INTERACTIVE PORTFOLIO
# All layouts are responsive HTML/CSS; images are real assets.
# ==========================================================

st.set_page_config(
    page_title="Andani Kusuma Dewi | Data Analyst Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

BASE = Path(__file__).parent
ASSETS = BASE / "assets"

NAVY = "#101F46"
NAVY_DARK = "#0B1737"
INK = "#14213D"
MUTED = "#667085"
PALE = "#F5F7FB"
WHITE = "#FFFFFF"
ACCENT = "#D7E3FF"

LINKEDIN = "https://www.linkedin.com/in/andani-kusuma-dewi-660441324"
EMAIL = "mailto:andanikd754@gmail.com?subject=Portofolio%20-%20Andani%20Kusuma%20Dewi"
WHATSAPP = "https://wa.me/6281270052004"

LINKS = {
    "poverty_dashboard": "https://datastudio.google.com/reporting/8879aca4-37ec-4f78-a8db-bc3ce7c74197",
    "poverty_colab": "https://colab.research.google.com/drive/10c5SLmhYozUxTug0a_TGbIJpymHd8Yuf?usp=sharing",
    "education": "https://datastudio.google.com/reporting/54d49033-80d8-4006-8635-279ec0f0842f",
    "stress": "https://datastudio.google.com/reporting/82787c28-82b4-4451-8bb2-77becf1ca070",
    "pilgrimage": "https://datastudio.google.com/reporting/25f2a4d6-e8b3-4078-8fb4-297f915cc810",
    "ewallet": "https://skripsisentimen.streamlit.app",
    "student_connect": "https://www.figma.com/proto/E4wcdZogSWRF1eDzpngJ4M?node-id=157-2&t=OQWxTboJfkqaujwa-6",
}

def img(name: str) -> str:
    path = ASSETS / name
    if not path.exists():
        return ""
    suffix = path.suffix.lower().replace(".", "")
    mime = "jpeg" if suffix in ("jpg", "jpeg") else suffix
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:image/{mime};base64,{encoded}"

def image_tag(name: str, alt: str, cls: str = "") -> str:
    source = img(name)
    if not source:
        return f'<div class="image-missing">Gambar {name} belum tersedia</div>'
    return f'<img class="{cls}" src="{source}" alt="{alt}" loading="lazy">'

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Playfair+Display:wght@500;600;700&display=swap');

:root {
  --navy: #101F46;
  --navy2: #0B1737;
  --ink: #14213D;
  --muted: #667085;
  --paper: #F5F7FB;
  --white: #FFFFFF;
  --line: #E7EBF3;
}
html { scroll-behavior: smooth; }
#MainMenu, footer, header, [data-testid="stSidebar"] {display:none !important;}
.stApp { background: #fff; color: var(--ink); }
.block-container { max-width: 1240px; padding: 0 1.35rem 3rem; }
div[data-testid="stVerticalBlock"] { gap: 0; }
.portfolio { width:100%; font-family:'DM Sans',sans-serif; color:var(--ink); }
a { text-decoration:none !important; }
.hero {
  position:relative; overflow:hidden; margin:1.25rem 0 2.3rem;
  padding:clamp(1.4rem,4vw,3.5rem);
  min-height:520px; border-radius:30px; color:white;
  background:linear-gradient(135deg,var(--navy) 0%,#182B5B 100%);
  display:grid; grid-template-columns:1.08fr .92fr; gap:2rem; align-items:center;
  box-shadow:0 18px 45px rgba(16,31,70,.15);
}
.hero:before {
  content:""; position:absolute; width:440px; height:440px; right:-150px; top:-180px;
  border:1px solid rgba(255,255,255,.12); border-radius:50%;
  box-shadow:0 0 0 35px rgba(255,255,255,.025),0 0 0 75px rgba(255,255,255,.02);
}
.hero-left,.hero-right {position:relative;z-index:1;}
.hero-kicker {font-size:.8rem;letter-spacing:.2em;text-transform:uppercase;color:#C9D6F7;font-weight:700;}
.hero-title {
  font-family:'Playfair Display',serif; font-size:clamp(3.2rem,7vw,6.3rem);
  line-height:.98; margin:.55rem 0 1rem; font-weight:600; letter-spacing:-.04em;
}
.hero-name {
  display:inline-block; background:#fff; color:var(--navy); padding:.8rem 1.2rem;
  border-radius:8px 18px 8px 18px; font-family:'Playfair Display',serif;
  font-size:clamp(1.1rem,2vw,1.65rem); transform:rotate(-1.2deg); margin:.2rem 0 1.2rem;
}
.pills {display:flex; flex-wrap:wrap; gap:.55rem; margin:1rem 0 1.2rem;}
.pill {
  display:inline-flex; align-items:center; padding:.55rem .9rem; border-radius:999px;
  background:#fff; color:var(--navy); font-size:.82rem; font-weight:700;
}
.hero-links {display:flex; flex-wrap:wrap; gap:.55rem; margin-top:1.25rem;}
.hero-link {
  color:#fff !important; border:1px solid rgba(255,255,255,.42); padding:.65rem .85rem;
  border-radius:999px; font-size:.82rem; font-weight:600; transition:.2s ease;
}
.hero-link:hover {background:#fff;color:var(--navy)!important;transform:translateY(-3px);}
.hero-right {display:flex; flex-direction:column; align-items:center; gap:1rem;}
.profile-frame {
  width:min(280px,72%); aspect-ratio:4/5; padding:10px; border:7px solid #fff;
  border-radius:150px 150px 26px 26px; background:#DCE5F8; overflow:hidden;
  box-shadow:0 20px 45px rgba(0,0,0,.25);
}
.profile-frame img {width:100%;height:100%;object-fit:cover;border-radius:120px 120px 18px 18px;}
.hero-summary {
  width:min(100%,460px); background:rgba(7,18,47,.84); border:1px solid rgba(255,255,255,.13);
  border-radius:18px; padding:1.2rem 1.35rem; color:#F4F6FC; line-height:1.8;
  font-size:.95rem; text-align:justify;
}
.section {margin:2.7rem 0;}
.section-head {display:flex;justify-content:space-between;align-items:end;gap:1rem;margin-bottom:1.25rem;}
.eyebrow {font-size:.72rem;letter-spacing:.18em;text-transform:uppercase;color:#7584A7;font-weight:800;}
.section-title {font-family:'Playfair Display',serif;color:var(--navy);font-size:clamp(1.8rem,3vw,2.65rem);line-height:1.15;margin:.25rem 0 0;}
.section-desc {color:var(--muted);font-size:.94rem;max-width:680px;line-height:1.7;margin:.5rem 0 0;}
.navy-panel {
  background:var(--navy); color:#fff; border-radius:26px; padding:clamp(1.1rem,3vw,2rem);
  box-shadow:0 14px 35px rgba(16,31,70,.10);
}
.navy-panel .section-title {color:#fff;}
.skill-pills {display:flex;flex-wrap:wrap;gap:.55rem;margin:1rem 0 1.35rem;}
.skill-pills span {background:#fff;color:var(--navy);padding:.5rem .85rem;border-radius:999px;font-size:.8rem;font-weight:700;}
.grid-3 {display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:1rem;}
.grid-2 {display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:1rem;}
.project-card,.info-card,.cert-card {
  background:#fff;border:1px solid var(--line);border-radius:20px;overflow:hidden;
  box-shadow:0 8px 25px rgba(16,31,70,.06); min-width:0;
}
.project-card {transition:transform .24s ease,box-shadow .24s ease; height:100%;}
.project-card:hover {transform:translateY(-8px);box-shadow:0 18px 38px rgba(5,16,44,.20);}
.project-image {position:relative;overflow:hidden;background:#E9EDF6;aspect-ratio:16/10;}
.project-image img {width:100%;height:100%;object-fit:cover;display:block;transition:transform .35s ease;}
.project-card:hover .project-image img {transform:scale(1.045);}
.project-overlay {
  position:absolute;inset:0;display:flex;align-items:center;justify-content:center;
  background:rgba(8,22,56,.0);opacity:0;transition:.22s ease;
}
.project-card:hover .project-overlay {background:rgba(8,22,56,.62);opacity:1;}
.project-overlay span {
  color:#fff;border:1px solid rgba(255,255,255,.85);border-radius:999px;
  padding:.65rem 1.05rem;font-size:.85rem;font-weight:700;
  transform:translateY(10px);transition:.22s ease;
}
.project-card:hover .project-overlay span {transform:translateY(0);}
.project-body {padding:1rem 1.05rem 1.15rem;}
.project-type {font-size:.68rem;color:#7180A2;text-transform:uppercase;letter-spacing:.12em;font-weight:800;}
.project-title {color:var(--navy);font-size:1.02rem;font-weight:800;line-height:1.4;margin:.4rem 0 .55rem;}
.project-text {color:#596579;font-size:.84rem;line-height:1.65;margin:0;}
.card-tools {display:flex;flex-wrap:wrap;gap:.4rem;margin-top:.85rem;}
.card-tools span {font-size:.7rem;background:#F0F3F9;color:#34466F;border-radius:999px;padding:.3rem .55rem;font-weight:600;}
.project-actions {display:flex;gap:.55rem;flex-wrap:wrap;padding:0 1.05rem 1.1rem;}
.action {
  display:inline-flex;align-items:center;justify-content:center;padding:.55rem .75rem;
  border-radius:9px;background:var(--navy);color:#fff!important;font-size:.75rem;font-weight:700;
  transition:.2s ease;
}
.action.secondary {background:#E9EEF9;color:var(--navy)!important;}
.action:hover {transform:translateY(-2px);filter:brightness(1.12);}
.bnsk-layout {display:grid;grid-template-columns:1fr 1fr 1fr .72fr;gap:1rem;align-items:stretch;}
.bnsk-image {height:100%;min-height:230px;object-fit:cover;width:100%;border-radius:15px;}
.bnsk-copy {display:flex;flex-direction:column;justify-content:center;}
.bnsk-copy p,.white-card p {line-height:1.75;font-size:.9rem;color:#E4EAF8;}
.white-card {background:#fff;color:var(--ink);border-radius:18px;padding:1rem;}
.white-card h3 {color:var(--navy);font-family:'Playfair Display',serif;margin:.1rem 0 .6rem;font-size:1.25rem;}
.white-card p {color:#566176;margin:0;}
.experience {display:grid;grid-template-columns:.9fr 1.1fr;gap:1.1rem;align-items:center;}
.experience-image {width:100%;height:100%;min-height:260px;max-height:390px;object-fit:cover;border-radius:20px;}
.experience-copy {background:#fff;border-radius:20px;padding:1.3rem;color:var(--ink);}
.experience-copy h3 {font-family:'Playfair Display',serif;color:var(--navy);font-size:1.35rem;margin:0 0 .6rem;}
.experience-copy ul {margin:.3rem 0 0;padding-left:1.2rem;color:#536078;line-height:1.8;font-size:.9rem;}
.pkkmb-grid {display:grid;grid-template-columns:1fr 1.4fr;gap:1rem;align-items:stretch;}
.pkkmb-grid img {width:100%;height:100%;min-height:200px;object-fit:cover;border-radius:18px;}
.pkkmb-note {background:#fff;border-radius:18px;padding:1.2rem;color:#566176;line-height:1.8;}
.cert-grid {display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:.9rem;}
.cert-card {padding:.6rem;transition:.22s ease;}
.cert-card:hover {transform:translateY(-6px);box-shadow:0 16px 30px rgba(16,31,70,.14);}
.cert-card img {width:100%;aspect-ratio:4/5;object-fit:contain;background:#F7F8FC;border-radius:12px;}
.cert-card div {font-size:.78rem;color:var(--navy);font-weight:800;text-align:center;padding:.6rem .2rem .2rem;}
.footer {
  margin:3rem 0 0;padding:2rem 1rem;background:var(--navy);border-radius:24px;
  color:#fff;text-align:center;
}
.footer h2 {font-family:'Playfair Display',serif;font-size:1.8rem;margin:0 0 .5rem;}
.footer p {color:#D5DDF0;margin:.2rem 0 1rem;}
.footer .hero-links {justify-content:center;}
.image-missing {padding:2rem;background:#eef1f7;color:#68748b;text-align:center;border-radius:12px;}
@media(max-width:900px) {
 .hero {grid-template-columns:1fr;min-height:unset;text-align:center;}
 .hero-links,.pills {justify-content:center;}
 .hero-right {grid-row:1;}
 .hero-summary {text-align:left;}
 .grid-3 {grid-template-columns:repeat(2,minmax(0,1fr));}
 .bnsk-layout {grid-template-columns:1fr 1fr;}
 .bnsk-layout > :last-child {grid-column:1/-1;}
 .cert-grid {grid-template-columns:repeat(3,minmax(0,1fr));}
}
@media(max-width:600px) {
 .block-container {padding:0 .65rem 2rem;}
 .hero {margin:.6rem 0 1.6rem;border-radius:20px;padding:1.2rem;}
 .profile-frame {width:190px;}
 .grid-3,.grid-2,.bnsk-layout,.experience,.pkkmb-grid {grid-template-columns:1fr;}
 .bnsk-layout > :last-child {grid-column:auto;}
 .cert-grid {grid-template-columns:repeat(2,minmax(0,1fr));}
 .section {margin:2rem 0;}
 .section-head {display:block;}
}
</style>
""", unsafe_allow_html=True)

def section_head(kicker, title, desc=""):
    return f"""
    <div class="section-head">
      <div><div class="eyebrow">{kicker}</div><h2 class="section-title">{title}</h2>
      {f'<p class="section-desc">{desc}</p>' if desc else ''}</div>
    </div>"""

def project_card(image, alt, category, title, description, url, label="Lihat Dashboard", tools=None):
    tools_html = "".join(f"<span>{t}</span>" for t in (tools or []))
    return f"""
    <a class="project-card" href="{url}" target="_blank" rel="noopener noreferrer" aria-label="{label}: {title}">
      <div class="project-image">
        {image_tag(image, alt)}
        <div class="project-overlay"><span>{label} ↗</span></div>
      </div>
      <div class="project-body">
        <div class="project-type">{category}</div>
        <div class="project-title">{title}</div>
        <p class="project-text">{description}</p>
        {f'<div class="card-tools">{tools_html}</div>' if tools else ''}
      </div>
    </a>"""

# ----------------------------- HERO -----------------------------
hero = f"""
<div class="portfolio">
<section class="hero" id="home">
  <div class="hero-left">
    <div class="hero-kicker">Portfolio · 2026</div>
    <h1 class="hero-title">Portfolio</h1>
    <div class="hero-name">Andani Kusuma Dewi</div>
    <div class="pills">
      <span class="pill">Data Analyst</span><span class="pill">Data Preprocessing</span>
      <span class="pill">Business Intelligence</span>
    </div>
    <div class="hero-links">
      <a class="hero-link" href="{LINKEDIN}" target="_blank">in&nbsp; LinkedIn</a>
      <a class="hero-link" href="{EMAIL}">✉&nbsp; Email</a>
      <a class="hero-link" href="{WHATSAPP}" target="_blank">☏&nbsp; WhatsApp</a>
    </div>
  </div>
  <div class="hero-right">
    <div class="profile-frame">{image_tag("diriku.png","Foto Andani Kusuma Dewi")}</div>
    <div class="hero-summary">
      Fresh Graduate S1 Sistem Informasi Universitas Gunadarma dengan IPK 3,73/4,00 dan
      tersertifikasi BNSP Okupasi Data Analyst. Memiliki pengalaman dalam pengolahan,
      pembersihan, analisis, dan visualisasi data melalui berbagai proyek berbasis Python
      dan Google Looker Studio. Terbiasa mengubah data menjadi informasi, insight, dan
      rekomendasi yang mendukung kebutuhan bisnis. Memiliki pengalaman pendukung dalam
      pengelolaan database, analisis sistem, dan administrasi operasional.
    </div>
  </div>
</section>
"""
st.markdown(hero, unsafe_allow_html=True)

# ------------------------ BNSP FEATURE --------------------------
bnsp_html = f"""
<section class="section navy-panel" id="certification">
  <div class="eyebrow" style="color:#B8C8F0">BNSP · DATA ANALYST</div>
  <h2 class="section-title">Badan Nasional Sertifikasi Profesi<br>Okupasi Data Analyst</h2>
  <div class="bnsk-layout" style="margin-top:1.3rem">
    <div class="bnsk-copy">
      <h3 style="font-family:'Playfair Display',serif;font-size:1.55rem;margin:0 0 .6rem">Analisis Faktor Kemiskinan</h3>
      <p>Melakukan proses analisis data kemiskinan untuk menghasilkan informasi yang dapat mendukung pengambilan keputusan terkait ketimpangan tingkat kemiskinan antar daerah di Indonesia.</p>
      <div class="project-actions" style="padding:0;margin-top:.8rem">
        <a class="action" href="{LINKS['poverty_colab']}" target="_blank">Lihat Notebook ↗</a>
        <a class="action secondary" href="{LINKS['poverty_dashboard']}" target="_blank">Lihat Dashboard ↗</a>
      </div>
    </div>
    <div><a href="{LINKS['poverty_dashboard']}" target="_blank" aria-label="Buka dashboard analisis kemiskinan">{image_tag("kemiskinan.png","Dashboard analisis faktor kemiskinan","bnsk-image")}</a></div>
    <div><a href="{LINKS['poverty_colab']}" target="_blank" aria-label="Buka notebook Google Colab">{image_tag("colabKemiskinan.png","Notebook Google Colab analisis kemiskinan","bnsk-image")}</a></div>
    <div>{image_tag("bnsp.png","Sertifikat kompetensi BNSP","bnsk-image")}</div>
  </div>
  <div class="skill-pills">
    <span>Data Collection</span><span>Preprocessing</span><span>Data Validation</span>
    <span>Correlation Analysis</span><span>Dashboard</span><span>Insight & Recommendation</span>
  </div>
</section>
"""
st.markdown(bnsp_html, unsafe_allow_html=True)

# ------------------------ DATA ANALYSIS -------------------------
st.markdown('<section class="section">', unsafe_allow_html=True)
st.markdown(section_head(
    "Selected Projects", "Data Analysis & Visualization",
    "Mengolah data melalui proses pembersihan, analisis, visualisasi, dan interpretasi untuk menghasilkan insight serta rekomendasi berbasis data."
), unsafe_allow_html=True)
st.markdown("""
<div class="skill-pills">
 <span>Data Cleaning</span><span>Preprocessing</span><span>EDA</span>
 <span>Data Interpretation</span><span>Dashboard Visualization</span><span>Correlation & Trend Analysis</span>
</div>
""", unsafe_allow_html=True)
cards = [
    project_card("sd.png","Dashboard workshop pendidikan","Workshop & Data Visualization",
      "Workshop Kelayakan Pendidikan Sekolah Dasar di Indonesia Tahun 2023",
      "Mengolah dataset pendidikan, membuat visualisasi berdasarkan indikator, membandingkan SD negeri dan swasta, menganalisis pola, mengidentifikasi insight, serta menyusun narasi hasil visualisasi.",
      LINKS["education"],"Lihat Dashboard",["Data Visualization","Education"]),
    project_card("stress.png","Dashboard analisis tingkat stres pelajar","Data Preparation & EDA",
      "Data Preparation for the Business Process of Analyzing Student Stress Levels",
      "Mengidentifikasi faktor-faktor yang berkaitan dengan tingkat stres pelajar untuk rekomendasi bisnis yang mendukung pengembangan layanan pendampingan akademik oleh perusahaan EdTech.",
      LINKS["stress"],"Lihat Dashboard",["Python","EDA","Looker Studio"]),
    project_card("islam.png","Dashboard Islamic Pilgrimage","Business Intelligence",
      "Creating Business Intelligence Case Islamic Pilgrimage",
      "Memahami kebutuhan bisnis, data cleaning, preprocessing, exploratory data analysis, analisis hubungan antarvariabel, dashboard visualisasi, interpretasi insight, dan rekomendasi sektor pariwisata religi.",
      LINKS["pilgrimage"],"Lihat Dashboard",["Python","Business Intelligence"]),
]
st.markdown('<div class="grid-3">' + "".join(cards) + '</div></section>', unsafe_allow_html=True)

# ----------------------- ACADEMIC PROJECTS ----------------------
st.markdown('<section class="section">', unsafe_allow_html=True)
st.markdown(section_head(
    "Academic Work", "Major Academic Projects",
    "Skripsi · Penulisan Ilmiah · Mata Kuliah Proyek Perancangan Sistem Informasi"
), unsafe_allow_html=True)
academic = [
    project_card("skripsi.png","Dashboard klasifikasi sentimen e-wallet","Individual Thesis",
      "Implementasi Dashboard Web Klasifikasi Sentimen E-Wallet Menggunakan Naive Bayes dan Support Vector Machine",
      "Mengumpulkan dan mengolah ulasan Google Play dari DANA, GoPay, dan ShopeePay. Melakukan text preprocessing, klasifikasi sentimen, evaluasi model, dan implementasi dashboard web interaktif berbasis Streamlit.",
      LINKS["ewallet"],"Lihat Dashboard",["Python","Naive Bayes","SVM","Streamlit"]),
    project_card("UIUX.png","Prototype Student Connect","UI/UX Design",
      "Perancangan User Interface (UI) dan User Experience (UX) Website Student Connect",
      "Melakukan riset kebutuhan terhadap 100 siswa melalui kuesioner. Merancang user flow, struktur navigasi, wireframe, UI mockup, dan prototype interaktif menggunakan Figma. Hasil usability testing: SUS 91,1.",
      LINKS["student_connect"],"Lihat Perancangan",["Figma","Design Thinking","SUS 91,1"]),
    project_card("tim.png","Dokumentasi proyek PAUDQu Al-Ikhlas","Team Project",
      "Proyek Tim; Laporan Proyek Perangkat Lunak Website PAUDQu Al-Ikhlas",
      "Proyek tim pengembangan website pendaftaran siswa baru. Menganalisis dan mendokumentasikan kebutuhan klien melalui wawancara dan observasi, menyusun Requirement Document, SRS, rancangan sistem, pengujian, dan panduan penggunaan.",
      "#paudqu","Lihat Dokumentasi",["Business Analysis","SRS","BPMN"]),
]
# PAUDQu card intentionally has no external URL; use a non-navigating accessible card.
academic[2] = academic[2].replace('href="#paudqu"', 'href="javascript:void(0)"').replace('target="_blank" rel="noopener noreferrer"', '')
st.markdown('<div class="grid-3">' + "".join(academic) + '</div></section>', unsafe_allow_html=True)

# ----------------------- EXPERIENCE: LAB ------------------------
st.markdown('<section class="section navy-panel">', unsafe_allow_html=True)
st.markdown('<div class="eyebrow" style="color:#B8C8F0">Experience · Academic</div><h2 class="section-title">Laboratory Assistant</h2><p style="color:#E4EAF8;margin:.45rem 0 1.4rem">Asisten Laboratorium hingga Tutor Praktikum Program Studi Sistem Informasi</p>', unsafe_allow_html=True)
lab = f"""
<div class="experience">
 {image_tag("aslab.png","Dokumentasi kegiatan asisten laboratorium","experience-image")}
 <div style="display:grid;gap:.8rem">
  <div class="white-card"><h3>Asisten Laboratorium (1 Semester)</h3><p>1. Memeriksa dan mengintegrasikan nilai hasil laporan praktikum ke dalam data nilai.<br>2. Membantu pelaksanaan praktikum.<br>3. Mengawasi praktikan serta membantu mengatasi kendala saat praktikum.</p></div>
  <div class="white-card"><h3>Tutor Praktikum Mata Kuliah Sistem Basis Pengetahuan (1 Semester)</h3><p>1. Membimbing proses belajar mahasiswa selama praktikum.<br>2. Menyampaikan materi praktikum.<br>3. Menyusun soal Laporan Pendahuluan (LP) dan Laporan Akhir (LA).</p></div>
 </div>
</div></section>
"""
st.markdown(lab, unsafe_allow_html=True)

# -------------------------- SWIMPLASH ----------------------------
swim = f"""
<section class="section navy-panel">
 <div class="eyebrow" style="color:#B8C8F0">Operations & Data Management</div>
 <h2 class="section-title">Operations Admin & Data Management</h2>
 <p style="color:#E4EAF8;margin:.45rem 0 1.3rem">Admin Operasional & Manajemen Data Swimplash Swimming Club</p>
 <div class="experience">
  <div class="white-card"><h3>Kontribusi</h3><p>1. Menambah, merapikan, dan memperbarui data murid serta pelatih melalui portal internal.<br>2. Menangani komunikasi dan follow-up calon murid dari tahap inquiry, trial, hingga keputusan pendaftaran.<br>3. Mengkoordinasikan kebutuhan murid antara orang tua dan pelatih.<br>4. Mengatur jadwal serta reschedule pelatih dan murid.<br>5. Membantu proses perpanjangan paket latihan.</p></div>
  {image_tag("swimplash.png","Dokumentasi Operations Admin dan Data Management","experience-image")}
 </div>
 <div class="skill-pills"><span>Administrative & Data Management</span><span>Customer Service</span><span>Lead Handling</span><span>Problem Solving</span></div>
</section>
"""
st.markdown(swim, unsafe_allow_html=True)

# ------------------------ GERAKAN SUKA BACA ---------------------
gsb = f"""
<section class="section navy-panel">
 <div class="eyebrow" style="color:#B8C8F0">Volunteer Experience</div>
 <h2 class="section-title">Gerakan Suka Baca Volunteer</h2>
 <p style="color:#E4EAF8;margin:.45rem 0 1.3rem">Divisi Operasional | Sekretaris Database & Presensi Relawan</p>
 <div class="experience">
  <div class="white-card"><h3>Peran</h3><p>1. Mengelola database relawan.<br>2. Mencatat presensi kegiatan online.<br>3. Mengirim reminder berdasarkan divisi/kegiatan.<br>4. Membantu penjadwalan dan koordinasi kegiatan.<br>5. Memperbarui data tracking presensi.</p></div>
  {image_tag("gsb.png","Dokumentasi Gerakan Suka Baca Volunteer","experience-image")}
 </div>
 <div class="skill-pills"><span>Update Data</span><span>Identify</span><span>Reminder</span><span>Attendance</span><span>Tracking</span></div>
</section>
"""
st.markdown(gsb, unsafe_allow_html=True)

# ------------------------------ PKKMB ---------------------------
pkkmb = f"""
<section class="section">
 {section_head("Committee Experience","PKKMB Event Committee","Panitia Acara Pengenalan Kehidupan Kampus Mahasiswa Baru")}
 <div class="pkkmb-grid">
  <div>{image_tag("pkkmb1.png","Andani menjadi panitia acara PKKMB")}</div>
  <div>{image_tag("pkkmb2.png","Dokumentasi kelompok PKKMB")}</div>
  <div class="pkkmb-note"><b style="color:#101F46">Kontribusi</b><br>Perencanaan dan koordinasi rangkaian acara PKKMB, termasuk penyusunan rundown, pengaturan waktu setiap sesi, koordinasi dengan penanggung jawab kegiatan, serta evaluasi pelaksanaan acara.<div class="skill-pills"><span>Event Planning & Coordination</span><span>Teamwork</span><span>Time Management</span></div></div>
  <div>{image_tag("pkkmb3.png","Dokumentasi kegiatan PKKMB")}</div>
 </div>
</section>
"""
st.markdown(pkkmb, unsafe_allow_html=True)

# -------------------------- CERTIFICATES ------------------------
certs = [
    ("seminarDA.png","Seminar Data Analyst"),
    ("mp.png","Sertifikat / kegiatan MP"),
    ("pengenalanDA.png","Pengenalan Data Analytics"),
    ("excel.png","Microsoft Excel bagi Admin"),
    ("sql.png","SQL Server Tingkat Pemula"),
]
cert_html = "".join(
    f'<div class="cert-card">{image_tag(file,title)}<div>{title}</div></div>'
    for file,title in certs
)
st.markdown(f"""
<section class="section navy-panel" id="certificates">
 <div class="eyebrow" style="color:#B8C8F0">Learning Journey</div>
 <h2 class="section-title">Certificates</h2>
 <p style="color:#E4EAF8;margin:.45rem 0 1.3rem">Sertifikat pelatihan, seminar, dan pengembangan kompetensi.</p>
 <div class="cert-grid">{cert_html}</div>
</section>
""", unsafe_allow_html=True)

# ------------------------------ FOOTER --------------------------
st.markdown(f"""
<div class="footer">
 <h2>Let’s Connect</h2>
 <p>Terbuka untuk kesempatan magang, kolaborasi, dan pengembangan di bidang Data Analyst.</p>
 <div class="hero-links">
  <a class="hero-link" href="{LINKEDIN}" target="_blank">LinkedIn ↗</a>
  <a class="hero-link" href="{EMAIL}">Email ↗</a>
  <a class="hero-link" href="{WHATSAPP}" target="_blank">WhatsApp ↗</a>
 </div>
 <p style="font-size:.75rem;margin-top:1.4rem;color:#AEBBDD">© 2026 Andani Kusuma Dewi</p>
</div>
</div>
""", unsafe_allow_html=True)
