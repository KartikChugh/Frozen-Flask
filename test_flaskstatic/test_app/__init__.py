from flask import Flask
from flaskext.static import StaticBuilder

from .admin import admin_module

def product(product_id):
    return 'Product num %i' % product_id

def init_app():
    app = Flask(__name__)
    app.register_module(admin_module, url_prefix='/admin')
    builder = StaticBuilder(app)

    @app.route('/')
    def index():
        return 'Main index'

    @app.route('/robots.txt')
    def robots_txt():
        content = 'User-agent: *\nDisallow: /'
        return app.response_class(content, mimetype='text/plain')

    app.route('/product_<int:product_id>/')(product)

    @builder.register_generator
    def app_urls():
        # endpoint, values
        for id in (0, 1):
            yield 'product', {'product_id': id}
        # single string: url
        yield '/product_2/'
    
    return app, builder

