# Video Uploader API

The Video Uploader API is a FastAPI-based application that allows you to upload videos to an Amazon S3 bucket and retrieve the URL of the stored video. This API is designed to simplify the process of uploading and managing video files.

## Getting Started

These instructions will guide you on how to set up and run the Video Uploader API on your local machine.

### Prerequisites

Before you begin, ensure you have the following prerequisites installed:

- Python (3.6+)
- FastAPI
- Boto3 (for interacting with AWS S3)
- An AWS S3 account and bucket
- AWS credentials configured on your machine

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/franciedigital/chrome-extension-video-plugin.git

   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

### Configuration

Before running the API, make sure to configure your AWS credentials and specify your S3 bucket name in the `.env` file:

```
# AWS S3 credentials and bucket name
AWS_ACCESS_KEY = 'your_access_key'
AWS_SECRET_KEY = 'your_secret_key'
S3_BUCKET_NAME = 'your_bucket_name'
```

### Usage

Start the FastAPI application:

```
uvicorn main:app  --reload
```

Access the API at http://localhost:8000 using your preferred API client (e.g., Postman or cURL).

Uploading a Video
Endpoint: POST /api/upload-video/
Request: Send a POST request with the video file as the request body.
Response: The API will store the video in the specified S3 bucket and return the URL where the video is stored.

Example cURL request:

```
curl -X POST -F "file=@path/to/video.mp4" http://localhost:8000/api/upload-video/

```
