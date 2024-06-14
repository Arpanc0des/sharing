from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas import (
     CustomerCreate, Customer,
     AccountCreate, Account,
     ProductCreate, Product,
     ShoppingCartCreate, ShoppingCart,
     TransactionCreate, Transaction
)
import crud

app=FastAPI()

@app.post("/customerswithacc/", response_model=Customer)
def create_customer_with_accounte(customer: CustomerCreate, account: AccountCreate, db: Session = Depends(get_db)):
    return crud.create_customer_with_account(db=db, customer=customer, account=account)

@app.get("/customers/{customer_id}", response_model=Customer)
def read_customer(customer_id: int, db: Session = Depends(get_db)):
    db_customer = crud.get_customer(db=db, customer_id=customer_id)
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return db_customer

@app.delete("/customers/{customer_id}", response_model=Customer)
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    db_customer = crud.delete_customer(db=db, customer_id=customer_id)
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return db_customer

# crud route for for Account
@app.post("/accounts/", response_model=Account)
def create_account(account: AccountCreate, db: Session = Depends(get_db)):
    return crud.create_account(db=db, customer_id=account.customer_id, account_balance=account.account_balance)

@app.get("/accounts/{account_id}", response_model=Account)
def read_account(account_id: int, db: Session = Depends(get_db)):
    db_account = crud.get_account(db=db, account_id=account_id)
    if db_account is None:
        raise HTTPException(status_code=404, detail="Account not found")
    return db_account

@app.delete("/accounts/{account_id}", response_model=Account)
def delete_account(account_id: int, db: Session = Depends(get_db)):
    db_account = crud.delete_account(db=db, account_id=account_id)
    if db_account is None:
        raise HTTPException(status_code=404, detail="Account not found")
    return db_account

# crud route for for Product
@app.post("/products/", response_model=Product)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db=db, product_name=product.product_name, unit_price=product.unit_price)

@app.get("/products/{product_id}", response_model=Product)
def read_product(product_id: int, db: Session = Depends(get_db)):
    db_product = crud.get_product(db=db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@app.delete("/products/{product_id}", response_model=Product)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    db_product = crud.delete_product(db=db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

# crud route for for ShoppingCart
@app.post("/shopping-cart/", response_model=ShoppingCart)
def create_shopping_cart(cart: ShoppingCartCreate, db: Session = Depends(get_db)):
    return crud.create_shopping_cart(db=db, customer_id=cart.customer_id,
                                     product_id=cart.product_id, quantity=cart.quantity)

@app.get("/shopping-cart/{cart_id}", response_model=ShoppingCart)
def read_shopping_cart(cart_id: int, db: Session = Depends(get_db)):
    db_cart = crud.get_shopping_cart_item(db=db, cart_id=cart_id)
    if db_cart is None:
        raise HTTPException(status_code=404, detail="ShoppingCart item not found")
    return db_cart

# @app.put("/shopping-cart/{cart_id}", response_model=ShoppingCart)
# def update_shopping_cart(cart_id: int, cart: ShoppingCartUpdate, db: Session = Depends(get_db)):
#     db_cart = crud.update_shopping_cart_item(db=db, cart_id=cart_id,
#                                              customer_id=cart.customer_id,
#                                              product_id=cart.product_id,
#                                              quantity=cart.quantity)
#     if db_cart is None:
#         raise HTTPException(status_code=404, detail="ShoppingCart item not found")
#     return db_cart

@app.delete("/shopping-cart/{cart_id}", response_model=ShoppingCart)
def delete_shopping_cart(cart_id: int, db: Session = Depends(get_db)):
    db_cart = crud.delete_shopping_cart_item(db=db, cart_id=cart_id)
    if db_cart is None:
        raise HTTPException(status_code=404, detail="ShoppingCart item not found")
    return db_cart

# crud route for for Transaction
@app.post("/transactions/", response_model=Transaction)
def create_transaction(transaction: TransactionCreate, db: Session = Depends(get_db)):
    return crud.create_transaction(db=db, cart_id=transaction.cart_id, payment_amount=transaction.payment_amount)

@app.get("/transactions/{transaction_id}", response_model=Transaction)
def read_transaction(transaction_id: int, db: Session = Depends(get_db)):
    db_transaction = crud.get_transaction(db=db, transaction_id=transaction_id)
    if db_transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return db_transaction