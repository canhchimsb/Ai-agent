from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "AI Agent is running on Render!"

if __name__ == "__main__":
    app.run()