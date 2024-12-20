# Hi Nabila

You have been given an html template.

You are required to fix:

1) Any issues with it loading correctly. 
2) Maintain good UI practises. (Hint: The dashboard shouldn't be empty on load)
3) Introduce animations where you think is appropriate. (Hint: Some apps load percentage numbers from 0)
4) (Optional) create a backend and make some components functional.
5) Update the bottom half of this README with your changes.

This assignment is intentionally ambiguos. And is meant to test your creative abilities.

You will notice this template does not contain any javascript files. This is because it uses [alpinejs](https://alpinejs.dev/) and [htmx](https://htmx.org)

You are required to maintain these two packages as much as possible. However, using regular javascript for complex tasks is allowed.



### Problems Identified:
1. The file URLs were incorrect, as each file had `web/..html` type URLs, but there is no `web` folder in the project.
2. The dashboard page was empty on load due to missing event handling on the click event.
3. The logo image was missing in the project folder, causing errors.
4. The absence of a favicon was also causing warnings.
5. Implemented functionality to handle both GET and POST requests using Flask and SQLAlchemy. This allows for the retrieval and submission of data to and from the server

### Changes Made:
**Project Overview**

This project is a Flask web application that integrates the CountUp.js library to display dynamic statistics on the dashboard.

**Changes Made**

1. **Fixed File URLs**: Corrected the paths to static files to ensure proper loading of assets.
2. **Dashboard Initialization**: Implemented event handling to ensure the dashboard loads correctly on page load.
3. **Added Logo Image**: Included the missing logo image in the project folder.
4. **Integrated CountUp.js**: Incorporated the CountUp.js library to animate numerical statistics on the dashboard.
5. **Backend Troubleshooting**: Addressed and resolved errors in the Flask backend; fixes have been committed and a pull request has been submitted.

**Setup Instructions**

To run this application locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Set Up Python Environment**:
   - Ensure Python 3.8 or higher is installed.
   - Create a virtual environment:
     ```bash
     python -m venv venv
     ```
   - Activate the virtual environment:
     - On Windows:
       ```bash
       venv\Scripts\activate
       ```
     - On macOS/Linux:
       ```bash
       source venv/bin/activate
       ```

3. **Install Python Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Node.js Environment**:
   - Ensure Node.js and npm are installed.
   - Navigate to the `static` directory:
     ```bash
     cd static
     ```
   - Initialize npm and install dependencies:
     ```bash
     npm init -y
     npm install
     ```

5. **Run the Application**:
   ```bash
   python app.py
   ```
   The application will be accessible at `http://127.0.0.1:5000/`.

**Notes**

- Ensure all environment variables and configurations are set as per the project's requirements.
- For deployment instructions or additional configurations, refer to the project's documentation or contact the project maintainer. 
---

## Dashboard look
![Dashboard](https://i.ibb.co.com/hV1TfJx/ui.png)
