from django.contrib import admin
from django.urls import path, include
import mainapp.views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainapp.views.index, name = 'index'),
    path('search/', mainapp.views.search, name = 'search' ),
    path('detail/<int:post_id>/', mainapp.views.detail, name = 'detail'),
    path('result/', mainapp.views.result, name = 'result'),
    path('write/', mainapp.views.write, name = 'write'),
    path('mypage/', mainapp.views.mypage, name = 'mypage'),
    path('introduce/',mainapp.views.introduce, name = 'introduce'),
    path('detail/<int:post_id>/delete/', mainapp.views.delete, name='delete'),
    path('detail/<int:post_id>/edit/', mainapp.views.edit, name='edit'),
    path('<int:post_id>/comments/', mainapp.views.add_comment, name='add_comment'),
    path('<int:post_id>/delete_comment/<int:comment_id>/', mainapp.views.delete_comment, name = 'delete_comment'),
    path('service/', mainapp.views.service, name = 'service'),
    path('service_detail/<int:complaint_id>/', mainapp.views.service_detail, name = 'service_detail'),
    # path('<int:complaint_id>/service_comment/', mainapp.views.service_comment, name = 'service_comment'),
    path('accounts/', include('accounts.urls')),
    path('search/', mainapp.views.search, name = 'search'),
    path('service_write/', mainapp.views.service_write, name='service_write'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
