from django.conf.urls import url
from users import views

urlpatterns = [
    url(r'^connexion$',views.connect,name="connection"),
    url(r'^deconnexion$',views.disconnect),
]