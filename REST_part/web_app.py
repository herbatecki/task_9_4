from flask import Flask, request, jsonify, abort, make_response
from compacts_methods import compacts

app = Flask(__name__)
app.config['SECRET_KEY']='okon'

@app.route('/api/v1/compacts/', methods = ['GET'])
def compacts_list_api_v1():
  return jsonify(compacts.collect())

@app.route('/api/v1/compacts/<int:compact_id>', methods = ['GET'])
def choose_compact(compact_id):
    compact = compacts.choose(compact_id)
    if not compact:
        abort(404)
    return jsonify({'compact': compact})

@app.errorhandler(404)
def not_found(error):
  return make_response(jsonify({'error': 'Not found', 'status_code': 404}), 404)

@app.route('/api/v1/compacts/', methods =['POST'])
def make_compact():
  if not request.json or not 'band' in request.json:
    abort(400)
  compact = {
    'id': compacts.collect()[-1]['id']+1,
    'band' : request.json['band'],
    'album' : request.json.get("album", ""), # tu i niżej użyta wbudowana metoda 'get', a nie własna funkcja, chociaż u mnie i tak jest 'choose' jako własna
    'year' : request.json.get('year', ""),
    'mark' : request.json.get('mark', "")
  }
  compacts.make(compact)
  return jsonify({'compact' : compact}), 201

@app.errorhandler(400)
def bad_request(error):
  return make_response(jsonify({'error': 'Bad request', 'status_code': 400}), 400)

@app.route('/api/v1/compacts/<int:compact_id>', methods =['DELETE'])
def delete(compact_id):
  cutting = compacts.delete(compact_id)
  if not cutting:
    abort(404)
  return jsonify({'cutting': cutting})

@app.route('/api/v1/compacts/<int:compact_id>', methods = ['PUT'])
def update_compact(compact_id):
    compact = compacts.choose(compact_id)
    if not compact:
        abort(404)
    if not request.json:
        abort(400)
    data = request.json
    if any([
      'band' in data and not isinstance(data.get('band'), str),
      'album' in data and not isinstance(data.get('album'), str),
      'year' in data and not isinstance(data.get('year'), int),
      'mark' in data and not isinstance(data.get('mark'), str)
    ]):
        abort(400)
    compact = {
      'band' : data.get('band', compact['band']),
      'album': data.get('album', compact['album']),
      'year' : data.get('year', compact['year']),
      'mark' : data.get('mark', compact['mark'])
    }
    compacts.adding(compact_id, compact)
    return jsonify({'compact' : compact}) # przy update z 'PUT' z 'curl' w terminalu należy brać dane w pojedynczy cudzysłów ', a wewnątrz opisywanego słownika stosować podwójne cudzysłowy ""

if __name__ == '__main__':
  app.run(debug=True)      