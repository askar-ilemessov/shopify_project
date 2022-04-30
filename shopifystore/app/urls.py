from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', home, name='home'),
    
    path('detail/<int:id>/', detail, name='detail'),

    path('new/', create, name='create'),
    path('update/', update, name='update'),
    path('delete/<int:id>/', delete, name='delete'),


    path('warehouses/', warehouse, name='warehouse'),
    path('newWarehouses/', createWarehouse, name='createWarehouse'),
    path('warehouses/updateWarehouse/', updateWarehouse, name='updateWarehouse'),
    path('deleteWarehouse/<int:id>/', deleteWarehouse, name='deleteWarehouse'),


    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)