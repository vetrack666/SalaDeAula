from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    return render_template("index.html", agora=agora)

if __name__ == "__main__":
    # Executa em http://127.0.0.1:5000
    app.run(debug=True)
