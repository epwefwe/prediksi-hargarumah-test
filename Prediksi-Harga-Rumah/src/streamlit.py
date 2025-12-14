import streamlit as st
import joblib
import pandas as pd
import numpy as np
import sys
from pathlib import Path
import yaml

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

import util as utils
import preprocessing as preprocessing
import data_preparation as data_preparation

# ==================== PAGE CONFIG ====================
st.set_page_config(
    page_title="Prediksi Harga Rumah Tebet",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================== CUSTOM STYLING ====================
st.markdown("""
    <style>
    .main {
        padding-top: 2rem;
    }
    .stMetric {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
    }
    .prediction-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 0.5rem;
        color: white;
        text-align: center;
    }
    .info-box {
        background-color: #e3f2fd;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #2196F3;
    }
    </style>
    """, unsafe_allow_html=True)

# ==================== LOAD MODEL & CONFIG ====================
@st.cache_resource
def load_model():
    konfig = utils.load_params(str(utils.dir_parent()) + utils.get_params())
    model = utils.pickle_load(str(utils.dir_parent()) + utils.cek_path_os(konfig["production_model_path"]))
    return model, konfig

try:
    model, config = load_model()
except Exception as e:
    st.error(f"Gagal memuat model: {e}")
    st.stop()

# ==================== HEADER ====================
col1, col2 = st.columns([1, 3])
with col1:
    st.image("https://img.icons8.com/color/96/000000/home.png", width=80)
with col2:
    st.title("🏠 Prediksi Harga Rumah Tebet")
    st.markdown("**Prediksi harga rumah berdasarkan karakteristik properti**")

st.divider()

# ==================== SIDEBAR ====================
with st.sidebar:
    st.header("ℹ️ Informasi Aplikasi")
    st.info("""
    Aplikasi ini menggunakan **Linear Regression Model** untuk memprediksi harga rumah 
    di area Tebet berdasarkan karakteristik properti yang Anda masukkan.
    
    **Fitur:**
    - Input data properti
    - Prediksi harga real-time
    - Validasi data otomatis
    """)
    
    st.divider()
    st.subheader("📊 Range Data")
    st.markdown(f"""
    - **Harga:** Rp {config['rentang_harga'][0]:,} - Rp {config['rentang_harga'][1]:,}
    - **Luas Bangunan:** {config['rentang_LB'][0]} - {config['rentang_LB'][1]} m²
    - **Luas Tanah:** {config['rentang_LT'][0]} - {config['rentang_LT'][1]} m²
    - **Kamar Tidur:** {config['rentang_KT'][0]} - {config['rentang_KT'][1]}
    - **Kamar Mandi:** {config['rentang_KM'][0]} - {config['rentang_KM'][1]}
    - **Garasi:** {config['rentang_GRS'][0]} - {config['rentang_GRS'][1]}
    """)

# ==================== MAIN CONTENT ====================
tab1, tab2 = st.tabs(["🔮 Prediksi", "📈 Informasi"])

with tab1:
    st.subheader("Masukkan Data Properti")
    
    # Create form
    with st.form(key="prediction_form", border=True):
        col1, col2, col3 = st.columns(3)
        
        with col1:
            harga = st.number_input(
                "💰 Harga Rumah (Rp)",
                min_value=int(config['rentang_harga'][0]),
                max_value=int(config['rentang_harga'][1]),
                value=5000000000,
                step=100000000,
                help="Estimasi harga rumah dalam rupiah"
            )
        
        with col2:
            lb = st.number_input(
                "📐 Luas Bangunan (m²)",
                min_value=int(config['rentang_LB'][0]),
                max_value=int(config['rentang_LB'][1]),
                value=150,
                help="Luas bangunan dalam meter persegi"
            )
        
        with col3:
            lt = st.number_input(
                "🌳 Luas Tanah (m²)",
                min_value=int(config['rentang_LT'][0]),
                max_value=int(config['rentang_LT'][1]),
                value=200,
                help="Luas tanah dalam meter persegi"
            )
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            kt = st.number_input(
                "🛏️ Jumlah Kamar Tidur",
                min_value=int(config['rentang_KT'][0]),
                max_value=int(config['rentang_KT'][1]),
                value=3,
                help="Jumlah kamar tidur"
            )
        
        with col2:
            km = st.number_input(
                "🚿 Jumlah Kamar Mandi",
                min_value=int(config['rentang_KM'][0]),
                max_value=int(config['rentang_KM'][1]),
                value=2,
                help="Jumlah kamar mandi"
            )
        
        with col3:
            grs = st.number_input(
                "🅿️ Kapasitas Garasi",
                min_value=int(config['rentang_GRS'][0]),
                max_value=int(config['rentang_GRS'][1]),
                value=2,
                help="Kapasitas garasi untuk mobil"
            )
        
        submitted = st.form_submit_button("🔮 Prediksi Harga", use_container_width=True)
    
    # Process prediction
    if submitted:
        try:
            # Prepare data
            input_data = pd.DataFrame({
                'HARGA': [int(harga)],
                'LB': [int(lb)],
                'LT': [int(lt)],
                'KT': [int(kt)],
                'KM': [int(km)],
                'GRS': [int(grs)]
            })
            
            # Validate data
            data_preparation.check_data(input_data, config, True)
            
            # Make prediction
            prediction = model.predict(input_data)[0]
            
            # Display result
            st.divider()
            st.markdown('<div class="prediction-box">', unsafe_allow_html=True)
            st.markdown(f"## Prediksi Harga Rumah")
            st.markdown(f"## Rp {prediction:,.0f}")
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Display input summary
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Luas Bangunan", f"{lb} m²")
                st.metric("Luas Tanah", f"{lt} m²")
            with col2:
                st.metric("Kamar Tidur", f"{kt}")
                st.metric("Kamar Mandi", f"{km}")
            with col3:
                st.metric("Garasi", f"{grs}")
                st.metric("Harga Input", f"Rp {harga:,.0f}")
            
            # Additional info
            st.divider()
            st.markdown('<div class="info-box">', unsafe_allow_html=True)
            st.markdown("""
            ✅ **Prediksi berhasil!** 
            
            Hasil prediksi di atas merupakan estimasi harga rumah berdasarkan model Machine Learning 
            yang telah dilatih dengan data properti di area Tebet. Prediksi ini dapat digunakan 
            sebagai referensi dalam proses valuation properti.
            """)
            st.markdown('</div>', unsafe_allow_html=True)
            
        except AssertionError as ae:
            st.error(f"❌ Validasi Data Gagal: {str(ae)}")
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

with tab2:
    st.subheader("📊 Informasi Model dan Data")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Model Information:**
        - Type: Linear Regression
        - Location: Tebet, Jakarta
        - Features: 6
        - Status: Production Ready ✅
        """)
    
    with col2:
        st.info("""
        **Dataset Information:**
        - Total Samples: Dataset rumah di Tebet
        - Features: HARGA, LB, LT, KT, KM, GRS
        - Preprocessing: Outlier removal & normalization
        """)
    
    st.divider()
    st.markdown("**Deskripsi Variabel:**")
    
    features_desc = {
        "HARGA": "Harga rumah dalam rupiah (target variable)",
        "LB": "Luas bangunan dalam meter persegi",
        "LT": "Luas tanah dalam meter persegi",
        "KT": "Jumlah kamar tidur",
        "KM": "Jumlah kamar mandi",
        "GRS": "Kapasitas garasi untuk mobil"
    }
    
    for feature, desc in features_desc.items():
        st.markdown(f"**{feature}:** {desc}")