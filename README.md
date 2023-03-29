# Webster

<h3><a href="https://webster00.herokuapp.com/">Live Site </a></h3>

<img width="800" alt="Screenshot 2023-03-29 at 00 31 35" src="https://user-images.githubusercontent.com/115544231/228381785-761b72f2-8978-43e5-af57-ee935fd4349f.png">



<strong> <h2> Introduction </h2></strong>

Welcome to Webster.

Webster is my fourth and final project, part of the Code Institute, Full Stack Web Developer Course.

The purpose of this project was a build a full-stack site based around a business logic used to control a centrally-owned dataset. The technologies used for this project are HTML, CSS, JavaScript, Python, and Django. Stripe handles online test payments and Heroku Postgres as a relational database.

Webster is a fictional brand, purchases on this project are accepted via Stripes test card details. For further information on which card number you should use, please refer to Stripe's official documentation.

<a href="https://stripe.com/docs/testing">Stripe Test Integration</a>

This project is for educational purposes only, No commercial revenue is generated from this project.  

-----------------------------------------------------------


<strong> <h2> UXD - User Experience Design </h2></strong>

<p>
A large part of the inspiration behind the planning for this project came from Code Institutes teaching course.

By keeping the user in mind throughout the design and development of the project, it would be easier to make the user experience a positive one.

The planning of the project is broken into 5 planes,

- The Strategy Plane
- The Scope Plane
- The Structure Plane
- The Skeleton Plane
- The Surface Plane
</p>

-----------------------------------------------------------

<strong> <h2> The Strategy Plane</h2></strong>
<br>

### Creator Goals
- As a creator, I want the site to be easy to navigate.
- As a creator, I want to allow users to filter through products.
- As a creator, I want to provide users with updates to any actions.
- As a creator, I want to allows admins to Add/Edit/Delete products to/from the store.

<br>

## User Stories

#### Regular Site User Stories
- As a site user, I want the main purpose of the site to be clear so that I can determine if this is the correct site for me.
- As a site user, I want to be able to navigate across the site, so that I can view different pages on the site.
- As a site user, I want to be able to sign up, so that I can have a personal account on the site.
- As a site user, I want to be able to receive an email confirmation after registering, so that I can verify that my account registration was successful.

<br>

<strong><h3>Customer Shopper Stories</h3></strong>



- As a shopper, I want to be to view all products, so that I can decide what I want to buy.
- As a shopper, I want to be able to view products in more detail.
- As a shopper, I want to be able to view reviews left by other customers for products, so that I can understand whether the product is worth purchasing.
- As a shopper, I want to be able to see a confirmation when a product is added to my shopping bag, so that I can avoid accidentally adding multiple quantities of the same item.
- As a shopper, I want to be able to view my bag, so that I can see what is in my bag and adjust quantities

<strong><h3>Customers (Logged in) Stories</h3></strong>
- As a logged-in user, I want to be able to save my details, so that I can avoid retyping my details again.
- As a logged-in user, I want to have my past orders viewable, so that I can verify what my past order was and view the order number.
- As a logged-in user, I want to be able to leave reviews on a product, so that other users may be able to benefit from my opinions on my purchase.
- As a logged-in user, I want to be able to edit my reviews, so that I can amend any errors or in case I change my opinion.
- As a logged-in user, I want to be able to add products to my wishlist, so that I can view those products later.
- As a logged-in user, I was to be able to remove products from my wishlist, so that my wishlist is only full of products I want to be saved.


My user stories were obtained by doing research into other stores and seeing how their sites ran. Harry my mentor in particular helped me to gauge what I would need to implement and what potentially could be left out or moved into a phase for later deployment.

-----------------------------------------------------------

<strong> <h2> The Scope Plane </h2></strong>

The features that I had thought about before designing the project and my deadline was not achievable. I opted for a phased release approach.

I was able to ascertain which features were more important and should be working on my initial deployment, and which features I could add later.

