# -*- coding: utf-8 -*-
from django import template

register = template.Library()

def big_user_name(user):
    """Renvoie le nom de l'utilisateur sous la meilleur forme en fonction des informations présentes"""

    result = ""

    if user.first_name:
        result += user.first_name
        if user.last_name:
            result += " " + user.last_name
    elif user.last_name:
        result += user.last_name
    else:
        result += user.username

    return result

register.filter('big_user_name',big_user_name)