from flask import Flask, jsonify, make_response, request
from db import get_db

app = Flask(__name__)
app.config['JSON_SORT_KEYS']= False

@app.get("/tarefa")
def recuperaTarefas():
  db = get_db()
  cursor = db.cursor()

  sql = 'SELECT * FROM task'

  cursor.execute(sql)
  res = cursor.fetchall()

  tarefas = list()

  for task in res:
    tarefas.append(
      {
        'id': task[0],
        'descricao': task[1],
        'data': task[2]
      }
    )
  
  db.close()
  return make_response(jsonify(tarefas), 200)

@app.post("/tarefa")
def criarTarefa():
  tarefa = request.json

  db = get_db()
  cursor = db.cursor()

  sql = f"INSERT INTO task (descricao, data) VALUES ('{tarefa['descricao']}', '{tarefa['data']}')"

  cursor.execute(sql)
  db.commit()

  return make_response(jsonify(tarefa), 201)

@app.delete("/tarefa/<id>")
def deleteTarefa(id):
  db = get_db()
  cursor = db.cursor()

  sql = f"DELETE FROM task WHERE id = {id}"

  cursor.execute(sql)
  db.commit()

  return make_response('', 200)

app.run(host='localhost', port=5001, debug=True)