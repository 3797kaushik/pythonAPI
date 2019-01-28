from bottle import run, get, post, request, delete
import pymongo
import json
from flask import Flask, jsonify

app = Flask(__name__)

animals = [{'name' : 'Ellie', 'type' : 'Elephant'},
			{'name' : 'Python', 'type' : 'Snake'},
			{'name' : 'Zed', 'type' : 'Zebra'}]

@app.route('/', methods=['GET'])
def getSignin1():
	
	return "success"
@app.route('/api/signin_api/firstname=<firstname>&lastname=<lastname>&phone_num=<phone_num>&address=<address>&username=<username>&password=<password>', methods=['GET'])
def getSignin(firstname,lastname,phone_num,address,username,password):
	myclient = pymongo.MongoClient("mongodb://localhost:27017/")
	print("inside sign in function")
	mydb = myclient["Merck_Hack"]
	mycol = mydb["login_Collection"]
	
	mydict = { "firstname": firstname, "lastname": lastname,"phone_num":phone_num, "address":address,"username":username,"password":password}
	try:
		x= mycol.insert_one(mydict)
	except:
		return "failure"
	print(mydict)
	print(x.inserted_id)
	return "success"
	
@app.route('/api/login_api/username=<username>&password=<password>', methods=['GET'])
def getLogin(username,password):
	myclient = pymongo.MongoClient("mongodb://localhost:27017/")
	print("inside sign in function")
	mydb = myclient["Merck_Hack"]
	mycol = mydb["login_Collection"]
	print("inside log in function")
	try :
		result = mydb.login_Collection.find_one({"username": username,'password':password})
		# will add pasword once  username is fine
	except:	
		return  jsonify("Username doesn't exist")
	# Access the status key.
	if result == None :
		return jsonify("Username doesn't exist")
	print(result.get('_id'))
	return jsonify(",".join([result.get('username'),str(result.get('_id'))]))

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})	
	
if __name__ == '__main__':
    app.run(host= '10.13.5.242', port=1234, debug=True)
	# host no continously changes
	
	