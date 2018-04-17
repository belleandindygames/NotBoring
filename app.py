from flask  import Flask, render_template

app = Flask(__name__)
@app.route("/")
def index():
    start = 0
    mid = -15
    end = 0
    return render_template('index.html', start=start, mid=mid, end=end)

if __name__ == "__main__":
    app.run(debug = True)