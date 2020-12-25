"""polster URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from hello.views import index
from hello.views import index1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', index),
    path('dj4e/solutions/guess/guess.php', index1),
]


# import os
# from django.contrib import admin
# from django.urls import include, path
# from django.conf.urls import url
# from django.views.static import serve

# from hello.views import index

# # Up two folders to serve "site" content
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# SITE_ROOT = os.path.join(BASE_DIR, 'site')

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     # path('polls/', include('polls.urls')),
#     path('site/dj4e.htm', index),
#     url(r'^site/(?P<path>.*)$', serve,
#         {'document_root': SITE_ROOT, 'show_indexes': True},
#         name='site_path'
#         ),
# ]
