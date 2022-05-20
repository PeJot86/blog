from blog.models import Entry, db
from faker import Faker

def generate_entries(how_many=10):
   fake = Faker('pl_PL')

   for i in range(how_many):
       post = Entry(
           title=fake.sentence(),
           body='\n'.join(fake.paragraphs(15)),
           is_published=True
       )
       db.session.add(post)
   db.session.commit()

generate_entries(10)