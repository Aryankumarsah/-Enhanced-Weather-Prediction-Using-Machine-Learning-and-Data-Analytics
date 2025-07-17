🌦️ Enhanced Weather Prediction Using Machine Learning and Data Analytics
📌 Project Summary
This project uses machine learning to predict the maximum daily temperature based on historical weather data. The model is trained using a Random Forest Regressor and deployed using Streamlit for real-time weather forecasting.

📄 Abstract
Weather forecasting plays a crucial role in agriculture, logistics, disaster response, and daily life. Traditional models often struggle with the complex and nonlinear nature of weather patterns.
This project enhances forecasting by leveraging data analytics and machine learning techniques to predict temperature more accurately and interactively.

🛠️ Methodology
Dataset: Seattle historical weather data (CSV format)

Preprocessing:

Handled missing values with forward fill

Extracted month, day, year from the date

Encoded weather labels into numeric codes

Features Used:

precipitation, temp_min, wind, weather_encoded, month, day

Model:

RandomForestRegressor (scikit-learn)

Evaluated using MAE and RMSE

Deployment:

Web app created using Streamlit

Takes user input and predicts temp_max

💻 Tech Stack
Language: Python

Libraries: Pandas, NumPy, scikit-learn, Streamlit, Matplotlib, Seaborn

Model Export: Pickle

Version Control: Git + GitHub

Deployment: Streamlit Cloud

📊 Results
Root Mean Squared Error (RMSE): X.XX°C

Mean Absolute Error (MAE): X.XX°C

High correlation between input weather features and predicted max temperature

🔮 Future Improvements
Integrate OpenWeatherMap API for real-time input

Use deep learning (e.g., LSTM) for time series modeling

Add weather condition decoding and interactive visualizations

