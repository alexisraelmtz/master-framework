from django.db import models
import datetime

# from django.db.models.fields import IntegerField

global maxBoards, maxColumns, maxTickets

maxBoards = 2
maxColumns = 600
maxTickets = 1000
maxUsers = 100


class user(models.Model):
    id = models.IntegerField(
        max_length=maxUsers,
        # auto_increment=True,
        primary_key=True,
        unique=True,
    )
    username = models.CharField(max_length=25)
    email = models.EmailField(max_length=85)
    passlock = models.CharField(max_length=255)


class board(models.Model):
    id = models.IntegerField(
        # auto_increment=True,
        primary_key=True,
        unique=True,
        max_length=maxBoards * maxUsers,
    )
    user_id = models.IntegerField(max_length=maxUsers)
    title = models.CharField(max_length=225)
    date = models.DateTimeField(datetime.datetime.now(tz=None))
    style = models.IntegerField(max_length=100)


class column(models.Model):
    id = models.IntegerField(
        # auto_increment=True,
        primary_key=True,
        unique=True,
        max_length=maxColumns * maxBoards * maxUsers,
    )
    board_id = models.IntegerField(max_length=maxBoards * maxUsers)
    name = models.CharField(max_length=125)
    date = models.DateTimeField(datetime.datetime.now(tz=None))
    position = models.IntegerField(max_length=600)
    style = models.IntegerField(max_length=100)


class ticket(models.Model):
    id = models.IntegerField(
        # auto_increment=True,
        primary_key=True,
        unique=True,
        max_length=maxTickets,
    )
    id = models.IntegerField(max_length=maxColumns * maxBoards * maxUsers)
    name = models.CharField(max_length=255)
    text = models.TextField(max_length=750)
    priority = models.IntegerField(max_length=5)
    progress = models.IntegerField(max_length=100)
    date = models.DateTimeField(datetime.datetime.now(tz=None))
    position = models.IntegerField(max_length=200)

    # class home(models.Model):
    #     hid = models.IntegerField(
    #         auto_increment=True, primary_key=True, unique=True, max_length=maxUsers
    #     )
    #
    #     board_id = models.IntegerField(max_length=maxBoards)
    #     title = models.CharField(max_length=225)
