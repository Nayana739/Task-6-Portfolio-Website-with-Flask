from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "your_secret_key"  # needed for flash messages


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    # You can replace this with an email sending logic later
    print(f"New message from {name} ({email}): {message}")

    flash('Your message has been sent successfully!', 'success')
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
