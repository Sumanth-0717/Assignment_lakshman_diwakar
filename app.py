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
    if period_type == 'years':
        if period_number == 1:
            fund_return = fund_data['returns_1yr'].values[0]
        elif period_number == 3:
            fund_return = fund_data['returns_3yr'].values[0]
        elif period_number == 5:
            fund_return = fund_data['returns_5yr'].values[0]
        else:
            return None  
    elif period_type == 'months':
        fund_return = fund_data['returns_1yr'].values[0] * (period_number / 12)
    elif period_type == 'weeks':
        fund_return = fund_data['returns_1yr'].values[0] * (period_number / 52)
    elif period_type == 'days':
        fund_return = fund_data['returns_1yr'].values[0] * (period_number / 365)
    else:
        return None

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
