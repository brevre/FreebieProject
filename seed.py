from models import Company, Dev, Freebie
from database import Session

session = Session()

# Create Companies
google = Company(name="Google", founding_year=1998)
microsoft = Company(name="Microsoft", founding_year=1975)

# Create Devs
alice = Dev(name="Alice")
bob = Dev(name="Bob")

# Create Freebies
f1 = Freebie(item_name="T-shirt", value=10, company=google, dev=alice)
f2 = Freebie(item_name="Sticker", value=2, company=microsoft, dev=bob)

# Add to session and commit
session.add_all([google, microsoft, alice, bob, f1, f2])
session.commit()
session.close()
