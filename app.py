
from flask_pymongo import PyMongo
from flask import Flask,request,jsonify

app=Flask(__name__)

app.config['MONGO_URI']='mongodb+srv://abc:abcd@flask-app-ckagf.mongodb.net/todo?retryWrites=true&w=majority'

mongo=PyMongo(app)

@app.route('/',methods=['POST'])
def post_one():
	tasks=mongo.db.task
	_id=request.json['_id']
	title=request.json['title']
	description=request.json['description']
	done=request.json['done']
	
	tasks.insert_one({
		'_id':_id,'title':title,'description':description,'done':done
	})

	return jsonify({'_id':_id,'title':title,'description':description,'done':done})


@app.route('/',methods=['GET'])
def get_all():
	tasks=mongo.db.task

	output=[]

	for task in tasks.find():
		output.append({'_id':task['_id'],'title':task['title'],'description':task['description'],'done':task['done']})
	return jsonify({'results':output})


@app.route('/task/<int:_id>',methods=['GET'])
def get_one(_id):
	tasks=mongo.db.task

	task=tasks.find_one({'_id':_id})
	
	if task:
		output={'_id':task['_id'],'title':task['title'],'description':task['description'],'done':task['done']}
	else:
		output='Not found'

	return jsonify({'output':output})


@app.route('/task/<int:_id>',methods=['PUT'])
def update(_id):
	tasks=mongo.db.task

	for task in tasks.find():
		if task['_id']==_id:
			task['title']=request.json['title']
			task['description']=request.json['description']
			task['done']=request.json['done']
			output={'_id':task['_id'],'title':task['title'],'description':task['description'],'done':task['done']}
			tasks.save(output)
		else:
			output='not found'
	return jsonify({'tasks':output})


@app.route('/task/<int:_id>',methods=['DELETE'])
def delete(_id):
	tasks=mongo.db.task
	for task in tasks.find():
		if task['_id']==_id:
			tasks.remove(task['_id'])
			output={'_id':task['_id'],'title':task['title'],'description':task['description'],'done':task['done']}
		else:
			output='Not Found'
	return jsonify({'output':output}) 






if __name__=='__main__':
	app.run(debug=True)