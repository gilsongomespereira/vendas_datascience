
from flask import Flask, jsonify
from data_preprocessing import load_data, preprocess_data
from data_analysis import analyze_data

app = Flask(__name__)

@app.route('/analyze', methods=['GET'])
def analyze():
    data = load_data('/app/data/retail_data.csv')
    data = preprocess_data(data)
    summary = analyze_data(data)
    return jsonify(summary.to_dict())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
