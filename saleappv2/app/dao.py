from app.models import Category, Product, User


def load_categories():
    return Category.query.all()


def load_products(kw):
    products = Product.query

    if kw:
        products = products.filter(Product.name.contains(kw))

    return products.all()


def get_user_by_id(id):
    return User.query.get(id)
