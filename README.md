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

### Changes Made:
1. Fixed the file URLs to point to the correct paths.
2. Set the dashboard to load correctly on page load by handling the necessary event.
3. Added the missing logo image to the project folder.
4. Integrated the CountUp animation library, which will require running `npm install` to properly load the dependencies, as `node_modules` was previously git-ignored.
5. Started troubleshooting errors on the backend with Flask and working on fixing them i will give push as soon as done then pull request also.

---

## Dashboard look
![Dashboard](https://i.ibb.co.com/hV1TfJx/ui.png)
