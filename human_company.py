import logging
from logging.config import dictConfig

from flask import Flask

from config import LOGGING

dictConfig(LOGGING)


app = Flask(__name__)
app.logger = logging.getLogger('human_company')
app.logger.info("Human_company started")


import views