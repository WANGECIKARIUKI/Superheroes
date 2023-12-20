from app import app
from models import Power, Hero, HeroPower, db

with app.app_context():

    Power.query.delete()
    Hero.query.delete()
    HeroPower.query.delete()

    heroes =[]
    heroes.append(Hero(name ='Super' , super_name ='Superman'))
    heroes.append(Hero(name ='Ant' , super_name ='Antman'))
    heroes.append(Hero(name ='Bat' , super_name ='BatWoman'))
    heroes.append(Hero(name ='Cat' , super_name ='Catwoman'))
    heroes.append(Hero(name ='BatM' , super_name ='Batman'))
    heroes.append(Hero(name ='Captain' , super_name ='CaptainMarvel'))
    heroes.append(Hero(name ='Black' , super_name ='BlackPanther'))
    heroes.append(Hero(name ='Hawk' , super_name ='HawkEye'))

    db.session.add_all(heroes)

    powers=[]
    powers.append(Power(name ='Psychokinesis', description=' ability to move objects using the mind.'))
    powers.append(Power(name ='Superhuman strength', description=' power to extract force and lift weights'))
    powers.append(Power(name ='Invisibility', description='the state of an object that cannot be seen'))
    powers.append(Power(name ='X-ray Vision', description='ability to peers through objects such as walls.'))
    powers.append(Power(name ='Heat Vision', description='a powerful form of energy manipulation that allows the user to shoot heat rays out of their eyes.'))
    powers.append(Power(name ='Super-speed', description='ability to move like a flash of lightning'))
  
    db.session.add_all(powers)

    heropowers =[]
    heropowers.append(HeroPower(strength='Strong', hero=heroes[6], power=powers[2]))
    heropowers.append(HeroPower(strength='Weak', hero=heroes[4], power=powers[2]))
    heropowers.append(HeroPower(strength='Average', hero=heroes[1], power=powers[5]))
    
    db.session.add_all(heropowers)
    db.session.commit()