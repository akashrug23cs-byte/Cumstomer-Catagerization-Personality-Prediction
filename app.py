from flask import Flask,render_template,request
import pickle
import pandas as pd



app=Flask(__name__)

with open('jupiter/Data/model.pkl','rb') as f:
    model=pickle.load(f)

@app.route('/',methods=['GET'])
def home():
    return render_template("index.html")

@app.route('/predict',methods=['POST'])
def prediction():
    try:
        #get from data
        data={
            'Education': request.form['Education'],
            'Marital Status': request.form['Marital Status'],
            'Income': float(request.form['Income']),
            'Recency': int(request.form['Recency']),
            'Wines': int(request.form['Wines']),
            'Fruits': int(request.form['Fruits']),
            'Meat': int(request.form['Meat']),
            'Fish': int(request.form['Fish']),
            'Sweets': int(request.form['Sweets']),
            'Gold': int(request.form['Gold']),
            'Discount Purchases': int(request.form['Discount Purchases']),
            'Web': int(request.form['Web']),
            'Catalog': int(request.form['Catalog']),
            'Store': int(request.form['Store']),
            'NumWebVisitsMonth': int(request.form['NumWebVisitsMonth']),
            'Age': int(request.form['Age']),
            'Children': int(request.form['Children']),
            'total_spend': float(request.form['total_spend']),
            'total_promo': float(request.form['total_promo']),
            'Parental_status': request.form['Parental_status'],
            'Days_as_Customer': int(request.form['Days_as_Customer'])
        }

        #covert into the dataframe
        df=pd.DataFrame([data])
        df['Marital Status'] = df['Marital Status'].map({
            "Together": 1,
            "Married": 1,
            "Single": 0,
            "Divorced": 0,
            "Widow": 0,
            "Alone": 0,
            "Absurd": 0,
            "YOLO": 0
            })
        df['Education'] = df['Education'].map({
            'Basic': 0,
            '2n cycle': 1,
            'Graduation': 2,
            'Master': 3,
            'PhD': 4
        })
        df['Parental_status'] = df['Parental_status'].map({'Parent': 1, 'Non-Parent': 0})
        
 

        


        #predict the cluster using the model
        cluster=model.predict(df)[0]
        return render_template('result.html', cluster=cluster)

    except Exception as e:
        return f"Error occured :{e}"

if __name__=='__main__':
    app.run(debug=True)