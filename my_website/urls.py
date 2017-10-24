from django.conf.urls import url, include
from django.contrib import admin
from accounts import views as accounts_views
from hello import views as hello_views
from products import views as product_views
from blog import views as blog_views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', blog_views.post_list, name='blog'),
    url(r'^blog/$', blog_views.post_list, name='blog'),
    url(r'^(?P<id>\d+)/$', blog_views.post_detail),
    url(r'^blog/(?P<id>\d+)/$', blog_views.post_detail),
    url(r'^register/$', accounts_views.register, name='register'),
    url(r'^profile/$', accounts_views.profile, name='profile'),
    url(r'^login/$', accounts_views.login, name='login'),
    url(r'^logout/$', accounts_views.logout, name='logout'),
    url(r'^products/$', product_views.all_products, name='products'),
    url(r'^blog/products/$', product_views.all_products, name='products'),
    url(r'^about/products/$', product_views.all_products, name='products'),
    url(r'^contact/products/$', product_views.all_products, name='products'),
    url(r'^about/$', hello_views.get_about, name='about'),
    url(r'^contact/$', hello_views.get_contact, name='contact'),
    url(r'^payment-accepted/$', hello_views.get_payment, name='payment'),
    url(r'^sent/$', hello_views.sent, name='sent'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

