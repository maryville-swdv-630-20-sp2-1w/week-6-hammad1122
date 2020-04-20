from sqlalchemy import *
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy import Column, String
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Teams(Base):
    def _init_(self, members):
        self.members = members
        
    _tablename_ = "team"
    
    id = Column(Integer, primary_key=True)
    members = Column(String)
    
    def _repr_(self):
        return "team[members{0}".format(self.members)
    
def main():
    engine = create_engine('sqlite:///memory', echo-False)
    
    Base.metadata.create_all(engine)
    
    team1 = Teams("Tim")
    print (team1)
    
    Session = sessionmaker(being=engine)
    session = Session()
    
    session.add(team1)
    
    newTeam1 = session.query(Teams).filter_by(members="Tim").first()
    print (newTeam1)
    session.commit()
    
    print(team1.id)
    
    session.add_all([
        Teams(members="Sam")])
    session.commit()
    
    for row in session.query(Teams).all():
        print (row.members)
# import sqlalchemy
# from sqlalchemy import create_engine
# engine = create_engine('sqlite:///:memory:', echo=True)
# from sqlalchemy.ext.declarative import declarative_base
# Base = declarative_base()
# from sqlalchemy import Column, Integer, String
# class Teams(Base):
#     __tablename__ = 'teams'
#     id = Column(Integer, primary_key=True)
#     members = Column(String)
# 
# def __repr__(self):
#     return "<Teams(members='%s')>" % (self.members)
# 
# Teams.__table__ 
# Table('teams', MetaData(bind=None),
#       id = Column(Integer, primary_key=True),
#       Column('id', Integer(), table=<teams>, primary_key=True, nullable=False),
#       Column('name', String(), table=<teams>), schema=None)
#       members = Column(String)
# 
# Base.metadata.create_all(engine)
# SELECT ...
# PRAGMA main.table_info("teams")
# ()
# PRAGMA temp.table_info("teams")
# ()
# CREATE TABLE teams (
#     id INTEGER NOT NULL, members VARCHAR,
#     PRIMARY KEY (id)
# )
# ()
# COMMIT
# 
# ed_teams = Teams(member='Tim')
# >>> ed_teams.members
# 
# from sqlalchemy.orm import sessionmaker
# Session = sessionmaker(bind=engine)
# Session = sessionmaker()
# Session.configure(bind=engine)
# session = Session()
# 
# ed_teams = Teams(member='Sam')
# session.add(ed_teams)
# 
# our_teams = session.query(Teams).filter_by(member='ed').first() 
# our_teams
# 
# ed_teams is our_teams
# 
# session.add_all([
#     Teams(members='John')])
# 
# session.dirty
# IdentitySet([<Teams(member='ed')>])
# 
# for row in session.query(Teams.members.label('members_label')).all():
#     print(row.members_label)