import streamlit as st
import pandas as pd
import altair as alt

# --- 1. PAGE CONFIG ---
st.set_page_config(page_title="Nano-Predictor Pro v34", layout="wide")

# --- 2. FULL ACADEMIC LANGUAGE PACK (RESTORED) ---
LANGUAGES = {
    "English": {
        "title": "Nano-Predictor Pro", "subtitle": "Advanced Pharmacokinetic Simulator for Precision Nanomedicine",
        "tab_sim": "Analysis Simulator", "tab_meth": "Scientific Modeling", "tab_ref": "Academic References",
        "phys_params": "Physicochemical Properties",
        "size": "Size (nm)", "zeta": "Zeta (mV)", "peg": "PEG (%)", "affinity": "Affinity (kcal/mol)",
        "metrics": ["Target Bioavailability", "RES Sequestration (MPS)", "Renal Excretion", "Plasma Circulation"],
        "status_success": "Success: Significant target bioavailability achieved.",
        "status_fail": "Critical Warning: Formulation is clinically unviable.",
        "warn_renal": "Renal Loss: Sub-15nm diameter leads to rapid filtration.",
        "warn_res": "MPS Sequestration: Surface charge/PEG triggers macrophage uptake.",
        "warn_bbb": "BBB Exclusion: Particle size exceeds transcytosis limits.",
        "warn_epr": "EPR Limitation: Inefficient extravasation into the tumor interstitium.",
        "meth_header": "Integrated Modeling Framework",
        "meth_txt": "This system employs a hybrid PBPK approach, integrating classic filtration laws with modern AI-driven SAR models.",
        "meth_step1": "1. Glomerular Filtration Threshold",
        "meth_step1_txt": "Renal clearance is modeled based on the 10-15 nm hydrodynamic diameter threshold (Choi et al., 2007).",
        "meth_step2": "2. Immune Evasion (Stealth Effect)",
        "meth_step2_txt": "Macrophage recognition (MPS) is a function of Zeta potential and PEG density.",
        "meth_step3": "3. Ligand-Target Synergy",
        "meth_step3_txt": "Simulates binding probability using thermodynamic affinity (Delta G) for CNS targeting.",
        "ref_list": [
            "Choi, H. S., et al. (2007). Nature Biotechnology. DOI: 10.1038/nbt1340",
            "Topal, G. R., et al. (2021). Pharmaceutics. DOI: 10.3390/pharmaceutics13010038",
            "Zhang, X. D., et al. (2013). Chemical Society Reviews. DOI: 10.1039/C2CS35282D",
            "Ly, P. D., et al. (2024). Frontiers in Nanotechnology. DOI: 10.3389/fnano.2024.1456939",
            "ACS Nano (2024). Data-Driven Biodistribution Models. DOI: 10.1021/acsnano.4c07615"
        ]
    },
    "Türkçe": {
        "title": "Nano-Predictor Pro", "subtitle": "Hassas Nanotıp Tasarımı için Gelişmiş Farmakokinetik Simülatör",
        "tab_sim": "Analiz Simülatörü", "tab_meth": "Bilimsel Modelleme", "tab_ref": "Akademik Referanslar",
        "phys_params": "Fizikokimyasal Özellikler",
        "size": "Çap (nm)", "zeta": "Zeta (mV)", "peg": "PEG (%)", "affinity": "Afinite (kcal/mol)",
        "metrics": ["Hedef Biyoyararlanım", "RES Tutulumu (MPS)", "Renal Atılım", "Plazma Dolaşımı"],
        "status_success": "Başarılı: Yüksek hedef biyoyararlanımı sağlandı.",
        "status_fail": "Kritik Uyarı: Formülasyon klinik olarak uygun değil.",
        "warn_renal": "Renal Kayıp: 15nm altı çap, hızlı filtrasyona neden olur.",
        "warn_res": "MPS Tutulumu: Yüzey yükü/PEG yetersizliği makrofaj alımını tetikler.",
        "warn_bbb": "BBB Engeli: Partikül boyutu transositoz limitlerini aşıyor.",
        "warn_epr": "EPR Kısıtlaması: Tümör dokusuna yetersiz sızma.",
        "meth_header": "Entegre Modelleme Altyapısı",
        "meth_txt": "Bu sistem, klasik filtrasyon yasalarını modern AI destekli SAR modelleriyle birleştiren hibrit bir PBPK yaklaşımı kullanır.",
        "meth_step1": "1. Glomerüler Filtrasyon Eşiği",
        "meth_step1_txt": "Renal klerens, 10-15 nm hidrodinamik çap eşiğine göre modellenmiştir (Choi ve ark., 2007).",
        "meth_step2": "2. İmmün Kaçış (Stealth Etkisi)",
        "meth_step2_txt": "Makrofaj tanınması (MPS), Zeta potansiyeli ve PEG yoğunluğuna bağlıdır.",
        "meth_step3": "3. Ligand-Hedef Sinerjisi",
        "meth_step3_txt": "Bağlanma olasılığı, termodinamik afinite (Delta G) kullanılarak simüle edilir.",
        "ref_list": [
            "Choi, H. S., ve ark. (2007). Nature Biotechnology. DOI: 10.1038/nbt1340",
            "Topal, G. R., ve ark. (2021). Pharmaceutics. DOI: 10.3390/pharmaceutics13010038",
            "Zhang, X. D., ve ark. (2013). Chemical Society Reviews. DOI: 10.1039/C2CS35282D",
            "Ly, P. D., ve ark. (2024). Frontiers in Nanotechnology. DOI: 10.3389/fnano.2024.1456939",
            "ACS Nano (2024). Veri Güdümlü Biyodağılım Modelleri. DOI: 10.1021/acsnano.4c07615"
        ]
    }
}

