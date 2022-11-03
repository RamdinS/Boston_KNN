import config
from project_app.utils import HousePrice

from flask import Flask,jsonify,render_template,request

app = Flask(__name__)

#Home API
@app.route('/')
def home():
    #return "Welcome to Home Page"
    return render_template('index.html')

#Postman requet API
@app.route('/json_pred')
def json_pred():
    input_data = request.get_json()
  
    CRIM=input_data['CRIM']
    ZN=input_data['ZN']
    INDUS=input_data['INDUS']
    CHAS=input_data['CHAS']
    NOX=input_data['NOX']
    RM=input_data['RM']
    AGE=input_data['AGE']
    DIS=input_data['DIS']
    RAD=input_data['RAD']
    TAX=input_data['TAX']
    PTRATIO=input_data['PTRATIO']
    B=input_data['B']
    LSTAT=input_data['LSTAT']

    house = HousePrice(CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT)
    price = house.pred_price()

    return jsonify({"Car Price: ": price})

#Web API
@app.route('/submit',methods=['POST','GET'])
def submit():
    if request.method == 'POST':
        CRIM=float(request.form['CRIM'])
        ZN=float(request.form['ZN'])
        INDUS=float(request.form['INDUS'])
        CHAS=float(request.form['CHAS'])
        NOX=float(request.form['NOX'])
        RM=float(request.form['RM'])
        AGE=float(request.form['AGE'])
        DIS=float(request.form['DIS'])
        RAD=float(request.form['RAD'])
        TAX=float(request.form['TAX'])
        PTRATIO=float(request.form['PTRATIO'])
        B=float(request.form['B'])
        LSTAT=float(request.form['LSTAT'])

        house = HousePrice(CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT)
        price = house.pred_price()

        return jsonify({"Car Price: ": price})



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)