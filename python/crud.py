from sqlalchemy.orm import Session
import models, schemas

# crud for  for Customer
def create_customer_with_account(db: Session, customer: schemas.CustomerCreate, account: schemas.AccountCreate):
    # Create customer
    db_customer = models.Customer(first_name=customer.first_name, last_name=customer.last_name, email=customer.email)
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    
    # Create account associated with the customer
    db_account = models.Account(customer_id=db_customer.id, account_balance=account.account_balance)
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    
    return db_customer

def get_customer(db: Session, customer_id: int):
    return db.query(models.Customer).filter(models.Customer.customer_id == customer_id).first()

def create_customer_with_account(db: Session, customer: schemas.CustomerCreate):
    db_customer = models.Customer(first_name=customer.first_name, last_name=customer.last_name, email=customer.email)
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    
    db_account = models.Account(customer_id=db_customer.id, account_balance=0.0)  # Initialize balance as needed
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    
    return db_customer

def update_customer(db: Session, customer_id: int, first_name: str, last_name: str, email: str, password: str):
    customer = db.query(models.Customer).filter(models.Customer.customer_id == customer_id).first()
    if customer:
        customer.first_name = first_name
        customer.last_name = last_name
        customer.email = email
        customer.password = password
        db.commit()
        db.refresh(customer)
    return customer

def delete_customer(db: Session, customer_id: int):
    customer = db.query(models.Customer).filter(models.Customer.customer_id == customer_id).first()
    if customer:
        db.delete(customer)
        db.commit()
    return customer

# crud for  for Account
def create_account(db: Session, customer_id: int, account_balance: float):
    new_account = models.Account(customer_id=customer_id, account_balance=account_balance)
    db.add(new_account)
    db.commit()
    db.refresh(new_account)
    return new_account

def get_account(db: Session, account_id: int):
    return db.query(models.Account).filter(models.Account.account_id == account_id).first()

def update_account(db: Session, account_id: int, customer_id: int, account_balance: float):
    account = db.query(models.Account).filter(models.Account.account_id == account_id).first()
    if account:
        account.customer_id = customer_id
        account.account_balance = account_balance
        db.commit()
        db.refresh(account)
    return account

def delete_account(db: Session, account_id: int):
    account = db.query(models.Account).filter(models.Account.account_id == account_id).first()
    if account:
        db.delete(account)
        db.commit()
    return account

# crud for  for Product
def create_product(db: Session, product_name: str, unit_price: float):
    new_product = models.Product(product_name=product_name, unit_price=unit_price)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.product_id == product_id).first()

def update_product(db: Session, product_id: int, product_name: str, unit_price: float):
    product = db.query(models.Product).filter(models.Product.product_id == product_id).first()
    if product:
        product.product_name = product_name
        product.unit_price = unit_price
        db.commit()
        db.refresh(product)
    return product

def delete_product(db: Session, product_id: int):
    product = db.query(models.Product).filter(models.Product.product_id == product_id).first()
    if product:
        db.delete(product)
        db.commit()
    return product

# crud for  for ShoppingCart
def create_shopping_cart(db: Session, customer_id: int, product_id: int, quantity: int):
    new_cart_item = models.ShoppingCart(customer_id=customer_id, product_id=product_id, quantity=quantity)
    db.add(new_cart_item)
    db.commit()
    db.refresh(new_cart_item)
    return new_cart_item

def get_shopping_cart_item(db: Session, cart_id: int):
    return db.query(models.ShoppingCart).filter(models.ShoppingCart.cart_id == cart_id).first()

def update_shopping_cart_item(db: Session, cart_id: int, customer_id: int, product_id: int, quantity: int):
    cart_item = db.query(models.ShoppingCart).filter(models.ShoppingCart.cart_id == cart_id).first()
    if cart_item:
        cart_item.customer_id = customer_id
        cart_item.product_id = product_id
        cart_item.quantity = quantity
        db.commit()
        db.refresh(cart_item)
    return cart_item

def delete_shopping_cart_item(db: Session, cart_id: int):
    cart_item = db.query(models.ShoppingCart).filter(models.ShoppingCart.cart_id == cart_id).first()
    if cart_item:
        db.delete(cart_item)
        db.commit()
    return cart_item

# crud for  for Transaction

def create_transaction(db: Session, cart_id: int, payment_amount: float):
    new_transaction = models.Transaction(cart_id=cart_id, payment_amount=payment_amount)
    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)
    return new_transaction

def get_transaction(db: Session, transaction_id: int):
    return db.query(models.Transaction).filter(models.Transaction.transaction_id == transaction_id).first()

def update_transaction(db: Session, transaction_id: int, cart_id: int, payment_amount: float):
    transaction = db.query(models.Transaction).filter(models.Transaction.transaction_id == transaction_id).first()
    if transaction:
        transaction.cart_id = cart_id
        transaction.payment_amount = payment_amount
        db.commit()
        db.refresh(transaction)
    return transaction

def delete_transaction(db: Session, transaction_id: int):
    transaction = db.query(models.Transaction).filter(models.Transaction.transaction_id == transaction_id).first()
    if transaction:
        db.delete(transaction)
        db.commit()
    return transaction
