# -*- coding: utf-8 -*-
"""Домашнее задание «Сохранение результатов эксперимента»

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gKfAqZe1P7vztRYWOnSZMHmT3NtV-Tkj

**Цель проекта:**

Цель проекта состоит в создании веб-приложения, которое предсказывает качество вина на основе доступных данных. Это позволит пользователям оценить и сравнить качество вина на основе его характеристик, что может быть полезно для профессионалов виноделия, сомелье, продавцов и любителей вина.

Основные задачи проекта включают:

1. Сбор и подготовка данных: Июзучение и сбор доступных данных о различных характеристиках вин (например, уровень кислотности, содержание сахара, pH и т.д.) и их соответствующих оценок качества. Подготовка данных путем очистки, преобразования и структурирования для дальнейшего анализа и моделирования.

2. Анализ данных: Исследование данных с целью выявления взаимосвязей и паттернов между характеристиками вин и их оценками качества. Это может включать визуализацию данных, статистический анализ и поиск ключевых факторов, влияющих на качество вина.

3. Моделирование: Разработка и обучение модели машинного обучения, которая будет предсказывать качество вина на основе его характеристик. Это может включать выбор и настройку соответствующих алгоритмов машинного обучения, разделение данных на обучающую и тестовую выборки, оценку производительности модели и выбор оптимальной модели.

4. Разработка веб-приложения: Создание пользовательского интерфейса для веб-приложения, который позволит пользователям вводить характеристики вина и получать предсказания о его качестве. Веб-приложение должно быть интуитивно понятным, отзывчивым и эстетически привлекательным.

5. Тестирование и оптимизация: Проверка функциональности и производительности веб-приложения. Тестирование приложения на различных сценариях использования и устранение возможных ошибок. Оптимизация приложения с целью обеспечения быстрой и надежной работы.

6. Развертывание веб-приложения на сервере или в облаке, чтобы оно стало доступным для пользователей.

Общая цель проекта состоит в создании полезного инструмента для предсказания качества вина на основе его характеристик и предоставления пользователям удобного интерфейса для использования этой информации.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
from scipy import stats

warnings.filterwarnings('ignore')

"""#Сбор и подготовка данных

Датасет Wine Quality (Качество вина) представляет собой набор данных, который содержит информацию о химических характеристиках вина и соответствующих оценках его качества. Этот датасет широко используется в задачах анализа и предсказания качества вина с помощью методов машинного обучения.

Описание колонок (характеристик) в датасете Wine Quality:

