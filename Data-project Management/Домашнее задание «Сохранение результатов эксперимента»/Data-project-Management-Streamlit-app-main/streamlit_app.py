import joblib
import numpy as np
import streamlit as st

st.title('Рассчитайте приблизительную оценку качества вина')
st.image('vine.jpeg')

st.sidebar.title('Для расчета приблизительной оценки качества вина, заполните параметры ниже. Формат ввода 0.00')

fixed_acidity = st.sidebar.text_input('Фиксированная кислотность (г/л)')
volatile_acidity = st.sidebar.text_input('Летучая кислотность (г/л)')
citric_acid = st.sidebar.text_input('Лимонная кислота (г/л)')
residual_sugar = st.sidebar.text_input('Остаточный сахар (г/л)')
chlorides = st.sidebar.text_input('Хлориды (г/л)')
free_sulfur_dioxide = st.sidebar.text_input('Свободный диоксид серы (мг/л)')
total_sulfur_dioxide = st.sidebar.text_input('Общий диоксид серы (мг/л)')
density = st.sidebar.text_input('Плотность (г/см³)')
pH = st.sidebar.text_input('уровень pH вина (0-14)')
sulphates = st.sidebar.text_input('Сульфаты (г/л)')
alcohol = st.sidebar.text_input('Алкоголь (% по объему)')
type = st.sidebar.selectbox('Тип вина', ['Красное','Белое'])
if type == 'Красное':
  type = 0
if type == 'Белое':
  type = 1

model = joblib.load("vine_predict_model.pkl")


if st.sidebar.button('Рассчитать оценку'):
    try:
        prediction_inp = np.array(list(map(float,[fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides,free_sulfur_dioxide,\
                    total_sulfur_dioxide, density, pH, sulphates, alcohol, type])))
        quality = round(float(model.predict(prediction_inp.reshape(1, -1))),2)

        st.write(f'### Приблизительная оценка вина:\n ## {quality}')
    except:
        st.write(f'#### ⚠ Проверьте правильность введенных данных')
