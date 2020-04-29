[![Build Status](https://travis-ci.org/MatijaBas/rugby-shop.svg?branch=master)](https://travis-ci.org/MatijaBas/rugby-shop)

# [Rugby shop](https://rugby-shop.herokuapp.com/)

**This is my Milestone Project 4: Full Stack Frameworks with Django - Code Institute**
-----

## Table of Contents
1. [UX](#ux)
    - [Goals](#goals)
        - [Visitor Goals](#visitor-goals)
        - [Business Goals](#business-goals)
    - [User Stories](#user-stories)
    - [Design Choices](#design-choices)
    - [Wireframes](#wireframes)

2. [Features](#features)
    - [Existing Features](#existing-features)
        - [Navbar](#navbar)
        - [Home Page](#home-page)
        - [About Us](#about-us)
        - [Shop](#shop)
            - [Product Details Page](#product-details-page)
        - [Contact Page](#contact-page)
        - [Register Page](#register-page)
        - [Login Page](#login-page)
        - [Profile Page](#profile-page)
        - [Log out Page](#log-out-page)
        - [Reviews Page](#reviews-page)
         - [Checkout page](#checkout-page)
            - [Cart](#cart)
            - [Payment](#payment)
        - [Terms & Condition Page](#terms-&-condition-page)
        - [Delivery Page](#delivery-page)
        - [Return Policy Page](#return-policy-page)
        - [Footer](#footer)
    - [Features for Future Releases](#features-for-future-releases)

3. [Information Architecture](#information-architecture)
    - [Database choice](#database-choice)
    - [Data Models](#data-models)
        - [User](#user)
        - [Products App Model](#products-app-model)
        - [Cart App Models](#cart-app-models)
        - [Accounts App Models](#accounts-app-models)
        - [Checkout app models](#checkout-app-models)

4. [Technologies Used](#technologies-used)
    - [Tools](#tools)
    - [Databases](#databases)
    - [Libraries](#libraries)
    - [Languages](#languages)

5. [Testing](#testing)
    - [Code Validation](#code-validation) 
    - [Manual Testing](#manual-testing)

6. [Deployment](#deployment)
    - [How to run this project locally](#how-to-run-this-project-locally)
    - [Heroku Deployment](#heroku-deployment)

7. [Credits](#credits)
    - [Content](#content)
    - [Images](#images)
    - [Code](#code)
    - [Acknowledgements](#acknowledgements)
    
8. [Contact](#contact)

***

<br/>

# Overview
[Rugby shop](https://rugby-shop.herokuapp.com/) was built and deployed by Matija Basanovic as his final project for 
the [Code Institute Full Stack Web Development Diploma](https://codeinstitute.net/). The project has been developed using [Django](https://www.djangoproject.com/), with the goal of 
fulfilling the requirements of the final, Full-Stack Milestone Project of the Code Institute Full-Stack Software Developer Course.
This page is made after a lot of thinking and negotiation with the man name Seamus who owns the shops.
The purpose of the Rugby shop online page is to help bussines owner Seamus to sell some of his products on line during lockdown in Ireland coused by global pandemic call COVID-19. Because all his 50 shops are closed now, this is the only way for Seamus to sell some products and try to save a company and try bussines to continue.

All images displayed in project are stored in an [AWS S3](https://aws.amazon.com/s3/) bucket, as are static files like CSS, icons and user-uploaded pictures.

The project is hosted at [Heroku](https://www.heroku.com/). A [Postgresql](https://www.postgresql.org/) database, also hosted at Heroku, is used to store image data and user data

# UX

## Goals

### Visitor Goals

The visitors that are targeted by Rugby Shop are:
- Professionals who are looking for good product for their team
- Amateurs that want to play a rugby in their favorite jersey
- People that want to get perfect birthay present
- People that are just bored becouse of COVID-19 and looking to spend some money

User goals are:
- Find a product that's gonna satisfied their needs 
- Buy from a trustworthy online shop.
- Show total price and number of items in cart.
- Be able to navigate the shop easily, find what I need and make a safe and secure purchase.


The online Rugby Shop is a great way to meet these needs because:
- The website has been designed to provide a clear view of product visitors are looking for.
- In navbar , visitors can find Home, Login and Register, Shop button with all products where they can search for specific product, Reviews and Cart
- Buyers can leave review if they are logged in

### Business Goals

The Goals of The Rugby Shop business are:
- Provide a professional online shop that helps the user to feel safe that they are buying from a trustworthy source. 
- Build brand awareness by including all the colors, fonts and logo associated with The Rugby Shop.
- Build Rugby Shop newsletter subscriptions.
- Fast and efficient delivery.
- Make sales of products easy for buyers to increase sales conversion.
- The presentation and layout of the site may not cause consternation, loss, or a desire to resign from shopping.

## User Stories

A Visitor to The Rugby Shop website  expects/wants/needs:

1. As a creative, mindful person I would rather buy products from local shop to support small local business owners with a personal touch, instead of buying products from big companies.

2. As new visitor I want ability to search through small amounts of information to find what I need, and then be able to easily click to get more detailed information.
As new customer I dont want to be confused by the layout or process of payment, and be able to easy find what i am looking for.

4. In order to avoid unawareness of purchase, I want product information must be sufficiently clear to understand.

5. A text search function so that I can quickly narrow down my search when looking for something specific.I need To be able to see a summary of my order on every page of the checkout process. When I am logged in I can access my account details and update them if I need to. 
I expect to be able to find information on my past orders. 
I expect to be able to easily get in contact with the shop owner via a contact form.

6. To be informed if I try to order more items than are available in stock.
Whenever a user adds an item to their cart or adjusts the quantity in their cart the current stock level for that item is checked from its database entry. A modal will alert the user if they attempt to add more to their cart than is available in stock, and their cart will be updated to reflect the maximum number available.

## Design Choices

The Rugby Shop website has a stylistic design with discrete and warm colors, inspiring images and simple buttons.

### Fonts
- The primary font [Merriweather](https://fonts.google.com/specimen/Merriweather?query=me) provides an artistic feeling, but are at the same time easy to read, which I think suits the purpose of the page and it´s audience.

My discrete & warm color design choices goes well together with the background image, and are listed here:

Color for the navbar | Color for the footer | Color for the New Collection carousel | Color for landing page | Color for about us text
--- | --- | --- | --- | ---
#ec7211 | #ec7211 | #4c2b22 | #f8f9fa | #1a251a

## Wireframes

Please click here to see all the [Wireframes](https://github.com/MatijaBas/rugby-shop/tree/master/wireframes) created.

# Features
 
## Existing Features

### Elements on every page

#### Navbar:

<div align="center">
    <img src="https://rugby-shop.s3-eu-west-1.amazonaws.com/static/img/navbar1.jpg" alt="Rugby Shop Navbar" aria-label="RugbyShop" />
</div>

- The navbar is top and fix , features on every page. RugbyShop logo on the far left which links to the home page of the site.

- Next to the logo is Home, Register and Login or Home, Profile and LogOut If user is loged in.

- In the middle of Navbar is name of the webpage so user know all the time where he is.

- On the right side of the navbar visitors can find links to Shop, reviews and cart

  -  The shopping cart counter works even for a user who is not logged in. This is because all the information about which products the user has added 
      to their cart is stored in their session data. This makes it possible for a new user to add things to their cart before being asked to log in or register. 
      This way user can add items to cart without registering, however when user will go to cart and will try to do checkout he/she will be directed to login/register page.
    
    - When user logs in a cart will remain with items picked as anonymous user.


<div align="center">
    <img src="https://rugby-shop.s3-eu-west-1.amazonaws.com/static/img/navbar-mobile.jpg" alt="Rugby Shop Navbar on mobile devices" aria-label="RugbyShop" />
</div>

- In mobile view logo is on left and the navigation bar changes to drop downtoggle with categories to choose from underneath logo.

***

<br/>

### Home Page

<br/>

<div align="center">
    <img src="https://rugby-shop.s3-eu-west-1.amazonaws.com/static/img/homepage.jpg" alt="Rugby Shop Homepage" aria-label="RugbyShop" />
</div>

<br/>

- The home page is welcoming users and ofering them a button to browse products, and underneath that is carousel with new collections

<br/>

### About Us

<div align="center">
    <img src="https://rugby-shop.s3-eu-west-1.amazonaws.com/static/img/about_us1.jpg" alt="Rugby Shop About Us" aria-label="RugbyShop" />
</div>

- Text about how did shop start and little bit of history about Rugby Shop

<br/>

<div align="center">
    <img src="https://rugby-shop.s3-eu-west-1.amazonaws.com/static/img/about_us2.jpg" alt="Rugby Shop About Us" aria-label="RugbyShop" />
</div>

- Few pictures from first days, when shop was open, 
- Subscribe me form for users who are interested in exclusive offers

<br/>

### Shop

<div align="center">
    <img src="https://rugby-shop.s3-eu-west-1.amazonaws.com/static/img/shop.jpg" alt="Rugby Shop Products" aria-label="RugbyShop" />
</div>

- At the top of products page is a search box where you look for desired item for example "irish jersey"
- The shop page comprises 3 columns in each row , with 21 product in total.
Every product is in a card with few details, picture, name, price , old price...
- When clicking on the image or product name user will be directed to product details where more info will be displayed.

<br/>

### Product details page

<div align="center">
    <img src="https://rugby-shop.s3-eu-west-1.amazonaws.com/static/img/product-details.jpg" alt="Rugby Shop Products details" aria-label="RugbyShop" />
</div>

- Larger image gives a customer an better overview what is about to buy
- The product **title, description, price and old price** are all clearly visible under product panel.
- Here user can choose a size and quantity of product
- From this point customer can either add desired item to basket go back shopping or  do checkout if any items in cart.

### Contact Page

<br/>

- The contact page contains a form for the user to fill in to send the shop owner an email.
- Name, email address and message are all required fields so that the shop owner receives all the information she needs to respond.
- If the user is logged in then their email address will already be populated in the email field.

***
<br/>


### Register Page

<br/>


- A user who is not logged in can create a new account using the register page. The page on this form includes a username (which must be unique), email address, password and password conformation fields. 
- Information about what characters are accepted by these fields is displayed with the form.
- If a user who is already logged in tries to access this page, they are redirected to the home page.

***
<br/>


### Login Page

- The login page features a standard login form asking for username and password.
- Validation for this form is handled in the back end and relevant feedback is sent to the user when they sign in.

<br/>

***

### Profile Page

<div align="center">
    <img src="https://rugby-shop.s3-eu-west-1.amazonaws.com/static/img/profile.jpg" alt="Rugby Shop Profile" aria-label="RugbyShop" />
</div>

- The users account page can only be accessed by a logged in user if user not logged in the Profile icon is not displayed.
- The account page has basic info about user. All this details are saved after filling shipping details, so user will have his profile filled after that step.
- The user can see history of shoping sorted by dates and on click, user can see what he bought

<br/>

### Log out page

- Any user who clicks on "Log out" from the navigation bar is automatically logged out and their session data cleared. 
- The message on top page will inform the user what action was made. After login back in the users cart will be empty.
***
<br/>

### Reviews page

<div align="center">
    <img src="https://rugby-shop.s3-eu-west-1.amazonaws.com/static/img/reviews.jpg" alt="Rugby Shop Reviews" aria-label="RugbyShop" />
</div>

- On the Reviews page the user can add own posts called review. The user can Add new Feedback, Edit an already existing Feedback post and View Feedback to see the post in an own page.

<br/>

### Checkout page

<br/>

- Checkout process starts when you click on cart that will show user summary of the shopping he made. From here you can either go back and
  continue shopping or proceed to shipping details. 
    
- The checkout process is broken up into 2 stages. The reason for this was to break up the process into small steps as is common in online shops.

    <br/>

    ***

    1. ### Cart

        <br/>

    <div align="center">
        <img src="https://rugby-shop.s3-eu-west-1.amazonaws.com/static/img/cart.jpg" alt="Rugby Shop cart" aria-label="RugbyShop" />
    </div>

- The shopping cart page features a summary of all the items the user has added to their cart.

- Each list item includes a picture of the item, the item title and price.

- The total amount and cart view is available to see in top right corner of the page.

- A quantity field is displayed with each cart item, giving the user the ability to adjust the quantity in their cart. Any time a quantity is adjusted the subtotal displayed is updated to reflect the change
- User that is not logged in will be directed to login page that also gives option to register. Only registered customer will be able to proceed to the checkout page. 

- Very important feature that starts in cart is that the user always have a two buttons to click KEEP SHOPPING or
 CONTINUE to Payment, this way user is never forced to use back button in the browser.

<br/>

- Here customer is introduced to items selected during shopping and total price.
- If applicable, amount saved thanks to discount provided will be displayed next to total.
- Here the user has option to:
    - amend amount of items purchased
    - delete item if necessary 
    - keep shopping
    - proceed to checkout

        <br/>

        - The "Checkout" button leads the user to the checkout page.

    <br/>

    ***

    2. ### Payment

    <div align="center">
        <img src="https://rugby-shop.s3-eu-west-1.amazonaws.com/static/img/checkout.jpg" alt="Rugby Shop checkout" aria-label="RugbyShop" />
    </div>

 - The Stripe payment page includes a summary of what the user is buying, and fields to enter credit card information.
    - All the validation and messages to the user on this page are handled by stripe.
    - On clicking the "Pay" button and on successful completion of payment.
    - On the end a confirmation email is send to customer, thanking for shopping.

<br/>

### Terms & Condition Page

- Every trustworthy online shop provides the legal documentation expected by the user on their site. Although these documents are a legal requirement of any online shop, including them also helps users to feel they can trust the outlet.

### Delivery Page

- Contain all information about delivery, from time and cost to different location around the world. There is also Frequently Asked Questions.

### Return Policy Page

- This page provides the user with shipping options to choose from. At this point there is only one shipping option available, however this page and functionality have been left in so that other options such as expedited shipping may be added with a future release.
- As a shipping method is automatically selected, the order summary now reflects the total cost including shipping.
- The "Continue to payment" button leads the user to the payment page hosted by Stripe.

### Footer

<div align="center">
    <img src="https://rugby-shop.s3-eu-west-1.amazonaws.com/static/img/footer.jpg" alt="Rugby Shop footer" aria-label="RugbyShop" />
</div>

- The footer background of orange was chosen to provide same contrast as navbar. The Headings are displayed same color as navbar.
- The footer features the copyright information.

- In the center of the footer icons are for the socialmedia of the Rugby Shop.

- Underneath socialmedia are copyright and socialmedia icons of Matija Basanovic

- Useful info about store (opening times phone number location) are located on right

- Footer also contains about, delivery information, return policy, contact pages where user would expect to find important information about policy and store it self.

<br/>

<div align="center">
    <img src="https://rugby-shop.s3-eu-west-1.amazonaws.com/static/img/footer-mobile.jpg" alt="Rugby Shop footer-mobile" aria-label="RugbyShop" />
</div>

- In the mobile view footer aligns all features one under another one.

<br/>

### Features for Future Releases

- I want to add pagination to the products page. As for now, there are only 21 products added in the products page, but pagination added would be great for when the amount of products can increase over time as the business grows.
- Coupons and discount codes.
- Additional payment methods.
- Auto login when registering a new account
- Ability to build combo buys with items selected by seller
- Option to buy a gift vouchers
- Live Chat
- Sending an email to customer when their new order has been placed.

# Information Architecture

### Database Choice

- As a framework Django works with SQL databases. During development on my local machine I worked with the standard **sqlite3** database installed with Django.
- On deployment, the SQL database provided by Heroku is a **PostgreSQL** database. 

## Data Models

* In the `products` app I have this model: 
1. Product 
* In the `checkout` app I have these models:
1. Order
2. OrderItem
* In the `review` app I have this model:
1. Review

### User

The User model utilized for this project is the standard one provided by `django.contrib.auth.models`

### Products app model

Within the `products` app, the **Product** model holds all the data needed for the products in the shop.

**Product model**

| Name | Key in db | Validation | Field Type |
--- | --- | --- | ---
Title | title | max_length=100 | CharField
Shop category | category | choices=CATEGORY_CHOICES | CharField
Product id| id | primary_key=True | AutoField
Product name | name | max_length=255 | CharField
Product info | description | ---- | TextField
Price | price | max_digits=6, decimal_places=2, default=1 | DecimalField
Image | image | blank=True, null=True | ImageField
Description | description | ---- | TextField
Price | price | max_digits=6, decimal_places=2 | DecimalField
Currency | currency | max_length=3, default="EUR | CharField
Category | category | blank=True,null=True, on_delete=models.CASCADE | ForeignKey("products.ProductCategory")
Quantity | quantity | ---- | IntegerField

<br/>

- The Product model uses Pillow to store all image files in an AWS S3 bucket.

### Cart app models
 
 <br/>

 **Cart(TimestampedModel)**

| Name | Key in db | Validation | Field Type |
--- | --- | --- | ---
User | user | User, on_delete=models.CASCADE | OneToOneField

<br/>

**CartItem**

| Name | Key in db | Validation | Field Type |
--- | --- | --- | ---
Cart | cart | Cart, on_delete=models.CASCADE| ForeignKey
Product_id | product_id | ----- | IntegerField
Quantity | quantity | ---- | IntegerField

<br/>

### Accounts app models

<br/>

**Customer model**

| Name | Key in db | Validation | Field Type |
--- | --- | --- | ---
User | user | OneToOneField to| User
Full Name | full_name | max_length=150 | CharField
Address line 1 | street_address1 | max_length=50, blank=True | CharField
Address line 2 | street_address2 | max_length=50, null=True, blank=True | CharField
Town / City | town_or_city | max_length=150 | CharField
County | county | max_length=20, blank=True | CharField
Postcode | postcode | max_length=10 | CharField
Date ordered | date_ordered | default=datetime.date.today | DateField
County | county | max_length=20 | CharField


### Checkout app models

<br/>

**Order model**

| Name | Key in db | Validation | Field Type |
--- | --- | --- | ---
customer | customer | Customer, on_delete=models.CASCADE| ForeignKey
Total Cost | total_cost | decimal_places=2, max_digits=6 | DecimalField

    
- this model holds the user order history for admin panel
    
<br/>

**OrderItem model**

| Name | Key in db | Validation | Field Type |
--- | --- | --- | ---
Order History | order_history | Order, on_delete=models.CASCADE| ForeignKey
Product | product | "products.Product", on_delete=models.CASCADE | ForeignKey
Quantity| quantity | ----- | IntegerField

<br/>

- this model holds the user order history item form admin panel

# Technologies Used

### Tools
- [Gitpod](https://gitpod.io/) is the IDE used for developing this project. 
- [Travis](https://travis-ci.org/) for continuous integration.
- [AWS S3 Bucket](https://aws.amazon.com/) to store images entered into the database.
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) to enable creation, configuration and management of AWS S3.
- [Coverage](https://coverage.readthedocs.io/en/v4.5.x/) to measure code coverage of python unittests.
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) to style django forms.
- [Django Heroku](https://pypi.org/project/django-heroku/) to improve deployment of django projects on heroku.
- [Django Storages](https://django-storages.readthedocs.io/en/latest/) a collection of custom storage backends with django to work with boto3 and AWS S3.
- [Pillow](https://pillow.readthedocs.io/en/stable/) as python imaging library to aid in processing image files to store in database.
- [PIP](https://pip.pypa.io/en/stable/installing/) for installation of tools needed in this project.
- [GitHub](https://github.com/) to store and share all project code remotely. 
- [Heroku](https://www.heroku.com/) for deployment


### Databases
- [PostgreSQL](https://www.postgresql.org/) for production database, provided by heroku.
- [SQlite3](https://www.sqlite.org/index.html) for development database, provided by django.

### Libraries
- [JQuery](https://jquery.com) to simplify DOM manipulation.
- [Bootstrap](https://www.bootstrapcdn.com/) to simplify the structure of the website and make the website responsive easily.
- [FontAwesome](https://www.bootstrapcdn.com/fontawesome/) to provide icons for The House of Mouse webshop.
- [Google Fonts](https://fonts.google.com/) to style the website fonts.
- [Django](https://www.djangoproject.com/) as python web framework for rapid development and clean design.
- [Stripe](https://stripe.com) as payment platform to validate and accept credit card payments securely.
- [Psycopg2](https://pypi.org/project/psycopg2/) as PostgreSQL database adapter for Python.
- [Gunicorn](https://pypi.org/project/gunicorn/) WSGI HTTP Server for UNIX to aid in deployment of the Django project to heroku.



### Languages
- This project uses:
- HTML
- CSS
- JavaScript
- [Python](https://www.python.org/)

# Testing 

- Testing information can be found in product app in the folder "tests"
    - to run test in desired app write command in CLI:
        - coverage run --source=name of app manage.py test

#### How to run Python tests

To run the existing Python tests:
1. Activate your virtual environment.
2. In the terminal enter the following command:
```
python manage.py test
```
3. If you wish to run the tests within a specific app only you can specify with: 
```
python manage.py test <app name here>
```
4. The test results will be shown within the terminal.

_NOTE: The `python` part of these commands assumes you are working with a windows operating system. Your Python command may differ, such as `python3` or `py`_

### Travis

- [Travis](https://travis-ci.org/) was used throughout the unit testing of this project to provide continuous integration with the deployed site. The [Travis Documentation](https://docs.travis-ci.com/) provides all the info needed to set it up.
- I set the heroku deployment settings for this project to only allow deployment when the travis had passed the latest push to the master branch on GitHub.

## Code Validation

- I used the [W3C HTML Validator tool](https://validator.w3.org/#validate_by_input) to validate my HTML code.
    - The W3C Validator tool doesn't recognize the Jinja templating, which has resulted in it showing a lot of errors in relation to the Jinja code. However, all other code is validating fine.
- I used the [W3C CSS Validator tool](https://jigsaw.w3.org/css-validator/#validate_by_input) to validate my CSS code.
- I used the [Pep8 Online tool](http://pep8online.com/) to validate my Python syntax.
- I used CLI to sort all my imports by using command  "isort -rc ."
- I used CLI to make sure line length is not going above 79 in one line by using command  "black --line-length=79"
- I used CLI to check all the errors in the code by using command  "flake8"
- I also removed some of the remaining errors manually

## Manual Testing

- I used Google Chrome's Development tools to constantly test each change that I<br/> 
made to my project and to ensure that it appeared in the desired way on different screen sizes. <br/>
- I also tested my app on different screen sizes (mobile, tablet and desktop) to ensure <br/>
it appeared in the desired way on different devices.
- [Am I Responsive](http://ami.responsivedesign.is/#) - developer tried to use this website to check responsiveness,
however Django has build in protection that does not allow to do it.

<br/>

## Deployment

### How to run this project locally

To run my code locally, users can download a local copy of my code to their desktop by completing the following steps:

1. Go to [my GitHub repository]https://github.com/MatijaBas/rugby-shop)
2. Click on 'Clone or download' under the repository name.
3. Copy the clone URL for the repository in the 'Clone with HTTPs section'.
4. Open 'Git Bash' in your local IDE.
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, then paste the URL you copied in Step 3:

    ```git clone https://github.com/USERNAME/REPOSITORY```

7. Press `Enter` to complete the process and create your local clone.
8. Complete one of the two below steps in your local workspace to set your own credentials for the environment variables:
    - Enter and save your own credentials in the `.baschrc` file; or
    - Create a `.env,py` file with your own credentials and import this into the `settings.py` file
9. Install the `requirements.txt` file by running the below command in your CLI Terminal:

    ```pip3 install -r requirements.txt```

10. Run one of the following commands in your Terminal to launch the Django project:

    ```python3 manage.py runserver```

11. Click the `http://` link that loads, and the project should load. If it doesn't load when you click the link, copy and paste it into a new browser tab instead.
12. Run the following commands to migrate the database models and create a super user:

    ```
    python3 manage.py makemigrations
    python3 manage.py migrate
    python3 manage.py createsuperuser
    ```

13. In the heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".
14. Set the following config vars in heroku :

<div align="center">
    <img src="https://rugby-shop.s3-eu-west-1.amazonaws.com/static/img/config-vars-heroku.jpg" alt="Rugby Shop configvars" aria-label="RugbyShop" />
</div>

<br/>

Once the migrations are completed and the super user has been created successfully, the site should be running locally.

### Media And Static Folders

During development, my `static` and `media` folders weren't pushed to GitHub only in the early parts of the project.
During the progress developer was instructed to keep them in .gitignore file, as they are hosted in my S3 bucket for 
the live version of the site.


  
To allow you to access all functionality on the site locally, ensure you have created free accounts with the following services:
    - [Stripe](https://dashboard.stripe.com/register)
    - [AWS](https://aws.amazon.com/) and [set up an S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html)
    - [emailjs](https://www.emailjs.com/)

Please click the links above for documentation on how to set these up and retrieve the necessary environment variables.


### In Gitpod you create env.py file in main directory and write in first line: import os. Use table below to copy required fields.

<br/>


| Default quote | Your key | 
--- | --- 
os.environ.setdefault | "AWS_ACCESS_KEY_ID", "access_key_goes_here" | 
os.environ.setdefault | "AWS_SECRET_ACCESS_KEY","secret_access_key_goes_here" |
os.environ.setdefault | "DATABASE_URL", "postgres://your postgres key, you get it from heroku") |
os.environ.setdefault | "EMAIL_ADDRESS","your_mail@gmail.com" | 
os.environ.setdefault | EMAIL_PASSWORD", "your_password" |
os.environ.setdefault | "SECRET_KEY", "secret_key_goes_here" | 
os.environ.setdefault | "STRIPE_PUBLISHABLE", "pk_test_your_key_goes_here" | 
os.environ.setdefault | "STRIPE_SECRET", "sk_test_dtripe_key_goes_here" | 

<br/>

### Repository Link

Click the link below to visit my project's GitHub repository:

[Rugby Shop GitHub Repository](https://github.com/MatijaBas/rugby-shop)

## Heroku Deployment

I used GitHub for my version control and Heroku to host the live version of my project. To deploy my website to Heroku, I used use the following steps:

1. Created the app in Heroku.
2. Went to the **Resources** tab in Heroku and searched for **Heroku Postgres** in the 'Add-Ons' section.
3. Selected the free **Hobby** level.
4. Updated the `.bashrc` file within my local workspace with the `DATABASE_URL` details, and the `settings.py` to connect to the database using the `dj_database_url` package.
5. Ran the `python3 manage.py makemigrations`, `python3 manage.py migrate`, `python3 manage.py createsuperuser` commands to migrate the models into Heroku Postgres and create a new super user in the new PostgreSQL database.
5. Went to the **Settings** tab in Heroku and clicked on the **Reveal Config Vars** button.
6. Copied and paste all of the default variables from env.py  in to Heroku's Config Vars section.

| Default quote | Your key | 
--- | --- 
os.environ.setdefault | "AWS_ACCESS_KEY_ID", "access_key_goes_here" | 
os.environ.setdefault | "AWS_SECRET_ACCESS_KEY","secret_access_key_goes_here" |
os.environ.setdefault | "DATABASE_URL", "postgres://your postgres key, you get it from heroku") |
os.environ.setdefault | "EMAIL_ADDRESS","your_mail@gmail.com" | 
os.environ.setdefault | EMAIL_PASSWORD", "your_password" |
os.environ.setdefault | "SECRET_KEY", "secret_key_goes_here" | 
os.environ.setdefault | "STRIPE_PUBLISHABLE", "pk_test_your_key_goes_here" | 
os.environ.setdefault | "STRIPE_SECRET", "sk_test_dtripe_key_goes_here" | 
 
  
7. Went to the **Deploy** tab in Heroku, connected my app to my GitHub repository and selected **Enable Automatic Deployment** as the deployment method.
8. Went to the **Developers** section in Stripe and clicked on **API Keys**.
9. Copied and pasted the **Publishable Key** and **Secret Key** and set them as the `STRIPE_PUBLISHABLE` and `STRIPE_SECRET` environment variables in the `.bashrc` file within my local workspace.
10. Updated the `settings.py` with the new Stripe environment variables.
11. Went to the **S3** section of AWS and created a new S3 bucket.
12. Updated the `settings.py` file in my local workspace with the relevant S3 bucket details:

    ```
    AWS_S3_OBJECT_PARAMETERS = {
        "Expires": "Thu, 31 Dec 2099 20:00:00 GMT",
        "CacheControl": "max-age=94608000",
    }
    AWS_STORAGE_BUCKET_NAME = "<s3-bucket-name>"
    AWS_S3_REGION_NAME = "<region-name>"
    AWS_ACCESS_KEY_ID = <access-key-id>
    AWS_SECRET_ACCESS_KEY = <secret-access-key>
    AWS_S3_CUSTOM_DOMAIN = "%s.s3.amazonaws.com" % AWS_STORAGE_BUCKET_NAME
    AWS_DEFAULT_ACL = None
    ```
13. Created a `custom_storages.py` file with classes to route to the relevant location settings for static and media files.
14. Updated the `settings.py` file with the relevant configuration for static and media file storage.
15. Ran the `python3 manage.py collectstatic` command to push the static files to my S3 bucket.
16. Created a requirements.txt file using the following command in the terminal window:

    ```pip3 freeze --local > requirements.txt```

17. Created a Procfile using the following command in the terminal window:

    ```web: gunicorn nutristore.wsgi:application> Procfile```

18. Ran the `git add .`, `git commit -m "<commit-message>"` and `git push` commands to push all changes to my GitHub repository.

The app was successfully deployed to Heroku at this stage.

### Live App Link

Click the link below to run my project in the live environment:

[Rugby shop](https://rugby-shop.herokuapp.com/)


# Credits

## Content
- Order Confirmation [Wokiee](https://themeforest.net/item/wokiee-multipurpose-shopify-theme/22559417)
- For the New Collections carousel I´m using a Carousel code snippet example, the third example With Indicators, copied from [MDBootstrap](https://mdbootstrap.com/docs/jquery/javascript/carousel/) and then modified for my own needs.
-  Inspiration was taken from fallowing websites:
    - [Elverys](https://www.elverys.ie/)
    - [SportsDirect.com](https://www.sportsdirect.com/)
    - [WorldRugbyShop](https://www.worldrugbyshop.com/)

## Images
- All product photography was taken from
    - [Elverys](https://www.elverys.ie/)
    - [SportsDirect.com](https://www.sportsdirect.com/)

## Code

- The following youtube video series provided much explanation about the use and operation of Django2
    - [Python Django Web Framework by freeCodeCamp.org](https://www.youtube.com/watch?v=F5mRW0jo-U4)
    - [Python Django Tutorial by Corey Schafer](https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p)

## Text verification

- To check and verify entire vocabulary in Readme.md file developer used  [Spell Checker](https://www.reverso.net/spell-checker/english-spelling-grammar/)

## Acknowledgements

- Special thanks to my mentor Brian Macharia for his time, expertise and friendship through my entire journey through the CodeInstitute full stack web development course.Thank to his incredible knowledge and patience that helped me get so far.

- Thanks to everybody on SLACK that help me when I was stuck and needed assistance. Thanks Tutors aswell. They help me to debug my Python code.

### And finally thanks to my wife and my family,to gave me precious time so I can work on my projects, she is biggest support I can imagine.

# Contact
To contact me feel free to email

 `mbasanov (at) gmail (dot) com`

 ## This project is for educational purposes only.