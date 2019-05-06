
from django.contrib import admin
from django.urls import path, include
import app.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('', include('theme.urls')),
    path('recipe/', include('app.urls')),
    # path('registe/', app.views.registe, name='registe'),
    # path('insert/', app.views.recipeform, name="recipeform"),
    # path('selectRecipe/', myapp.views.selectRecipe, name='selectRecipe'),
    # path('selectResult/', myapp.views.selectResult, name='selectResult'),
] # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

