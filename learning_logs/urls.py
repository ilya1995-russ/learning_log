"""Определяет схемы URL для learning_logs."""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Домашняя страница.
    path('', views.index, name='index'),

    # Вывод всех тем.
    path('topics/', views.topics, name='topics'),

    # Страница с подробной информацией по отдельной теме
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    # Страница для добавления нововй темы.
    path('nem_topic/', views.new_topic, name='new_topic'),

    # Страница для добавления говой записи
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),

    # Страница для редактирование записи
    path('edit_entry/<int:entry_id>', views.edit_entry, name='edit_entry'),

    # path('edit_topic/<int:topic_id>', views.edit_topic, name='edit_topic'),
]
