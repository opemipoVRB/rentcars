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
↓↓      models.py  Created by  Durodola Opemipo 2021                         ↓↓
↓↓            Personal Email : <opemipodurodola@gmail.com>                   ↓↓
↓↓                 Telephone Number: +2348182104309                          ↓↓
↓↓→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→↓↓
↓↓←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←↓↓

"""
import mysql.connector
from pydantic import BaseModel, EmailStr

connection = mysql.connector.connect(
    host="localhost",
    user="denis",
    password="toor@2021",
    database="rentcars",
)


class NotFound(Exception):
    pass


class Customer(BaseModel):
    """
    Customer
    """
    id: str = connection.cursor(buffered=True, dictionary=True).lastrowid
    first_name: str
    last_name: str
    phone_number: str
    email: EmailStr
    address: str
    city: str

    @classmethod
    def create_model(cls):
        connection.cursor().execute(
            "CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, first_name VARCHAR(255),"
            "last_name VARCHAR(255),phone_number VARCHAR(255), "
            "email VARCHAR(255) NOT NULL UNIQUE, address VARCHAR(255), city VARCHAR(255))")
        print("customers model created")

    @classmethod
    def destroy_model(cls):
        connection.cursor().execute("DROP TABLE customers")
        print("customers model destroyed")

    def create_customer(self):
        sql = "INSERT INTO customers (first_name, last_name, phone_number, email, address, city)" \
              " VALUES (%s,%s,%s,%s,%s,%s)"
        val = (self.first_name, self.last_name, self.phone_number, self.email, self.address, self.city)
        cnx = connection.cursor(buffered=True)
        cnx.execute(sql, val)
        connection.commit()
        print("customer added")
        self.id = cnx.lastrowid
        return self

    @classmethod
    def update_customer(cls, id, updates={}):
        cnx = connection.cursor(buffered=True, dictionary=True)
        sql = "UPDATE customers SET first_name=%s, " \
              "last_name =%s, phone_number =%s, " \
              "email=%s, address=%s, city=%s " \
              " WHERE id = %s"
        columns = updates.keys()
        values = tuple([updates[column] for column in columns]) + tuple((id,))
        cnx.execute(sql, values)
        connection.commit()
        print("Customer Updated ")
        return updates

    @classmethod
    def get_by_email(cls, email):
        cnx = connection.cursor(buffered=True, dictionary=True)
        sql = "SELECT * FROM customers WHERE email =%s"
        val = (email,)
        cnx.execute(sql, val)
        results = cnx.fetchone()
        if results is None:
            raise NotFound

        return results

    @classmethod
    def get(cls, id=None):
        cnx = connection.cursor(buffered=True, dictionary=True)
        if id is None:
            sql = "SELECT * FROM customers"
            cnx.execute(sql)
            results = cnx.fetchall()
        else:
            sql = "SELECT * FROM customers WHERE id =%s"
            val = (id,)
            cnx.execute(sql, val)
            results = cnx.fetchone()
            if results is None:
                raise NotFound

        return results

    @classmethod
    def delete_customer(cls, id):
        cnx = connection.cursor(buffered=True, dictionary=True)
        sql = "DELETE FROM customers WHERE id =%s"
        val = (id,)
        cnx.execute(sql, val)
        connection.commit()
        return "Deleted"


class VehicleType:
    @classmethod
    def create_model(cls):
        connection.cursor().execute(
            "CREATE TABLE vehicle_types (type_id INT AUTO_INCREMENT PRIMARY KEY,"
            " name VARCHAR(255))")
        print("Vehicle model created")


class Car:
    @classmethod
    def create_model(cls):
        connection.cursor().execute(
            "CREATE TABLE cars (car_id INT AUTO_INCREMENT PRIMARY KEY, brand VARCHAR(255), color VARCHAR(255),size INT, license_no VARCHAR(255) NOT NULL UNIQUE,"
            " is_available BOOLEAN, type_id INT, CONSTRAINT fk_type FOREIGN KEY (type_id) REFERENCES vehicle_types(type_id))")
        print("Car model created")


class Booking:
    @classmethod
    def create_model(cls):
        connection.cursor().execute(
            "CREATE TABLE bookings (booking_id INT AUTO_INCREMENT PRIMARY KEY, cost FLOAT ,is_paid BOOLEAN,"
            "date_of_hire DATE , date_of_return DATE,"
            "id INT, CONSTRAINT fk_customer FOREIGN KEY (id) REFERENCES customers(id) )")
        print("Booking model created")


class BookedCar:
    @classmethod
    def create_model(cls):
        connection.cursor().execute(
            "CREATE TABLE booked_cars ("
            "car_id INT, CONSTRAINT fk_car FOREIGN KEY (car_id) REFERENCES cars(car_id),"
            " booking_id INT, CONSTRAINT fk_booking FOREIGN KEY (booking_id) REFERENCES bookings(booking_id))")
        print("BookedCar model created")


# VehicleType.create_model()
# Car.create_model()
# Booking.create_model()
# BookedCar.create_model()
# Customer.create_model()
# Customer(
#     first_name="Opemipo",
#     last_name="Durodola",
#     phone_number="08182104309",
#     email="opemipodurodola@gmail.com",
#     address="Row 3 House 6 Staff Qtrs",
#     city="Lagos"
# ).create_customer()

# update = {
#     "first_name": "Emmanuel",
#     "last_name": "Caster",
#     "phone_number": "08182104309",
#     "email": "emmanuelcaster@gmail.com",
#     "address": "Row 3 House 6 Staff Qtrs",
#     "city": "Lagos",
# }
# customer = Customer.get()
# print(customer)
# Customer.update_customer(id=1, updates=update
#                          )
# customer = Customer.get()
# print(customer)
