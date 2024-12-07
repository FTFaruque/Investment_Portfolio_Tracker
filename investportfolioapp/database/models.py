from investportfolioapp.database.db_init import db


class Asset(db.Model):
    __tablename__ = "assets"
    _id = db.Column("id", db.Integer, primary_key=True)
    category = db.Column("category", db.String)
    name = db.Column("name", db.String)
    amount = db.Column("amount", db.Float)
    currency = db.Column("currency", db.String)
    event_date = db.Column("event_date", db.Date)

    Cash = db.relationship("Cash", back_populates="asset", cascade="save-update, delete, delete-orphan" )
    Gold = db.relationship("Gold", back_populates="asset", cascade="save-update, delete, delete-orphan" )
    Stock = db.relationship("Stock", back_populates="asset", cascade="save-update, delete, delete-orphan" )
    RealEstate = db.relationship("RealEstate", back_populates="asset", cascade="save-update, delete, delete-orphan" )

    def __init__(self, currency, category, name, amount, event_date):
        self.category = category
        self.currency = currency
        self.name = name
        self.amount = amount
        self.event_date = event_date


class Cash(db.Model):
    __tablename__ = "cash"
    _id = db.Column("asset_id", db.Integer, db.ForeignKey("assets.id"), primary_key=True)
    interest_rate = db.Column("interest_rate", db.Float)
    account_type = db.Column("account_type", db.String)

    asset = db.relationship("Asset", back_populates="Cash")

    def __init__(self, interest_rate, account_type):
        self.interest_rate = interest_rate
        self.account_type = account_type


class Gold(db.Model):
    __tablename__ = "gold"
    _id = db.Column("asset_id", db.Integer, db.ForeignKey("assets.id"), primary_key=True)
    weight = db.Column("weight", db.Integer)
    val_at_purchase = db.Column("current_value_per_unit", db.Float)
    karat = db.Column("karat", db.Integer)

    asset = db.relationship("Asset", back_populates="Gold")

    def __init__(self, weight, val_at_purchase, karat):
        self.weight = weight
        self.val_at_purchase = val_at_purchase
        self.karat = karat


class Stock(db.Model):
    __tablename__ = "stocks"
    _id = db.Column("asset_id", db.Integer, db.ForeignKey("assets.id"), primary_key=True)
    tick_sym = db.Column("ticker_symbol", db.String(5))
    shares = db.Column("shares", db.Integer)
    sector = db.Column("sector", db.String)

    asset = db.relationship("Asset", back_populates="Stock")

    def __init__(self, tick_sym, shares, sector):
        self.tick_sym = tick_sym
        self.shares = shares
        self.sector = sector


class RealEstate(db.Model):
    __tablename__ = "real_estates"
    _id = db.Column("asset_id", db.Integer, db.ForeignKey("assets.id"), primary_key=True)
    property_type = db.Column("property_type", db.String)
    occupancy = db.Column("occupancy", db.String)
    size = db.Column("size", db.String)
    rent_income = db.Column("rent_income", db.Integer)

    asset = db.relationship("Asset", back_populates="RealEstate")

    def __init__(self, property_type, occupancy, size, rent_income):
        self.property_type = property_type
        self.occupancy = occupancy
        self.size = size
        self.rent_income = rent_income