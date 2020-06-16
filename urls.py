from django.urls import path

from .import views

app_name = "KontraktApp"
urlpatterns = [
    path('', views.index, name='index'),
    path("login/",views.login, name='login'),
    path("overview/", views.OverviewView.as_view(), name='overview' ),
    path("customers/", views.AllCustomersView.as_view(), name='customers'),
    path("editCustomer/<int:pk>/", views.EditCustomerView.as_view(),name="editCustomer"),
    path("editCustomer/new/", views.EditCustomerView.as_view(),name="editCustomerNew"),
    path("editContract/<int:pk>/", views.EditContractView.as_view(),name="editContract"),
    path("editContract/new/", views.EditContractView.as_view(),name="editContractNew")
]