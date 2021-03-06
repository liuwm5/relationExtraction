"""REtest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
'''
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]
'''
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from REweb import views  # 导入views模块
from django.conf.urls import url

urlpatterns = [
    #    url(r'index/', views.index)  # 配置当访问index/时去调用views下的index方法
    url(r'^$', views.index),
    url(r'getTriple', views.getTriple)
]
urlpatterns += staticfiles_urlpatterns()
