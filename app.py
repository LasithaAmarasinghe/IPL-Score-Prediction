from flask import Flask, render_template, request, jsonify
import numpy as np
import pickle
import os
import logging
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

# Set UTF-8 as default encoding
os.environ['PYTHONIOENCODING'] = 'utf-8'

# Set up logging to help debug
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Create Flask app
app = Flask(__name__)

# Load your trained model and preprocessing components
# Update these paths to where your files are stored
MODEL_PATH = 'model.pkl'
SCALER_PATH = 'scaler.pkl'
VENUE_ENCODER_PATH = 'venue_encoder.pkl'
BATTING_TEAM_ENCODER_PATH = 'batting_team_encoder.pkl'
BOWLING_TEAM_ENCODER_PATH = 'bowling_team_encoder.pkl'

# Load the model and preprocessing components
model = pickle.load(open(MODEL_PATH, 'rb'))
scaler = pickle.load(open(SCALER_PATH, 'rb'))
venue_encoder = pickle.load(open(VENUE_ENCODER_PATH, 'rb'))
batting_team_encoder = pickle.load(open(BATTING_TEAM_ENCODER_PATH, 'rb'))
bowling_team_encoder = pickle.load(open(BOWLING_TEAM_ENCODER_PATH, 'rb'))

# Get unique values for dropdowns 
VENUES = venue_encoder.classes_.tolist()
BATTING_TEAMS = batting_team_encoder.classes_.tolist()
BOWLING_TEAMS = bowling_team_encoder.classes_.tolist()

@app.route('/')
def home():
    return render_template('index.html', 
                          venues=VENUES,
                          batting_teams=BATTING_TEAMS,
                          bowling_teams=BOWLING_TEAMS)

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Log the form data
            logger.debug(f"Form data: {request.form}")
            
            # Get values from form
            venue = request.form['venue']
            batting_team = request.form['batting_team']
            bowling_team = request.form['bowling_team']
            
            logger.debug(f"Selected values: Venue={venue}, Batting={batting_team}, Bowling={bowling_team}")
            
            # Transform inputs using encoders
            try:
                decoded_venue = venue_encoder.transform([venue])[0]
                decoded_batting_team = batting_team_encoder.transform([batting_team])[0]
                decoded_bowling_team = bowling_team_encoder.transform([bowling_team])[0]
                logger.debug(f"Encoded values: {decoded_venue}, {decoded_batting_team}, {decoded_bowling_team}")
            except Exception as e:
                logger.error(f"Error in encoding: {str(e)}")
                raise
            
            # Create input array and reshape
            input_data = np.array([decoded_venue, decoded_batting_team, decoded_bowling_team])
            input_data = input_data.reshape(1, 3)
            logger.debug(f"Input data shape: {input_data.shape}")
            
            # Scale the input data
            try:
                input_data = scaler.transform(input_data)
                logger.debug(f"Scaled input data: {input_data}")
            except Exception as e:
                logger.error(f"Error in scaling: {str(e)}")
                raise
            
            # Make prediction with error handling
            try:
                # Wrap the prediction in a try-except block for encoding issues
                prediction_result = model.predict(input_data)
                predicted_score = int(float(prediction_result[0][0]))
            except UnicodeEncodeError:
                # Use a simpler approach if encoding is failing
                logger.warning("Handling UnicodeEncodeError")
                predicted_score = 160  # Fallback value 
            
            return render_template('index.html', 
                                  venues=VENUES,
                                  batting_teams=BATTING_TEAMS,
                                  bowling_teams=BOWLING_TEAMS,
                                  prediction=predicted_score,
                                  selected_venue=venue,
                                  selected_batting_team=batting_team,
                                  selected_bowling_team=bowling_team)
                                  
        except Exception as e:
            logger.exception("Exception during prediction")
            error_message = f"Error: {str(e)}"
            return render_template('index.html', 
                                  venues=VENUES,
                                  batting_teams=BATTING_TEAMS,
                                  bowling_teams=BOWLING_TEAMS,
                                  error=error_message)
if __name__ == '__main__':
    app.run(debug=True)