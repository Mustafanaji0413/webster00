# Webster

<h3><a href="https://webster00.herokuapp.com/">Live Site </a></h3>

<img width="800" alt="Screenshot 2023-03-29 at 00 31 35" src="https://user-images.githubusercontent.com/115544231/228381785-761b72f2-8978-43e5-af57-ee935fd4349f.png">



<strong> <h2> Introduction </h2></strong>

Welcome to Webster.

Webster is my fourth and final project, part of the Code Institute, Full Stack Web Developer Course.

The purpose of this project was a build a full-stack site based around a business logic used to control a centrally-owned dataset. The technologies used for this project are HTML, CSS, JavaScript, Python, and Django. Stripe handles online test payments and Heroku Postgres as a relational database.

Lifty is a fictional brand, purchases on this project are accepted via Stripes test card details. For further information on which card number you should use, please refer to Stripe's official documentation.

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
