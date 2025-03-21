from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base, Session

session = Session()

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    founding_year = Column(Integer, nullable=False)

    freebies = relationship('Freebie', back_populates='company', cascade="all, delete")
    devs = relationship('Dev', secondary='freebies', back_populates='companies', viewonly=True)

    def give_freebie(self, dev, item_name, value):
        new_freebie = Freebie(item_name=item_name, value=value, company=self, dev=dev)
        session.add(new_freebie)
        session.commit()

    @classmethod
    def oldest_company(cls):
        return session.query(cls).order_by(cls.founding_year).first()


class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    freebies = relationship('Freebie', back_populates='dev', cascade="all, delete")
    companies = relationship('Company', secondary='freebies', back_populates='devs', viewonly=True)

    def received_one(self, item_name):
        return session.query(Freebie).filter_by(dev_id=self.id, item_name=item_name).first() is not None

    def give_away(self, dev, freebie):
        if freebie in self.freebies:
            freebie.dev = dev
            session.commit()


class Freebie(Base):
    __tablename__ = 'freebies'

    id = Column(Integer, primary_key=True)
    item_name = Column(String, nullable=False)
    value = Column(Integer, nullable=False)
    company_id = Column(Integer, ForeignKey('companies.id', ondelete="CASCADE"))
    dev_id = Column(Integer, ForeignKey('devs.id', ondelete="CASCADE"))

    company = relationship('Company', back_populates='freebies')
    dev = relationship('Dev', back_populates='freebies')

    def print_details(self):
        return f"{self.dev.name} owns a {self.item_name} from {self.company.name}"
