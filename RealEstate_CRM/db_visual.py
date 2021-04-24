import sqlite3
import os
from pathlib import Path


# conn = sqlite3.connect(":memory:")
default = Path(os.getcwd())
def_db = Path.joinpath(default, "master-framework/RealEstate_CRM/db.sqlite3")
# print(def_db)
conn = sqlite3.connect(def_db)
c = conn.cursor()


# c.execute(
#     """CREATE TABLE product (
#     first TEXT,
#     last TEXT,
#     pay INTEGER
#     )"""
# )


def insert_emp(emp):
    with conn:
        c.execute(
            "INSERT INTO product VALUES (:first, :last, :pay)",
            {"first": emp.first, "last": emp.last, "pay": emp.pay},
        )


def get_emps_by_name(lastname):
    c.execute("SELECT * FROM product WHERE last=:last", {"last": lastname})
    return c.fetchall()


def update_pay(emp, pay):
    with conn:
        c.execute(
            """UPDATE product SET pay = :pay
                    WHERE first = :first AND last = :last""",
            {"first": emp.first, "last": emp.last, "pay": pay},
        )


def remove_emp(emp):
    with conn:
        c.execute(
            "DELETE from product WHERE first = :first AND last = :last",
            {"first": emp.first, "last": emp.last},
        )


def all():
    with conn:
        c.execute("SELECT * FROM inventory_product")
        return c.fetchall()


print(all())
conn.close()