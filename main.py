from flask import Flask, render_template, request
import pandas as pd
from datetime import datetime, timedelta

app = Flask(__name__)
df = pd.read_csv('mutual_funds_data.csv')
fund_names = df['scheme_name'].unique()

def calculate_custom_return(fund_name, period_number, period_type):
    fund_data = df[df['scheme_name'].str.contains(fund_name, case=False, na=False)]
    if fund_data.empty:
        return None
    fund_data['start_date'] = pd.to_datetime(fund_data['start_date']) 
    latest_date = fund_data['start_date'].max()
    if period_type == 'months':
        start_date = latest_date - pd.DateOffset(months=period_number)
    elif period_type == 'days':
        start_date = latest_date - timedelta(days=period_number)
    elif period_type == 'weeks':
        start_date = latest_date - timedelta(weeks=period_number)
    elif period_type == 'years':
        start_date = latest_date - pd.DateOffset(years=period_number)
    else:
        return None
    filtered_data = fund_data[(fund_data['start_date'] >= start_date) & (fund_data['start_date'] <= latest_date)]
    
    if filtered_data.empty:
        return None
    fund_return = filtered_data['returns_1yr'].mean()
    return round(fund_return, 2)

@app.route('/')
def home():
    return render_template('index.html', fund_names=fund_names)

@app.route('/track_allocation', methods=['POST'])
def track_allocation():
    fund_name = request.form['fund_name']
    period_number = int(request.form['period_number'])
    period_type = request.form['period_type']
    calculated_return = calculate_custom_return(fund_name, period_number, period_type)   
    allocation = {
        'calculated_return': calculated_return
    }   
    return render_template('index.html', fund_names=fund_names, fund_name=fund_name, allocation=allocation, period_number=period_number, period_type=period_type)

if __name__ == '__main__':
    app.run(debug=True)

