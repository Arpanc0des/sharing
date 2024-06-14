from sqlalchemy import Column, Integer, String, DECIMAL, TIMESTAMP
from sqlalchemy.orm import relationship
from database import Base

class Customer(Base):
    __tablename__ = 'Customer'
    customer_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(100))
    password = Column(String(100))

class Account(Base):
    __tablename__ = 'Account'

    account_id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer)
    account_balance = Column(DECIMAL(10, 2))

class Product(Base):
    __tablename__ = 'Product'

    product_id = Column(Integer, primary_key=True, autoincrement=True)
    product_name = Column(String(100))
    unit_price = Column(DECIMAL(10, 2))

class ShoppingCart(Base):
    __tablename__ = 'ShoppingCart'

    cart_id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer)
    product_id = Column(Integer)
    quantity = Column(Integer)

class Transaction(Base):
    __tablename__ = 'Transaction'

    transaction_id = Column(Integer, primary_key=True, autoincrement=True)
    cart_id = Column(Integer)
    payment_amount = Column(DECIMAL(10, 2))
    transaction_date = Column(TIMESTAMP, server_default='CURRENT_TIMESTAMP')