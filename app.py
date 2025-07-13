from flask import Flask, request, jsonify

app = Flask(__name__)

def SommeChiffres(X: int):
    S = 0
    while X != 0:
        S = S + X % 10
        X = X // 10
    return S

def Vérifier(X):
    test = True
    for i in range(X):
        if X == SommeChiffres(i) + i:
            test = False
    return test

def Chercher(N, M):
    autonombres = ""
    first = True
    for i in range(N, M):
        if Vérifier(i):
            if first:
                autonombres += str(i)
                first = False
            else:
                autonombres += "-" + str(i)
    return autonombres

@app.route('/')
def home():
    return "Flask server is running!"

@app.route('/autonombres', methods=['POST'])
def get_autonombres():
    data = request.json
    N = int(data.get("N"))
    M = int(data.get("M"))

    if 20 <= N <= 50 and N < M <= 100:
        string = Chercher(N, M)
        if string == "":
            msg = f"Aucun Autonombre entre {N} et {M}"
        else:
            msg = f"Le(s) nombre(s) Autonombre(s) : {string}"
    else:
        msg = "Veuillez respecter : 20<=N<=50 et N<M<=100"

    return jsonify({"message": msg})
