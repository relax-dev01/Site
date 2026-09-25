import streamlit as st

# Səhifə konfiqurasiyası
st.set_page_config(page_title="TurboDeals - Avtomobil Elanları", page_icon="🚗", layout="wide")

# Xüsusi CSS üslubları (Turbo dizaynına oxşatmaq üçün)
st.markdown("""
    <style>
    .main { background-color: #f4f5f7; }
    .car-card {
        background-color: white;
        padding: 15px;
        border-radius: 8px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        margin-bottom: 15px;
    }
    .price { font-size: 20px; font-weight: bold; color: #d9534f; }
    .car-title { font-size: 16px; font-weight: bold; color: #333; }
    .car-info { font-size: 13px; color: #777; }
    </style>
""", unsafe_allow_html=True)

# Yuxarı Başlıq / Menyu
st.markdown("<h1>🚗 TurboDeals <span style='font-size:16px; color:gray;'>Azərbaycanın Onlayn Avtomobil Bazarı</span></h1>", unsafe_allow_html=True)
st.markdown("---")

# Yan Panel (Filtrlər)
st.sidebar.header("🔍 Axtarış və Filtrlər")
selected_brand = st.sidebar.selectbox("Marka", ["Bütün markalar", "BMW", "Mercedes", "Toyota", "Kia", "Hyundai", "Chevrolet"])
selected_city = st.sidebar.selectbox("Şəhər", ["Bütün şəhərlər", "Bakı", "Gəncə", "Sumqayıt", "Şəki", "Lənkəran"])
sort_by = st.sidebar.selectbox("Sıralama", ["Yeni elanlar", "Ucuzdan bahaya", "Bahadan ucuza"])

st.sidebar.markdown("---")
st.sidebar.info("💡 Bu səhifə tamamilə pulsuzdur və heç bir ödəniş tələb etmir.")

# Əsas səhifədə axtarış sətri
search_query = st.text_input("🔍 Modellərə görə axtar (məsələn: F30, 320, C 200, Equinox)...", "")

st.subheader("📢 Elanlar Siyahısı")

# Zənginləşdirilmiş elan verilənləri (BMW və digər modellər)
listings = [
    {"title": "BMW 320", "year": 2018, "engine": "2.0 L", "km": "75,000 km", "price": 28500, "city": "Bakı", "desc": "Ideal veziyyetde, bezkraska, F30 restyling."},
    {"title": "BMW 328i", "year": 2014, "engine": "2.0 L", "km": "130,000 km", "price": 21500, "city": "Bakı", "desc": "M-paket yığılıb, mator karobka yaxşı."},
    {"title": "BMW M3", "year": 2021, "engine": "3.0 L", "km": "35,000 km", "price": 78000, "city": "Bakı", "desc": "Full komplektasiya, vuruqsuz gəlib."},
    {"title": "Mercedes C 200", "year": 2017, "engine": "1.6 L", "km": "90,000 km", "price": 24000, "city": "Gəncə", "desc": "Heç bir xərc tələb etmir, ideal vəziyyətdə."},
    {"title": "Chevrolet Equinox", "year": 2020, "engine": "1.5 L", "km": "65,000 km", "price": 26000, "city": "Bakı", "desc": "Ailə maşınıdır, səliqəli sürülüb."},
    {"title": "Toyota Prius", "year": 2013, "engine": "1.8 L", "km": "160,000 km", "price": 14200, "city": "Sumqayıt", "desc": "Şəhər içi az yanacaq işlədir, taksidə olmayıb."},
    {"title": "Kia Optima", "year": 2019, "engine": "2.4 L", "km": "60,000 km", "price": 31000, "city": "Bakı", "desc": "Full komplektasiya, panorama dam."}
]

# Filtrləmə məntiqi
filtered_listings = listings
if selected_brand != "Bütün markalar":
    filtered_listings = [l for l in filtered_listings if selected_brand.lower() in l['title'].lower()]

if selected_city != "Bütün şəhərlər":
    filtered_listings = [l for l in filtered_listings if l['city'] == selected_city]

if search_query:
    filtered_listings = [l for l in filtered_listings if search_query.lower() in l['title'].lower() or search_query.lower() in l['desc'].lower()]

# Sıralama məntiqi
if sort_by == "Ucuzdan bahaya":
    filtered_listings = sorted(filtered_listings, key=lambda x: x['price'])
elif sort_by == "Bahadan ucuza":
    filtered_listings = sorted(filtered_listings, key=lambda x: x['price'], reverse=True)

# Elanları səhifədə kartlar şəklində göstərmək
if not filtered_listings:
    st.warning("Axtarışınıza uyğun elan tapılmadı.")
else:
    for item in filtered_listings:
        with st.container():
            st.markdown(f"""
                <div class="car-card">
                    <div style="float: right;" class="price">{item['price']} ₼</div>
                    <div class="car-title">{item['title']}, {item['year']}</div>
                    <div class="car-info">{item['engine']} • {item['km']} • {item['city']}</div>
                    <p style="margin-top: 8px; font-size: 14px; color: #444;">{item['desc']}</p>
                </div>
            """, unsafe_allow_html=True)
