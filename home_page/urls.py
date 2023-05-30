from django.urls import path
from .views import HomePageView, AboutPageView

# oddiy funksyiya (def) orqali yaratilgan views.py ni url.py ga chaqirish
# urlpatterns = [
#     path('', HomePageView, name='home')
# ]


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),  # klassdan foydalanganda as_view() qoshilishi kk
    path('about/', AboutPageView.as_view(), name='about')
]
