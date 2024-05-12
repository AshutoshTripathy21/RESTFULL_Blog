# RESTFULL_Blog

This is a simple RESTful API for a blogging platform built using Python FastAPI and MongoDB.

## Setup and Running Locally

### Prerequisites

- Python 3.x
- MongoDB
- FastAPI
- uvicorn

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/AshutoshTripathy21/RESTFULL_Blog.git

2. Navigate to the project directory:

   cd RESTFULL_Blog

4. Install dependencies

   pip install fastapi uvicorn pymongo python-dotenv pydantic

5. Configuration

   Ensure that MongoDB is running on your system. You can adjust the MongoDB connection settings in database.py if needed.

6. Start the FastAPI server:

   uvicorn main:app --reload

7. The API will be available at http://127.0.0.1:8000/docs

8. API Usage
   Endpoints
     Create User: POST /users/
     Get Users: GET /users/
     Create Post: POST /posts/
     Get Posts: GET /posts/
     Get Single Post: GET /posts/{post_id}
     Add Comment to Post: POST /posts/{post_id}/comments/
     Like Post: PUT /posts/{post_id}/like/
     Dislike Post: PUT /posts/{post_id}/dislike/
     Delete Post: DELETE /posts/{post_id}/

9. Data Models
    User
      username (string): Username of the user.
      email (string): Email address of the user.
    Comment
      text (string): Text content of the comment.
      user (User): User who posted the comment.
    Post
      title (string): Title of the post.
      content (string): Content of the post.
      author (User): Author of the post.
      comments (List[Comment]): List of comments on the post.
      likes (int): Number of likes on the post.
      dislikes (int): Number of dislikes on the post.

   