1. Type - тип вина (красное, белое)
2. Fixed acidity (Фиксированная кислотность): содержание фиксированной кислоты в вине (г/л). Фиксированная кислотность обусловлена наличием неизбежных кислот в вине. Например, винная кислота, лимонная кислота или яблочная кислота. Этот тип кислоты обеспечивает баланс вкуса вина и придает свежесть вкусу.
3. Volatile acidity (Летучая кислотность): содержание летучей кислоты в вине (г/л). Летучая кислотность представляет собой часть кислоты в вине, которую можно почувствовать запахом. В отличие от кислот, ощутимых на вкус (о которых мы говорили выше), летучая кислотность, или, другими словами, закисление вина, является одним из наиболее распространенных дефектов.
4. Citric acid (Лимонная кислота): содержание лимонной кислоты в вине (г/л). Допускается использование в виноделии в соответствии с резолюцией Международной организации виноделия и виноградарства No. 23/2000. Она может использоваться в трех случаях: для обработки вина кислотой (увеличение кислотности), для сбора винограда, для очистки фильтров от возможных грибковых и плесневых инфекций.
5. Residual sugar (Остаточный сахар): содержание остаточного сахара в вине (г/л). Остаточный сахар - это виноградный сахар, который не был переведен в алкоголь при брожении.
6. Chlorides (Хлориды): содержание хлоридов в вине (г/л). Структура вина также зависит от содержания минералов, определяющих такие вкусовые ощущения, как соленость (сапидность). В вине присутствуют анионы неорганических кислот (хлориды, сульфаты, сульфиты...), анионы передвижных кислот, катионы металлов (калий, натрий, магний...). Их содержание зависит в основном от климатической зоны (холодный или теплый регион, солончаковые почвы в зависимости от близости моря), винодельческих практик, хранения и выдержки вина.
7. Free sulfur dioxide (Свободный диоксид серы): содержание свободного диоксида серы в вине (мг/л). Диоксид серы (сернистый оксид, диоксид серы, растворимость E220, SO2) используется как консервант благодаря своим антиоксидантным и антимикробным свойствам. Молекулярный SO2 является чрезвычайно важным антибиотиком, влияющим на значительное потребление (включая дикую дрожжь), что может проявиться в порче вина.
8. Total sulfur dioxide (Общий диоксид серы): содержание общего диоксида серы в вине (мг/л).
9. Density (Плотность): плотность вина (г/см³). Плотность вина может быть как меньше, так и больше плотности воды. Ее значение определяется прежде всего концентрацией алкоголя и сахара. Белые, розовые и красные вина обычно легкие - их плотность при 20°C ниже 998,3 кг/м3.
10. pH: уровень pH вина (0-14). pH - это мера кислотности вина. Все вина идеально имеют уровень pH от 2,9 до 4,2. Чем ниже pH, тем более кислое вино; чем выше pH, тем менее кислое вино.
11. Sulphates (Сульфаты): содержание сульфатов в вине (г/л). Сульфаты - это естественный результат брожения дрожжей сахара в вине в алкоголь. То есть наличие сульфитов в вине исключено.
12. Alcohol (Алкоголь): содержание алкоголя в вине (% по объему). Содержание алкоголя в винах зависит от многих факторов: сорта винограда и количества сахара в ягодах, технологии производства и условий выращивания. Вина сильно различаются по степени: этот параметр варьирует в диапазоне от 4,5 до 22 в зависимости от категории.
13. Quality (Качество): оценка качества вина, оцененная экспертами по шкале от 0 до 10 (целевая переменная).
"""

df = pd.read_csv('winequalityN.csv')

df.head()

# статистическая информация
df.describe()

#преобразование категориальных переменных
df['type'] = df['type'].replace({'white':1, 'red':0})

# информация о типе данных
df.info()

# проверка на наличие пустых значений
df.isnull().sum()

"""Заполняем пропущенные значения"""

from sklearn.impute import KNNImputer

imputer=KNNImputer(n_neighbors=5, weights='uniform')

imputer.fit(df)

wine_transform = imputer.transform(df)

wine = pd.DataFrame(wine_transform,columns = df.columns)

wine.head()

# проверка на наличие пустых значений
wine.isnull().sum()

# сохраняем данные после обработки
wine.to_csv('winequality_correct.csv',index=False)

"""#Анализ данных"""

winequality = pd.read_csv('winequality_correct.csv')

winequality.head()

# Исследование распределения оценок качества
sns.countplot(x=winequality['quality'])
plt.title('Распределение оценок качества')
plt.show()

"""Большинство образцов вина имеют оценку качества в диапазоне от 5 до 7"""

sns.countplot(x=winequality['type'].replace({0:'red', 1:'white'}))
plt.title('Распределение по типу вина')
plt.show()

"""В данном датасете наблюдаем дисбаланс классов красного и белого вина, это нужно будет учитывать при построении модели машинного обучения"""

sns.countplot(x=(winequality.loc[winequality['type'] == 0]).quality)
plt.title('Распределение оценок качества красного вина')
plt.show()

sns.countplot(x=(winequality.loc[winequality['type'] == 1]).quality)
plt.title('Распределение оценок качества белого вина')
plt.show()

print(f"Средняя оценка белого вина {(winequality.loc[winequality['type'] == 1]).quality.mean()}")

print(f"Средняя оценка красного вина {(winequality.loc[winequality['type'] == 0]).quality.mean()}")

"""По распределению оценок по типу вина, видно что белому вину чаще ставят более высокие оценки"""

# построим график отображения признаков
fig, ax = plt.subplots(12, 3, figsize=(30, 90))

for index, i in enumerate((winequality.drop('type', axis=1, inplace=False)).columns):
    sns.distplot(winequality[i], ax=ax[index, 0], color='green')
    sns.boxplot(winequality[i], ax=ax[index, 1], color='yellow')
    stats.probplot(winequality[i], plot=ax[index, 2])

    ax[index, 0].tick_params(axis='both', labelsize=20)
    ax[index, 1].tick_params(axis='both', labelsize=20)
    ax[index, 2].tick_params(axis='both', labelsize=20)

    ax[index, 0].set_title(i, fontsize=30)
    ax[index, 1].set_title(i, fontsize=30)
    ax[index, 2].set_title(i, fontsize=30)

