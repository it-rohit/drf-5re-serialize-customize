
from django.urls import path

from . views import Watchlist_View_Create,Watchlist_Update_Delete,Streamplatform_list,Streamplatform_update

urlpatterns = [
    
    path('create/',Watchlist_View_Create.as_view(),name='Watchlist_View_Create'),
    path('update/<int:pk>/',Watchlist_Update_Delete.as_view(),name='Watchlist_Update_Delete'),

    ## Streamplatform
    path('Streamcreate/',Streamplatform_list.as_view(),name='Streamplatform_list'),
    path('Streamupdate/<int:pk>/',Streamplatform_update.as_view(),name='Streamplatform_update'),

]