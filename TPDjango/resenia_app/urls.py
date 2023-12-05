from django.contrib import admin
from django.urls import path , include
#from .router import router



from .views import      ReseniaListView   \
                    ,   ReseniaEditView \
                    ,   ReseniaCreateView \
                    ,   ReseniaDeleteView

app_name = "resenia"

urlpatterns = [
    path("", ReseniaListView.as_view(), name="resenia"),
    path("create/", ReseniaCreateView.as_view(), name="create"),
    path("<int:pk>/edit/", ReseniaEditView.as_view(), name="edit"),
    path("<int:pk>/delete/", ReseniaDeleteView.as_view(), name="delete"),
    
]

#urlpatterns += router.urls