fig.tight_layout()
fig.subplots_adjust(top=0.95)
plt.suptitle('Графики распределение признаков', fontsize=50)

plt.show()

"""У большенства признаков распределение близкое к нормальному, так же имеются выбросы которые позднее нужно будет обработать перед обучением модели"""

# построим матрицу корреляции для определения зависимости признаков
corr = winequality.corr()
plt.figure(figsize=(20,10))
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.show()

"""Наибольшее значение корреляции с целевой переменной у признака 'alcogol', данный признак будет являться основным для определения качества вина, так же присутствует не очень сильная отрицательная корреляция с признаком 'density'(плотность)

# Подготовка данных для обучения модели
"""

# удаляем выбросы
for col in winequality.columns:
  up = (winequality[col].quantile(0.75)-winequality[col].quantile(0.25)) * 1.5 + winequality[col].quantile(0.75)
  low = winequality[col].quantile(0.25)- (winequality[col].quantile(0.75)-winequality[col].quantile(0.25)) * 1.5
  data = winequality[(winequality[col]<up)&(winequality[col]>low)]
print(f'Длина датасета после удаления выбросов {len(data)}, удалено {round(100-len(data)/len(winequality)*100, 2)} % данных')

"""Устраним дисбаланс классов красного и белого вина"""

from collections import Counter
from imblearn.over_sampling import SMOTE

sm = SMOTE(random_state=42, k_neighbors= 5)

X_type, y_type = data.drop('type', axis = 1), data['type']

X_smout, y_smout = sm.fit_resample(X_type, y_type)

Counter(y_smout)

winequality_for_ML = pd.concat([X_smout, y_smout], axis= 1)

winequality_for_ML.head()

"""Сохраним готовый датасет для обучения модели"""

winequality_for_ML.to_csv('winequality_for_ML.csv',index=False)

"""#Выбор модели и обучение"""

df = pd.read_csv('winequality_for_ML.csv')

df.head()

"""**PyCaret** - это библиотека машинного обучения на языке Python, которая предоставляет простой и удобный интерфейс для автоматизации и ускорения процесса разработки моделей машинного обучения. Она обладает множеством функций, предназначенных для выполнения различных задач в рамках процесса разработки моделей, включая предобработку данных, выбор моделей, настройку гиперпараметров, оценку моделей и развертывание моделей.

Вот основные особенности и возможности библиотеки PyCaret:

1. Упрощенный рабочий процесс: PyCaret предлагает упрощенный рабочий процесс, который позволяет разработчикам быстро перейти от идеи к моделированию, минимизируя необходимость вручную выполнять множество шагов, таких как предобработка данных, кодирование категориальных переменных, масштабирование данных и выбор признаков.

2. Автоматический выбор модели: PyCaret предоставляет функции для автоматического выбора наиболее подходящей модели для задачи машинного обучения. Он автоматически применяет и оценивает несколько моделей, используя предустановленные наборы гиперпараметров, и выводит ранжированный список моделей по метрике производительности.

3. Тюнинг гиперпараметров: PyCaret предлагает возможность настройки гиперпараметров моделей с использованием автоматической оптимизации. Он применяет алгоритмы оптимизации, такие как случайный поиск или генетические алгоритмы, для настройки гиперпараметров моделей и выбора оптимальной комбинации.

4. Оценка моделей: PyCaret предоставляет обширный набор метрик оценки производительности моделей, таких как точность, полнота, F1-мера, ROC-AUC и другие. Он также предоставляет графические инструменты для визуализации результатов оценки моделей.

5. Развертывание моделей: PyCaret предоставляет функции для сохранения обученных моделей и их развертывания в производственной среде. Он позволяет сохранять модели в различных форматах, включая Python-скрипты, сериализованные объекты и формат PMML.

6. Поддержка различных задач: PyCaret поддерживает различные задачи машинного обучения, включая классификацию, регрессию, кластеризацию, а также обработку несбалансированных данных и временных рядов.

Благодаря своей простоте использования и широкому функционалу, PyCaret может значительно ускорить процесс разработки моделей машинного обучения и упростить их развертывание в производственной среде.
"""

