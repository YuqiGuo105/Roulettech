# Roulettech App

#### URL: http://roulettech-frontend-app.s3-website-us-west-2.amazonaws.com
#### Backend URL: http://ec2-35-93-146-72.us-west-2.compute.amazonaws.com:8001
#### Demo: https://youtu.be/DHcVVtwSVZM

## Tech Stack and Architecture Overview
Include an overview of the technologies used in this project:

- Frontend: React, Axios, ReactQuill (WYSIWYG)
- Backend: Django, Django REST Framework
- Authentication: AWS Cognito
- Storage: AWS S3
- API Integration: OpenAI

## Usage

### Login/Register via Cognito

1. Navigate to the login/register page.
2. Fill in the required fields and submit the form to register a new account or log in with an existing account.
3. On successful login, you will be redirected to the recipe management page.

### Recipe Post and View

#### Posting a Recipe

1. Enter the recipe name.
2. Select an image file.
3. Enter the recipe content using the rich text editor.
4. Click the "Submit" button.
5. Upon successful submission, the recipe data is sent to the backend, and the new recipe is created.

#### Viewing Recipes

1. Navigate to the recipes list page.
2. Browse through the list of recipes.
3. Click on a recipe to view its details.

### Generate Recipe with Voice Input

1. Navigate to the recipe generation page.
2. Click the "Start Voice Input" button and speak your recipe instructions.
3. The voice input will be converted to text and sent to the OpenAI API.
4. Review the generated recipe and make any necessary edits.
5. Click the "Submit" button to save the generated recipe.

### Example Workflow

1. **Login/Register**: Register a new account or log in with an existing account.
2. **Post a Recipe**: Create a new recipe by filling in the details and submitting the form.
3. **View Recipes**: Browse and view the list of existing recipes.
4. **Generate Recipe**: Use voice input to generate a new recipe with the help of OpenAI API.
