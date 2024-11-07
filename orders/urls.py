from django.urls import path
from . import views

urlpatterns = [
    path('created/',views.order_created,name='order_create' ),
    path('',views.order_list,name='order_list'),
    path('reportes/',views.report_view,name='report_view'),
]
