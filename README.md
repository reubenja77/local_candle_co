# local_candle_co
Hand-poured scented candles. Small batch. Delivered.

## Table of Contents

- [Introduction](#introduction)
- [Business Model](#business-model)
  - [Business Type](#business-type)
  - [Revenue Model](#revenue-model)
  - [Customer Segment](#customer-segment)
  - [Value Proposition](#value-proposition)
  - [Customer Acquisition](#customer-acquisition)
  - [Reason for Authentication](#reason-for-authentication)
- [UX Design](#ux-design)
  - [Project Goals](#project-goals)
  - [Target Audience](#target-audience)
  - [User Stories](#user-stories)
  - [Wireframes](#wireframes)
  - [Entity Relationship Diagram (ERD)](#entity-relationship-diagram-erd)
  - [Design Choices](#design-choices)
- [Features](#features)
  - [Implemented Features](#implemented-features)
  - [Future Features](#future-features)
- [Technologies Used](#technologies-used)
  - [Backend](#backend)
  - [Frontend](#frontend)
  - [Payments](#payments)
  - [Hosting](#hosting)
- [SEO Implementation](#seo-implementation)
- [Testing](#testing)
- [Code Validation (PEP8)](#code-validation-pep8)
- [Deployment](#deployment)
- [Credits](#credits)

---

## Introduction

Local Candle Co is a fully functional e-commerce application built using Django, featuring product browsing, cart management, checkout and payment processing using Stripe, user authentication with Django-Allauth, wishlist functionality, newsletter signup, FAQ management, and a contact system.

This project is my Portfolio Project for the E-Commerce Applications module. It demonstrates a full-stack cloud-hosted online store with marketing tools, SEO, UX design, and secure authentication.

![Responsiveness](static/images/ami-response.png) 

💻 [Visit live website](https://local-candle-co-8ac3df963878.herokuapp.com/)  
(Ctrl + click to open in new tab)

---

## Business Model

Local Candle Co follows a straightforward e-commerce business model, focusing on single-purchase retail through a product catalogue.

### Business Type

B2C (Business to Consumer) retail of scented candles.

### Revenue Model
- Direct product sales through a checkout system powered by Stripe.
- No subscriptions or recurring payments.
- Newsletter allows for future promotions and product launches.

### Customer Segment
- Home décor enthusiasts
- Gift buyers
- Candle lovers who prefer artisanal, hand-poured products
- Customers seeking locally sourced candles

### Value Proposition
- Hand-crafted, small-batch candles
- Simple, fast checkout
- Quality scents
- Fast delivery
- Easy communication through built-in contact form

### Customer Acquisition
- SEO
- Newsletter signups
- Facebook business page mockup (marketing presence)
- Clean UX design that reduces friction in browsing and purchasing

### Reason for Authentication
Users create accounts to:
- Save wishlist items
- View previous orders in My Orders (order history)
- Save contact details for future purchases

---

## UX Design
### Project Goals
- Provide a simple, beautiful candle store
- Let users browse and purchase easily
- Allow admin to manage catalogue, orders, FAQs, and contact messages
- Include marketing features (newsletter, SEO, mock Facebook page)
- Provide accessible UX with clean navigation and messaging
- Post-purchase user experience is enhanced through a dedicated “My Orders” page, allowing users to view their completed purchases at any time.

### Target Audience
- Adults aged 20–50
- Online shoppers looking for décor items
- Gift buyers

### User Stories
#### MUST-HAVES:
- Browse all available candles
- View product detail
- Add candle to cart
- View cart and checkout securely
- Admin can manage products
- Admin can manage orders
- User registration, login & logout
- Wishlist items
- Order history
- Newsletter signup
- Contact the store
- View FAQs

![kanban board](static/images/kanban-01.png)
![kanban board](static/images/kanban-02.png)

### Wireframes
####  Home / Product list  
![home](static/images/landing-wireframe.jpg)
####  Product detail
![product](static/images/product-details-wireframe.jpg)  
#### Cart
![cart](static/images/cart-wireframe.jpg)  
####  Checkout
![chekout](static/images/checkout-wireframe.jpg)  
####  Contact Us
![contact](static/images/contact-wireframe.jpg)

### Entity Relationship Diagram (ERD)
![ERD diagram](static/images/wireframe-erd.png)

### Design Choices

The visual design of Local Candle Co was intentionally kept minimal and elegant to reflect a premium, handcrafted product. A neutral colour palette consisting of warm creams, soft browns, and charcoal tones was chosen to complement candle imagery and avoid visual clutter. Bootstrap was used to ensure consistent spacing, alignment, and responsive behaviour across devices, allowing the layout to scale cleanly from mobile to desktop.

Typography combines clean sans-serif fonts for readability with subtle serif accents for headings to convey warmth and craftsmanship. Whitespace was used deliberately to reduce cognitive load and guide the user’s focus toward products and calls to action. Navigation was kept shallow, with key pages accessible within one or two clicks, improving usability and supporting conversion-focused user journeys.

---

## Features
### Implemented Features
- Browse products
- Product detail pages
- Wishlist
- Session-based cart
- Checkout with Stripe
- Order creation
- Contact form
- Newsletter signup
- FAQ page
- Admin management for products, reviews, FAQs, contacts, orders
- Order history (My Orders) page allowing authenticated users to view previous purchases
- SEO (meta tags, robots.txt, sitemap.xml)
- Custom error pages (404, 500)
- Mock Facebook Business Page

### Order History (User Profile)

Authenticated users have access to a **My Orders** page, where all completed purchases are displayed in chronological order. Each order entry includes the order number, date and time placed, total amount, and payment status. This provides users with clear post-purchase feedback and allows them to reference previous orders at any time after checkout.

This feature directly addresses the requirement for persistent order references following successful transactions, ensuring users are not solely reliant on confirmation emails.

#### Order History Interface

The screenshot below shows the user-facing order history page displaying completed purchases for an authenticated user.

![Order history page](static/images/orders-history.webp)


### Future Features
- Product reviews
- Coupon codes
- Delivery tracking
- Product categories

---

## Technologies Used
### Backend:
- Python
- Django
- Django Allauth (authentication)
- Django Sitemaps

### Frontend
- Bootstrap 5
- HTML5, 
- CSS3

### Payments
- Stripe PaymentIntent API

### Hosting
- Heroku
- Gunicorn
- Whitenoise

---

## SEO Implementation
The application includes a dynamically generated sitemap and robots.txt file.
These reference the deployed production URL and ensure proper indexing by search engines.
- `robots.txt`
- `sitemap.xml`
- Meta description tags on key pages
- Friendly URLs
- Human-readable page titles
- Internal linking via navbar and footer
- No lorem ipsum
- 404 and 500 pages with correct responses

### Sitemap & Robots Fix (Resubmission Update)

As part of assessor feedback, the sitemap implementation was expanded to include **all relevant site routes**, not only product pages. The sitemap now aggregates multiple sitemap classes covering core site pages, marketing pages (FAQ and Contact), authentication pages (Login and Signup), and active product detail pages. The `robots.txt` file was updated to dynamically reference the live sitemap URL using Django URL reversing, ensuring accurate indexing in production. This results in complete crawl coverage and aligns with real-world SEO best practices.

#### Robots.txt:
![robots.txt](static/images/robots.webp)

#### Sitemap:
![sitemap](static/images/sitemaps.webp)

---

## Marketing

### Mock Facebook Business Page

A **Mock Facebook Business Page** was created for Local Candle Co. This demonstrates how the brand would be promoted on social media to attract customers, build trust, and support product sales.

This page is **unpublished** and used solely for academic assessment. It visually represents how Local Candle Co would establish an online marketing presence.

#### Purpose of the Mock Facebook Page
- Showcase brand identity through consistent visuals  
- Demonstrate a real-world marketing channel for customer acquisition  
- Provide a location for users to “follow” for updates and specials  
- Align with portfolio expectations for demonstrating marketing methodology  
- Reinforce credibility beyond the website  

#### Page Includes:
- Cover photo featuring product imagery  
- Profile picture of candle product  
- Bio describing the brand  
- Contact information  
- Sample promotional post linking to the live Heroku deployment  
- Featured photos  
- Location and business category  
- Embedded post preview  

#### Screenshot of Mock Facebook Page

Below is the full screenshot of the unpublished page:

![Mock Facebook Page](static/images/fb-page.png)

> **Note:** This screenshot is stored in the repository here:  
`static/images/fb-page.png`

---

## Testing

A full detailed testing document is available here:

🔗 **[View Full Testing Document](TESTING.md)**

---

## Deployment

### Run locally
1. Clone the repository.
2. Create and activate a virtual environment.
3. Install dependencies:
   - `pip install -r requirements.txt`
4. Create an `.env` file (do not commit it) and add required variables (example):
   - `SECRET_KEY`
   - `DEBUG=True`
   - Stripe keys (if testing payments)
5. Run migrations:
   - `python manage.py migrate`
6. Create a superuser (optional):
   - `python manage.py createsuperuser`
7. Start the server:
   - `python manage.py runserver`

### Heroku deployment
1. Create a new Heroku app.
2. In **Heroku Config Vars**, set:
   - `SECRET_KEY`
   - `DEBUG=False`
   - `DATABASE_URL` (automatically added if using Heroku Postgres)
   - `STRIPE_PUBLIC_KEY`
   - `STRIPE_SECRET_KEY`
   - Email settings (production SMTP): `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`, `EMAIL_USE_TLS`, `DEFAULT_FROM_EMAIL`
3. In Heroku **Buildpacks**, add:
   - `heroku/python`
4. Connect Heroku to the GitHub repository and deploy from the `main` branch.
5. Run migrations on Heroku:
   - `heroku run python manage.py migrate`
6. Confirm the deployed site loads and key flows work (login, checkout, email confirmation, order history).


## Credits
### Reference Material & Learning Resources

The following websites were used throughout development for guidance,
documentation, and best practices:

- **Django Documentation**  
  https://docs.djangoproject.com/  
  Official documentation used for models, forms, admin, URL routing,
  static files, and deployment settings.

- **Stripe Documentation**  
  https://stripe.com/docs  
  Used for implementing PaymentIntent, client secret handling,
  and understanding the checkout flow.

- **Bootstrap 5 Documentation**  
  https://getbootstrap.com/docs/5.0/getting-started/introduction/  
  For layout grids, utilities, spacing, and responsive components.

- **W3Schools**  
  https://www.w3schools.com/  
  General HTML, CSS, and JavaScript references.

- **MDN Web Docs (Mozilla Developer Network)**  
  https://developer.mozilla.org/  
  For CSS behaviour, accessibility, ARIA attributes, and semantic HTML.

- **Code Institute Course Material**  
  Django and Stripe lessons from the *Boutique Ado* walkthrough provided structural guidance, best practices,
  and deployment patterns.

- **Django-Allauth Documentation**  
  https://django-allauth.readthedocs.io/  
  For login, logout, registration, email fields, and templates.

- **Code Institute**  
  Code structure inspired by Boutique Ado walkthrough project

### Media
#### Product images:
- **Unsplash**  
  https://unsplash.com/  
  Source of product placeholder photos (free commercial use license).

- **Pexels**  
  https://pexels.com/  
  Additional product images under a free license.

#### Icons:
- Font Awesome
- Emoji symbols (unicode)

#### Tools:
- **dbdiagram.io**  
  https://dbdiagram.io  
  Used to create the Entity Relationship Diagram (ERD).

- **uizard.io**  
  https://app.uizard.io  
  Used to create wireframes.


#### Acknowledgements:
Thanks goes to my mentor, Rory Sheridan, for his motivating words of encouragement, advice and guidance through not only this project but also the other 4 milestone projects.