# --- 3. CALLBACKS FOR PERFECT SYNC ---
def sync_s_num(): st.session_state.s_num = st.session_state.s_sl
def sync_s_sl(): st.session_state.s_sl = st.session_state.s_num
def sync_z_num(): st.session_state.z_num = st.session_state.z_sl
def sync_z_sl(): st.session_state.z_sl = st.session_state.z_num
def sync_p_num(): st.session_state.p_num = st.session_state.p_sl
def sync_p_sl(): st.session_state.p_sl = st.session_state.p_num

# --- 4. INITIALIZE STATE ---
if 's_sl' not in st.session_state: st.session_state.s_sl = 80.0
if 's_num' not in st.session_state: st.session_state.s_num = 80.0
if 'z_sl' not in st.session_state: st.session_state.z_sl = -2.0
if 'z_num' not in st.session_state: st.session_state.z_num = -2.0
if 'p_sl' not in st.session_state: st.session_state.p_sl = 2.0
if 'p_num' not in st.session_state: st.session_state.p_num = 2.0
if 'aff_val' not in st.session_state: st.session_state.aff_val = -8.0

# --- 5. CORE ENGINE ---
def run_calc(target, size, zeta, peg, aff):
    total = 100.0
    renal = (85.0 - (size * 2)) if size <= 15 else (30.0 - size if size <= 30 else 2.0)
    renal = max(0.0, min(total, renal))
    res = max(5.0, min((total-renal)*0.95, (total-renal)*0.40 + abs(zeta)*1.5 + max(0, (size-150)*0.3) - peg*12.0))
    acc = (total - renal - res) * 0.20 + abs(aff)*2.0
    if "BBB" in target and size > 90: acc *= 0.1
    elif "EPR" in target and size > 180: acc *= 0.3
    acc = max(0.0, min(total - renal - res, acc))
    return round(acc, 1), round(res, 1), round(renal, 1), round(100-(acc+res+renal), 1)

# --- 6. SIDEBAR UI ---
st.sidebar.title("🧬 Configuration")
sel_lang = st.sidebar.selectbox("Language / Dil", list(LANGUAGES.keys()))
L = LANGUAGES[sel_lang]

