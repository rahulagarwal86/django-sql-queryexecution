from django.conf.urls.defaults import patterns, url, include

urlpatterns = patterns( 'sqloperation.views',
  
  url( r'$', 'execute_sql', name = 'execute_sql' ),
 )
