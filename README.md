# Sportpulse


Welcome to SportPulse, the ultimate Reddit-style community for fitness enthusiasts! Whether you’re a seasoned athlete, a gym newbie, or someone looking to stay active, SportPulse is your go-to hub for everything workout-related. Share your progress, ask for advice, discover routines, and connect with like-minded individuals who share your passion for fitness. From lifting tips to yoga hacks, SportPulse keeps the energy high and the motivation stronger than ever. 💪

![Home Screen](/staticfiles/readme_img/amiresponsive-sportpulse.png)

[View Sportpulse live website here](https://sportpulse-6bad7f07e667.herokuapp.com)
- - -

## Table of Contents
### [User Experience](#user-experience-ux)
* [Project Goals](#project-goals)
* [Agile Methodology](#agile-methodology)
* [First time user](#first-time-user)
* [Registered user](#registered-user)
### [Design](#design-1)
* [Color Scheme](#color-scheme)
* [Cabin Images](#cabin-images)
* [Wireframes](#wireframes)
* [Data Model](#data-models)
* [User Journey](#user-journey)
* [Database Scheme](#database-scheme)
### [Security Features](#security-features-1)
### [Features](#features-1)
* [Existing Features](#existing-features)
* [Features Left to Implement](#features-left-to-implement)
### [Technologies Used](#technologies-used-1)
* [Languages Used](#languages-used)
* [Databases Used](#databases-used)
* [Frameworks Used](#frameworks-used)
* [Programs Used](#programs-used)
### [Deployment and Local developement](#deployment-and-local-developement-1)
* [Local Developement](#local-developement)
* [ElephantSQL Database](#elephantsql-database)
* [Cloudinary](#cloudinary)
* [Heroku Deployment](#heroku-deployment)
### [Testing](#testing-1)
### [References](#references-1)
* [Docs](#docs)
* [Content](#content)
* [Acknowledgments](#acknowledgments)

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

## Features

* Home page showcases a rotating carousel that contains available cabins
* The website features a comprehensive list of amenities accompanied by detailed descriptions for each one.
* User can make an account and login
* When logged in, users get access to the cabin overview and are able to book cabins
* Users can edit and delete their bookings
* Every user action is accompanied by a corresponding message to ensure that users are promptly notified of any changes or updates.
* Total price of booking is displayed to users.

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


![Browse Cabins](documentation/readme_images/browse-cabins.PNG)

* Cabin pagination
    * On the bottom of the page

![Pagination](documentation/readme_images/pagination.PNG)

* Logout
    * User can logout

![Logout](documentation/readme_images/logout.PNG)

* Make a Booking
    * Users can make a booking by clicking the cabin they want and then read details and fill in the booking form.
    * Form validation is implemented to make sure form are submitted correctly and if there is an error user will be notified with alert message, also if everything is good, user gets a message to notifiy them.
    * Form contains amenities which are completely optional and they dont have to be selected.

    ![Message](documentation/readme_images/alert-message.PNG)

![Make a Booking](documentation/readme_images/make-a-booking.PNG)

* Booking Succesful
    * If booking is succesfull, user gets a notified message and an overview of the booking they just made, which includes all the details and a total price of the booking, also there is a button for contact page and my booking button that leads to all of the users bookings.

![Booking Succesful](documentation/readme_images/booking-successful.PNG)

* Booking Overview
    * Includes all of the user bookings, which have buttons to edit or delete bookings.

![Booking Overview](documentation/readme_images/my-bookings.PNG)

* Already booked dates
    * User won't be able to book dates that are already booked.
    * Dates in the past are unavailable.

![Booked Dates](documentation/readme_images/booked-dates.PNG)

* Edit Booking
    * User can change their booking and save changes

![Edit Booking](documentation/readme_images/edit-booking.PNG)

* Delete Booking
    * User can delete their booking, before it is deleted it has to be confirmed.

![Delete Booking](documentation/readme_images/delete-booking.PNG)

* Alert messages
    * For every action there is an alert message to notify user
    * Here is one example

![Alert Message](documentation/readme_images/delete-message.PNG)

* Admin Features
    * Django built in admin panel allows admin control over the website.
    * Admin can access admin panel through his navigation bar
    * Can add, update, delete cabins.
    * Create amenities, update existing amenities which are connected to the cabins.
    * Delete accounts, verifiy emails, delete bookings...

* Error Pages
    * There are custom 404 and 500 error pages set up.
    * They contain buttons to redirect to home page if there is an error.

![Error 404](documentation/readme_images/error.PNG)
![Error 500](documentation/readme_images/500-error-page.PNG)

### Features Left to Implement 

* User Reviews: Allow users to leave reviews and ratings for cabins they have booked, providing valuable feedback for other users.
* Advanced Search: Implement an advanced search functionality, enabling users to search for cabins based on specific criteria such as price range, amenities, and availability.
* Cabin Recommendations: Develop a recommendation engine that suggests cabins to users based on their previous bookings, interests, or preferences.
* Online Payment: Implement an online payment system to allow users to securely make payments for their bookings directly through the website.
* For the purposes of this project these implemenation were not necessary.

## Technologies Used

### Languages Used

* [HTML5](https://en.wikipedia.org/wiki/HTML5)
* [CSS3](https://en.wikipedia.org/wiki/CSS)
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Databases Used

* [ElephantSQL](https://www.elephantsql.com/) - Postgres database
* [Cloudinary](https://cloudinary.com/) - Online static file storage

### Frameworks Used

* [Django](https://www.djangoproject.com/) - Python framework
* [Bootstrap 4.6.1](https://getbootstrap.com/docs/4.6/getting-started/introduction/) - CSS framework

### Programs Used

* [Github](https://github.com/) - Storing the code online
* [Gitpod](https://www.gitpod.io/) - To write the code.
* [Heroku](https://www.heroku.com/) - Used as the cloud-based platform to deploy the site.
* [Google Fonts](https://fonts.google.com/) - Import main font the website.
* [Figma](https://www.figma.com/) - Used to create wireframes and schemes
* [Craiyon](https://www.craiyon.com/) - Generate AI images of cabins and logo based on my words descriptions
* [Am I Responsive](https://ui.dev/amiresponsive) - To show the website image on a range of devices.
* [Git](https://git-scm.com/) - Version control
* [Jinja](https://jinja.palletsprojects.com/en/3.1.x/) - Templating engine
* [Favicon Generator](https://realfavicongenerator.net/) - Used to create a favicon
* [JSHint](https://jshint.com/) - Used to validate JavaScript
* [W3C Markup Validation Service](https://validator.w3.org/) - Used to validate HTML
* [CSS Validation Service](https://jigsaw.w3.org/css-validator/) - Used to validate CSS
* [CI Python Linter](https://pep8ci.herokuapp.com/#) - Used to validate Python
* [Colormind](http://colormind.io/) - Color Scheme

## Deployment and Local Developement

Live deployment can be found on this [View Woodland Whispers Retreat live website here](https://woodland-whispers-retreat.herokuapp.com/)

### Local Developement

#### How to Fork
1. Log in(or Sign Up) to Github
2. Go to repository for this project [Woodland Whispers Retreat](https://github.com/Thomas-Tomo/woodland-whispers-retreat)
3. Click the fork button in the top right corner

#### How to Clone
1. Log in(or Sign Up) to Github
2. Go to repository for this project [Woodland Whispers Retreat](https://github.com/Thomas-Tomo/woodland-whispers-retreat)
3. Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
4. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
5. Type the following command in the terminal (after the git clone you will need to paste the link you copied in step 3 above)
6. Set up a virtual environment (this step is not required if you are using the Code Institute Template in GitPod as this will already be set up for you).
7. Install the packages from the requirements.txt file - run Command pip3 install -r requirements.txt

### ElephantSQL Database
[Woodland Whispers Retreat](https://github.com/Thomas-Tomo/woodland-whispers-retreat) is using [ElephantSQL](https://www.elephantsql.com/) PostgreSQL Database

1. Click Create New Instance to start a new database.
2. Provide a name (this is commonly the name of the project: tribe).
3. Select the Tiny Turtle (Free) plan.
4. You can leave the Tags blank.
5. Select the Region and Data Center closest to you.
6. Once created, click on the new database name, where you can view the database URL and Password.

### Cloudinary
[Woodland Whispers Retreat](https://github.com/Thomas-Tomo/woodland-whispers-retreat) is using [Cloudinary](https://cloudinary.com/)
1. For Primary interest, you can choose Programmable Media for image and video API.
2. Optional: edit your assigned cloud name to something more memorable.
3. On your Cloudinary Dashboard, you can copy your API Environment Variable.
4. Be sure to remove the CLOUDINARY_URL= as part of the API value; this is the key.



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
* Add the Cloudinary URL to env.py
* Add the Cloudinary libraries to the list of installed apps.
* Add the STATIC files settings - the url, storage path, directory path, root path, media url and default file storage path.
* Link the file to the templates directory in Heroku.
* Change the templates directory to TEMPLATES_DIR
* Add Heroku to the ALLOWED_HOSTS list the format ['app_name.heroku.com', 'localhost']

#### Add the following Config Vars in Heroku:

* SECRET_KEY - This can be any Django random secret key
* CLOUDINARY_URL - Insert your own Cloudinary API key
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
Please see  [TESTING.md](TESTING.md) for all the detailed testing performed.

## References
### Docs

* [Stack Overflow](https://stackoverflow.com/)
* [Code Institute](https://learn.codeinstitute.net/dashboard)
* [Bootstrap 4.6](https://getbootstrap.com/docs/4.6/getting-started/introduction/)
* [Django docs](https://docs.djangoproject.com/en/4.2/releases/3.2/)
* [Django Allauth](https://django-allauth.readthedocs.io/en/latest/)
* [Django and Static Assets](https://devcenter.heroku.com/articles/django-assets)
* [Cloudinary](https://cloudinary.com/documentation/diagnosing_error_codes_tutorial)
* [Google](https://www.google.com/)

### Content

* All of the content is imaginary and written by the developer, me, Thomas-Tomo Domitrovic.
* All images were generated with Artificial intelligence (AI) based on my word input and description of the cabins and logo.

### Acknowledgments

* I would like to thank my mentor for support and feedback throughout this project, Mitko Bachvarov.
* I would also like to extend my appreciation to the Slack community for their continuous engagement and willingness to share knowledge. The collaborative environment provided a platform for learning, troubleshooting, and gaining inspiration from fellow developers.