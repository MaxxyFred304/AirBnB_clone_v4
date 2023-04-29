from flask import Blueprint
from api.v1.views.index import *

# Create a Blueprint instance with the url prefix "/api/v1"
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Import all the views from api.v1.views.index using a wildcard import
