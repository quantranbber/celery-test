# from django.contrib import admin
from django.urls import path, include
from store.views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('stores', ListCreateStoreView.as_view()),
    path('users', ListCreateUserView.as_view()),
]

urlpatterns = [path('api/', include(urlpatterns))]
