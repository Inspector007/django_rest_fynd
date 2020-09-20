from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateImdbRatingView, DetailsImdbRatingView,\
	RetrieveImdbRatingView	
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = {
    url(r'^imdbrating/$', CreateImdbRatingView.as_view(), name="imdbratingcreate"),
    url(r'^imdbrating/(?P<pk>[0-9]+)/$',
        DetailsImdbRatingView.as_view(), name="imdbratingdetails"),
    url(r'^imdbratingretrieve/$', RetrieveImdbRatingView.as_view(), name="imdbratingretrieve"),
    url(r'^auth/', include('rest_framework.urls',
                           namespace='rest_framework')),
}

urlpatterns = format_suffix_patterns(urlpatterns)
