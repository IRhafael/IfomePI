from django.urls import path
from . import views
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),    
    path ('', views.home, name="ifome"),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('salvar/', views.salvar, name='salvar')
]   

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)