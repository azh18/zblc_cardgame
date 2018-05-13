# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from game.player import *
from game.Card import *
from game.market import *
from django.shortcuts import render,render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from models import User
from django import template

Players = {}
CardPiles = None
Markets = None


register = template.Library()
def get_value(map, key):
    return map[key]
key = register.filter('key', get_value)



# Create your views here.
class UserForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=50)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())

class Hello:
    def __init__(self):
        self.body = ""
        self.title = ""


# Create your views here.
def say_hello(request):
    hello = Hello()
    hello.body = "hello world"
    hello.title = "hello title"
    users = [1,2,3,4,5]
    return render(request, 'index.html', {"hello": hello, "users":users})



def login(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']

            user = User.objects.filter(username__exact=username, password__exact=password)
            if user:
                return HttpResponseRedirect("/test/?user={}".format(username))
            else:
                return HttpResponse('用户名或密码错误,请重新登录')
    else:
        userform = UserForm()
    return render(request, 'login.html', {'userform': userform})


def register(request):
    global Players
    global CardPiles
    global Markets
    uname = request.REQUEST.get("username", "")
    Players[uname] = Player(Markets, CardPiles)
    return render(request, 'index.html', {"username": uname, "players": Players, "cardpiles": CardPiles, "markets": Markets})


def new_game(request):
    global Players
    global CardPiles
    global Markets
    uname = request.GET.get("user")
    Markets = Market()
    Players = {}
    CardPiles = CardPile()
    Markets.init()
    CardPiles.init()
    return render(request, 'index.html', {"username": uname, "players": Players, "cardpiles": CardPiles, "markets": Markets})

def test(request):
    global Players
    global CardPiles
    global Markets
    uname = request.GET.get("user")
    print uname
    Markets = Market()
    CardPiles = CardPile()
    p1 = Player(Markets, CardPiles, "p1")
    p2 = Player(Markets, CardPiles, "p2")
    p3 = Player(Markets, CardPiles, "p3")
    p1.name = "p1"
    p2.name = "p2"
    p3.name = "p3"
    Players['p1'] = p1
    Players['p2'] = p2
    Players['p3'] = p3
    Players['zhangbowen'] = Player(Markets, CardPiles, "zhangbowen")
    CardPiles.init()
    p1.wupin_card[CardPiles.wupin_card["1"].id] = CardPiles.wupin_card["1"]
    p2.wupin_card["2"] = CardPiles.wupin_card["2"]
    p2.wupin_card["1"] = CardPiles.wupin_card["1"]
    return render(request, 'index.html', {"username": uname, "players": Players, "cardpiles": CardPiles, "markets": Markets})

def get_wupin_card_pile(request):
    global Players
    global CardPiles
    global Markets
    user = request.GET.get("user")
    uname = user
    print("uname=", uname)
    Players[user].get_a_wupin_card()
    print(CardPiles)
    return render(request, 'index.html', {"username": uname, "players": Players, "cardpiles": CardPiles, "markets": Markets})

def get_ziyuan_card_pile(request):
    global Players
    global CardPiles
    global Markets
    user = request.GET.get("user")
    uname = user
    print("uname=", uname)
    Players[user].get_a_ziyuan_card()
    return render(request, 'index.html', {"username": uname, "players": Players, "cardpiles": CardPiles, "markets": Markets})


def flush(request):
    global Players
    global CardPiles
    global Markets
    user = request.GET.get("user")
    uname = user
    return render(request, 'index.html', {"username": uname, "players": Players, "cardpiles": CardPiles, "markets": Markets})


def get_card_from_consider(request):
    global Players
    global CardPiles
    global Markets
    user = request.GET.get("user")
    card_id = request.GET.get("card")
    uname = user
    print("uname=", uname)
    Players[user].get_card_from_consider(card_id)
    print(CardPiles)
    return render(request, 'index.html', {"username": uname, "players": Players, "cardpiles": CardPiles, "markets": Markets})



