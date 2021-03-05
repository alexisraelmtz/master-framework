import sqlite3


# conn = sqlite3.connect(":memory:")
conn = sqlite3.connect(r"/mnt/c/Users/7K/Documents/Python/master-framework/db.sqlite3")
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
    c.execute("SELECT * FROM product")
    return c.fetchall()


print(all())
conn.close()