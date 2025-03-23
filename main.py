from flask import Flask
from YTInsight.views import ytinsight

app = Flask(__name__)  
app.register_blueprint(ytinsight)

if __name__ == '__main__':
    app.run(debug=True)