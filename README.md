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

# Wistia API Endpoints Documentation

## Endpoints

### 1. Add Video

- **Endpoint:** `/wistia/`
- **Request Type:** POST
- **Request Body:**
  ```json
  {
    "video_name": "string"
  }
  ```
- **Response:**
  ```json
  {
    "message": "Video uploaded successfully",
    "status": 201,
    "data": {
      "video_name": "string",
      "wistia_video_id": "string"
    },
    "errors": null
  }
  ```
- **Description:** Uploads a video to Wistia with the provided name.

### 2. Get Video Data

- **Endpoint:** `/wistia/<video_id>`
- **URL Parameters:**
  - `video_id` (string): The ID of the video to retrieve.
- **Request Type:** GET
- **Response:**
  ```json
  {
    "message": "Video data retrieved successfully",
    "status": 200,
    "data": {
      // Wistia video data
    },
    "errors": null
  }
  ```
- **Description:** Retrieves the data of a video from Wistia using the provided video ID.

### 3. Update Video Data

- **Endpoint:** `/wistia/<video_id>`
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
- **Description:** Updates the data of a video on Wistia with the provided name and/or description.

### 4. Delete Video

- **Endpoint:** `/wistia/<video_id>`
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
- **Description:** Deletes a video from Wistia using the provided video ID.

# Survey Monkey API Endpoints Documentation

## Endpoints

### 1. Get OAuth URL

- **Endpoint:** `/survey_monkey/oauth_url`
- **Request Type:** GET
- **Response:**
  ```json
  {
    "message": "OAuth URL generated successfully",
    "status": 201,
    "data": {
      "uri": "string"
    },
    "errors": null
  }
  ```
- **Description:** Generates the OAuth URL for Survey Monkey authentication.

### 2. Exchange Code for Token

- **Endpoint:** `/survey_monkey/get_token`
- **Request Type:** POST
- **Request Body:**
  ```json
  {
    "code": "string"
  }
  ```
- **Response:**
  ```json
  {
    "message": "Token retrieved successfully",
    "status": 201,
    "data": {
      // Token data
    },
    "errors": null
  }
  ```
- **Description:** Exchanges the authorization code for an access token.

### 3. Get Survey List

- **Endpoint:** `/survey_monkey/get_survey_list`
- **Request Type:** GET
- **Response:**
  ```json
  {
    "message": "Survey list retrieved successfully",
    "status": 200,
    "data": {
      // Survey list data
    },
    "errors": null
  }
  ```
- **Description:** Retrieves the list of surveys.

### 4. Create Survey

- **Endpoint:** `/survey_monkey/create_survey`
- **Request Type:** POST
- **Request Body:**
  ```json
  {
    "title": "string"
  }
  ```
- **Response:**
  ```json
  {
    "message": "Survey created successfully",
    "status": 201,
    "data": {
      // Created survey data
    },
    "errors": null
  }
  ```
- **Description:** Creates a new survey.

### 5. Update Survey

- **Endpoint:** `/survey_monkey/update_survey/<survey_id>`
- **URL Parameters:**
  - `survey_id` (string): The ID of the survey to update.
- **Request Type:** PUT
- **Request Body:**
  ```json
  {
    "title": "string"
  }
  ```
- **Response:**
  ```json
  {
    "message": "Survey updated successfully",
    "status": 200,
    "data": {
      // Updated survey data
    },
    "errors": null
  }
  ```
- **Description:** Updates an existing survey.

### 6. Get Survey Details

- **Endpoint:** `/survey_monkey/survey_detail/<survey_id>`
- **URL Parameters:**
  - `survey_id` (string): The ID of the survey to retrieve.
- **Request Type:** GET
- **Response:**
  ```json
  {
    "message": "Survey details retrieved successfully",
    "status": 200,
    "data": {
      // Survey details data
    },
    "errors": null
  }
  ```
- **Description:** Retrieves the details of a specific survey.

### 7. Delete Survey

- **Endpoint:** `/survey_monkey/delete_survey/<survey_id>`
- **URL Parameters:**
  - `survey_id` (string): The ID of the survey to delete.
- **Request Type:** DELETE
- **Response:**
  ```json
  {
    "message": "Survey deleted successfully",
    "status": 200,
    "data": null,
    "errors": null
  }
  ```
- **Description:** Deletes a specific survey.

### 8. Create Page

- **Endpoint:** `/survey_monkey/create_page/<survey_id>`
- **URL Parameters:**
  - `survey_id` (string): The ID of the survey to add a page to.
- **Request Type:** POST
- **Request Body:**
  ```json
  {
    "title": "string",
    "description": "string", // optional
    "position": "integer" // optional
  }
  ```
- **Response:**
  ```json
  {
    "message": "Page created successfully",
    "status": 201,
    "data": {
      // Created page data
    },
    "errors": null
  }
  ```
- **Description:** Creates a new page in a survey.

### 9. Get Page List

