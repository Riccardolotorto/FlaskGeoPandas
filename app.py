from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/reg", methods = ["GET"])
def reg():
    import pandas 
    import geopandas
    regione = request.args.get("regione")
    regioni = geopandas.read_file("Reg01012023_g")
    ris = regioni[regioni["DEN_REG"] == regione.capitalize()][["DEN_REG"]]
    if len(ris) == 0:
        map = "regione non trovata"
    else:
        map = ris.to_html()
    return render_template("risultato.html", mappa = map)

if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 3245, debug=True)

