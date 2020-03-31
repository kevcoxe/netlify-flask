from flask_frozen import Freezer
from app import app
from app.models import Stuff

freezer = Freezer(app)


@freezer.register_generator
def api_get_stuff():
    for stuff in Stuff.query.all():
        yield stuff.json()


if __name__ == '__main__':
    freezer.freeze()
