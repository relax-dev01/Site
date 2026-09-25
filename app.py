import streamlit as st

st.set_page_config(page_title="TurboDeals Analiz", page_icon="🚗", layout="centered")

st.title("🚗 Turbo.az Elan Analizatoru")
st.write("Elanın mətnini və qiymətini daxil edin, sistem bazar dəyəri ilə müqayisə edib anomaliyanı yoxlasın.")

# İstifadəçi girişləri
car_title = st.text_input("Maşının Adı / Modeli", "BMW 320, 2018")
listing_price = st.number_input("Elandakı Qiymət (AZN)", min_value=0, value=21000)
market_avg_price = st.number_input("Bazarın Orta Qiyməti (AZN)", min_value=0, value=29000)
description = st.text_area("Elanın Açıqlama Mətni", "Maşın ideal vəziyyətdədir, heç bir xərc tələb etmir, bezkraska.")

if st.button("Analiz Et"):
    st.markdown("---")
    st.subheader("📊 Analiz Nəticəsi")
    
    # Açar sözlər
    problem_keywords = ['udar', 'vuruq', 'dəyişən', 'mator', 'karobka', 'xərc', 'kraska', 'rənglənib', 'problemli']
    positive_keywords = ['ideal', 'zavod', 'bezkraska', 'orijinal', 'heç bir xərc yoxdur']
    
    desc_lower = description.lower()
    found_problems = [word for word in problem_keywords if word in desc_lower]
    found_positives = [word for word in positive_keywords if word in desc_lower]
    
    # Fərq hesablama
    diff = listing_price - market_avg_price
    diff_percent = (diff / market_avg_price) * 100
    
    st.write(f"**Qiymət Fərqi:** {round(diff_percent, 1)}% (Bazar ortalamasından {'baha' if diff > 0 else 'ucuz'})")
    
    # Status təyini
    if diff_percent <= -20:
        if len(found_problems) == 0:
            st.error("🚨 **ANOMAL UCUZ!** Qiymət bazardan çox aşağıdır və açıqlamada heç bir problem qeyd olunmayıb. Fırıldaq və ya gizli ciddi problem ola bilər!")
        else:
            st.warning("⚠️ **Güzəştli / Problemli Təklif:** Qiymət ucuzdur, amma açıqlamada qüsurlar aşkarlandı.")
    elif diff_percent >= 15:
        st.warning("📈 **Bazar Qiymətindən Bahadır!**")
    else:
        st.success("✅ **Normal Qiymət Aralığı.**")
        
    # Tapılan detallar
    st.write("**Açıqlamadan Tapılanlar:**")
    st.write(f"- Mənfi/Qüsur sözləri: {found_problems if found_problems else 'Tapılmadı'}")
    st.write(f"- Müsbət sözlər: {found_positives if found_positives else 'Tapılmadı'}")
