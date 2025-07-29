import streamlit as st
from Python_Programs.backend_processing import main_function,color_code_AQI,Precautions
from Python_Programs.AQI_Calc_Using_Params import AQI_Using_Params
import datetime

st.set_page_config(
    page_icon="🌇",
    page_title="Delhi AQI Predictor",
    layout = "wide"
)

st.markdown(f"""
        <div style="background-color: #CFE1E3; padding: 30px; margin-top: 20px;
                border-radius: 15px; text-align: center; box-shadow: 0 4px 8px rgba(0,0,0,0.2);">
            <div style="font-size: 35px; font-weight: bold; color:#2BD935 ;">Delhi Air Quality Predictor 🌍 </div>
        </div>
        """, unsafe_allow_html=True)
st.write("")
with st.form("AQI Prediction"):
    selected_date = st.date_input("Choose a date", value=datetime.date.today(), format="DD/MM/YYYY")
    Date = selected_date.day
    Month = selected_date.month
    Year = selected_date.year

    submitted = st.form_submit_button("Submit")

if submitted:
    AQI, PM25, PM10, NO2, SO2, CO, O3, Grade = main_function(Date, Month, Year)

    AQI_Param,color_code_params = AQI_Using_Params(Date, Month, Year)

    # Ranging the values using their respective Mean Absolute Error(s)
    final_AQI = f"{(AQI_Param)} - {int(AQI[0])}"
    final_PM25 = f"{max(0, round(PM25[0] - 23.14, 2))} - {round(PM25[0] + 23.14, 2)}"
    final_PM10 = f"{max(0, round(PM10[0] - 51.40, 2))} - {round(PM10[0] + 51.40, 2)}"
    final_NO2 = f"{max(0, round(NO2[0] - 9.55, 2))} - {round(NO2[0] + 9.55, 2)}"
    final_SO2 = f"{max(0, round(SO2[0] - 10, 2))} - {round(SO2[0] + 10, 2)}"
    final_CO = f"{max(0, round(CO[0] - 0.25, 2))} - {round(CO[0] + 0.25, 2)}"
    final_O3 = f"{max(0, round(O3[0] - 18, 2))} - {round(O3[0] + 18, 2)}"
    AQI_Color_Codes = color_code_AQI(AQI)
    Precaution = Precautions(AQI)

    def info_card(title, value, icon, unit="",color_code="#0072C6"):
        st.markdown(f"""
            <div style="background-color: #f0f2f6; padding: 20px; margin-bottom: 10px; margin-top: 5px; 
                    border-radius: 15px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); text-align: center;">
                <div style="font-size: 30px;">{icon}</div>
                <div style="font-size: 27px; font-weight: bold; margin-top: 5px;">{title}</div>
                <div style="font-size: 25px;; font-weight: bold; color: {color_code};">{value}</div>
                <div style="font-size: 14px; color: #0072C6;">{unit}</div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown(f"""
        <div style="background-color: #e0f7da; padding: 30px; margin-top: 20px;
                border-radius: 15px; text-align: center; box-shadow: 0 4px 8px rgba(0,0,0,0.2);">
            <div style="font-size: 20px; font-weight: bold;">Predicted AQI For</div>
            <div style="font-size: 25px; font-weight: bold; color:#573FD1 ;">{Date}/{Month}/{Year}</div>
            <div style="font-size: 42px; font-weight: bold; color: {AQI_Color_Codes}; margin-top: 15px;">{final_AQI}</div>
        </div>
        """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        info_card("PM 2.5", final_PM25, "🌫️", "µg/m^3",color_code_params[0])
    with col2:
        info_card("PM 10", final_PM10, "🏭", "µg/m^3",color_code_params[1])
    with col3:
        info_card("NO2", final_NO2, "🚗", "µg/m^3",color_code_params[2])

    col4, col5, col6 = st.columns(3)
    with col4:
        info_card("SO2", final_SO2, "🔋", "µg/m^3",color_code_params[3])
    with col5:
        info_card("CO", final_CO, "♨️", "mg/m^3",color_code_params[4])
    with col6:
        info_card("Ozone", final_O3, "🌐", "µg/m^3",color_code_params[5])

    st.markdown(f"""
        <div style="background-color: #e0f7da; padding: 30px; margin-top: 20px;
                border-radius: 15px; text-align: center; box-shadow: 0 4px 8px rgba(0,0,0,0.2);">
            <div style="font-size: 20px; font-weight: bold;">Overall Air Quality </div>
            <div style="font-size: 42px; font-weight: bold; color: {AQI_Color_Codes}; margin-top: 15px;">{Grade}</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown(f"""
        <div style="background-color: #e0f7da; padding: 30px; margin-top: 20px;
                border-radius: 15px; text-align: center; box-shadow: 0 4px 8px rgba(0,0,0,0.2);">
            <div style="font-size: 30px; font-weight: bold; color: #1C9CD9;">PRECAUTIONS ⛅ </div>
            <div style="font-size: 20px; font-weight: bold; color: #000000; margin-top: 15px;">{Precaution[0]}</div>
            <div style="font-size: 20px; font-weight: bold; color: #000000; margin-top: 15px;">{Precaution[1]}</div>
            <div style="font-size: 20px; font-weight: bold; color: #000000; margin-top: 15px;">{Precaution[2]}</div>
            <div style="font-size: 20px; font-weight: bold; color: #000000; margin-top: 15px;">{Precaution[3]}</div>
            <div style="font-size: 20px; font-weight: bold; color: #000000; margin-top: 15px;">{Precaution[4]}</div>
        </div>
        """, unsafe_allow_html=True)
    st.write("")
    with st.expander("📄 Which Dataset is used to train the model?"):
        st.markdown("""
            You may find all the files of the dataset used to train the model below :-

            - https://www.kaggle.com/datasets/kunshbhatia/delhi-air-quality-dataset
            - The above mentioned dataset is taken from CPCB's official website .
        """)
    with st.expander("📄 Terms & Conditions "):
        st.markdown("""
            Last updated: July 25, 2025
            - **Informational Use Only :** This model is for educational and informational purposes only , NOT for medical or emergency decisions.
            - **No Real-Time Guarantee:** Predictions are based on past data (2021-2024) and may not match official real time AQI reports.
            - **No Liability:** The developer is not responsible for any actions taken based on the model's output.
            - **Data Source:** Dataset(s) are sourced from publicly available platforms like CPCB,SBCB etc.
            - **Ownership:** All code and logic are original. Reuse or distribution without permission is prohibited ⚠️.
        """)

st.markdown("""
    <hr style="margin-top: 2rem; margin-bottom: 0;">
    <div style="text-align: center; color: grey; font-size: 14px; padding: 10px 0;">
        Disclaimer : The data is taken from CPCB's official website and the model is trained using DTU and Bawana's dataset(s).
    </div>
    <div style="text-align: center; color: grey; font-size: 14px; padding: 10px 0;">
        © 2025 Kunsh Bhatia | Built with ❤️ and ☕
    </div>
""", unsafe_allow_html=True)
