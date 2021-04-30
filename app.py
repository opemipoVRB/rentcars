from flask import Flask, jsonify, request
from pydantic import ValidationError

from src.commands import CreateCustomerCommand
from src.modifications import UpdateCustomerCommand
from src.queries import GetCustomerByIDQuery, ListCustomersQuery

app = Flask(__name__)


@app.errorhandler(ValidationError)
def handle_validation_exception(error):
    response = jsonify(error.errors())
    response.status_code = 400
    return response


@app.route('/create-customer/', methods=['POST'])
def create_customer():
    cmd = CreateCustomerCommand(
        **request.json
    )
    return jsonify(cmd.execute().dict())


@app.route('/customer/<customer_id>/', methods=['GET'])
def get_customer(customer_id):
    query = GetCustomerByIDQuery(
        id=customer_id
    )
    return jsonify(query.execute())


@app.route('/customer-list/', methods=['GET'])
def get_customers():
    query = ListCustomersQuery()
    records = [record for record in query.execute()]
    return jsonify(records)


@app.route('/update-customer/<customer_id>/', methods=['PUT'])
def update_customer(customer_id):
    cmd = UpdateCustomerCommand(
        id=int(customer_id),
        update = request.json
    )
    return jsonify(cmd.execute())


@app.route('/')
def index():
    return 'Index!!!'


if __name__ == '__main__':
    app.run()
