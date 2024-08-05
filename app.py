from flask import Flask

app = Flask(__name__) # creating the app instance


@app.route('/home')
def home():
    return  '<h2> Welcome to flask mastery series part 1</h2>'

if __name__=='__main__':
    app.run(debug=True)