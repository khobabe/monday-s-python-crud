
from django.contrib import admin
from django.urls import path
from notebook.views import home,delete_work

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="home-page"),
    path('contact/delete/<int:note_id>',delete_work,name='delete-contact')
]
