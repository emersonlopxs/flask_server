from flask import Flask, render_template, request
from data import People
import json

# placeholder for the module
app = Flask(__name__)

# simple app ever
# mock data
people = People()


@app.route('/')
def hello():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html', people=people)


@app.route('/new', methods=["GET", "POST"])
def new():
    print(f'\n\n request: {request.method} \n\n')
    # tranform shit in json
    # print(json.dumps(people))

    if request.method == 'POST':
        print(request.values.get('title'))
        print(request.values.get('autor'))

        # do shit with the data you get from the input here
        return 'success!'

    return render_template('new.html')


if __name__ == '__main__':
    app.run(debug=True)
