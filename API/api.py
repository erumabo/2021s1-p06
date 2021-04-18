import mysql.connector
from mysql.connector import errorcode
from bottle import run, get, post, put, delete, request, abort
"""
  post ---> Create
  get ----> Read
  put ----> Update
  delete -> Delete
"""

# NOTA: los credenciales estan expuestos por rapidez de desarrollo
config = {
  'user':'mabo',
  'password':'obam',
  'host':'127.0.0.1',
  'database':'p06'
}

# Una unica funcion que maneja la db
def db(query, params=None, commit=False):
  
  try:
    conn = mysql.connector.connect(**config);
  except mysql.connector.Error as err:
    print(err);
    raise err;
  
  cursor = conn.cursor();
  rows = [];

  try:
    cursor.execute(query, params=params, multi=False);
  except mysql.connector.Error as err:
    if(err.errno == errorcode.ER_BAD_NULL_ERROR):
      rows = abort(400,err.msg);
    elif(err.errno == errorcode.ER_DUP_ENTRY):
      rows = abort(409,err.msg);
    else:
      print(err);
      raise err;
  else:
    columns = cursor.column_names;
    rows = [dict(zip(columns,row)) for row in cursor];
    if commit: conn.commit();
  finally:
    # Exito o no, debemos cerrar la coneccion
    cursor.close();
    conn.close();
  
  # Retornar lo que sea que se obtuvo
  return rows;


@get('/')
@get('/items')
def get_all():
  return { 'items': db("SELECT id, nombre, valor, disponible FROM items") };

@get('/item/<item>')
def get_item(item:int):
  rows = db("SELECT id, nombre, valor, disponible FROM items WHERE id = %s",(item,))
  if(len(rows)>0): return rows[0];
  else: return abort(404,'Item no existe');


@post('/items')
def post_item():
  query = (
    " INSERT INTO items"
    " (nombre, valor, disponible)"
    " VALUES ( %(nombre)s, %(valor)s, %(disponible)s )"
  );
  params = {
    'nombre'    :request.forms.get('nombre',    type=str ),
    'valor'     :request.forms.get('valor',     type=int ),
    'disponible':request.forms.get('disponible',type=bool) or False
  };
  return db(query,params,commit=True);

@put('/item/<item>')
def put_item(item:int):
  query = (
    " UPDATE items"
    " SET nombre = %(nombre)s, valor = %(valor)s, disponible = %(disponible)s"
    " WHERE id = %(id)s"
  );
  params = {
    'id'        :item,
    'nombre'    :request.forms.get('nombre',    type=str ),
    'valor'     :request.forms.get('valor',     type=int ),
    'disponible':request.forms.get('disponible',type=bool) or False
  };
  print(params);
  return db(query,params,commit=True);

@delete('/item/<item>')
def delete_item(item:int):
  query = (
    " DELETE FROM items"
    " WHERE id = %s"
  )
  return db(query,(item,),commit=True);

run(host='localhost', port=8080, debug=True, reloader=True)