My plan for a phased deployment,

<strong><h3>Phase 1</strong></h3>

A project that would satisfy my user stories.
Home Page with an introduction
Navbar allowing the user to navigate to different pages
Products page allowing users to view all products.
A product detail page.
E-commerce functionality allowing the user to make purchases.

<strong><h3>Phase 2</strong></h3>

Building upon the Phase 1 project with additional features.
A functional blog app that allows admins to post blogs.
Allow users the filter blog types.
Allow users to post comments on the blogs.

<strong><h3>Phase 3</strong></h3>

My final planned phase would focus on user feedback
Review feedback gathered to understand what can be improved.

-----------------------------------------------------------

<strong> <h2> The Structure Plane </h2></strong>

<strong>Key Models</strong>

<br>

<strong>UserProfile</strong>

- The user profile is connected to the User model created by Allauth on registration.
- The default fields are saved fields by the user to speed up the checkout process by pre-populating shipping details.

<strong>Order</strong>

- The order model is connected to the User Profile, allows the user to view their previous orders.

<strong>Product</strong>

- The product model holds key information for each product. Each product has a unique ID.
- The product model is connected to the category model, this allows the user to filter products by category.

<strong>ProductReview</strong>

- Reviews for products can be left for products with this model, having it connect to the Product model via the ID.
- The review model also is connected to the User model to obtain the user's username. This allows the user to see the name of the user on each review.
WishList

<strong>WishList</strong>

- The wishlist model allows users to save items for quicker access. These items can be removed.
- This model also acts as a container for the WishListItem model. Just like the Order model, each wishlist is unique to each user but connecting to the user ID.


<strong> <h2> The Surface Plane </h2></strong>

## Features

### Navigation Bar

- Navbar is implemented on every page and is fully responsive across all resolutions.
- Users can navigate across the site freely.
- Users shopping have the cost of the current shopping basket displayed.

<img width="800" alt="Screenshot 2023-03-29 at 00 36 45" src="https://user-images.githubusercontent.com/115544231/228382156-7d49a31d-2afe-47a3-a860-e2e6c3821d00.png">


### Home page

- Home page features a short text that encourages them to start shopping, and a button to the products page.

<img width="1439" alt="Screenshot 2023-03-29 at 00 37 33" src="https://user-images.githubusercontent.com/115544231/228382258-d9109290-f1c7-41d6-a38e-703ff537f666.png">


### Products Page
- Store page offer products on large resolutions in a row of four. Images are large to attract the user's attention, and clicking the image will redirect the user to the product detail page.

<img width="800" alt="Screenshot 2023-03-29 at 00 38 26" src="https://user-images.githubusercontent.com/115544231/228382351-b269ec94-bfcc-430f-9a6f-93c7585cc8b8.png">


### Search Functionality

- Users can take advantage of the search function within the navigation bar to search for products or descriptions.
- Search results are shown in a simple format with a link to redirect to the general store page.

<img width="400" alt="Screenshot 2023-03-29 at 00 39 17" src="https://user-images.githubusercontent.com/115544231/228382483-3d0e5b07-d450-40d1-bdb0-0be7c532d817.png">


### Reviews

- Users can choose to view the reviews left by users for a specific product.
- Logged-in users can post a review, whereas users not logged in are shown a small message to log in to leave a product review.
- User choosing the leave a review can choose to pick a title, give a star rating out of five, and write a review.

<img width="800" alt="Screenshot 2023-03-29 at 00 41 38" src="https://user-images.githubusercontent.com/115544231/228382897-d5ae4fd7-93e4-4e9d-811b-b7b785a695ef.png">


### Toasts

- Almost all actions provide feedback to the user via the bootstrap toasts written to provide user feedback.
- Users shopping can view the current items within the bag and total cost.
- At the bottom of the toast is a link to the checkout page.

<img width="400" alt="Screenshot 2023-03-29 at 00 42 53" src="https://user-images.githubusercontent.com/115544231/228383245-74728365-cd30-497c-9e39-4344a7f5bc40.png">


