import os, sys

#Calculate the path based on the location of the WSGI script.
#apache_configuration= os.path.dirname(__file__)
#project = os.path.dirname(apache_configuration)
#workspace = os.path.dirname(project)
#sys.path.append(workspace)

#Add the path to 3rd party django application and to django itself.
sys.path.insert(0, '/home/areplogle/dev/Booktype/')
sys.path.insert(1, '/home/areplogle/dev/Booktype/mybooktype/lib/')
sys.path.insert(2, '/home/areplogle/dev/Booktype/lib/')

os.environ['DJANGO_SETTINGS_MODULE'] = 'mybooktype.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

