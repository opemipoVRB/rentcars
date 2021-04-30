#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←
←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←
↓↓...........................................................................↓↓
↓↓..........................↓↓↓↓↓↓↓↓↓↓↓↓↓....................................↓↓
↓↓.......................↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓.................................↓↓
↓↓.....................↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓...............................↓↓
↓↓....................↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓..............................↓↓
↓↓...................↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓.↓↓...............................↓↓
↓↓...................↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓...↓↓..............................↓↓
↓↓...................↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓.↓↓...↓↓↓.............................↓↓
↓↓...................↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓..............................↓↓
↓↓....................↓↓↓↓↓↓↓↓↓↓↓↓↓.....↓↓↓↓↓↓↓↓↓............................↓↓
↓↓......................↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓..↓↓↓↓↓↓↓............................↓↓
↓↓...................................↓↓↓.....................................↓↓
↓↓.................↓↓................↓↓↓↓ ↓↓↓↓↓↓↓........↓...................↓↓
↓↓...............↓↓↓↓↓↓..............↓↓↓↓↓↓↓↓↓↓↓↓↓...↓↓↓↓↓↓..................↓↓
↓↓............↓↓↓↓..↓↓↓↓↓.........................↓↓↓↓↓↓↓↓↓..................↓↓
↓↓............↓↓↓↓...↓↓↓↓↓↓↓....................↓↓↓↓↓↓.↓↓.↓↓.................↓↓
↓↓...............↓↓↓↓↓↓↓↓↓↓↓↓↓↓............↓↓↓↓↓↓↓↓..........................↓↓
↓↓.........................↓↓↓↓↓↓↓↓↓...↓↓↓↓↓↓↓...............................↓↓
↓↓..............................↓↓↓↓↓↓↓↓↓↓...................................↓↓
↓↓..........................↓↓↓↓↓....↓↓↓↓↓↓↓↓↓...............................↓↓
↓↓............↓↓.↓↓↓↓↓↓↓↓↓↓↓↓↓............↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓..................↓↓
↓↓............↓↓.↓↓..↓↓↓↓.....................↓↓↓↓↓↓↓↓↓↓↓↓↓↓.................↓↓
↓↓..............↓↓↓↓↓↓............................↓↓.↓↓↓↓↓↓↓.................↓↓
↓↓..................                                   ......................↓↓
↓↓.................. ↑↑↑  ↑↑↑  ↑↑↑↑↑↑↑        ↑↑↑↑↑↑↑ .......................↓↓
↓↓.................. ↑↑↑  ↑↑↑  ↑↑↑   ↑↑↑↑     ↑↑↑   ↑↑↑↑.....................↓↓
↓↓.................. ↑↑↨  ↑↑↑  ↑↑↨   ↨↑↑      ↑↑↨   ↨↑↑......................↓↓
↓↓.................. ↨↑↨  ↑↨↑  ↨↑↨   ↨↑↨      ↨↑↨   ↨↑↨......................↓↓
↓↓.................. ↑↨↑  ↨↑↨  ↨↨↑↨↑↨↨↑↑↨     ↨↨↑↨↑↨↨↑↑↨.....................↓↓
↓↓.................. ↨↑↨  ↨↨↨  ↨↨↨      ↨↨↨   ↨↨↨     ↨↨↨....................↓↓
↓↓.................. :↨:  ↨↨:  ↨↨:      :↨↨   ↨↨:     :::....................↓↓
↓↓................... ::↨↨:↨   :↨:      :↨:   :↨:     :::....................↓↓
↓↓.................... ::::    :::      :::   :::     :::....................↓↓
↓↓...................... :      :        :      :::::::  ....................↓↓
↓↓...........................................................................↓↓
↓↓←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←↓↓
↓↓→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→↓↓
↓↓      test_app.py  Created by  Durodola Opemipo 2021                       ↓↓
↓↓            Personal Email : <opemipodurodola@gmail.com>                   ↓↓
↓↓                 Telephone Number: +2348182104309                          ↓↓
↓↓→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→↓↓
↓↓←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←↓↓

