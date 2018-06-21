from django.conf.urls import url, include

from . import views


app_name = 'setMsg'
urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^default', views.defaultView, name='default'),
	url(r'(?P<ts_code>\d+)/result/', views.defaultDetail, name='defaultDetail'),
	url(r'^custom', views.customView, name='custom'),
	url(r'(?P<ts_code>\d+)/result/', views.customDetail, name='customDetail'),
	url(r'(?P<country_code>\d+)/(?P<ts_code>\d+)', views.delete, name='delete'),
	url(r'^insert', views.insert, name='insert'),
]

