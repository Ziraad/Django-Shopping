from django.contrib import admin

from pooshak.models import Size, SportSet
from account.models import Profile

admin.site.register(Size)
admin.site.register(SportSet)
admin.site.register(Profile)