- **Endpoint:** `/survey_monkey/get_page_list/<survey_id>`
- **URL Parameters:**
  - `survey_id` (string): The ID of the survey to retrieve pages from.
- **Request Type:** GET
- **Response:**
  ```json
  {
    "message": "Pages retrieved successfully",
    "status": 200,
    "data": {
      // Page list data
    },
    "errors": null
  }
  ```
- **Description:** Retrieves the list of pages in a survey.

### 10. Get Page

- **Endpoint:** `/survey_monkey/get_page/<survey_id>/<page_id>`
- **URL Parameters:**
  - `survey_id` (string): The ID of the survey.
  - `page_id` (string): The ID of the page to retrieve.
- **Request Type:** GET
- **Response:**
  ```json
  {
    "message": "Page retrieved successfully",
    "status": 200,
    "data": {
      // Page data
    },
    "errors": null
  }
  ```
- **Description:** Retrieves a specific page in a survey.

### 11. Update Page

- **Endpoint:** `/survey_monkey/update_page/<survey_id>/<page_id>`
- **URL Parameters:**
  - `survey_id` (string): The ID of the survey.
  - `page_id` (string): The ID of the page to update.
- **Request Type:** PUT
- **Request Body:**
  ```json
  {
    "title": "string",
    "description": "string", // optional
    "position": "integer" // optional
  }
  ```
- **Response:**
  ```json
  {
    "message": "Page updated successfully",
    "status": 200,
    "data": {
      // Updated page data
    },
    "errors": null
  }
  ```
- **Description:** Updates an existing page in a survey.

### 12. Delete Page

- **Endpoint:** `/survey_monkey/delete_page/<survey_id>/<page_id>`
- **URL Parameters:**
  - `survey_id` (string): The ID of the survey.
  - `page_id` (string): The ID of the page to delete.
- **Request Type:** DELETE
- **Response:**
  ```json
  {
    "message": "Page deleted successfully",
    "status": 200,
    "data": null,
    "errors": null
  }
  ```
- **Description:** Deletes a specific page in a survey.

### 13. Create Question

- **Endpoint:** `/survey_monkey/create_question/<survey_id>/<page_id>`
- **URL Parameters:**
  - `survey_id` (string): The ID of the survey.
  - `page_id` (string): The ID of the page to add a question to.
- **Request Type:** POST
- **Request Body:**
  ```json
  {
    "heading": "string",
    "choices": ["string"], // required if not open-ended
    "family": "string" // single_choice, multiple_choice, open_ended
  }
  ```
- **Response:**
  ```json
  {
    "message": "Question created successfully",
    "status": 201,
    "data": {
      // Created question data
    },
    "errors": null
  }
  ```
- **Description:** Creates a new question in a page.

### 14. Get Question List

- **Endpoint:** `/survey_monkey/get_question_list/<survey_id>/<page_id>`
- **URL Parameters:**
  - `survey_id` (string): The ID of the survey.
  - `page_id` (string): The ID of the page to retrieve questions from.
- **Request Type:** GET
- **Response:**
  ```json
  {
    "message": "Questions retrieved successfully",
    "status": 200,
    "data": {
      // Question list data
    },
    "errors": null
  }
  ```
- **Description:** Retrieves the list of questions in a page.

### 15. Get Question

- **Endpoint:** `/survey_monkey/get_question/<survey_id>/<page_id>/<question_id>`
- **URL Parameters:**
  - `survey_id` (string): The ID of the survey.
  - `page_id` (string): The ID of the page.
  - `question_id` (string): The ID of the question to retrieve.
- **Request Type:** GET
- **Response:**
  ```json
  {
    "message": "Question retrieved successfully",
    "status": 200,
    "data": {
      // Question data
    },
    "errors": null
  }
  ```
- **Description:** Retrieves a specific question in a page.

### 16. Update Question

- **Endpoint:** `/survey_monkey/update_question/<survey_id>/<page_id>/<question_id>`
- **URL Parameters:**
  - `survey_id` (string): The ID of the survey.
  - `page_id` (string): The ID of the page.
  - `question_id` (string): The ID of the question to update.
- **Request Type:** PUT
- **Request Body:**
  ```json
  {
    "heading": "string",
    "choices": ["string"], // required if not open-ended
    "family": "string" // single_choice, multiple_choice, open_ended
  }
  ```
- **Response:**
  ```json
  {
    "message": "Question updated successfully",
    "status": 200,
    "data": {
      // Updated question data
    },
    "errors": null
  }
  ```
- **Description:** Updates an existing question in a page.

### 17. Delete Question

- **Endpoint:** `/survey_monkey/delete_question/<survey_id>/<page_id>/<question_id>`
- **URL Parameters:**
  - `survey_id` (string): The ID of the survey.
  - `page_id` (string): The ID of the page.
  - `question_id` (string): The ID of the question to delete.
- **Request Type:** DELETE
- **Response:**
  ```json
  {
    "message": "Question deleted successfully",
    "status": 200,
    "data": null,
    "errors": null
  }
  ```
- **Description:** Deletes a specific question in a page.
