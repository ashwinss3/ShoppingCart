
# Django Shopping Cart API

This project is a simple Django application for managing a shopping cart system with RESTful APIs.

## Design 

### Models and Relations

#### User:
- Contains the details of a User like name, email, username, etc.
- Other Possibilities:
  - User can have permissions like to upload products. Then users with this permission can upload/update various products. 
All users would have default permissions to view and buy products. 

#### Product:
- Contains the details of a Product like name, description, price, image, availability, etc.
- Many-to-Many relationship with Order: A product can be part of multiple orders, 
and an order can contain multiple products. The relationship is maintained using OrderItem model.
- Other Possibilities:
  - Foreign Key relationship with User to denote the uploader of the Product. 
  - We can support same product being uploaded by different users as well. 
    In that case we can have another table "Sellers" denoting sellers of the product 
    and details of the product from each seller.


#### Order:
- Contains details of an Order like user creating the order, total cost of the order.  
- Foreign Key relationship with User: Each order is associated to a user who placed it.
- Related to products via OrderItem table.
- Other Possibilities
  - Add validity before which user should complete the order. 
  - In case of validity expiration refresh the order contents.


#### OrderItem:
- Contains details of products present in an order.
- Responsible to maintain relation between Product and Order.
- Other Possibilities
  - We can add price of the product when added to the order, in case price can change later.


#### Payment:
- Contains details of Payment of an order like order id, payment method, amount paid, transaction id, etc.
- Foreign Key relationship with Order: A payment is associated with the order for which it was made.
- Other Possibilities:
  - We could allow split payment for an order. 
    The partial payment amounts can be decided based on the Products in the Order.



### Business Logic/Validations
#### Adding Products to an Order
- Make sure availability is verified before adding products to an Order.
- Update the price of the order when a product is added to the order.
- (TBA) Ideally just add the products and the price of the products at that time. 
And then add a separate API to get/calculate the price of the order using the products in order. 
With the current implementation, parallel addition of products can bring ambiguity. 
- (TBA) Make sure logged in user owns the order being edited currently.

#### During Payment
- Ensure the payment amount is matching the order amount.
- (TBA) Allow partial payments.

#### Post Payment Operations
- On successful payment, update the quantities of products.
- (TBA) Mark the order as Completed.
- (TBA) In case of any unavailability of product, then mark order as failed, and refund the amount.

### Authentication

- Added JWT authentication using rest_framework_simplejwt module.
- Make sure user is logged in while creating order. 
- (TBA) Add authentication to all API related to order, and make sure the authenticated user is thr owner of the order.


## Usage

### API Endpoints

- **Users:**
  - `GET /shopping_cart/users/`: List all users.
  - `POST /shopping_cart/users/`: Create a new user.
  - `GET /shopping_cart/users/<user_id>/`: Retrieve user details.
  - `PUT /shopping_cart/users/<user_id>/`: Update user details.
  - `DELETE /shopping_cart/users/<user_id>/`: Delete a user.

- **Products:**
  - `GET /shopping_cart/products/`: List all products.
  - `POST /shopping_cart/products/`: Create a new product.
  - `GET /shopping_cart/products/<product_id>/`: Retrieve product details.
  - `PUT /shopping_cart/products/<product_id>/`: Update product details.
  - `DELETE /shopping_cart/products/<product_id>/`: Delete a product.

- **Orders:**
  - `GET /shopping_cart/orders/`: List all orders.
  - `POST /shopping_cart/orders/`: Place a new order.
  - `GET /shopping_cart/orders/<order_id>/`: Retrieve order details.
  - `PUT /shopping_cart/orders/<order_id>/`: Update order details.
  - `DELETE /shopping_cart/orders/<order_id>/`: Cancel an order.
  - `POST /shopping_cart/orderitems/`: Add products to an order.

- **Payments:**
  - `GET /shopping_cart/payments/`: List all payments.
  - `POST /shopping_cart/payments/`: Make a new payment.
  - `GET /shopping_cart/payments/<payment_id>/`: Retrieve payment details.
  - `PUT /shopping_cart/payments/<payment_id>/`: Update payment details.
  - `DELETE /shopping_cart/payments/<payment_id>/`: Cancel a payment.

#### Improvement Points:
- Add Pagination in all the List APIs.



## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```bash
   cd django-shopping-cart-api
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```


## Notes

- This project uses Django Rest Framework for building RESTful APIs.
- This project uses rest_framework_simplejwt module for authentication.


This README provides instructions for setting up the project, details about available API endpoints, authentication method, and additional notes about the project's implementation. Adjustments can be made as necessary based on specific project details or additional features implemented.