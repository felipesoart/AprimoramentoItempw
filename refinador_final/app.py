from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

chances = {
    0: 50,
    1: 30,
    2: 30,
    3: 30,
    4: 30,
    5: 30,
    6: 30,
    7: 30
}

levels = [0, 0, 0]
logs = []

@app.route("/")
def index():
    return render_template("index.html", levels=levels, logs=logs)

@app.route("/aprimorar", methods=["POST"])
def aprimorar():
    global levels, logs
    index = int(request.form["item_index"])

    level = levels[index]
    chance = chances.get(level, 0)
    sucesso = random.random() < (chance / 100)

    if sucesso:
        levels[index] += 1
        logs.insert(0, f"✅ Sucesso no aprimoramento do item {index+1} para nível {levels[index]}")
        return jsonify({"resultado": "sucesso", "nivel": levels[index], "index": index, "log": logs})
    else:
        logs.insert(0, f"❌ Falha! Item {index+1} resetado para nível 0 (estava no {level})")
        levels[index] = 0
        return jsonify({"resultado": "falha", "nivel": 0, "index": index, "log": logs})

if __name__ == "__main__":
    app.run(debug=True)