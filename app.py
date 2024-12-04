from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    services = [
        '1.Consulting',
        '2.Project Management',
        '3.Software Development',
        '4.IT Support',
        '5.Custom Solutions'
    ]

    return render_template('index.html', services=services)


if __name__ == '__main__':
    app.run(debug=True)
