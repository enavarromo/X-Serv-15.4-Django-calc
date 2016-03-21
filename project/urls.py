from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'(\d+)-(\d+)','calc.views.resta'),
    url(r'(\d+)\+(\d+)','calc.views.suma'),
    url(r'(\d+)\*(\d+)','calc.views.multiplica'),
    url(r'(\d+)/(\d+)','calc.views.divide'),
    url(r'.*','calc.views.la404')
)