### Shopping Bag

- The shopping bag page is fully responsive, showing users a picture of the item, name, price per unit, and total price.
- Users can also choose to increase/decrease the number of items in their bag, click the update button to have the prices update.
- Users can click the remove link and have all the items within the bag removed, regardless of quantity.
- At the bottom of the page user can find the cost of the bag, cost of delivery, the total and how much they must spend to be eligible for free delivery.

<img width="800" alt="Screenshot 2023-03-29 at 00 43 28" src="https://user-images.githubusercontent.com/115544231/228383325-b51f0703-69da-425a-aefb-c689ee36cdbf.png">


### Checkout Overlay

- Users who checkout will see a simple overlay with a spinning icon while the payment is processed.

<img width="800" alt="Screenshot 2023-03-29 at 00 44 13" src="https://user-images.githubusercontent.com/115544231/228383458-2bf0ce82-25c3-45a9-867f-52515fc18b11.png">


### Footer

- Almost every page throughout the project has a footer with social media links.
- Clicking the social media like redirect the user to the social media page in a new tab, so as not to disrupt the user experience.
- The footer also contains a link to a contact form so that the user can reach out to us.
- On the footer there is also a Mail Chimp newsletter subscription field, that lets the user enter their email to subscribe to our weekly newsletter. 

<img width="800" alt="Screenshot 2023-03-29 at 00 46 19" src="https://user-images.githubusercontent.com/115544231/228383710-f724d051-a391-4bac-a5dd-d245fd45771d.png">


### Wishlist 

- The user has the option to add a product to Add a product to their wishlist.
- On the wishlist page the user can see what products they have added to it, along with removing items from the wishlist.
- If the wishlist is empty the page displays a block of text letting the user know that the wishlist is empty.

<img>

### My profile

- The user can navigate to 'My Profile' page through the navigation bar where they can see their default delivery information.
- The 'My Profile' page also shows the privous orders the user has purchased along with the order number od that order. 

<img width="800" alt="Screenshot 2023-03-29 at 00 48 25" src="https://user-images.githubusercontent.com/115544231/228384003-413e08a9-a320-4eca-bac3-1f7c161ba5a7.png">


### Contact Form

- On the contact form the user has the option to write us a message by entering some rwquired fields and sending it to us.
- After submitting a message the user is redriceted to a successs and sees a message on the screen that we have reccived the message.
- The Contact page also includes a button that takes the user back to the home page for a better user experiance.

<img width="650" alt="Screenshot 2023-03-29 at 00 49 15" src="https://user-images.githubusercontent.com/115544231/228384114-c1a3182d-de37-4876-b0a5-23dc9191605e.png">


### Admin Page

- If the user is a superuser, he/she has the option to view the Admin page.
- On the Admin page the user add products to the store.

<img width="800" alt="Screenshot 2023-03-29 at 00 50 20" src="https://user-images.githubusercontent.com/115544231/228384248-b62ad541-40c3-4186-a8ed-dab98243fe53.png">



### Checkout Success

- After the user made a purchase, he/she is redirected to a checkout success page. The page shows the orders the user has made, along with the ordernumber and other usful information

<img width="800" alt="Screenshot 2023-03-29 at 00 45 19" src="https://user-images.githubusercontent.com/115544231/228384452-72bd929a-6039-4da8-a908-e7a0378c7f57.png">


-----------------------------------------------------------

<strong> <h2> Marketing  </h2></strong>

<br>

<strong> <h3> Plan  </h3></strong>

Webster is a business to customer e-commerce platform, built and designed to sell products to the user. Before beginning this project I wrote a marketing plan which can be found here:
<img width="619" alt="Screenshot 2023-03-29 at 15 25 43" src="https://user-images.githubusercontent.com/115544231/228552643-4094d172-5a5f-4601-9ae4-6d9aa0e098f5.png">
 Marketing Strategy

