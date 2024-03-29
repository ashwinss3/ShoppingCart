
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


