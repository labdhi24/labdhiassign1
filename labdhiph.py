import boto3

def upload_csv_from_s3(bucket_name,s3_key,file_name):
	s3=boto3.client('s3')
	try:
		s3.download_file(bucket_name,s3_key,file_name)
		print("File download successfully to S3")
	except Exception as e:
		print(f"An error occurred: {str(e)}")

bucket_name='fintech704324'
file_name='Account32.xlsx'
s3_key='Account1.xlsx'

upload_csv_from_s3(bucket_name,s3_key,file_name)