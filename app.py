from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)

# Load data with error handling
try:
    df = pd.read_csv('faculty_schedule.csv')
except FileNotFoundError:
    df = pd.DataFrame()  # Fallback to empty DataFrame if CSV not found
except Exception as e:
    print(f"Error loading CSV: {e}")
    df = pd.DataFrame()

@app.route('/')
def index():
    faculty_list = df[['Faculty_id', 'Name', 'Phone']].drop_duplicates()
    return render_template('index.html', faculty_list=faculty_list)

@app.route('/search', methods=['GET', 'POST'])
def search():
    result = None
    if request.method == 'POST':
        faculty_id = request.form['faculty']
        day = request.form['day']
        period = int(request.form['period'])

        match = df[
            (df['Faculty_id'] == faculty_id) &
            (df['Week_Day'] == day) &
            (df['Period'] == period)
        ]
        if not match.empty:
            result = match.iloc[0].to_dict()
        else:
            result = 'No record found.'

    faculty_list = df[['Faculty_id', 'Name']].drop_duplicates()
    return render_template('search.html', result=result, faculty_list=faculty_list)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)