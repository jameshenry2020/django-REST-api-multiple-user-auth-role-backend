from django.urls import path
from .views import ( FreelanceSignupView,
 ClientSignupView,
 CustomAuthToken, LogoutView, ClientOnlyView, FreelanceOnlyView)

urlpatterns=[
    path('signup/freelance/', FreelanceSignupView.as_view()),
    path('signup/client/', ClientSignupView.as_view()),
    path('login/',CustomAuthToken.as_view(), name='auth-token'),
    path('logout/', LogoutView.as_view(), name='logout-view'),
    path('freelance/dashboard/', FreelanceOnlyView.as_view(), name='freelance-dashboard'),
    path('client/dashboard/', ClientOnlyView.as_view(), name='client-dashboard'),
]