# -*- coding: utf-8 -*-
from django.conf.urls import url
from api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'articles',views.BlogArticlesViewSet)
router.register(r'users',views.UsersViewSet)
router.register(r'comments',views.CommentsViewSet)
router.register(r'events',views.EventViewSet)
router.register(r'projects',views.ProjectViewSet)
router.register(r'tasks',views.TaskViewSet)
router.register(r'wiki',views.WikiArticleViewSet)