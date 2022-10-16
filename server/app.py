from flask import Flask, request, make_response, render_template, redirect, jsonify
import json
from cohere_utils import *
from db_utils import *
from gc_function import *
from generic_functions import *


app = Flask(__name__, template_folder='templates')

@app.route('/interview/create', methods=['POST'])
def create_interview():

	db = db_utils()

	criteria = request.json['criteria']
	
	if (criteria['interview-questions']):
		questions = criteria['interview-questions']
	else:
		questions = generate_questions(criteria)

	res = db.insert(criteria, questions)
	print("Insert Successful")
	
	resp = make_response("successfully added interview", 200, {'Content-Type': 'application/json', 'Set-Cookie': 'interview_id='+str(res)+';HttpOnly;Secure'})
	return resp

@app.route('/interview/get', methods=['GET'])
def get_interview():
	db = db_utils()

	interview_id = request.cookies.get('interview_id')
	print(interview_id)
	res = db.query('SELECT * FROM interviews WHERE id = '+str(interview_id))
	print(res)
	resp = make_response(res, 200, {'Content-Type': 'application/json'})
	return resp
"""
# Trying to build audio file acceptance
@app.route("/", methods=["GET", "POST"])
def index():
	if request.method == "POST":
		print("FORM DATA RECEIVED")

		if "file" not in request.files:
			return redirect(request.url)

		file = request.files["file"]
		if file.filename == "":
			return redirect(request.url)

		if file:
			save_path = os.path.join('./server', "temp.mp3")
			request.files["file"].save(save_path)

		# now we have an uploaded folder as temp.mp3
		bucket_name='splinter-demo-bucket7'
		create_bucket(bucket_name)
		create_new_folder(bucket_name, 'data/')
		upload_to_cloud(bucket_name, './server/temp.mp3', 'data/mp3')
		transcription = transcript_audio(bucket_name, 'data/mp3')
		common_words = mostCommonWords(transcription, 3)
		print(common_words)


	
	return render_template('index.html')
	"""

# For now, pretend like we already have an ID
@app.route("/interview/process/id", methods=["GET", "POST"])
def process():
	id = request.cookies.get('interview_id')
	bucket_name = '' ##### CHANGE THIS LATER
	
	db = db_utils()
	res = db.query('SELECT criteria FROM interviews WHERE id = {id}')
	criteria = json.loads(res[0])
	print(f'criteria:\n{criteria}\n')

	res = db.query('SELECT questions FROM interviews WHERE id = {id}')
	questions = res[0]
	print(f'Questions:\n{questions}\n')
	#print(res)
	
	# Also creates transcript.txt in root direcrtory
	answers = []
	for i in range(1, len(questions)+1):
		path_mp3 = 'data/'+id+'/'+i+'/mp3'
		answers.append(transcript_audio(bucket_name, path_mp3))
	
	# Analyze transcription for alternate responses and put into JSON_data
	json_data = {'processed-questions':[]}
	for q in range(len(questions)):
		question_set = {'question':questions[q]}
		question_set['response'] = answers[q]
		question_set['alternatives'] = []
		for a in range(NUMBER_OF_ALTERNATIVES):
			question_set['alternatives'].append(generate_alternative(criteria, answers[q], questions[q]))
		json_data['processed-questions'].append(question_set)
	
	db.update(id, criteria, questions, {}, json_data)
	return json_data


if __name__ == '__main__':
	app.run(host='localhost', port=5003, debug=True)


