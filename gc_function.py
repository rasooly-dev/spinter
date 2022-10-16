import os
from google.cloud import speech
from google.cloud import storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'cred_key.json'

# Clients
speech_client = speech.SpeechClient()
storage_client = storage.Client()

# Google Speech to Text Demo
# Speech demo file comes from cloud storage

def transcript_audio(file_uri):
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
# - bucket_name: string, name of bucket (where to upload to)
# - source_file_path: string, file path (for file about be uploaded)
# - destination_blob_name is a string you want to name the blob (name inside bucket)
def upload_to_cloud(bucket_name, source_file_path, destination_blob_name):
	bucket = storage_client.bucket(bucket_name)
	blob = bucket.blob(destination_blob_name)
	blob.upload_from_filename(source_file_path)
	print(
		f"File {source_file_path} uploaded to {destination_blob_name}\n"
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

# This file is already in my GC Bucket
# test_file_uri = 'gs://gc_api_speech/intro.mp3'
# transcript_audio(test_file_uri)
bucket_name = "demo_bucket_real_good_stuff"
file_to_upload = './demo_bucket_file.mp3'
cloud_blob_name = 'demo_intro'
source_blob = './blob_downloads/download_test.mp3'
create_bucket(bucket_name)
upload_to_cloud(bucket_name, file_to_upload, cloud_blob_name)
download_from_cloud(bucket_name, source_blob, cloud_blob_name)
