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
↓↓      queries.py  Created by  Durodola Opemipo 2021                        ↓↓
↓↓            Personal Email : <opemipodurodola@gmail.com>                   ↓↓
↓↓                 Telephone Number: +2348182104309                          ↓↓
↓↓→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→↓↓
↓↓←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←↓↓
"""

from typing import List

from pydantic import BaseModel

from src.models import Customer


class ListCustomersQuery(BaseModel):

    def execute(self) -> List[Customer]:
        customer = Customer.get()

        return customer


class GetCustomerByIDQuery(BaseModel):
    id: str

    def execute(self) -> Customer:
        customer = Customer.get(self.id)

        return customer
