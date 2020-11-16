#not the final work still making some changes on it...this is for reference that includes the index.py
/from flask import Flask, render_template

app=Flask(__name__)
# Route for handling the login page logic
@app.route('/SignIn', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['Enter email..'] != 'admin' or request.form[' Enter password..'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('index.html', error=error)

@app.route('/')
def home():
    app.route('/')
    return render_template("signup.html")

@app.route('/about/')
def about():
    return render_template("payment.html")

if __name__=="__main__":
    app.run(debug=True)


    <div class="sub-menu-l">
