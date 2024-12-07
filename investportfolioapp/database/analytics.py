from investportfolioapp.database.db_init import db
from investportfolioapp.database.models import Asset

def alloc_across_categories(currency_code="USD"):
    rate = db.session.execute(db.text("SELECT rate FROM exchange_rates WHERE currency = :code;"), {"code":currency_code}).one()[0]
    result = db.session.execute(db.text("""
        SELECT category, SUM("standard"), COUNT(category) AS counts FROM (
            SELECT category, (amount/rate*:base) AS "standard" FROM assets 
            JOIN exchange_rates ON exchange_rates.currency=assets.currency
        ) GROUP BY category;
    """), {"base":rate}).all()

    if len(result) == 0:
        return [("Empty",), (1,), (1,)]
    return list(zip(*result))


def alloc_across_currencies(filter=False, column=None, criteria=None ):
    query = db.select(Asset.currency, db.func.count(Asset.currency).label("counts"))
    if filter:
        query = query.where(column == criteria)
    query = query.group_by(Asset.currency)
    result = db.session.execute(query).all()
    
    if len(result) == 0:
        return (("Empty",), (1,))

    return list(zip(*result))


def alloc_in_categories(category, currency_code="USD"):
    rate = db.session.execute(db.text("SELECT rate FROM exchange_rates WHERE currency = :code;"), {"code":currency_code}).one()[0]
    result = db.session.execute(db.text("""
        SELECT name, (amount/rate*:base) AS "standard" FROM assets
        JOIN exchange_rates ON exchange_rates.currency=assets.currency
        WHERE category=:category;
    """), {"base":rate, "category":category}).all()

    if len(result) == 0:
        return [('Empty',),(1,)]
    return list(zip(*result))
    