### Patrick Trollip's Full Stack Frameworks with Django Milestone Project.


### Link to Website:

### What is the project?
    Cyber Sappers is a cyber security business with it's products and services based on a website that gives users
    the ability to easily find a range of cyber security solutions to their own websites, databases, code, servers and general 
    online security. The Cyber Sappers website gives users the ability to browse the range of services and products via dropdown menu,
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



### Wire Frames and UX:
# Wireframes:
    https://www.wireframes.org/tiger/data/codinghamster90/home_page_5e44596f3a303.htm
    https://www.wireframes.org/tiger/data/codinghamster90/login_page_5e4474971ca53.htm
    https://www.wireframes.org/tiger/data/codinghamster90/register_page_5e447350de782.htm
    https://www.wireframes.org/tiger/data/codinghamster90/profile_page_5e447b619894a.htm
    https://www.wireframes.org/tiger/data/codinghamster90/rename_new_5e4434013dea9.htm
    https://www.wireframes.org/tiger/data/codinghamster90/products__5e445d24d36d4.htm
    https://www.wireframes.org/tiger/data/codinghamster90/products_and_services_5e4459a2c8b7a.htm
    https://www.wireframes.org/tiger/data/codinghamster90/shopping_basket_5e4476d14c930.htm
    https://www.wireframes.org/tiger/data/codinghamster90/payment_form_5e4471ddde48a.htm


# User stories:

    As a business owner I want to have a way to easily manage the security of my website and my business data. I want
    to be able to have a tailored cyber security system in place that I can add as much or as little as I feel I need.

    As a website owner and sole trader I want my website to be secure from cyber threats that could steal my customers details
    or my business data that I can risk having leaked or stolen. I need a easy way to find a range of products or services
    and get a affordable quote to suit my budget. I don't have alot of time to browse so I want a easy to manage account and want the 
    provider to easily be able to know what I need and get their advice.

    As a individual who had their data stolen I need a service like Cyber Sappers that can anaylize my website code and databases
    and fix the vulnerabilities and maybe provide some hardware that will manage traffic that is coming to my server so that I don't
    get my website flooded with spam calls or get requests, that block genuine users from using my own business and crashing my server.

    As a user of Cyber Sappers I can manage my account and buy services and products to keep my data servers and websites secure.

    As a user of Cyber Sappers I can easily navigate and browse the website and find what cyber security solutions I need without hassle.

    As a user of the website payments are secure and I don't have to worry about my password or card details being seen by spyware as it is hidden
    incase someone was watching my screen.


### Project planning:

# Defensive design:
    For defensive design I created links to images that will give a ALt attribute incase the image is not supported or the 
    user is visually impared. I added IF statements to my javascript code that will end with a else statement that will make sure something happens other than
    a error being displayed to the user that they won't understand. I also tried to make code that is simple enough not to slow down low band width connections
    that may lead to bad user experience.To do that I tried to use a appropriate layout for different devices. I tried to make my forms user friendly too with messages
    that display when something is missing on the form, when the form is sent and when the form is unable to send. I also tried to have a short term memory on a page 
    that will not force the user to resubmit certain data they already added to a form.

### Testing:

    Testing was done using Chrome Developer tools, Travis, debug mode set to true and functionality tested and passed before releasing
    the final product which is the website. The tests involved checking for typos, syntax errors, bugs, layout on multiple platforms and 
    checking that whne code was added that other functionality on each page and app still worked as appropriate.

### Deployment:
    I deployed my code on gitpod to my github repository.
    From my github repository it was connected to the Heroku server, Travis tool for testing each version.
    The website was wired up to AWS S£ cloud database and was wired up with Stripe for secure payments.
    When deploying I made sure not to push any secret keys or data that could be exploited by cyber criminals.
    I made sure the debug was switched off to prevent unwanted leaks of sensitive code.
    All code was working and then submitted for assessment via appropriate links and stored on github.

### Index and referenced code
    I modelled my django code from my courses mini-project as a reference and then tried to modify it so that it suited my website and was my 
    tailored code for the project. I used the Bootstrap framework to help build the site and fontawesome for icons and then customized it 
    so that it was unique.

### Technologies and tools used
 Wire frames tool = https://www.wireframes.org/tiger/getin.php
 Bootstrap version 4 =
 Fontawesome =
 CSS
 HTML5
 Javascript
 Python3
 Git version control
 AWS S3
 Heroku server
 Travis
 Stripe
 Django
