from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "PC Optimizer Backend Running"

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data received"}), 400

    suggestions = []

    # Analyze RAM
    if data.get("ram_gb", 0) < 4:
        suggestions.append("Consider upgrading your RAM to at least 8GB.")

    # Analyze Disk
    if data.get("disk_usage_percent", 0) > 85:
        suggestions.append("Free up disk space: Your disk usage is high.")

    # Analyze CPU
    cpu_brand = data.get("cpu", "").lower()
    if any(old in cpu_brand for old in ["i3", "pentium", "celeron", "amd a4", "amd e1"]):
        suggestions.append("Your CPU is relatively weak. Consider upgrading.")

    # Analyze running processes
    processes = data.get("running_processes", [])
    if len(processes) > 100:
        suggestions.append("Too many background apps running. Close unused programs.")

    if not suggestions:
        suggestions.append("Your system seems OK. No major optimizations needed.")

    return jsonify({"actions": suggestions})

