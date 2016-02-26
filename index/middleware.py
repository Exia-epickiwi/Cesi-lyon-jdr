from django.core.exceptions import ObjectDoesNotExist
from index import models as indexModels
from django.shortcuts import render
from django.core.urlresolvers import resolve, Resolver404


class maintenanceMiddleware(object):

    def process_request(self,request):

        try:
            maintenance = indexModels.Setting.objects.get(key="maintenance")
        except ObjectDoesNotExist:
            return None

        if maintenance.value == "1" and not request.user.is_authenticated():

            try:
                path = resolve(request.path)
            except Resolver404:
                return render(request,"index/maintenance.html",locals())

            if path.url_name == "connection":
                return None

            return render(request,"index/maintenance.html",locals())

class viewSettingsMiddleware(object):

    def process_request(self, request):

        settings = indexModels.Setting.objects.all()
        settingsDictionary = {}

        for setting in settings:
            settingsDictionary[setting.key] = setting.value

        request.settings = settingsDictionary