<br>

To further enhance sales there is also a heiwa gallery Facebook page, that will display information about new exhibitions or prints that are for sale:

<img width="319" alt="Screenshot 2023-03-13 at 18 45 44" src="https://user-images.githubusercontent.com/115544231/228543689-67607bc2-fcb4-47c5-8cf3-8481f7ce64c3.png">

<br>

Users are also able to subscribe to receive the gallery's newsletter, using the MailChimp form found in the footer.

<img width="464" alt="Screenshot 2023-03-29 at 15 03 10" src="https://user-images.githubusercontent.com/115544231/228543965-3322106f-993d-4d0d-9e6f-fc8ebe914dfb.png">

<br>

<strong> <h3> SEO's  </h3></strong>

I conducted SEO research to decide on the keywords and phrases that would be used across the website, I wrote a list of as many words and phrases I could think of and then using Google, I searched by these keywords to see the sort of websites that were returned.

<img width="800" alt="Screenshot 2023-03-29 at 15 07 31" src="https://user-images.githubusercontent.com/115544231/228545120-35528649-fbef-4e92-ae51-9d244d7dadf8.png">

<br>


-----------------------------------------------------------

<strong> <h2> Technologies Used </h2></strong>

- <a href="https://www.python.org/"> Python</a>
-  The following Python modules were used on this project,
- - asgiref==3.6.0
- - boto3==1.26.96
- - botocore==1.29.96
- - dj-database-url==0.5.0
- - Django==3.2
- - django-allauth==0.41.0
- - django-countries==7.2.1
- - django-crispy-forms==1.14.0
- - django-storages==1.13.2
- - gunicorn==20.1.0
- - jmespath==1.0.1
- - oauthlib==3.2.2
- - Pillow==9.4.0
- - psycopg2==2.9.5
- - python3-openid==3.2.0
- - pytz==2022.7.1
- - requests-oauthlib==1.3.1
- - s3transfer==0.6.0
- - sqlparse==0.4.3
- - stripe==5.2.0

- <a href="https://www.heroku.com/home">Heroku</a>
- <a href="https://aws.amazon.com/"> AWS S3</a>
- <a href="https://developer.mozilla.org/en-US/docs/Web/HTML"> HTML</a>
- <a href="https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics">CSS </a>
- <a href="https://getbootstrap.com/"> Bootstrap</a>
- <a href="https://jquery.com/"> jQuery</a>
- <a href="https://www.javascript.com/"> JavaScript</a>
- <a href="https://fonts.google.com/"> Google Fonts</a>
- <a href="https://fontawesome.com/"> Font Awesome</a>
- <a href="https://developer.chrome.com/docs/devtools/"> Google Developer Tools</a>
- <a href="https://github.com/"> Github</a>
- <a href="https://git-scm.com/"> Git </a>
- <a href="https://www.gitpod.io/"> Gitpod</a>
- <a href="https://app.grammarly.com/"> Grammerly </a>
- <a href="https://validator.w3.org/"> W3C Markup Validation</a>
- <a href=""> </a>


-----------------------------------------------------------

<strong> <h2> Testing </h2></strong>

I have made use of automated testing to ensure the website's functionality meets the desired intent.

<br>

<strong> <h3> Code Validation </h3></strong>

<br>

All of my code has been validated using an online validator specific to the language, all code now passes with zero errors.

- <a href="https://validator.w3.org/">W3C Markup Validation Services</a>
- - Used to validate all HTML code written and used in this webpage.

<img width="800" alt="Screenshot 2023-03-29 at 16 36 29" src="https://user-images.githubusercontent.com/115544231/228681261-ec9ea018-0901-4a7b-8882-68bca693b6c8.png">

- <a href="https://jigsaw.w3.org/css-validator/#validate_by_input">W3C CSS Validation Services</a>
- - Used to validate all CSS code written and used in this webpage.

