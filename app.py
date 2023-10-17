from flask import Flask, render_template, request
import pickle

model = pickle.load(open('churn_model.pkl', 'rb'))

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/churn', methods=['GET', 'POST'])
def get_churn():
    if request.method == "POST":
        crs = int(request.form.get("CreditScore"))
        geo = int(request.form.get("Geography"))
        gender = int(request.form.get("Gender"))
        age = int(request.form.get("Age"))
        balance = float(request.form.get("Balance"))
        hcc = int(request.form.get("HasCrCard"))
        ess = float(request.form.get("EstimatedSalary"))

        prediction = model.predict([[crs, geo, gender, age, balance, hcc, ess]])[0]

        if prediction == 1:
            pred = "The customer will exit"
        else:
            pred = "The customer will stay"
        return render_template('churn.html', pred=pred)


if __name__ == "__main__":
    app.run(debug=True)