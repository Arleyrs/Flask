from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="crud_flask_python"
)
cursor = db.cursor()

@app.route('/')
def index():
    cursor.execute("SELECT * FROM registros")
    registros = cursor.fetchall()
    return render_template('index.html', registros=registros)

@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    if request.method == 'POST':
        nombre = request.form['nombre']
        telefono = request.form['telefono']
        direccion = request.form['direccion']
        cursor.execute("INSERT INTO registros (nombre, telefono, direccion) VALUES (%s, %s, %s)", (nombre, telefono, direccion))
        db.commit()
        return redirect('/')
    return render_template('agregar.html')

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        telefono = request.form['telefono']
        direccion = request.form['direccion']
        cursor.execute("UPDATE registros SET nombre = %s, telefono = %s, direccion = %s WHERE id = %s", (nombre, telefono,direccion,id))
        db.commit()
        return redirect('/')
    cursor.execute("SELECT * FROM registros WHERE id = %s", (id,))
    registro = cursor.fetchone()
    return render_template('editar.html', registro=registro)

@app.route('/eliminar/<int:id>')
def eliminar(id):
    cursor.execute("DELETE FROM registros WHERE id = %s", (id,))
    db.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
