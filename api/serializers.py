import blog.models as blogModels
import events.models as calendarModel
import projects.models as projetModels
import wiki.models as wikiModels
from django.contrib.auth.models import User
from rest_framework import serializers

class BlogArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = blogModels.Article
        fields = ("url","title","date","author","content","formatedContent","comment_set")

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ("url","username","first_name","last_name")

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = calendarModel.Comment
        fields = ("url","author","authorName","date","content")

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = calendarModel.Event
        fields = ("url","title","date","place","shortDescription","description")

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = projetModels.Project
        fields = ("url","name","wikiArticle","progression","task_set")

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = projetModels.Task
        fields = ("url","name","progression")

class WikiArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = wikiModels.Article
        fields = ("url","title","creation","content","formatedContent")