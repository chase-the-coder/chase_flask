from basic import db, Puppy

my_puppy = ('Rufus', 5)
db.session.add(my_puppy)
db.session.commit()

all_puppies = Puppy.query.all()
print(all_puppies)

puppy_one = Puppy.query.get(1)
print(puppy_one.name)