"""

import json
import pathlib

import pytest
import requests
from jsonschema import RefResolver, validate

from app import app
from src.models import Customer

HOST = "localhost"
PORT = "5000"


@pytest.fixture
def client():
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client


def validate_payload(payload, schema_name):
    """
    Validate payload with selected schema
    """
    schemas_dir = str(
        f'{pathlib.Path(__file__).parent.absolute()}/schemas'
    )
    schema = json.loads(pathlib.Path(f'{schemas_dir}/{schema_name}').read_text())
    validate(
        payload,
        schema,
        resolver=RefResolver(
            'file://' + str(pathlib.Path(f'{schemas_dir}/{schema_name}').absolute()),
            schema  # it's used to resolve file: inside schemas correctly
        )
    )


def test_create_customer(client):
    """
    GIVEN request data for new customer
    WHEN endpoint /create-customer/ is called
    THEN it should return Customer in json format matching schema

    """
    data = {
        'first_name': 'Emmanuel',
        'last_name': 'Caster',
        'phone_number': '08182104309',
        'email': 'emmanuelcaster@gmail.com',
        'address': 'Row 3 House 6 Staff Qtrs',
        'city': 'Ogun',
    }
    response = client.post(
        '/create-customer/',
        data=json.dumps(
            data
        ),
        content_type='application/json',
    )

    validate_payload(response.json, 'Customer.json')


def test_get_customer(client):
    """
    GIVEN ID of customer stored in the database
    WHEN endpoint /customer/<id-of-customer>/ is called
    THEN it should return Customer in json format matching schema
    """
    customer = Customer(
        first_name="Opemipo",
        last_name="Durodola",
        phone_number="08182104309",
        email="opemipodurodola@gmail.com",
        address="Row 3 House 6 Staff Qtrs",
        city="Lagos"
    ).create_customer()
    response = client.get(
        f'/customer/{customer.id}/',
        content_type='application/json',
    )

    validate_payload(response.json, 'Customer.json')


def test_get_customers(client):
    """

    GIVEN customer stored in the database
    WHEN endpoint /customer-list/ is called
    THEN it should return list of Customer in json format matching schema

    """
    Customer(
        first_name="Opemipo",
        last_name="Durodola",
        phone_number="08182104309",
        email="opemipodurodola@gmail.com",
        address="Row 3 House 6 Staff Qtrs",
        city="Lagos"
    ).create_customer()
    response = client.get(
        '/customer-list/',
        content_type='application/json',
    )

    validate_payload(response.json, 'CustomerList.json')


def test_update_customer(client):
    """
    GIVEN ID of customer stored in the database
    WHEN endpoint /update-customer/<id-of-customer>/ is called
    THEN it should update
    """
    data = {
        'first_name': 'Emmanuel',
        'last_name': 'Caster',
        'phone_number': '08182104309',
        'email': 'emmanuelcaster@gmail.com',
        'address': 'Row 3 House 6 Staff Qtrs',
        'city': 'Ogun',
    }

    customer = Customer(
        first_name="Opemipo",
        last_name="Durodola",
        phone_number="08182104309",
        email="opemipodurodola@gmail.com",
        address="Row 3 House 6 Staff Qtrs",
        city="Lagos"
    ).create_customer()

    response = client.put(
        f'/update-customer/{customer.id}/',
        data=json.dumps(
            data),
        content_type='application/json',
    )

    validate_payload(response.json, 'UpdateCustomer.json')


@pytest.mark.parametrize(
    'data',
    [
        {
            "first_name": None,
            "last_name": None,
            "phone_number": "08182104309",
            "email": "emmanuelcaster@gmail.com",
            "address": None,
            "city": "Ogun",
        },
        {
            "first_name": "Emmanuel",
            "last_name": "Caster",
            "phone_number": "08182104309",
            "email": "emmanuelcaster@gmail.com",
            "address": "Row 3 House 6 Staff Qtrs",
            "city": None,
        },
        {
            "first_name": "Emmanuel",
            "last_name": "Caster",
            "phone_number": "08182104309",
            "email": None,
            "address": "Row 3 House 6 Staff Qtrs",
            "city": None,
        }
    ]
)
def test_create_customer_bad_request(client, data):
    """
    GIVEN request data with invalid values or missing attributes
    WHEN endpoint /create-customer/ is called
    THEN it should return status 400 and JSON body
    """
    response = client.post(
        '/create-customer/',
        data=json.dumps(
            data
        ),
        content_type='application/json',
    )

    assert response.status_code == 400
    assert response.json is not None


@pytest.mark.e2e
def test_create_list_get(client):
    requests.post(
        'http://{}:{}/create-customer/'.format(HOST, PORT),
        json={
            "first_name": "Emmanuel",
            "last_name": "Caster",
            "phone_number": "08182104309",
            "email": "emmanuelcaster@gmail.com",
            "address": "Row 3 House 6 Staff Qtrs",
            "city": "Lagos",
        }
    )
    response = requests.get(
        'http://{}:{}/customer-list/'.format(HOST, PORT),
    )

    customers = response.json()

    response = requests.get(
        f'http://%s:%s/customer/{customers[0]["id"]}/' % (HOST, PORT),
    )

    assert response.status_code == 200