<img width="800" alt="Screenshot 2023-03-29 at 16 35 58" src="https://user-images.githubusercontent.com/115544231/228681498-c19e740e-c600-48a1-9e7d-305ff536b2b2.png">

- <a href="http://ww1.pep8online.com/">Pep8</a>

- - Used to test my Python code for any issues or errors.






-----------------------------------------------------------

<strong> <h2> Deployment </h2></strong>

The main branch of this repository is the most current version and has been used for the deployed version of the site.

The Code Institiue student template was used to create this project.

<a href="https://github.com/Code-Institute-Org/gitpod-full-template">Code Institute Full Template</a>

- Click the Use This Template button.
- Give your repository a name, and description if you wish.
- Click the Create Repository from Template to create your repository.
- Click the Gitpod button to create a gitpod workspace, this can take a few minutes.
- When working on project using Gitpod, please open the workspace from Gitpod, this will open your previous workspace rather than creating a new one. Use the following commands to commit your work,
- git add . - adds all modified files to a staging area.
- git commit -m "A short message exlaining your commit - commits all changes to a local repository.
- git push - pushes all your commited changes to your Github repository.

<br>

<strong> <h3> Requirements </h3></strong>

- Python 3
- Pip
- Git
- AWS S3


<strong> <h3> Heroku Deployment </h3></strong>
<br>

1. Log into Heroku
2. Create a new app, choose a location closest to you
3. Search for Heroku Postgres from the resources tab and add to your project
4. Make sure to have dj_database_url and psycopg2 installed.
```
pip3 install dj_database_url
pip3 install psycopg2
```

5. Login to the Heroku CLI - heroku login -i
6. Run migrations on Heroku Postgres - heroku run python manage.py migrate
7. Create a superuser - python manage.py createsuperuser
8. Install gunicorn - pip3 install gunicorn
9. Create a requirements.txt file - pip3 freeze > requirements.txt
10. Create a Procfile (note the capital P), and add the following,
```
web: gunicorn project_name.wsgi:application
```
11. Disable Heroku from collecting static files - heroku config:set DISABLE_COLLECTSTATIC=1 --app <your-app-name>
12. Add the hostname to project settings.py file
```
ALLOWED_HOSTS = ['<you-app-name>.herokuapp.com', 'localhost']
```

13. Connect Heroku to you Github, by selecting Github as the deployment method and search for the github repository and pressing connect
14. In Heroku, within settings, under config vars select Reveal config vars
15. Add the following,
```
AWS_ACCESS_KEY_ID =	<your variable here>
AWS_SECRET_ACCESS_KEY =	<your variable here>
DATABASE_URL =	<added by Heroku when Postgres installed>
DISABLE_COLLECTSTATIC =	1 
EMAIL_HOST_PASS = <your variable here>
EMAIL_HOST_USER = <your variable here>
SECRET_KEY = <your variable here>
STRIPE_PUBLIC_KEY = <your variable here>
STRIPE_SECRET_KEY = <your variable here>
STRIPE_WH_SECRET = <different from env.py>
USE_AWS = True
```

16. Go back to the Deploy tab and under Automatic deploys choose Enable Automatic Deploys
17. Back in your CLI add, commit and push your changes and Heroku will automatically deploy your app:
```
git add .
git commit -m "Initial commit"
git push
```
18. Your deployed site can be launched by clicking Open App from its page within Heroku.
<br>
<strong> <h3> AWS S3 Bucket setup </h3></strong>


1. Create an Amazon AWS account
2. Search for S3 and create a new bucket
3. Allow public access
4. Under Properties > Static website hosting
- - Enable
- - index.html as index.html
- - save
- - Under Permissions > CORS use the following:
```
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
```
5. Under Permissions > Bucket Policy:
- - Generate Bucket Policy and take note of Bucket ARN
- - Chose S3 Bucket Policy as Type of Policy
- - For Principal, enter *
- - Enter ARN noted above
- - Add Statement
- - Generate Policy
- - Copy Policy JSON Document
- - Paste policy into Edit Bucket policy on the previous tab
- - Save changes
6. Under Access Control List (ACL):
- - For Everyone (public access), tick List
- - Accept that everyone in the world may access the Bucket
- - Save changes
<br>

