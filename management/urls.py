from django.conf.urls import patterns, url
from management import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',

    url(r'^$', views.index, name='index'),
    url(r'^add_package/$', views.add_package, name='add_package'),
    url(r'^reorder_package/(?P<sender_url>\w+)/(?P<receiver_url>\w+)/$', views.reorder_package, name='reorder_package'),
    url(r'^sender/edit_sender/(?P<sender_url>\w+)/$', views.edit_sender, name='edit_sender'),
    url(r'^receiver/edit_receiver/(?P<receiver_url>\w+)/$', views.edit_receiver, name='edit_receiver'),
    url(r'^package/edit_package/(?P<package_url>\w+)/$', views.edit_package, name='edit_package'),
    url(r'^sender/(?P<sender_url>\w+)/$', views.detail_sender, name='detail_sender'),
    url(r'^receiver/(?P<receiver_url>\w+)/$', views.detail_receiver, name='detail_receiver'),
    url(r'^package/(?P<package_url>\w+)/$', views.detail_package, name='detail_package'),
    url(r'^logout/$',views.logout_view,name='logout'),
    url(r'^login/$',views.login_view,name='login'),
    url(r'search/$',views.search,name='search'),
    url(r'daily_report/$',views.daily_report,name='daily_report'),
    url(r'daily_report/$',views.daily_report,name='daily_report'),

    #testing
    url(r'^package/(?P<package_url>\w+)/print_receipt/$',views.print_receipt,name='print_receipt'),
    url(r'pdf_test/$',views.pdf_test,name='pdf_test'),
    url(r'not_ship/$',views.display_not_shipped_package,name='display_not_shipped_package'),
    ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)








if settings.DEBUG:
        urlpatterns += patterns(
                'django.views.static',
                (r'media/(?P<path>.*)',
                'serve',
                {'document_root': settings.MEDIA_ROOT}), )
