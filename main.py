from flask import Flask,render_template

app=Flask(__name__,template_folder='templates')

@app.route('/')
def index():
    chart_data1 = [
        {"name": "Category 1", "y": 30},
        {"name": "Category 2", "y": 50},
        {"name": "Category 3", "y": 20}
    ]

    chart_data2 = [
        {"name": "Apple", "y": 40},
        {"name": "Banana", "y": 25},
        {"name": "Orange", "y": 35}
    ]
    chart_data3 = [
        {"Category": "A", "Value": 10},
        {"Category": "B", "Value": 20},
        {"Category": "C", "Value": 15},
        {"Category": "D", "Value": 30}
    ]

    return render_template('index.html',chart_data1=chart_data1,chart_data2=chart_data2,chart_data3=chart_data3)

@app.route('/abt')
def aboutpage():
    return render_template('about.html')


@app.route('/con')
def conpage():
    return render_template('contact.html')
app.run(debug=True)