<strong> <h3> AWS IAM (Identity and Access Management) setup </h3></strong>


1. From the IAM dashboard within AWS, select User Groups:
- - Create a new group
- - Click through and Create Group
2. Select Policies:
- - Create policy
- - Under JSON tab, click Import managed policy
- - Choose AmazongS3FullAccess
- - Edit the resource to include the Bucket ARN noted earlier when creating the Bucket Policy
- - Click next step and go to Review policy
- - Give the policy a name and description of your choice
- - Create policy
3. Go back to User Groups and choose the group created earlier
- - Under Permissions > Add permissions, choose Attach Policies and select the one just created
- - Add permissions
4. Under Users:
- - Choose a user name
- - Select Programmatic access as the Access type
- - Click Next
- - Add the user to the Group just created
- - Click Next and Create User
5. Download the .csv containing the access key and secret access key.
<br>

<strong> <h3> Connecting Heroku to AWS S3 </h3></strong>

1. Install boto3 and django-storages
```
pip3 install boto3
pip3 install django-storages
pip3 freeze > requirements.txt
```
2. Add the values from the .csv you downloaded to your Heroku Config Vars under Settings:
3. Delete the DISABLE_COLLECTSTATIC variable from your Cvars and deploy your Heroku app
4. With your S3 bucket now set up, you can create a new folder called media (at the same level as the newly added static folder) and upload any required media files to it.
- - PLEASE MAKE SURE media AND static FILES ARE PUBLICLY ACCESSIBLE UNDER PERMISSIONS
-----------------------------------------------------------
<strong> <h2> Credits </h2></strong>
<br>
<strong> <h3> Product Images / Names / Descriptions </h3></strong>
<br>

- All the content relating to the products all came from the Casall website. Although the images were altered the original images were screen shots taken from items from there.
- <a href="https://www.casall.com/en-eu/searchresults?q=KETTLEBELL">Casall</a>
- - This project is made solely for educational purposes. There is no financial gain from the project.

<br>
<strong> <h3> Code </h3></strong>

- A large amount of code came from the Code Institute, Boutique Ado Project.
- <a href="https://boutique-ado0413.herokuapp.com/">Code Institute, Boutique Ado</a>
- - Boutique Ado is a walkthrough project by Code Institute, this project gave students an introduction to Django/AWS S3/Stripe/Heroku Postgres
- - The core functionality of Nourish and Lift is all taken from the Boutique Ado project.

<br>
<strong> <h3> Bootstrap </h3></strong>

- The Bootstrap Library was used through the project. The project used version 4.6.
- <a href="https://getbootstrap.com/">Bootstrap </a>
- - Toasts/Navigation Bar/Forms/Dropdown Menu/Buttons, the core elements mentioned are all found in the Bootstrap components section and built upon.


<br>
<strong> <h3> Django Documentation </h3></strong>

- Django have amazing documentation with a tutorial project and in depth explanations on core components.
- <a href="https://docs.djangoproject.com/en/3.2/"> Django Documentation </a>

<br>
<strong> <h2> Aknowledgements </h2></strong>
<br>
<strong> <h3> Harry Dhillon </h3></strong>

- My mentor thorught the entire program.
- - He has been a huge help and support throughout this project, not only to me but to countless other students. Takes time out of his day to help and respond to messages and has always been extremely courteous and respectful.


<br>
<strong> <h3> Code Institue Tutors </h3></strong>

- Course Tutors
- - The tutors at code institute has been a major help, guiding me through torubles and always beeing there to ask sometimes silly questions with a great attitude. Without them i would have had a much more difficult time. Thank you!

Finally thank you for viewing this project. I hope whoever you are, that you are in good health and doing well. God Bless!










