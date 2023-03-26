from app import app, login_manager
from flask import flash, render_template, request, redirect, url_for
from app.db.db_models import session
from app.db.db_models import add_new_item#
from app.db.items import Item#
from app.db.users import User#

from cloudipsp import Api, Checkout

from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash


@app.route("/main")
def index():
    items = session.query(Item).all()

    return render_template("index.html", data=items)


@app.route("/")
def start():

    return render_template("start.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/buy/<int:id>")
def item_buy(id):
    item = session.query(Item).where(Item.id == id).first()

    api = Api(merchant_id=1396424,
          secret_key='test')
    checkout = Checkout(api=api)
    data = {
    "currency": "UAH",
    "amount": str(item.price) + "00"
    }
    url = checkout.url(data).get('checkout_url')
    return redirect(url)



@app.route("/create", methods=["GET", "POST"])
def create():

    if request.method == "POST":
        title = request.form["title"]
        price = request.form["price"]
        experience = request.form["experience"]
        score = request.form["score"]
        phone = request.form["phone"]

        new_item = Item(title=title, price=price, experience=experience, score=score, phone=phone)

        try:
            add_new_item(new_item)

        except:
            return "Error in form"
        return redirect("main")
    return render_template("create.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = session.query(User).where(User.username == username).first()
        is_password_correct = False

        if user:
            is_password_correct = check_password_hash(user.password, password)

        if not user or not is_password_correct:
            flash("Try again and check your login details")
            return redirect(url_for("login"))

        login_user(user)
        return redirect("main")
    return render_template("login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = generate_password_hash(request.form["password"])
        email = request.form["email"]

        new_user = User(username=username, password=password,
                              email=email)
        add_new_item(new_user)
        return redirect("main")
    return render_template("signup.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("main")

@login_manager.user_loader
def load_user(user):
    return session.query(User).get(int(user))