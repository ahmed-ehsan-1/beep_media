# Vimeo API Endpoints Documentation

## Endpoints

### 1. Add Video

- **Endpoint:** `/vimeo/`
- **Request Type:** POST
- **Request Body:**
  ```json
  {
    "video_name": "string",
    "video_description": "string" // optional
  }
  ```
- **Response:**
  ```json
  {
    "message": "Video uploaded successfully",
    "status": 201,
    "data": {
      "video_name": "string",
      "video_description": "string",
      "vimeo_video_id": "string"
    },
    "errors": null
  }
  ```
- **Description:** Uploads a video to Vimeo with the provided name and description.

### 2. Get Video Data

- **Endpoint:** `/vimeo/<video_id>`
- **URL Parameters:**
  - `video_id` (string): The ID of the video to retrieve.
- **Request Type:** GET
- **Response:**
  ```json
  {
    "message": "Video data retrieved successfully",
    "status": 200,
    "data": {
      // Vimeo video data
    },
    "errors": null
  }
  ```
- **Description:** Retrieves the data of a video from Vimeo using the provided video ID.

### 3. Update Video Data

- **Endpoint:** `/vimeo/<video_id>`
- **URL Parameters:**
  - `video_id` (string): The ID of the video to update.
- **Request Type:** PUT
- **Request Body:**
  ```json
  {
    "video_name": "string", // optional
    "video_description": "string" // optional
  }
  ```
- **Response:**
  ```json
  {
    "message": "Video data updated successfully",
    "status": 200,
    "data": {
      "video_name": "string",
      "video_description": "string"
    },
    "errors": null
  }
  ```
- **Description:** Updates the data of a video on Vimeo with the provided name and/or description.

### 4. Delete Video

- **Endpoint:** `/vimeo/<video_id>`
- **URL Parameters:**
  - `video_id` (string): The ID of the video to delete.
- **Request Type:** DELETE
- **Response:**
  ```json
  {
    "message": "Video deleted successfully",
    "status": 200,
    "data": null,
    "errors": null
  }
  ```
- **Description:** Deletes a video from Vimeo using the provided video ID.
