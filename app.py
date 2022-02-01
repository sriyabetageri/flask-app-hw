import json
from flask import Flask, jsonify, request
from classifier import  get_prediction

app = Flask(__name__)
if __name__ == "__main__":
  app.run(debug=True)

@app.route("/add-data", methods=["POST"])
def add_task():
  if not request.json:
      return jsonify({
    "status": "error"
    "message": "please provide data"
  },400)
  
  task = {
    'id': tasks[-1]['id'] + 1
    'title':request.json['title'],
    'description': request.json.get('description', "")
    'done': False
  
    tasks.append(task)
    return jsonify({
      "status": "success"
      "message": "task added succesfully"

    })
  
  }