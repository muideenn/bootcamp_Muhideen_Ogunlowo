
from flask import Flask, request, jsonify, send_file, Response
import io
import numpy as np
import matplotlib.pyplot as plt

from src.utils import load_model

app = Flask(__name__)

def _predict_array(arr):
    model = load_model()
    return model.predict(np.array(arr))

@app.route("/", methods=["GET"])
def index():
    return jsonify({"status": "ok", "endpoints": ["/predict (POST)", "/predict/<x1>", "/predict/<x1>/<x2>", "/plot"]})

@app.route("/predict", methods=["POST"])
def predict_post():
    # Expect JSON: {"features": [[x1, x2], [x1, x2], ...]}
    try:
        data = request.get_json(force=True)
        feats = data.get("features", None)
        if feats is None:
            return jsonify({"error": "Missing 'features'"}), 400
        preds = _predict_array(feats).tolist()
        return jsonify({"predictions": preds})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/predict/<x1>", methods=["GET"])
def predict_get_one(x1):
    try:
        x1 = float(x1)
        preds = _predict_array([[x1, 0.0]])  # assume x2 = 0 if omitted
        return jsonify({"input": {"x1": x1, "x2": 0.0}, "prediction": float(preds[0])})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/predict/<x1>/<x2>", methods=["GET"])
def predict_get_two(x1, x2):
    try:
        x1 = float(x1)
        x2 = float(x2)
        preds = _predict_array([[x1, x2]])
        return jsonify({"input": {"x1": x1, "x2": x2}, "prediction": float(preds[0])})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/plot", methods=["GET"])
def plot_route():
    # Return a tiny scatter of random points + a line
    buf = io.BytesIO()
    xs = np.linspace(-3, 3, 50)
    ys = 2.0 * xs + 1.0
    plt.figure(figsize=(5,3))
    plt.scatter(xs, ys + np.random.normal(scale=0.5, size=len(xs)))
    plt.plot(xs, ys)
    plt.title("Sample Plot")
    plt.tight_layout()
    plt.savefig(buf, format="png")
    plt.close()
    buf.seek(0)
    return Response(buf.getvalue(), mimetype="image/png")

if __name__ == "__main__":
    # Use: python app.py
    # Then in another terminal:
    #   curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d '{"features":[[1.0,2.0],[0.5,-1.2]]}'
    app.run(host="0.0.0.0", port=5000, debug=False)
