from flask import Flask,jsonify,request
from flask_mysqldb import MySQL


app=Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='!@Kiop0987654321'
app.config['MYSQL_DB']='flask'
app.config['MYSQL_CURSORCLASS']= 'DictCursor'

mysql=MySQL(app)

 
@app.route('/',methods=['GET'])
def get_all():
	cur=mysql.connection.cursor()
	cur.execute('''SELECT * FROM flask ''')
	result=cur.fetchall()
	return jsonify({'result':result})


@app.route('/task/<int:id>',methods=['GET'])
def get_one(id):
	cur=mysql.connection.cursor()
	cur.execute('''SELECT title,description,done FROM flask WHERE id = id''')
	result=cur.fetchone()
	return jsonify({'result':result})

@app.route('/add',methods=['POST'])
def post_one():
	cur=mysql.connection.cursor()
	id=request.json['id']
	title=request.json['title']
	description=request.json['description']
	done=request.json['done'] 
	cur.execute('''INSERT INTO flask (id,title,description,done) VALUES (%s,%s,%s,%s)''',(id,title,description,done))
	cur.execute('''SELECT * FROM flask''')
	result=cur.fetchall()
	mysql.connection.commit()
	return jsonify({'result':result})

@app.route('/task/<int:id>',methods=['DELETE'])
def delete(id):
	cur=mysql.connection.cursor()
	cur.execute('''DELETE FROM flask WHERE id=id''')
	cur.execute('''SELECT * FROM flask''')
	result=cur.fetchall()
	mysql.connection.commit()
	return jsonify({'result':result})

@app.route('/task/<int:id>',methods=['PUT'])
def update(id):
	cur=mysql.connection.cursor()
	title=request.json['title']
	description=request.json['description']
	done=request.json['done'] 
	cur.execute('''UPDATE flask SET (title,description,done) WHERE id=id''',(title,description,done))
	cur.execute('''SELECT * FROM flask''')
	result=cur.fetchall()
	mysql.connection.commit()
	return jsonify({'result':result})






if __name__=='__main__':
	app.run(debug=True)