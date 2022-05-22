from django.urls import path
from subscribers import views
urlpatterns = [
    path('addSubscriber/',views.add_subscriber,name='add_subscriber'),
    path('viewSubscribers/',views.view_subscribers,name='view_subscribers'),
    path('updateSubscriber/<int:pk>/updateSubscriber',views.SubscriberUpdateView.as_view(),name='update_subscriber'),
    path('deleteSubscriber/<int:pk>/deleteSubscriber',views.SubscriberDeleteView.as_view(),name='delete_subscriber'),
    path('subscribeNow/',views.subscribe_now,name='subscribe_now'),
    path('login/',views.subscriber_login,name='login'),
    path('logout/',views.logout_request,name='logout'),
]