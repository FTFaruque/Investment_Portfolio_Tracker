from flask import render_template, request, redirect, jsonify
from investportfolioapp.database.cud_operations import *
from investportfolioapp.database.analytics import *
from datetime import date

def register_routes(app, db):
    
    @app.route("/dashboard", methods=["GET"])
    @app.route("/", methods=["GET"])
    def dashboard():
        selected_category = request.args.get("filter", "All")
        if selected_category == "All":
            investments = db.session.query(Asset).all()
            all_category_data = alloc_across_categories()
            
            currency_data = alloc_across_currencies()
            return render_template(
                "dashboard.html",
                investments=investments,
                selected_category=selected_category,
                labelData = all_category_data[0],
                amountData = all_category_data[1],
                categoryFrequency = all_category_data[2],
                currencyLabel = currency_data[0],
                currencyFrequency = currency_data[1]
            )
        else:
            investments = db.session.query(Asset)\
                .filter(Asset.category == selected_category).all()
            graph_data = alloc_in_categories(selected_category)

            currency_data = alloc_across_currencies(filter=True, column=Asset.category, criteria=selected_category)

            return render_template('dashboard.html', 
                investments=investments, 
                selected_category=selected_category, 
                labelData=graph_data[0],
                amountData=graph_data[1],
                currencyLabel = currency_data[0],
                currencyFrequency = currency_data[1]
            )


    @app.route("/manage-investments", methods=["GET","POST"])
    def manage_investment():
        investment_to_delete = request.form.get('investment_to_delete')
        if investment_to_delete != None:
            delete_database_entry(int(investment_to_delete))
        investments = db.session.query(Asset).all()
        return render_template("manage_investments.html", investments=investments)


    @app.route('/add-investment', methods=['GET', 'POST'])
    def add_investment():
        if request.method == 'POST':
            name = request.form.get("name")
            category = request.form.get("category")
            amount = request.form.get("amount")
            currency = request.form.get("currency")
            yy, mm, dd = request.form.get("investment_date").split("-")
            event_date = date(int(yy), int(mm), int(dd))
            
            asset = Asset(category=category, currency=currency, name=name, amount=amount, event_date=event_date)
            
            if category == 'Stocks':
                create_database_entry(
                    asset, "Stock", 
                    tick_sym = request.form.get("stock_ticker"),
                    shares = request.form.get("number_of_shares"),
                    sector = request.form.get("sector")
                )

            elif category == 'Gold':
                create_database_entry(
                    asset, "Gold",
                    weight = request.form.get("gold_weight"),
                    karat = request.form.get("gold_karat"),
                    val_at_purchase = request.form.get("val_at_purchase")
                )

            elif category == 'Cash':
                create_database_entry(
                    asset, "Cash",
                    interest_rate = request.form.get('interest_rate'),
                    account_type = request.form.get("account_type")
                )

            elif category == "Real Estate":
                create_database_entry(
                    asset, "RealEstate",
                    property_type = request.form.get("property_type"),
                    occupancy = request.form.get("occupancy"),
                    size = request.form.get("size"),
                    rent_income = request.form.get("rental_income")
                )

            return redirect('/manage-investments')
        return render_template('add_investment.html')