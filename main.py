from fastapi import FastAPI, UploadFile
import boto3
from botocore.exceptions import NoCredentialsError
from decouple import config

app = FastAPI()

# Read the AWS_ACCESS_KEY from the .env file
aws_access_key = config("AWS_ACCESS_KEY")
aws_secret_key = config("AWS_SECRET_KEY")
s3_bucket = config("S3_BUCKET_NAME")

# Initialize an S3 client
s3 = boto3.client('s3', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)

@app.get("/")
def index():
    return {"message": "status ok"}

@app.post("/upload-video/")
async def upload_video(file: UploadFile):
    try:
        # Generate a unique S3 key for the video
        s3_key = f"videos/{file.filename}"

        # Upload the video to S3
        s3.upload_fileobj(file.file, s3_bucket, s3_key)

        # Generate the S3 URL for the uploaded video
        s3_url = f"https://{s3_bucket}.s3.amazonaws.com/{s3_key}"

        print(f"Video URL: {s3_url}")

        return {"message": "Video uploaded successfully", "video_url": s3_url}
    except NoCredentialsError:
        return {"error": "AWS credentials are not configured"}
    except Exception as e:
        return {"error": str(e)}
