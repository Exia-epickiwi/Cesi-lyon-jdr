from datetime import datetime
from rest_framework import viewsets
import api.serializers as serializers
import blog.models as blogModels
import projects.models as projetModels
import wiki.models as wikiModels
import events.models as calendarModel
from django.contrib.auth.models import User
from rest_framework import permissions

class BlogArticlesViewSet(viewsets.ModelViewSet):
    queryset = blogModels.Article.objects.filter(date__lte=datetime.now()).order_by("-date")
    serializer_class = serializers.BlogArticleSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class CommentsViewSet(viewsets.ModelViewSet):
    queryset = calendarModel.Comment.objects.order_by("-date")
    serializer_class = serializers.CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class EventViewSet(viewsets.ModelViewSet):
    queryset = calendarModel.Event.objects.all()
    serializer_class = serializers.EventSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = projetModels.Project.objects.all()
    serializer_class = serializers.ProjectSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class TaskViewSet(viewsets.ModelViewSet):
    queryset = projetModels.Task.objects.all()
    serializer_class = serializers.TaskSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class WikiArticleViewSet(viewsets.ModelViewSet):
    queryset = wikiModels.Article.objects.all()
    serializer_class = serializers.WikiArticleSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)