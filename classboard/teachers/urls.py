from django.urls import path, re_path
from .views import view_teachers

app_name = 'teachers'

urlpatterns = [
    # Это общий путь для вывода всех учителей
    path(r'', view_teachers, name='view_teachers'),
    # Это путь для вывода определенного учителя по его id (в данном случае pk)
    re_path(r'^(?P<pk>[0-9]+)/$', view_teachers, name="view_teachers"),
    # Это путь для создания Учителя с именем Кравец или случайного изменения его данных если такой уже сещуствует
    re_path(r'^create/$', view_teachers, name='view_teacher'),
]