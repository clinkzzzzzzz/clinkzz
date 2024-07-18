from flask import Flask, render_template, request

app = Flask(__name__)

# Gravity values for each planet (in m/s^2)
planet_gravity = {
    "Mercury": 3.7,
    "Venus": 8.87,
    "Earth": 9.81,
    "Mars": 3.71,
    "Jupiter": 24.79,
    "Saturn": 10.44,
    "Uranus": 8.87,
    "Neptune": 11.15
}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        weight_on_earth = float(request.form["weight_on_earth"])
        results = {}
        for planet, gravity in planet_gravity.items():
            weight_on_planet = weight_on_earth * (gravity / 9.81)
            results[planet] = round(weight_on_planet, 2)
        return render_template("index.html", results=results)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)