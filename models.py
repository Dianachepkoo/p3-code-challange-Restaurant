from sqlalchemy import create_engine, func
from sqlalchemy import ForeignKey, Table, Column, Integer, String
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///many_to_many.db')

Base = declarative_base()

restaurant_user = Table(
    'restaurant_users',
    Base.metadata,
    Column('restaurant_id', ForeignKey('restaurants.id'), primary_key=True),
    Column('customer_id', ForeignKey('customers.id'), primary_key=True),
    extend_existing=True,
)

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer(), primary_key=True)
    name  = Column(String())
    price = Column(Integer())
   
    customers = relationship('Customer', secondary=restaurant_user, back_populates='restaurants')
    reviews = relationship('Review', backref=backref('restaurant'))

    def __repr__(self):
        return f'Restaurant(id={self.id}, ' + \
            f'name={self.name}, ' + \
            f'price={self.price})'

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer(), primary_key=True)
    f_name = Column(String())
    l_name = Column(String())

    restaurants = relationship('Restaurant', secondary=restaurant_user, back_populates='customers')
    reviews = relationship('Review', backref=backref('customer'))

    def __repr__(self):
        return f'Customer(id={self.id}, ' + \
            f'f_name={self.f_name})'

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer(), primary_key=True)
    restaurant_id = Column(Integer(), ForeignKey('restaurants.id'))
    customer_id = Column(Integer(), ForeignKey('customers.id'))
    star_rating = Column(Integer())

    def __repr__(self):
        return f'Review(id={self.id}, ' + \
            f'restaurant_id={self.restaurant_id}, ' + \
            f'customer_id={self.customer_id})'