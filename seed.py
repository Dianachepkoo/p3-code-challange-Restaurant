#!/usr/bin/env python3

from faker import Faker
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Restaurant, Review, Customer

if __name__ == '__main__':
    engine = create_engine('sqlite:///many_to_many.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Restaurant).delete()
    session.query(Review).delete()
    session.query(Customer).delete()
    fake = Faker()

    names = ['INTI', 'ALAS&CO', 'SPOONZOOM',
        'The Nook', 'SANKARA', 'OLE SERENI']
   
    restaurants = []
    for i in range(50):
        restaurant = Restaurant(
            name=fake.unique.name(),
            price=random.randint(5, 60)
        )

        # add and commit individually to get IDs back
        session.add(restaurant)
        session.commit()

        restaurants.append(restaurant)

    reviews = []
    for restaurant in restaurants:
        for i in range(random.randint(1,5)):
            
            review = Review(
                star_rating=random.randint(0, 10),
                restaurant_id=restaurant.id,
            )

            reviews.append(review)

    session.bulk_save_objects(reviews)
    session.commit()
    session.close()