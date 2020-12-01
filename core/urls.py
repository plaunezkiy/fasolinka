from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('cdbdladq/', views.one, name='one'),
    path('cdbdladq/rhwsddmsg/', views.two, name='two'),
    path('cdbdladq/rhwsddmsg/ldlnqhzk/', views.three, name='three'),
    path('cdbdladq/rhwsddmsg/ldlnqhzk/ozqj/', views.four, name='four'),
    path('cdbdladq/rhwsddmsg/ldlnqhzk/ozqj/entq/', views.five, name='five'),
    # TODO:
    path('cdbdladq/rhwsddmsg/ldlnqhzk/ozqj/entq/hm/', views.six, name='six'),
    path('cdbdladq/rhwsddmsg/ldlnqhzk/ozqj/entq/hm/sgd/', views.seven, name='seven'),
    # --
    path('cdbdladq/rhwsddmsg/ldlnqhzk/ozqj/entq/hm/sgd/zesdqmnnm/', views.eight, name='eight'),
    path('<path:resource>', views.not_found, name='404'),
]
'''
    path('cdbdladq/sgd/rhwsddmsg/vzq/ldlnqhzk/', views.five, name='five'),
    path('cdbdladq/sgd/rhwsddmsg/vzq/ldlnqhzk/ozqj/', views.six, name='six'),
    path('cdbdladq/sgd/rhwsddmsg/vzq/ldlnqhzk/ozqj/entq/', views.seven, name='seven'),
    path('cdbdladq/sgd/rhwsddmsg/vzq/ldlnqhzk/ozqj/entq/hm/', views.eight, name='eight'),
    path('cdbdladq/sgd/rhwsddmsg/vzq/ldlnqhzk/ozqj/entq/hm/sgd/', views.nine, name='nine'),
'''
