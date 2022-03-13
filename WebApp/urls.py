
from unicodedata import name
from django.urls import path
from WebApp.views import Fin, Form_Report, Remainder_Report, Remainder_Update, Sign_up, Update,Search
from WebApp.views import Remainder,Web_Ser

urlpatterns=[
    path('Fin/',Fin),
    path('Report/',Form_Report),
    path('search/WA/update/<int:id>',Update),
    path('Report/WA/update/<int:id>',Update),
    path('search/',Search,name='search'),
    path('Report/remainder/<int:id>',Remainder),
    path('report/',Remainder_Report),
    path('report/<int:id>',Remainder_Report),
    path('report/remainder_update/<int:id>',Remainder_Update),
    path('search/remainder/<int:id>',Remainder),
    path('search/report/',Remainder_Report),
    path('search/remainder/report/remainder_update/<int:id>',Remainder_Update),
    path('Web/',Web_Ser.as_view())
]