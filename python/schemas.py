from pydantic import BaseModel, Field
from typing import Optional, List

class CustomerBase(BaseModel):
    first_name: str
    last_name: str
    email: str

class CustomerCreate(CustomerBase):
    password: str

class CustomerUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None

class Customer(CustomerBase):
    customer_id: int

class AccountBase(BaseModel):
    customer_id: int
    account_balance: float

class AccountCreate(AccountBase):
    pass

class Account(AccountBase):
    account_id: int

class ProductBase(BaseModel):
    product_name: str
    unit_price: float

class ProductCreate(ProductBase):
    pass

# class ProductUpdate(BaseModel):
#     product_name: Optional[str] = None
#     unit_price: Optional[float] = None

class Product(ProductBase):
    product_id: int

class ShoppingCartBase(BaseModel):
    customer_id: int
    product_id: int
    quantity: int

class ShoppingCartCreate(ShoppingCartBase):
    pass

class ShoppingCart(ShoppingCartBase):
    cart_id: int

class TransactionBase(BaseModel):
    cart_id: int
    payment_amount: float

class TransactionCreate(TransactionBase):
    pass

class Transaction(TransactionBase):
    transaction_id: int