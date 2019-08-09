from django.contrib import admin
from django.urls import path, include
import mainapp.views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainapp.views.index, name = 'index'),
    path('search/', mainapp.views.search, name = 'search'),
    path('detail/<int:post_id>/', mainapp.views.detail, name = 'detail'),
    path('result/', mainapp.views.result, name = 'result'),
    path('write/', mainapp.views.write, name = 'write'),
    path('mypage/', mainapp.views.mypage, name = 'mypage'),
    path('detail/<int:post_id>/delete/', mainapp.views.delete, name='delete'),
    path('detail/<int:post_id>/edit/', mainapp.views.edit, name='edit'),
    path('<int:post_id>/comments/', mainapp.views.add_comment, name='add_comment'),
    path('<int:post_id>/delete_comment/<int:comment_id>/', mainapp.views.delete_comment, name = 'delete_comment'),
    path('review_board/', mainapp.views.review_board, name = 'review_board'),
    path('review_detail/', mainapp.views.review_detail, name = 'review_detail'),
    path('review_write/', mainapp.views.review_write, name = 'review_write'),
    path('accounts/', include('accounts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
