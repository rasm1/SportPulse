# Sportpulse


Welcome to SportPulse, the ultimate Reddit-style community for fitness enthusiasts! Whether you’re a seasoned athlete, a gym newbie, or someone looking to stay active, SportPulse is your go-to hub for everything workout-related. Share your progress, ask for advice, discover routines, and connect with like-minded individuals who share your passion for fitness. From lifting tips to yoga hacks, SportPulse keeps the energy high and the motivation stronger than ever. 💪

![Home Screen](/staticfiles/readme_img/amiresponsive-sportpulse.png)

[View Sportpulse live website here](https://sportpulse-6bad7f07e667.herokuapp.com)
- - -

## Table of Contents
### User Experience
* Project Goals
* Agile Methodology
* First time user
* Registered user
### Design
* Color Scheme
* Wireframes
* Data Model
* Database Scheme
### Security Features
* User authentication
* Login Decorator
* CSRF Protection
* Custom error pages
* Custom error pages
* author verification
### Features
* Existing Features
* Features Left to Implement
### Technologies Used
* Languages Used
* Databases Used
* Frameworks Used
* Programs Used
### Deployment and Local developement
* Local Developement
* PostgreSQL Database
* Heroku Deployment
### Testing
* Responsiveness Testing
* Browser Compatibility Testing
* Device Testing
* Code Validation
* bugs
* Features Testing
### References
* Docs
* Content
* Acknowledgments

---

## User Experience (UX)

Gym enthusiast unite and find each other on the Sportpulse forum. Our website offers an intuitive and engaging way to connect with fellow hym enthusiast. Wondering how to start on your fitness journey? Looking for tips and tricks on how to perform your favorite exercises? Or are you just curious what other gym goers are talking about these days, Sportpulse offers an easy and seamless way to connect to like-minded individuals. Discover the latest trends on all things fitness here at Sportpulse.

### Project Goals

The goal of Sportpulse is to create a forum where users can easily and seamlessly communicate with like minded individuals to learn more about everything fitness related.

### Agile Methodology

Agile Methodology was used to help prioritize and organize tasks, writting the user stories and using Project Boards on Github. Template was created to help write User Stories

* User stories were created by looking at possible user needs and through iterations.
* Project Board is set to public.
* Project Board was used to track progression of the task through the Todo, In progress and Done columns
* Labels were added to sort the issues based on the importance and difficulty.

<details>
<summary> User Stories Template
</summary>

![User Stories Template](/staticfiles/readme_img/user-story-template.png)
</details>

<details>
<summary> Project Board
</summary>

![Project Board](/staticfiles/readme_img/user_story_board.png)
</details>

### User Stories

#### User Stories
1. Initial Deployment
* Create new Heroku application
* Link Github repository to the Heroku app
2. Home Page
* Create a navigation bar
* Create a footer
* create a list of posts
3. creating a post
* create posts page
* Add custom properties to the page
4. creating comments
* Add a post detail page
* Add comment submitting functionality
5. deleting posts & comments
* create a delete button for posts and comments
* attach a modal to delete buttons for confirmation
6. User Registration and authentication
* Sign Up page
* User registration, log in, log out
* Display users name
7. Website Admin 
* Alert messages
* Crud functionality
* Admin panel
8. Maintain consistent design with responsiveness in mind
* Maintain consistent design
* Test responsiveness

Detailed look can be found in the [project board](https://github.com/users/rasm1/projects/2/views/1)

### First time user

* Simple and intuitive website navigation for easy exploration and discovery.
* Informative content providing usefull and interesting information to the user.
* User-friendly forms with clear validation messages to ensure accurate input.
* Easy Registration process.

### Registered User

* Seamless login process with a secure and personalized user account.
* Ability to easily modify or cancel posts and comments


## Design

The Sportpulse forum provides a clear and concise design. The navigation bar features a slick logo with an easy to read contrast in colours. Darker tones were used in contrast with the white background to make posts pop out. Horizontal lines were used for clarity. The footer highlights the social media links for more engagement.

### Color Scheme
Main color for application was: rgb(249, 250, 252) (background color)
header color: rgb(54, 111, 199);
footer color: rgb(0, 0, 0);


### Typography

The 'Lato' font is specificied as the primary font with the standard 'sans-serif' font specified as a fallback.

### Wireframes

<details>
<summary> Home Page
</summary>

![Home Page](/staticfiles/readme_img/wireframe-home.png)
</details>

<details>
<summary> Home Page when logged in
</summary>

![Home Page when logged in](/staticfiles/readme_img/wireframe-logged-in.png)
</details>

<details>
<summary> Create post Page
</summary>

![Create post Page](/staticfiles/readme_img/wireframe-create-post.png)
</details>

<details>
<summary> Edit post Page
</summary>

![Edit post Page](/staticfiles/readme_img/wireframe-edit-post.png)
</details>


<details>
<summary> Comments Page
</summary>

![Comments Page](/staticfiles/readme_img/wireframe-comments.png)
</details>

<details>
<summary> User Login Page
</summary>

![User Login Page](/staticfiles/readme_img/wireframe-login.png)
</details>

<details>
<summary> User Sign Up Page
</summary>

![User Sign Up Page](/staticfiles/readme_img/wireframe-register.png)
</details>

### Data Models

1. AllAuth User Model
    * Django Allauth, the User model is the default user model provided by the Django authentication system
    
---
2. Comment Model
    * Model made so that users can leave a comment on all posts
    * Comments can only be edited/ deleted by the original author
    * The User entity has a one-to-many relationship with the Comments entity. This means that a User can have multiple comments. But multiple comments cannot be made multiple users.
---
3. Post model
    * Model made so users can make posts on the forum.
    * the user entity has a one-to-many relationship with the post model. This means that one user can make multiple posts but multiple posts cannot have multiple users.
    * Only Admin can change the data in the backend.
    * input provided: title, content, topic, subtopic, experience_level, goal, equipment_available, workout frequency, nutrition focus
---

### Database Scheme

Entity Relationship Diagram (ERD)

![DataScheme](/staticfiles/readme_img/erd.png)

This data scheme allows for the management of users, posts, and comments. Users can make a post and each post can have multiple comments.
## Security Features

### User Authentication

* Django Allauth is a popular authentication and authorization library for Django, which provides a set of features for managing user authentication, registration, and account management.

### Login Decorator

* used on all CRUD views for posts and comments.

### CSRF Protection

* Django provides built-in protection against Cross-Site Request Forgery (CSRF) attacks. CSRF tokens are generated for each user session, and they are required to submit forms or perform state-changing actions. When a user logs out, the session and associated CSRF token are invalidated, making it difficult for an attacker to forge a valid request using a copied URL.


### Custom error pages

* 404 Error Page, provides user with a button the redirect to home page.
* 500 Error Page, provides user with a button the redirect to home page.

### author verification
* verifies if user is the original author during the editing of a post, if not when clicking 'submit' the user is redirected to the homepage and recieve an alert message.

## Features

* Home page showcasing a paginated list of posts
* User can make an account and login
* When logged in, user has access to full CRUD functionality on their posts and comments
* Every user action is accompanied by a corresponding message to ensure that users are promptly notified of any changes or updates.

### Existing Features

1. homepage
* homepage shows list of posts pagined on the 6th post
* next and previous button to see next /previous 6 posts
* clickable post titles to redirect to comments page
2. comments page
* displays title of the page , author, content and time of posting
* displays comments (if placed)
* has an edit_post button that redirects to edit posts page (if the user is the author)
* has a delete button that deletes post from database (if the user is the author)
* has an edit button that lets user edit the comments (if the user is the author)
* clicking the edit button prepopulates the body with content 
* has a delete button that deletes the comment from the database (if the user is the author)
3. create post page
* link in header (create post) redirects to create post page
* dynamicly generates SLUG
* automaticly records the time and date of post creation
* displays an input field for title
* displays an input field for content
* displays an input field for topics
* displays an input field for subtopics depending on what topic is selected, if no topic is selected it hides
* displays an input field for goal
* displays an input field for workout_frequency
* displays an input field for available equipment if the user selects the form or training schedule topic, if not selected it hides
* displays an input field for nutrion focus if the user selects the diet topic, if not selected it hides.
* displays notification if the user has succesfully created a post or if the post was unsuccesfull 
4. edit post page
* mostly the same as create post page
* automaticly shows title in at the top
* prepopulates the content fields with previously inputted data
* displays notification if the user has edited a post succesfully or if an error occured
5. header
* contains logo linking to homepage
* contains 'home' button linking to homepage
* when logged in contains the create post button that links to create post page
* when logged in contains the logout button that links to logout page
* when logged out contains the register button that links to sign up page
* when loggout out contains the login button that links to login page
6. footer
* contains links to various social media websites
<hr>
* Sign up
    * User can create an account


* Login
    * User can login into an account, if they have created one


* Logout
    * User can logout


* Error Pages
    * There are custom 404 and 500 error pages set up.
    * They contain buttons to redirect to home page if there is an error.


### Features Left to Implement 

* Ability to like and dislike comments
* a search option so users can filter to what posts they would like to see based on topics/subtopics or other properties
* property displays based on selected properties when post is created
* implement more pages to handle custom errors related to authentication

## Technologies Used

### Languages Used

* HTML5
* CSS3
* JavaScript
* Python

### Databases Used

* PostgreSQL - Postgres database

### Frameworks Used

* Django
* Bootstrap 4.6.1

### Programs Used

* Github- Storing the code online
* Gitpod - To write the code.
* Heroku - Used as the cloud-based platform to deploy the site.
* Google Fonts - Import main font the website.
* Figma - Used to create wireframes and schemes
* Am I Responsive - To show the website image on a range of devices.
* Git - Version control
* Jinja - Templating engine
* JSHint - Used to validate JavaScript
* W3C Markup Validation Service - Used to validate HTML
* CSS Validation Service - Used to validate CSS
* CI Python Linter - Used to validate Python

## Deployment and Local Developement

Live deployment can be found on this [View Sportpulse live website here](https://sportpulse-6bad7f07e667.herokuapp.com)

### Local Developement

#### How to Fork
1. Log in(or Sign Up) to Github
2. Go to repository for this project [Sportpulse](https://github.com/rasm1/SportPulse)
3. Click the fork button in the top right corner

#### How to Clone
1. Log in(or Sign Up) to Github
2. Go to repository for this project [Sportpulse](https://github.com/rasm1/SportPulse)
3. Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
4. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
5. Type the following command in the terminal (after the git clone you will need to paste the link you copied in step 3 above)
6. Set up a virtual environment (this step is not required if you are using the Code Institute Template in GitPod as this will already be set up for you).
7. Install the packages from the requirements.txt file - run Command pip3 install -r requirements.txt

### Heroku Deployment
* Log into [Heroku](https://www.heroku.com/) account or create an account.
* Click the "New" button at the top right corner and select "Create New App".
* Enter a unique application name
* Select your region
* Click "Create App"

#### Prepare enviroment and settings.py
* In your GitPod workspace, create an env.py file in the main directory.
* Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file.
* Update the settings.py file to import the env.py file and add the SECRETKEY and DATABASE_URL file paths.
* Comment out the default database configuration.
* Save all files and make migrations.
* Add the STATIC files settings - the url, storage path, directory path, root path, media url and default file storage path.
* Link the file to the templates directory in Heroku.
* Change the templates directory to TEMPLATES_DIR
* Add Heroku to the ALLOWED_HOSTS list the format ['app_name.heroku.com', 'localhost']

#### Add the following Config Vars in Heroku:

* SECRET_KEY - This can be any Django random secret key
* PORT = 8000
* DISABLE_COLLECTSTATIC = 1 - this is temporary, and can be removed for the final deployment
* DATABASE_URL - Insert your own ElephantSQL database URL here

#### Heroku needs two additional files to deploy properly

* requirements.txt
* Procfile

#### Deploy

1. Make sure DEBUG = False in the settings.py
2. Go to the deploy tab on Heroku and connect to GitHub, then to the required repository.
3. Scroll to the bottom of the deploy page and either click Enable Automatic Deploys for automatic deploys or Deploy Branch to deploy manually. Manually deployed branches will need re-deploying each time the GitHub repository is updated.
4. Click 'Open App' to view the deployed live site.

Site is now live

## Testing

### Responsiveness Testing

The deployed website underwent rigorous testing on multiple devices and screen sizes to ensure its responsiveness and adaptability. Developer Tools were utilized to simulate various screen sizes, enabling thorough examination of how the website behaves across different devices. Bootstrap classes and media queries were implemented to achieve the desired design, ensuring that the website maintains its visual and functional integrity on all platforms, enhancing the user experience.

[AmIResponsive](/staticfiles/readme_img/amiresponsive-sportpulse.png)

### Browser Compatibility Testing

This project was tested using multiple web browser to check for compatibility issues. 

1. testing browsers include:
* opera 
* google chrome
* microsoft edge
* mozilla firefox

### Device Testing

Device testing was conducted on a variety of phone models, including Samsung Galaxy A12, iPhone 12, oppo. Family and friends have been asked to assist with this phase of testing.

### Code Validation

#### HTML validation
[Basepage](/staticfiles/readme_img/base-page.png)

[Create_PostPage](/staticfiles/readme_img/create-post-page.png)

[Commentspage](/staticfiles/readme_img/commentspage.png)


#### CSS Validation

[CSS](/staticfiles/readme_img/css.png)

#### javascript validation

[posts js](/staticfiles/readme_img/postsjs.png)
[comments JS](/staticfiles/readme_img/commentsjs.png)
[topics js](/staticfiles/readme_img/topicjs.png)

#### Python Validation
[admin.py](/staticfiles/readme_img/adminpy.png)
[forms.py](/staticfiles/readme_img/formspy.png)
[models.py](/staticfiles/readme_img/modelspy.png)
[urls.py](/staticfiles/readme_img/urlspy.png)
[views.py](/staticfiles/readme_img/viewspy.png)

## Bugs

### Resolved bugs

1. When comment was posted and page was refreshed, would duplicate comment and submit it to database
* resolved by adding a hTTpresponse to edit_comment view
2. Comment body was prepopulated when refreshing comments page
* resolved by clearing commentform after comment submission
3. when clicked delete post button, delete comment modal would pop up
* resolved by giving the 2 modals seperate ID's

## Features Testing 

| Page          | User Action   | Expected Result  | Notes            |
|---------------|---------------|------------------|------------------|
| Home Page     |               |                  |                  |
|               | Click on Logo | Redirect to Home Page | PASS        |
|               | Click on register button (Navigation bar) | Redirect to Sign Up page | PASS |
|               | Click on login (Navigation bar) | Move to login page | PASS |
|               | Click on social links in footer | Open new tab with appropriate link | PASS |
|               | Click on post title | Redirect to comments page | PASS |
| Home Page (Logged In - User)  |                 |          |  |
|               | After Login | register button is now create posts button | PASS |
|               | Click on create posts | Redirect to create posts | PASS |
|               | Click on logo | Redirects to homepage | PASS |
|               | After Login | Users name is displayed under navigation bar | PASS |
|               | Click on burger icon | Open dropdown menu | PASS |
|               | Click on home in dropdown | Redirect to homepage | PASS |
|               | Click on create post in dropdown | Redirect to create post page | PASS |
|               | Click on Logout  | Redirect to Logout Page | PASS |
| Create Post (Logged In - Admin)    |               |                  |                  |
|               | leave title empty | alert to fill in field | PASS |
|               | leave content empty | alert to fill in field | PASS |
|               | set workout frequency to > 7 | alert to set workout frequency to 7 or lower | PASS |
|               | set workout frequency to < 1| alert to set workout frequency to 1 or higher | PASS |
|               | Copy paste create post url to igcognito tab| redirected to login page | PASS |
|               | Copy paste create post url to igcognito tab logged in on other account | submits post under logged in account name | PASS |
| edit Post (Logged In - Admin)    |               |                  |                  |
|               | leave title empty | alert to fill in field | PASS |
|               | leave content empty | alert to fill in field | PASS |
|               | set workout frequency to > 7 | alert to set workout frequency to 7 or lower | PASS |
|               | set workout frequency to < 1| alert to set workout frequency to 1 or higher | PASS |
|               | Copy paste edit post url to igcognito tab| redirected to login page | PASS |
|               | Copy paste edit post url to igcognito tab logged in on other account | on submit, show alert message | PASS |
| Register Page  |                  |                  |                  |
|               | Enter invalid email | Field will only accept email address format | PASS |
|               | Enter valid email | No error | PASS |
|               | Email field left empty | Email is optional | PASS |
|               | Type invalid password | Must contain atleast 8 char | PASS |
|               | Type valid password | No error | PASS |
|               | Type password again (different) | Password must be the same | PASS |
|               | Fill all the form fields | Account created, alert message that you Signed in | PASS |
| Login Page  |                  |                  |                  |
|               | Try invalid username | Username is not correct | PASS |
|               | Try invalid password | Password is not correct | PASS |
|               | Valid password and username | Logs in, message that you signed in | PASS |
|               | Click Sign In with empty form | Fill in the form fields | PASS |
| Logout Page  |                  |                  |                  |
|               | Click on logout button | Sign user out, message that user signed out | PASS |
| 404 Error Page |  |    |    |
|               | Type in URL that does not exists | Custom 404 Error page is displayed | PASS |
|               | Click on Take Me Home button | Redirect to Home page | PASS |
| 500 Error Page |  |    |    |
|               | Admin raise exception in views.py | Custom 500 Error page is displayed, local development testing | PASS |
|               | Click on Go to Homepage button | Redirect to Home page | PASS |
| Admin Panel |  |    |    |
|               | CRUD functionality | Working as expected | PASS |
## References
### Docs

* [Stack Overflow](https://stackoverflow.com/)
* [Code Institute](https://learn.codeinstitute.net/dashboard)
* [Bootstrap 4.6](https://getbootstrap.com/docs/4.6/getting-started/introduction/)
* [Django docs](https://docs.djangoproject.com/en/4.2/releases/3.2/)
* [Django Allauth](https://django-allauth.readthedocs.io/en/latest/)
* [Google](https://www.google.com/)

### Content

* Custom error handlers and pages were inspired from Thomas-Tomo Domitrovic's [Woodland Whispers Retreat](https://github.com/Thomas-Tomo/woodland-whispers-retreat)
* README.md was inspired by Thomas-Tomo Domitrovic's [Woodland Whispers Retreat](https://github.com/Thomas-Tomo/woodland-whispers-retreat)
* CSS layout was inspired by Code Institute's Codestar blog
* Some functionality was inspirired by Code Institute's Codestar blog (comments CRUD functionality)
* All of the content is imaginary.


### Acknowledgments

* I would like to thank my mentor for support and feedback throughout this project, Mitko Bachvarov.
* I would like to thank the tutor support at Code Institute for their contineaud support over the course of this project
* I would like to thank my friends and family for their assistance in this project.