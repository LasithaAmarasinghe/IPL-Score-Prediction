# 🏏 IPL-Score-Predictor

This is a Flask-based web application that predicts the first innings score for an IPL match based on the venue, batting team, and bowling team.  

![Image](https://github.com/LasithaAmarasinghe/IPL-Score-Prediction/raw/main/static/ui.png)

## 🎥 Demo

Here’s a quick demo of the **IPL-Score-Predictor**:

[![▶️ Watch the demo](https://github.com/LasithaAmarasinghe/IPL-Score-Prediction/raw/main/static/thumbnail.png)](https://vimeo.com/1068352477/3408347730)

## 🚀 Features  
- User-friendly **web interface** built with HTML, CSS, and Flask.  
- **Machine Learning model** trained on IPL data to predict match scores.  
- **Flask backend** for handling requests and making predictions.

## 🛠️ Technologies/ Tools

* Jupyter Notebook / [Google Colab](https://colab.research.google.com/)
* Python 3+
* Python packages
  * Tensorflow  - `pip install tensorflow`
  * Pandas - `pip install pandas`
  * Numpy - `pip install numpy`
  * Scikit-learn - `pip install scikit-learn`
  * Seaborn - `pip install seaborn`
  * Flask - `pip install flask`
* HTML5
* CSS3
  
![Python](https://img.shields.io/badge/python-3670A0?logo=python&logoColor=FFFF00)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?logo=jupyter&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?logo=TensorFlow&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas_-%20green?logo=pandas)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?logo=numpy&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikit-learn&logoColor=FFFFFF)
![seaborn](https://img.shields.io/badge/seaborn_-&logoColor=blue)
![flask](https://img.shields.io/badge/flask_-black)
![html5](https://img.shields.io/badge/html5-%23FF6F00.svg?logo=html5&logoColor=white)
![css3](https://img.shields.io/badge/css3-8A2BE2.svg?logo=css3&logoColor=white)


## 📈 Data

Data used are from the IPL tournaments from 2008-2017.

You can download the data set used in this project here:
* [IPL data.csv](https://github.com/LasithaAmarasinghe/IPL-Score-Prediction/blob/main/ipl_data.csv)

## 📖 Setup Instructions  

1. Clone the repository:
   ```sh
   git clone https://github.com/LasithaAmarasinghe/IPL-Score-Prediction.git
   ```
2. Navigate to the project directory:
   ```sh
   cd IPL-Score-Prediction
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the Flask application:
   ```sh
   python app.py
   ```
5. Open 🌍 `http://127.0.0.1:5000/` in your browser to access the website.

## 📝 How This Works

### 1. **User Input**
- The user selects:
  - **Venue** of the match
  - **Batting Team**
  - **Bowling Team**
- These inputs are provided through a web form.

### 2. **Data Processing**
- The selected inputs are encoded using pre-trained encoders.
- The encoded values are then scaled using a preloaded scaler to ensure the model receives properly formatted data.

### 3. **Prediction**
- The processed data is fed into the pre-trained machine learning model that predicts the score.
- The model outputs the estimated score based on historical IPL data.

### 4. **Result Display**
- The predicted score is displayed on the webpage.

## 📋 License
 
 * This project is licensed under the MIT License. See the [LICENSE](MIT-LICENSE.txt) file for details.
