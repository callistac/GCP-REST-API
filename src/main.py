from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/test/')
def hello2():
    return 'Hello, World 2!'


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
