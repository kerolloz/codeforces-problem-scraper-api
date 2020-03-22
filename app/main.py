import flask
import codeforces_wrapper


app = flask.Flask(__name__)
PROBLEM_LINK = 'https://codeforces.com/problemset/problem/'


@app.route('/', methods=['GET'])
def home():
    problem_id = flask.request.args['id']
    return flask.jsonify(codeforces_wrapper.parse_problem(PROBLEM_LINK + problem_id))