pip install pycaret

from pycaret.regression import *

reg = setup(data=df, target='quality')

"""Сравниваем производительность различных моделей"""

best_model = compare_models()

"""Выберем лучшую модель на основе результатов сравнения. Ей оказалась Extra Trees Regressor.

**Алгоритм Extra Trees Regressor** (Extremely Randomized Trees Regressor) является одним из ансамблевых методов машинного обучения, основанным на деревьях решений. Он является вариантом случайного леса (Random Forest), но с некоторыми отличиями в построении и обучении модели.

Вот основные характеристики и принцип работы Extra Trees Regressor:

1. Ансамбль деревьев: Extra Trees Regressor использует ансамбль решающих деревьев, где каждое дерево обучается на случайной подвыборке обучающих данных и случайном подмножестве признаков. При этом в отличие от случайного леса, Extra Trees Regressor выбирает случайные разделения для каждого узла дерева, не ища оптимальные разделения, что делает его еще более случайным.

2. Случайные разделения: В отличие от обычных деревьев решений и случайного леса, где выбор разделения в узлах дерева осуществляется на основе наилучшего разделения (например, по критерию наибольшего прироста информации), Extra Trees Regressor использует случайные разделения, что приводит к дополнительному увеличению случайности и разнообразия моделей в ансамбле.

3. Случайная подвыборка признаков: Каждое дерево строится на случайном подмножестве признаков из общего набора признаков. Это позволяет деревьям быть более независимыми и разнообразными, улучшая обобщающую способность модели.

4. Агрегирование прогнозов: Прогнозы каждого дерева в ансамбле усредняются для получения окончательного прогноза модели. В случае регрессии, прогнозы деревьев усредняются, например, путем вычисления среднего значения.

Extra Trees Regressor обладает несколькими преимуществами:

- Более низкая склонность к переобучению: Благодаря случайному выбору разделений и случайной подвыборке признаков, Extra Trees Regressor обладает меньшей склонностью к переобучению по сравнению с обычными деревьями решений.

- Высокая скорость обучения и предсказ

ания: За счет использования случайных разделений и более простой процедуры обучения, Extra Trees Regressor может работать быстрее, особенно на больших наборах данных.

- Хорошая устойчивость к выбросам: Благодаря агрегации прогнозов из множества деревьев, Extra Trees Regressor обладает хорошей устойчивостью к выбросам в данных.

Однако Extra Trees Regressor также имеет некоторые ограничения:

- Меньшая интерпретируемость: В отличие от обычных деревьев решений, Extra Trees Regressor не предоставляет явной информации о важности признаков или причинности.

- Более высокая вычислительная сложность: По сравнению с обычными деревьями решений, Extra Trees Regressor требует больше вычислительных ресурсов из-за большего числа случайных разделений.

Extra Trees Regressor является мощным инструментом для решения задач регрессии, особенно в случаях, когда данные содержат шумы, выбросы или большое количество признаков. Он может быть использован как самостоятельный алгоритм или включен в ансамблевые методы, такие как случайный лес или градиентный бустинг, для еще более точных предсказаний.
"""

best_model = create_model('et')

"""Выводим метрики оценки производительности модели, график остатков и другую информацию"""

evaluate_model(best_model)

"""Судя по графику Feature Importance Plot, как и предполагалось ранее, главным предиктором для модели является признак 'alcogol', следующим важным признаком является 'volatile acidity', остальный признаки приблизительно одинаково, но тем не менее значительно, приносят вклад в качество предсказания модели.

**Разделяем на тренировочные и тестовые данные**
"""

from sklearn.model_selection import train_test_split

X, y = df.drop('quality', axis= 1), df['quality']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=True, random_state = 1)

"""**Оптимизация гиперпараметров модели**"""

from sklearn.ensemble import ExtraTreesRegressor

from sklearn.metrics import mean_squared_error

from sklearn.model_selection import cross_val_score

!pip install optuna

import optuna

