from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^dashboard$', dashboard, name='dashboard'),
    url(r'^facemasks$', display_facemasks, name="display_facemasks"),
    url(r'^sanitizers$', display_sanitizers, name="display_sanitizers"),
    url(r'^faceshields$', display_faceshields, name="display_faceshields"),

    url(r'^add_facemask$', add_facemask, name="add_facemask"),
    url(r'^add_sanitizer$', add_sanitizer, name="add_sanitizer"),
    url(r'^add_faceshield$', add_faceshield, name="add_faceshield"),

    url(r'^facemasks/edit_item/(?P<pk>\d+)$', edit_facemask, name="edit_facemask"),
    url(r'^sanitizers/edit_item/(?P<pk>\d+)$', edit_sanitizer, name="edit_sanitizer"),
    url(r'^faceshields/edit_item/(?P<pk>\d+)$', edit_faceshield, name="edit_faceshield"),

    url(r'^facemasks/delete/(?P<pk>\d+)$', delete_facemask, name="delete_facemask"),
    url(r'^sanitizers/delete/(?P<pk>\d+)$', delete_sanitizer, name="delete_sanitizer"),
    url(r'^faceshields/delete/(?P<pk>\d+)$', delete_faceshield, name="delete_faceshield")

]
