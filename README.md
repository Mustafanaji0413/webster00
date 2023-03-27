# Webster

<h3><a href="https://webster00.herokuapp.com/">Live Site </a></h3>

<img> Image



## Introduction

<p>
Welcome to Lifty.

Lifty is my fourth and final project, part of the Code Institute, Full Stack Web Developer Course.

The purpose of this project was a build a full-stack site based around a business logic used to control a centrally-owned dataset. The technologies used for this project are HTML, CSS, JavaScript, Python, and Django. Stripe handles online test payments and Heroku Postgres as a relational database.

Lifty is a fictional brand, purchases on this project are accepted via Stripes test card details. For further information on which card number you should use, please refer to Stripe's official documentation.

<a href="https://stripe.com/docs/testing">Stripe Test Integration</a>

This project is for educational purposes only, No commercial revenue is generated from this project.
</p>

## UXD - User Experience Design

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

## The Strategy Plane
### Creator Goals
- As a creator, I want the site to be easy to navigate.
- As a creator, I want to allow users to filter through products.
- As a creator, I want to provide users with updates to any actions.
- As a creator, I want to allows admins to Add/Edit/Delete products to/from the store.
### User Stories
#### Regular Site User Stories
- As a site user, I want the main purpose of the site to be clear so that I can determine if this is the correct site for me.
- As a site user, I want to be able to navigate across the site, so that I can view different pages on the site.
- As a site user, I want to be able to sign up, so that I can have a personal account on the site.
- As a site user, I want to be able to receive an email confirmation after registering, so that I can verify that my account registration was successful.
#### Customer Shopper Stories
- As a shopper, I want to be to view all products, so that I can decide what I want to buy.
- As a shopper, I want to be able to view products in more detail.
- As a shopper, I want to be able to view reviews left by other customers for products, so that I can understand whether the product is worth purchasing.
- As a shopper, I want to be able to see a confirmation when a product is added to my shopping bag, so that I can avoid accidentally adding multiple quantities of the same item.
- As a shopper, I want to be able to view my bag, so that I can see what is in my bag and adjust quantities
#### Customers (Logged in) Stories
- As a logged-in user, I want to be able to save my details, so that I can avoid retyping my details again.
- As a logged-in user, I want to have my past orders viewable, so that I can verify what my past order was and view the order number.
- As a logged-in user, I want to be able to leave reviews on a product, so that other users may be able to benefit from my opinions on my purchase.
- As a logged-in user, I want to be able to edit my reviews, so that I can amend any errors or in case I change my opinion.
- As a logged-in user, I want to be able to add products to my wishlist, so that I can view those products later.
- As a logged-in user, I was to be able to remove products from my wishlist, so that my wishlist is only full of products I want to be saved.


My user stories were obtained by doing research into other stores and seeing how their sites ran. Harry my mentor in particular helped me to gauge what I would need to implement and what potentially could be left out or moved into a phase for later deployment.


## The Scope Plane

The features that I had thought about before designing the project and my deadline was not achievable. I opted for a phased release approach.

I was able to ascertain which features were more important and should be working on my initial deployment, and which features I could add later.

My plan for a phased deployment,

<strong>Phase 1</strong>

A project that would satisfy my user stories.
Home Page with an introduction
Navbar allowing the user to navigate to different pages
Products page allowing users to view all products.
A product detail page.
E-commerce functionality allowing the user to make purchases.

<strong>Phase 2</strong>

Building upon the Phase 1 project with additional features.
A functional blog app that allows admins to post blogs.
Allow users the filter blog types.
Allow users to post comments on the blogs.

<strong>Phase 3</strong>

My final planned phase would focus on user feedback
Review feedback gathered to understand what can be improved.

## The Structure Plane

##### Key Models

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

- The wishlist model allows users to save items for quicker access. These items can be removed.
This model also acts as a container for the WishListItem model. Just like the Order model, each wishlist is unique to each user but connecting to the user ID.


# The Surface Plane

## Features

### Navigation Bar

- Navbar is implemented on every page and is fully responsive across all resolutions.
- Users can navigate across the site freely.
- Users shopping have the cost of the current shopping basket displayed.

<img>

### Home page

- Home page features a short text that encourages them to start shopping, and a button to the products page.

<img>

### Products Page
- Store page offer products on large resolutions in a row of four. Images are large to attract the user's attention, and clicking the image will redirect the user to the product detail page.

<img>

### Search Functionality

- Users can take advantage of the search function within the navigation bar to search for products or descriptions.
- Search results are shown in a simple format with a link to redirect to the general store page.

<img>

### Reviews

- Users can choose to view the reviews left by users for a specific product.
- Logged-in users can post a review, whereas users not logged in are shown a small message to log in to leave a product review.
- User choosing the leave a review can choose to pick a title, give a star rating out of five, and write a review.

<img>

### Toasts

- Almost all actions provide feedback to the user via the bootstrap toasts written to provide user feedback.
- Users shopping can view the current items within the bag and total cost.
- At the bottom of the toast is a link to the checkout page.

<img>

### Shopping Bag

- The shopping bag page is fully responsive, showing users a picture of the item, name, price per unit, and total price.
- Users can also choose to increase/decrease the number of items in their bag, click the update button to have the prices update.
- Users can click the remove link and have all the items within the bag removed, regardless of quantity.
- At the bottom of the page user can find the cost of the bag, cost of delivery, the total and how much they must spend to be eligible for free delivery.

<img>

### Checkout Overlay

- Users who checkout will see a simple overlay with a spinning icon while the payment is processed.

<img>

### Social Media Links

- Almost every page throughout the project has a footer with social media links.
- Clicking the social media like redirect the user to the social media page in a new tab, so as not to disrupt the user experience.

<img>

### Wishlist 