def objective(trial):
    params = {
        'n_estimators': trial.suggest_int('n_estimators', 100, 1000),
        'max_depth': trial.suggest_categorical('max_depth', [3, 4, 5, 6, 7]),
        'min_samples_split': trial.suggest_int('min_samples_split', 1, 50),
        'min_samples_leaf': trial.suggest_int('min_samples_leaf', 1, 50),
        'random_state': 149
    }

    model = ExtraTreesRegressor()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    return mean_squared_error(y_test, predictions)

study = optuna.create_study(direction="minimize")
study.optimize(objective, n_trials=50)

print(f'Best value: {study.best_trial.value}')
print(f'Best params: {study.best_trial.params}')

model = ExtraTreesRegressor(n_estimators= 234, max_depth= 4, min_samples_split=10, min_samples_leaf = 45, random_state= 149)
model.fit(X_train, y_train)

"""Прверим качество модели на кроссвалидации"""

cv_scores = cross_val_score(model, X, y, cv=10,scoring= 'neg_mean_squared_error')

print(f'cross_val_score MSE: {cv_scores}',f'cross_val_score MSE mean: {round(cv_scores.mean(),2)}', sep = '\n')

"""Сохраняем модель"""

!pip install joblib

import joblib

joblib_file = "vine_predict_model.pkl"
joblib.dump(model, joblib_file)

"""#Создание веб-приложения с помощью библиотеки Streamlit"""

!pip install -q streamlit

# Commented out IPython magic to ensure Python compatibility.
# %%writefile streamlit_app.py
# import joblib
# import streamlit as st
# import numpy as np
# 
# 
# st.title('Рассчитайте приблизительную оценку качества вина')
# st.image('vine.jpeg')
# 
# st.sidebar.title('Для расчета приблизительной оценки качества вина, заполните параметры ниже. Формат ввода 0.00')
# 
# fixed_acidity = st.sidebar.text_input('Фиксированная кислотность (г/л)')
# volatile_acidity = st.sidebar.text_input('Летучая кислотность (г/л)')
# citric_acid = st.sidebar.text_input('Лимонная кислота (г/л)')
# residual_sugar = st.sidebar.text_input('Остаточный сахар (г/л)')
# chlorides = st.sidebar.text_input('Хлориды (г/л)')
# free_sulfur_dioxide = st.sidebar.text_input('Свободный диоксид серы (мг/л)')
# total_sulfur_dioxide = st.sidebar.text_input('Общий диоксид серы (мг/л)')
# density = st.sidebar.text_input('Плотность (г/см³)')
# pH = st.sidebar.text_input('уровень pH вина (0-14)')
# sulphates = st.sidebar.text_input('Сульфаты (г/л)')
# alcohol = st.sidebar.text_input('Алкоголь (% по объему)')
# type = st.sidebar.selectbox('Тип вина', ['Красное','Белое'])
# if type == 'Красное':
#   type = 0
# if type == 'Белое':
#   type = 1
# 
# model = joblib.load("vine_predict_model.pkl")
# 
# 
# if st.sidebar.button('Рассчитать оценку'):
#     try:
#         prediction_inp = np.array(list(map(float,[fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides,free_sulfur_dioxide,\
#                     total_sulfur_dioxide, density, pH, sulphates, alcohol, type])))
#         quality = round(float(model.predict(prediction_inp.reshape(1, -1))),2)
# 
#         st.write(f'### Приблизительная оценка вина:\n ## {quality}')
#     except:
#         st.write(f'#### ⚠ Проверьте правильность введенных данных')

!npm install localtunnel

!streamlit run /content/streamlit_app.py &>/content/logs.txt &

import urllib
print("Password/Enpoint IP for localtunnel is:",urllib.request.urlopen('https://ipv4.icanhazip.com').read().decode('utf8').strip("\n"))

!npx localtunnel --port 8501

"""#Развертывание приложения в облаке Streamlit

Полный процесс развертывания приложения описан по ссылке https://docs.streamlit.io/streamlit-community-cloud/get-started/deploy-an-app

Итоговая ссылка на веб-приложение https://vine-quality-prediction.streamlit.app/

---

#Тестирование веб-приложения

Работа приложения проверялась на различных браузерах. Ошибки и исключения обрабатываются корректно. Работа приложения под большой нагрузкой не проверялась.
"""