
import hello_world
import flask

@hello_world.app.route('/', methods=["GET"])
def main(methods=["GET"]):
    """ Main route, entry point for react. """
    return flask.render_template('index.html')
