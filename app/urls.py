from django.conf.urls import patterns, url
from app.views import (
    PictureCreateView, BasicPlusVersionCreateView
)
from app.decaf_views import DecafCreateView, DecafModelCreateView
from app.classify_views import ClassifyCreateView
from app.poi_views import PoiCreateView
from app.trainaclass_views import TrainaclassCreateView

urlpatterns = patterns('',
                       url(r'^image-stitch/$', PictureCreateView.as_view(), name='image-stitching'),
                       url(r'^basicplus/$', BasicPlusVersionCreateView.as_view(), name='upload-basic-plus'),
                       url(r'^decaf-server/$', DecafCreateView.as_view(), name='decaf-server'),
                       (r'^decaf-server-new/$', DecafModelCreateView.as_view(), {}, 'decaf'),
                       (r'^classify/$', ClassifyCreateView.as_view(), {}, 'classify'),
                       (r'^vip/$', PoiCreateView.as_view(), {}, 'poi'),
                       (r'^trainaclass/$', TrainaclassCreateView.as_view(), {}, 'trainaclass'),
                       )

urlpatterns += patterns('app.views',
                        url(r'^$', 'homepage', name="home"),
                        url(r'^demoupload/(?P<executable>\w+)/$', 'demoUpload', name='demoUpload'),
                        url(r'^auth/(?P<auth_name>\w+)/$', 'authenticate', name='authenticate'),
                        url(r'^callback/(?P<auth_name>\w+)/$', 'callback', name='callback'),
                        url(r'^matlab/$', 'matlabReadRequest', name='matlabReadRequest'),
                        url(r'^api/$', 'matlabReadRequest', name='apiRequest'),
                        url(r'^ec2/$', 'ec2', name='ec2'),
                        )

urlpatterns += patterns('app.decaf_views',
                        url(r'^decaf_dropbox/$', 'decafDropbox', name="decafDropbox"),
                        url(r'^decaf_train/$', 'decaf_train', name="decaf_train"),
                        url(r'^demo_decaf/$', 'demoDecaf', name="demoDecaf"),
                        )

urlpatterns += patterns('app.classify_views',
                        url(r'^demo_classify/$', 'demoClassify', name="demoClassify"),
                        )

urlpatterns += patterns('app.poi_views',
                        url(r'^demo_poi/$', 'demoPoi', name="demoPoi"),
                        )

urlpatterns += patterns('app.trainaclass_views',
                        url(r'^trainmodel/$', 'trainamodel', name="trainamodel"),
                        url(r'^testmodel/$', 'testmodel', name="testmodel"),
                        )
