<h1 align="center">
Patrick Trollip's Full Stack Frameworks with Django Milestone Project.
</h1>

[![Build Status](https://travis-ci.org/Patoman90/Patrick-s-Full-Stack-Frameworks-with-Django-Milestone-Project.svg?branch=master)](https://travis-ci.org/Patoman90/Patrick-s-Full-Stack-Frameworks-with-Django-Milestone-Project)

## Link to Website: 
https://patricks4thmilestoneproject.herokuapp.com/

[Cyber Sappers LTD](https://patricks4thmilestoneproject.herokuapp.com/) Cyber Sappers is a cyber security business with it's products and services based on a website that gives users
    the ability to easily find a range of cyber security solutions to their own websites, databases, code, servers and general 
    online security.

The Cyber Sappers website gives users the ability to browse the range of services and products via dropdown menu,
    use a button that will link to form that gives the user the ability to get a quote on what service the user wants to possibly buy.
    The website allows the user to login,logout,register an account so they can have a account that will give them the ability to manage
    their services with Cyber Sappers. The login functionality will have certain actions restricted to being logged in like paying with
    Stripe and storing data. The website will be business orientated and allow the user to save some user data to a database securely with no 
    sensitive code exposed to anyone looking at the code and version history for example.
    The website also remain consistant while being readable and visually good looking and easy to use on multiple devices by use of Bootstrap
    and custom cascading style sheets to help evoke a good user experience. This will be coupled with interactive elements that javascript will
    add that helps the user interact and know that their input provides a reaction from the website. The website will allow verifiction
    processes to help the user feel that any data they provide is on a secure website and database and that their payment details are reasonably
    secure. The value it adds to the user is that they can be a private or commercial user and have the ability to upgrade,maintain and repair
    their code to keep it up to date with cyber threats and if they have been comprimised, then Cyber Sappers can help them  repair the damage
    and help them mitigate it in the future. The website will also give the user the freedom to use it from their mobile device, tablet or desktop.
    The website is hosted on the Heroku server with data being stored to the cloud database S3 from AWS. The users of the website will have peace 
    of mind that their data and own IT related hardware and software is secured with the most up to date cyber security through the website.


<br><br>
[**View Cyber Sappers on Heroku!**](https://patricks4thmilestoneproject.herokuapp.com/)


## UX

### Project Purpose

The goal of Cyber Sappers is to give the user a good experience when purchasing cyber security products and services in a simple & effective   way using the following:

- User registration form
- User log in control
- Profile Information page
- Easy navigation
- Viewing brands or types of a product and services
- Finding product and services information
- Viewing product and services information
- Adding products and services to the cart
- Adjusting the quantity of item(s) in cart
- Removing item(s) from cart
- Secure online payment


### User Experience

- Users are presented with simple user interface that uses buttons and drop down menu for easy navigation at the top of
the screen for mobile & tablet display & a navigation list on the side on desktop display for a Home, Register, Services, Products, Cart, Login & Review depending on the login in state of the user.

- There is a navigation bar at the bottom of the page to prevent a user on a device being forced to hit back or scroll back up to the menu to navigate.

- All items on the product page and services page have a title and a brief description, specifications & and price. There is also a add to cart button and add review button depending on if the user is logged in or not they can do more.

- The layout remains the same to try keep things simple and hassle free when navigating from one page to the next which prevents the user having to click the browser back button.

- Forms for the login or registration will display to the user required input so as to help them complete the forms for correct validation.

- Pagination has been included in the products and services pages to keep layout clean & speed up loading time if there are lots of products or services to display on a device.

- Log in & Registration has been implemented into the website to help with securing user data such as confidetial information and Stripe takes care of card payments.


### User Stories:

- As a business owner I want to have a way to easily manage the security of my website and my business data. I want
to be able to have a tailored cyber security system in place that I can add as much or as little as I feel I need.

- As a website owner and sole trader I want my website to be secure from cyber threats that could steal my customers details
or my business data that I can risk having leaked or stolen. I need a easy way to find a range of products or services
and get a affordable quote to suit my budget. I don't have alot of time to browse so I want a easy to manage account and want the 
provider to easily be able to know what I need and get their advice.

- As a individual who had their data stolen I need a service like Cyber Sappers that can anaylize my website code and databases
and fix the vulnerabilities and maybe provide some hardware that will manage traffic that is coming to my server so that I don't
get my website flooded with spam calls or get requests, that block genuine users from using my own business and crashing my server.

- As a user of Cyber Sappers I can manage my account and buy services and products to keep my data servers and websites secure.

- As a user of Cyber Sappers I can easily navigate and browse the website and find what cyber security solutions I need without hassle.

- As a user of the website payments are secure and I don't have to worry about my password or card details being seen by spyware as it is       hidden incase someone was watching my screen.


### Design Ideas

The design of the website based on trying to give a simple but straight forward layout without over complication or a sense of too much going on.

- #### Fonts

    - The standard font was used to keep things simple.

- #### Colors

    <b>rgb(204, 204, 204)</b>
    This color was used for the majority of the webiste pages including navigation elements and buttons.
    <br>

   
    <b>rgb(0, 204, 255)</b>
    This colour was used for a background color.
    <br>
    
- #### Styling
    
    **Special styles include:**
    
    - **Buttons -** Buttons have been styled using bootstrap & colours have been picked using the bootstrap colour scheme. I used Font                           awesome to add icons to the buttons to help users better understand the purpose at a glance.
        
    
    - **Pagination -** Pagination consists of a navigation menu at the top and a navigation bar at the bottom of the page.


### Wireframes

Wireframes were made using [MockupTiger](https://www.wireframes.org/).

- #### Wireframes

    - [Home Page](https://www.wireframes.org/tiger/data/codinghamster90/home_page_5e44596f3a303.htm)
    - [Product Page](https://www.wireframes.org/tiger/data/codinghamster90/products__5e445d24d36d4.htm)
    - [Services Page](https://www.wireframes.org/tiger/data/codinghamster90/products_and_services_5e4459a2c8b7a.htm)
    - [Login Page](https://www.wireframes.org/tiger/data/codinghamster90/login_page_5e4474971ca53.htm)
    - [Registration Page](https://www.wireframes.org/tiger/data/codinghamster90/register_page_5e447350de782.htm)
    - [Cart Page](https://www.wireframes.org/tiger/data/codinghamster90/shopping_basket_5e4476d14c930.htm)
    - [Payment form](https://www.wireframes.org/tiger/data/codinghamster90/payment_form_5e4471ddde48a.htm)
    - [Quote Page](https://www.wireframes.org/tiger/data/codinghamster90/rename_new_5e4434013dea9.htm)
    - [Profile Page](https://www.wireframes.org/tiger/data/codinghamster90/profile_page_5e447b619894a.htm)
    - [Reviews Page](https://www.wireframes.org/tiger/data/codinghamster90/reviews_page_5e4b3f48b9c2e.htm)


### Developer and Business Purpose

- Must show clear & professional examples of HTML, CSS, JavaScript & Python.

- Must show use of Django knowledge.


## Features
 
### Existing Features


#### Navbar:

- The navbar is featured on the bottom of the page for easy navigation when the user is at the bottom.


**Desktop** 
- In the top left-hand corner, a set of buttons for quick navigation and a drop down menu for available options for navigation.

- Beneath that is a button to access the get a quote details and form.

- The last button is a review button to add a customer review to a product or service.

- When a user is logged in, there are different options available like profile page and more privlages.


**Tablet & Mobile**

- The menu is displayed with the burger layout and the navbar remains at the bottom.

- The content of the page resizes to a appropriate layout for the size of the smaller device screen dimensions.


#### Footer:

- Displays the website creator.


#### Home Page:

- Gives the user details about the company and thei background/services.


#### Product Page:

- Shows users the product available with pricing and description.

- Buttons like add review and add to cart are available as well as the remove item from cart button and checkout button.


#### Login Page:

- **Login Form** - A Login form has been added so that the user has somewhere to login to the website. If a user enter invalid credentials, you will be declined access. Also both fields are required for successful login.

#### Registration Page:

- **Registration Form** - A Registration form has been added so that the user where somewhere to register for an account. There are four required fields, Username, Email Address, Password & Confirm Password. All fields must be filled before you can successfully register otherwise they will get notified by the form to fill in missing details. Also Password & Confirm Password fields must match before a user can successfully register. If registered successfully, You will be notified & logged in to the account you have just created. There is also a link to the sign in page if you already have a account and want to log in.


#### Cart Page:

- **Cart** - When a user has placed something in their cart, it will show the cart items and the user can proceed to checkout or apend their items if they want to edit the quantity.


#### Checkout Page:

- **Checkout Form** - The idea was to use stripe to complete the purchase securely but unfortunately this feature was not something I was able to figure out how to implement for the first time on my own.


#### Successful Payment Page:

- **Successful Payment Box** -The idea was to use stripe to complete the purchase securely but unfortunately this feature was not something I was able to figure out how to implement for the first time on my own.

#### Profile Page:

- **User Profile** - When a user is logged in, they can view their profile on the profile page, this will tell them their Username, Name which consists of their first name & last name, their email address & the date & time the account was created. It was not finished though the way I planned to make it in time.

## Project planning:

### Defensive design:

- For defensive design I created links to images that will give a ALt attribute incase the image is not supported or the 
user is visually impared. I added IF statements to my javascript code that will end with a else statement that will make sure something happens other than
a error being displayed to the user that they won't understand. I also tried to make code that is simple enough not to slow down low band width connections
that may lead to bad user experience.To do that I tried to use a appropriate layout for different devices. I tried to make my forms user friendly too with messages
that display when something is missing on the form, when the form is sent and when the form is unable to send. I also tried to have a short term memory on a page 
that will not force the user to resubmit certain data they already added to a form.

## Testing:
- Testing was done using Chrome Developer tools to try fig, Travis, debug mode set to true and functionality tested and passed before releasing
the final product which is the website. The tests involved checking for typos, syntax errors, bugs, layout on multiple platforms and 
checking that when code was added that other functionality on each page and app still worked as appropriate and to my best ability at the time.

## Known Issues to be fixed:
- Unfortunatly I was unable at the time to get the reviews form to send the data to a databse where the data would be rendered on 
a html page for users to view the user reviews.  I will fix this after assessment.

- I was also unable given my resources at hand, not able to get the quote form to send to the desired email. I will fix this after          assessment.

- Also I needed the email to work to get the reset password function to work but I will have to come back and fix it.

- I had made a type error when making my gitignore file. So I changed it to be correct and then changed all keys and assigned them to new variables on Heroku and gitpod with the key pair to reference the appropriate variables to rescure everything. Not ideal but I will remember next time.

## Deployment:
- I deployed my code on gitpod to my github repository.
From my github repository it was connected to the Heroku server, Travis tool for testing each version.
The website was wired up to AWS S3 cloud database and was wired up with Stripe for secure payments.
When deploying I made sure not to push any secret keys or data that could be exploited by cyber criminals.
- I made sure the debug was switched off to prevent unwanted leaks of sensitive code.
All code was working and then submitted for assessment via appropriate links and stored on github.
- I also changed the debug to false before deployment.
The tests were passing on travis.


## Database

### Database Choice

- I used AWS S3 to deploy my database to a remote cloud service.



## Technologies Used

### Tools
- [Wireframes](Wire frames tool = https://www.wireframes.org/tiger/getin.php) Tool used to build project prototype.
- [Gitpod](https://gitpod.io) IDE used. 
- [Django](https://www.djangoproject.com/) The python framework used as required by the project requirements.
- [Travis](https://travis-ci.org/) Used for testing code was working the way it is meant to after changes.
- [Stripe](https://stripe.com) was the planned tool for use of secure payments.
- [AWS S3 Bucket](https://aws.amazon.com/) to store all database info fr products and services. Could not get the images to show up.
- [PIP](https://pip.pypa.io/en/stable/installing/) used to install requirements into the project.
- [Gunicorn](https://pypi.org/project/gunicorn/)Used for the deployment of a Django project in Heroku.
- [Psycopg2](https://pypi.org/project/psycopg2/) is a PostgreSQL database adapter for the Python programming language.
- [Django Heroku](https://pypi.org/project/django-heroku/) is used to view the deployed project.
- [GitHub](https://github.com/) is used as a remote backup of code used in the project & used to showcase code remotely.


### Libraries

- [Bootstrap](https://www.bootstrapcdn.com/) to assist with website layout & styling.
- [FontAwesome](https://www.bootstrapcdn.com/fontawesome/) to apply informative icons used throughout the website.


### Languages
- The languages used throughout the website are HTML, CSS, JavaScript & Python.

## Index and referenced code
- I modelled my django code from my courses mini-project as a reference and then tried to modify it so that it suited my website and was my 
tailored code for the project. I used the Bootstrap framework to help build the site and fontawesome for icons and then customized it 
so that it was unique.

### Images:
- https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fevent.asme.org%2FEvents%2Fmedia%2Flibrary%2Fimages%2Ficons%2Fhome-page%2Fprev-year-conference-info-480_icon.png%3Fext%3D.png&f=1&nofb=1
- https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fcogitogroup.net%2Fwp-content%2Fuploads%2Fhardware.png&f=1&nofb=1
- https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fcdn2.iconfinder.com%2Fdata%2Ficons%2Fantivirus-internet-security-  1%2F33%2Fcybersecurity-512.png&f=1&nofb=1
- https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimage.freepik.com%2Ffree-photo%2Fabstract-technology-binary-code-background_34629-592.jpg&f=1&nofb=1


### Acknowledgements
I wish to say thank you to everyone who helped me when and where they could and that this was a big challenge for me given my limited availability to do work on the project and balance my other commitments.

## Disclaimer

All content on the website, including images, are used for educational purposes only.
