# FastAPI Project Documentation

This document provides an overview of the API endpoints, request and response models, and usage examples for the FastAPI project.

## Table of Contents

- [API Endpoints](#api-endpoints)
- [Request and Response Models](#request-and-response-models)
- [Usage Examples](#usage-examples)

## API Endpoints

### Index

- **Endpoint:** `/`
- **Method:** GET
- **Summary:** Check the status of the API.
- **Response:**
  - HTTP Status Code: 200
  - Content Type: JSON
  - Response Body:
    ```json
    {}
    ```

### Upload Video

- **Endpoint:** `/api/upload-video/`
- **Method:** POST
- **Summary:** Upload a video file.
- **Request:**
  - Content Type: Multipart/form-data
  - Request Body:
    - `file` (File): The video file to upload.
- **Responses:**
  - HTTP Status Code: 200 (Success)
    - Content Type: JSON
    - Response Body:
      ```json
      {}
      ```
  - HTTP Status Code: 422 (Validation Error)
    - Content Type: JSON
    - Response Body:
      ```json
      {}
      ```

## Request and Response Models

### Body_upload_video_api_upload_video__post

- **Properties:**
  - `file` (File, binary): The video file to upload.
- **Required:** `file`

### HTTPValidationError

- **Properties:**
  - `detail` (array of ValidationError)
    - `loc` (array of string or integer): The location of the error.
    - `msg` (string): The error message.
    - `type` (string): The error type.
- **Type:** object

### ValidationError

- **Properties:**
  - `loc` (array of string or integer): The location of the error.
  - `msg` (string): The error message.
  - `type` (string): The error type.
- **Required:** `loc`, `msg`, `type`

## Usage Examples

### Check API Status

```bash
curl -X POST -F "file=@path/to/video.mp4" http://localhost:8000/api/upload-video/
