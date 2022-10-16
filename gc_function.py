import os
from google.cloud import speech
from google.cloud import storage
from google.cloud import videointelligence

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'cred_key.json'

# Clients
speech_client = speech.SpeechClient()
storage_client = storage.Client()
video_client = videointelligence.VideoIntelligenceServiceClient()

def transcript_audio(bucket_name, path_to_file):
	file_uri = "gs://" + bucket_name + '/' + path_to_file
	audio_file = speech.RecognitionAudio(uri=file_uri)
	config = speech.RecognitionConfig(
		sample_rate_hertz = 48000,
		enable_automatic_punctuation = True,
		language_code = 'en-US',
		use_enhanced = True
	)
	response = speech_client.recognize(config=config, audio=audio_file)

	for result in response.results:
		print("Transcript: {}".format(result.alternatives[0].transcript))	

# parameters
# - bucket_name is a string the user wants to name bucket 
# (must be unique! no other cloud users can have this name)
def create_bucket(bucket_name):
	cloud_bucket_name = bucket_name
	cloud_bucket_name = bucket_name
	bucket = storage_client.bucket(cloud_bucket_name)
	bucket.storage_class = "COLDLINE"
	new_bucket = storage_client.create_bucket(bucket, location="us")
	print(
		"\nCreated bucket {} in {} with storage class {}\n".format(
			new_bucket.name, new_bucket.location, new_bucket.storage_class
		)
	)

# parameters
# - bucket_name: string, bucket "directory" destination to put folder
# - destination_folder: string, name of folder to be inserted
def create_new_folder(bucket_name, destination_folder):
	bucket = storage_client.get_bucket(bucket_name)
	blob = bucket.blob(destination_folder)
	blob.upload_from_string('')
	print('Created folder {} .\n'.format(destination_folder))


# parameters
# - bucket_name: string, name of bucket (where to upload to)
# - local_file_path: string, file path (for file about be uploaded)
# - path_to_destination_blob: string you want to for path to blob. eg. id/blob or just blob
def upload_to_cloud(bucket_name, local_file_path, path_to_destination_blob):
	bucket = storage_client.bucket(bucket_name)
	blob = bucket.blob(path_to_destination_blob)
	blob.upload_from_filename(local_file_path)
	print(
		f"File {local_file_path} uploaded to {path_to_destination_blob}\n"
	)

# parameters
# - source_bucket_name: string, name of destination bucket
# - source_blob_name: string, name of destination blob (inside the bucket)
# - destination_file_name: string, path to download file as (include extension)
def download_from_cloud(source_bucket_name, destination_file_name, source_blob_name):
	bucket = storage_client.bucket(source_bucket_name)
	blob = bucket.blob(source_blob_name)
	blob.download_to_filename(destination_file_name)

	print(
		"Downloaded storage object {} from bucket {} as local file {}.\n".format(
			source_blob_name, source_bucket_name, destination_file_name
		)
	)

# def detect_faces returns something like this 
"""
Face detected:
Segment: 0.0s to 18.1s
Bounding box:
        left  : 0.23399999737739563
        top   : 0.0957999974489212
        right : 0.8817999958992004
        bottom: 0.5194000005722046
Attributes:
        glasses: 0.02645360678434372
        headwear: 0.002668177941814065
        eyes_visible: 0.9963971376419067
        mouth_open: 0.005508669186383486
        looking_at_camera: 0.9245946407318115
        smiling: 0.00484338728711009


"""
def detect_faces(bucket_name, path_to_file):
	gcs_uri = "gs://" + bucket_name + '/' + path_to_file
	
	client = video_client

	# Configure the request
	config = videointelligence.FaceDetectionConfig(
		include_bounding_boxes=True, include_attributes=True
	)
	context = videointelligence.VideoContext(face_detection_config=config)

	# Start the asynchronous request
	operation = client.annotate_video(
		request={
			"features": [videointelligence.Feature.FACE_DETECTION],
			"input_uri": gcs_uri,
			"video_context": context,
		}
	)

	print("\nProcessing video for face detection annotations.")
	result = operation.result(timeout=300)

	print("\nFinished processing.\n")

	# Retrieve the first result, because a single video was processed.
	annotation_result = result.annotation_results[0]

	for annotation in annotation_result.face_detection_annotations:
		print("Face detected:")
		for track in annotation.tracks:
			print(
				"Segment: {}s to {}s".format(
					track.segment.start_time_offset.seconds
					+ track.segment.start_time_offset.microseconds / 1e6,
					track.segment.end_time_offset.seconds
					+ track.segment.end_time_offset.microseconds / 1e6,
				)
			)

			# Each segment includes timestamped faces that include
			# characteristics of the face detected.
			# Grab the first timestamped face
			timestamped_object = track.timestamped_objects[0]
			box = timestamped_object.normalized_bounding_box
			print("Bounding box:")
			print("\tleft  : {}".format(box.left))
			print("\ttop   : {}".format(box.top))
			print("\tright : {}".format(box.right))
			print("\tbottom: {}".format(box.bottom))

			# Attributes include glasses, headwear, smiling, direction of gaze
			print("Attributes:")
			attributes = {}
			for attribute in timestamped_object.attributes:
				print(
					"\t{}:{} {}".format(
						attribute.name, attribute.value, attribute.confidence
					)
				)
				attributes[attribute.name] = attribute.confidence
			print()
			return attributes
				
# Testing
bucket_name = "main_data_bucket_demo"
file_to_upload = './demo_bucket_file.mp4'
cloud_blob_name = 'demo_intro'
source_blob = './blob_downloads/download_test.mp3'

create_bucket(bucket_name)
create_new_folder(bucket_name, 'data/id/')
#upload_to_cloud(bucket_name, file_to_upload, 'data/id/'+cloud_blob_name)
#transcript_audio(bucket_name, 'data/id/'+cloud_blob_name)
#download_from_cloud(bucket_name, source_blob, cloud_blob_name)

mp4_ci_test = './mp4_ci_test.mp4'
upload_to_cloud(bucket_name, mp4_ci_test, 'data/mp4_ci_test')
attributes_analysis = detect_faces(bucket_name, 'data/mp4_ci_test')

print(attributes_analysis)
