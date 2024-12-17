from flask import Flask
from flask.blueprints import Blueprint

import config
import routes
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

app.debug = config.DEBUG

for blueprint in vars(routes).values():
    if isinstance(blueprint, Blueprint):
        app.register_blueprint(blueprint, url_prefix=blueprint.url_prefix)

if __name__ == "__main__":
    print("Application running on http://{}:{}".format(config.HOST, config.PORT))
    app.run(host=config.HOST, port=config.PORT)