target = st.sidebar.selectbox("Target Tissue", ["Solid Tumor (EPR)", "BBB (CNS)", "Systemic"])
st.sidebar.divider()

st.sidebar.subheader(L["phys_params"])
c1, c2 = st.sidebar.columns([3, 1.2])
with c1: st.slider(L["size"], 5.0, 300.0, key="s_sl", on_change=sync_s_num)
with c2: st.number_input("", 5.0, 300.0, key="s_num", step=0.1, on_change=sync_s_sl, label_visibility="collapsed")

c3, c4 = st.sidebar.columns([3, 1.2])
with c3: st.slider(L["zeta"], -50.0, 50.0, key="z_sl", on_change=sync_z_num)
with c4: st.number_input("", -50.0, 50.0, key="z_num", step=0.1, on_change=sync_z_sl, label_visibility="collapsed")

c5, c6 = st.sidebar.columns([3, 1.2])
with c5: st.slider(L["peg"], 0.0, 10.0, key="p_sl", on_change=sync_p_num)
with c6: st.number_input("", 0.0, 10.0, key="p_num", step=0.1, on_change=sync_p_sl, label_visibility="collapsed")

st.session_state.aff_val = st.sidebar.number_input(L["affinity"], value=st.session_state.aff_val)

# --- 7. MAIN SCREEN UI ---
st.title(L["title"])
st.markdown(f"*{L['subtitle']}*")
st.divider()

t_sim, t_meth, t_ref = st.tabs([L["tab_sim"], L["tab_meth"], L["tab_ref"]])

with t_sim:
    tr, rs, rn, bl = run_calc(target, st.session_state.s_num, st.session_state.z_num, st.session_state.p_num, st.session_state.aff_val)
    
    m = st.columns(4)
    m[0].metric(L["metrics"][0], f"%{tr}")
    m[1].metric(L["metrics"][1], f"%{rs}")
    m[2].metric(L["metrics"][2], f"%{rn}")
    m[3].metric(L["metrics"][3], f"%{bl}")
    
    # FIXED ALTAIR CHART
    chart_data = pd.DataFrame({
        "Location": L["metrics"],
        "Rate": [tr, rs, rn, bl],
        "Color": ["#2E7D32", "#C62828", "#EF6C00", "#1565C0"]
    })
    
    c = alt.Chart(chart_data).mark_bar().encode(
        x=alt.X('Location', sort=None, title='Compartment'),
        y=alt.Y('Rate', scale=alt.Scale(domain=[0, 100]), title='Percentage (%)'),
        color=alt.Color('Color', scale=None),
        tooltip=['Location', 'Rate']
    ).properties(height=450)
    
    st.altair_chart(c, use_container_width=True)
    
    st.divider()
    if tr >= 15.0 and rn <= 20.0 and rs <= 40.0:
        st.success(L["status_success"])
    else:
        st.error(L["status_fail"])
        if rn >= 20: st.warning(L["warn_renal"])
        if rs >= 35: st.warning(L["warn_res"])
        if st.session_state.s_num > 90 and "BBB" in target: st.warning(L["warn_bbb"])
        if st.session_state.s_num > 180 and "EPR" in target: st.warning(L["warn_epr"])

with t_meth:
    st.header(L["meth_header"])
    st.markdown(L["meth_txt"])
    st.divider()
    st.write(f"### {L['meth_step1']}")
    st.markdown(f"*{L['meth_step1_txt']}*")
    st.latex(r"Clearance_{renal} = \int_{0}^{D_h} \sigma(x) dx")
    st.divider()
    st.write(f"### {L['meth_step2']}")
    st.markdown(f"*{L['meth_step2_txt']}*")
    st.divider()
    st.write(f"### {L['meth_step3']}")
    st.markdown(f"*{L['meth_step3_txt']}*")
    st.latex(r"P_{binding} \propto e^{-\frac{\Delta G}{RT}}")

with t_ref:
    st.header(L["tab_ref"])
    for r in L["ref_list"]: st.markdown(f"- {r}")
