from flask import Flask
import wavelengthAnalysis as wa
import youtubeConverter as yc

app = Flask(__name__)

@app.route("/")
def timeStamps():
    title = request.get_json()
    song_title
    return {"Bound 2" : ["Kanye West", "1:15"]
            "Bound" : ["Ponderosa Twins Plus One", "1:45"]}
if __name__ == "__main__":
    app.run(debug=True)

