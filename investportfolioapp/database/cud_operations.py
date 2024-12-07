from investportfolioapp.database.models import *


def create_database_entry(asset:Asset, class_name:str, **kwargs):   
    class_map = {
        'Cash': Cash,
        'Gold':Gold,
        'RealEstate':RealEstate,
        'Stock':Stock
    }
    asset_relation = class_map[class_name](**kwargs)
    setattr(asset, class_name, [asset_relation])

    db.session.add(asset)
    db.session.add(asset_relation)
    db.session.commit()


def delete_database_entry(id):
    asset = db.session.query(Asset).filter(Asset._id == id).one()
    db.session.delete(asset)
    db.session.commit()


def update_database_entry():
    print("hello")