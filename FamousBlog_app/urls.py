
from django.contrib import admin
from django.urls import path, include
from FamousBlog_app.Blog_app import views as blog_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog_views.home, name='home'),
    path('', include('FamousBlog_app.Autenfication_app.urls')),
    path('blog/', include('FamousBlog_app.Blog_app.urls')),
    path('advertisements/', include('FamousBlog_app.Advertisement_app.urls')),
    path('articles/', include('FamousBlog_app.Articles_app.urls')),
    path('categorys/', include('FamousBlog_app.Categorys_app.urls')),
    path('images/', include('FamousBlog_app.Image_app.urls')), 
    path('categorys/technologys/', include('FamousBlog_app.Technology_app.urls')),
    path('categorys/sports/', include('FamousBlog_app.Zal_app.urls')),
    path('categorys/paints/', include('FamousBlog_app.Art_app.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





