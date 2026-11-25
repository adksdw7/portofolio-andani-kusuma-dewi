from pathlib import Path
import base64
import streamlit as st

# ------------------------------------------------------------
# Andani Kusuma Dewi | Portfolio Website
# Visual pages are rendered from idePorto.pdf to preserve the
# original composition. Responsive percentage hotspots sit on
# top of each page, so the artwork scales as one fixed canvas.
# ------------------------------------------------------------

st.set_page_config(
    page_title="Andani Kusuma Dewi | Data Analyst Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

ROOT = Path(__file__).parent
ASSET_DIR = ROOT / "assets"

LINKEDIN = "https://www.linkedin.com/in/andani-kusuma-dewi-660441324"
EMAIL = "mailto:andanikd754@gmail.com?subject=Portofolio%20-%20Andani%20Kusuma%20Dewi"
WHATSAPP = "https://wa.me/6281270052004"

PROJECT_LINKS = {
    "poverty_dashboard": "https://datastudio.google.com/reporting/8879aca4-37ec-4f78-a8db-bc3ce7c74197",
    "poverty_colab": "https://colab.research.google.com/drive/10c5SLmhYozUxTug0a_TGbIJpymHd8Yuf?usp=sharing",
    "education": "https://datastudio.google.com/reporting/54d49033-80d8-4006-8635-279ec0f0842f",
    "student_stress": "https://datastudio.google.com/reporting/82787c28-82b4-4451-8bb2-77becf1ca070",
    "islamic_pilgrimage": "https://datastudio.google.com/reporting/25f2a4d6-e8b3-4078-8fb4-297f915cc810",
    "ewallet": "https://skripsisentimen.streamlit.app",
    "student_connect": "https://www.figma.com/proto/E4wcdZogSWRF1eDzpngJ4M?node-id=157-2&t=OQWxTboJfkqaujwa-6",
}

st.markdown("""
<style>
    #MainMenu, footer, header {visibility: hidden;}
    [data-testid="stSidebar"] {display: none;}
    .stApp {background: #ffffff;}
    .block-container {
        max-width: 1320px;
        padding: 1.25rem 1rem 2.5rem 1rem;
    }
    .portfolio-page {
        position: relative;
        width: 100%;
        aspect-ratio: 16 / 9;
        overflow: hidden;
        line-height: 0;
        margin: 0 auto 1.15rem auto;
        background: #101f46;
        border-radius: 2px;
    }
    .portfolio-page img {
        display: block;
        width: 100%;
        height: 100%;
        object-fit: fill;
        user-select: none;
        -webkit-user-drag: none;
    }
    .hotspot {
        position: absolute;
        display: flex;
        align-items: center;
        justify-content: center;
        box-sizing: border-box;
        border-radius: 10px;
        text-decoration: none !important;
        color: transparent !important;
        background: transparent;
        outline: none;
        line-height: 1.2;
        transition: background .16s ease, box-shadow .16s ease;
        z-index: 5;
    }
    .hotspot::after {
        content: attr(data-label);
        position: absolute;
        left: 50%;
        top: 50%;
        transform: translate(-50%, -50%);
        padding: .45rem .75rem;
        border-radius: 999px;
        background: rgba(16, 31, 70, .96);
        color: #fff;
        font: 600 clamp(8px, 1.05vw, 14px)/1.2 Arial, sans-serif;
        white-space: nowrap;
        opacity: 0;
        pointer-events: none;
        box-shadow: 0 3px 14px rgba(0,0,0,.22);
        transition: opacity .16s ease;
    }
    .hotspot:hover, .hotspot:focus-visible {
        background: rgba(255,255,255,.13);
        box-shadow: inset 0 0 0 2px rgba(255,255,255,.85);
    }
    .hotspot:hover::after, .hotspot:focus-visible::after {opacity: 1;}
    .hotspot.contact:hover, .hotspot.contact:focus-visible {
        background: rgba(255,255,255,.10);
        box-shadow: inset 0 0 0 1.5px #ffffff;
    }
    .hotspot.contact::after {font-size: clamp(8px, .85vw, 12px);}
    .page-note {
        color: #596174;
        text-align: center;
        font: 12px/1.5 Arial, sans-serif;
        margin: -.45rem 0 1.3rem;
    }
    @media (max-width: 640px) {
        .block-container {padding: .45rem .25rem 1.5rem;}
        .portfolio-page {margin-bottom: .45rem;}
        .page-note {font-size: 10px;}
    }
</style>
""", unsafe_allow_html=True)


def page_image(page_number: int) -> str:
    """Return a local slide image as a base64 data URI."""
    path = ASSET_DIR / f"slide_{page_number:02d}.png"
    if not path.exists():
        st.error(f"File gambar tidak ditemukan: {path}")
        st.stop()
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:image/png;base64,{encoded}"


def render_page(page_number: int, links: list[dict] | None = None) -> None:
    """Render one 16:9 slide with responsive percentage-based links."""
    links = links or []
    image_uri = page_image(page_number)
    overlays = []
    for item in links:
        left, top, width, height = item["rect"]
        overlays.append(
            f'<a class="hotspot {item.get("class", "")}" '
            f'href="{item["url"]}" target="_blank" rel="noopener noreferrer" '
            f'aria-label="{item["label"]}" title="{item["label"]}" '
            f'data-label="{item["label"]}" '
            f'style="left:{left}%;top:{top}%;width:{width}%;height:{height}%;"></a>'
        )

    html = (
        '<div class="portfolio-page">'
        f'<img src="{image_uri}" alt="Portfolio Andani Kusuma Dewi - halaman {page_number}" />'
        + "".join(overlays)
        + "</div>"
    )
    st.markdown(html, unsafe_allow_html=True)


# PAGE 1 — Cover: links are placed over the original contact details.
render_page(1, [
    {"rect": (6.4, 72.7, 33.2, 5.2), "url": LINKEDIN, "label": "Buka LinkedIn", "class": "contact"},
    {"rect": (6.4, 80.8, 23.2, 5.0), "url": EMAIL, "label": "Kirim email", "class": "contact"},
    {"rect": (6.4, 87.8, 13.0, 5.2), "url": WHATSAPP, "label": "Chat WhatsApp", "class": "contact"},
])

# PAGE 2 — BNSP Data Analyst: notebook and dashboard are separate links.
render_page(2, [
    {"rect": (5.0, 72.0, 12.0, 5.5), "url": PROJECT_LINKS["poverty_colab"], "label": "Lihat Notebook"},
    {"rect": (13.0, 52.0, 32.0, 43.0), "url": PROJECT_LINKS["poverty_dashboard"], "label": "Lihat Dashboard"},
])

# PAGE 3 — Three portfolio dashboard cards.
render_page(3, [
    {"rect": (5.0, 33.0, 29.0, 60.0), "url": PROJECT_LINKS["education"], "label": "Lihat Dashboard"},
    {"rect": (35.0, 33.0, 30.0, 60.0), "url": PROJECT_LINKS["student_stress"], "label": "Lihat Dashboard"},
    {"rect": (66.0, 33.0, 29.0, 60.0), "url": PROJECT_LINKS["islamic_pilgrimage"], "label": "Lihat Dashboard"},
])

# PAGE 4 — E-wallet and Student Connect are linked; PAUDQu remains visual-only.
render_page(4, [
    {"rect": (5.0, 27.0, 27.0, 64.0), "url": PROJECT_LINKS["ewallet"], "label": "Lihat Dashboard"},
    {"rect": (34.0, 27.0, 28.0, 64.0), "url": PROJECT_LINKS["student_connect"], "label": "Lihat Perancangan"},
])

# PAGE 5–9 — Experience, activities, and certificates; visual-only.
for number in range(5, 10):
    render_page(number)

st.markdown(
    '<div class="page-note">Portfolio © Andani Kusuma Dewi · '
    'Klik area proyek untuk membuka dashboard atau hasil perancangan.</div>',
    unsafe_allow_html=True,
)
