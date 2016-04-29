# -*- coding: utf-8 -*-
from django import template
from users.templatetags.user_extras import big_user_name

register = template.Library()

def comment_user(comment):
    if not comment.authorName:
        return big_user_name(comment.author)
    else:
        return comment.authorName

register.filter('comment_user',comment_user)