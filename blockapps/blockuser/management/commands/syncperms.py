#encoding=utf8
import importlib
from django.core.management.base import BaseCommand
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission
from django.contrib.auth.management import create_permissions
from django.apps import apps
from bookuser.models import BookUser

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.syncCustomPermissions()
        self.add_view_permissions()
        self.syncOtherPerms()

    def add_view_permissions(self):
        # for each of our content types
        for content_type in ContentType.objects.all():
            # build our permission slug
            codename = "view_%s" % content_type.model
    
            # if it doesn't exist..
            if not Permission.objects.filter(content_type=content_type, codename=codename):
                # add it
                Permission.objects.create(content_type=content_type,
                                          codename=codename,
                                          name="Can view %s" % content_type.name)
                print("Added view permission for %s" % content_type.name)

    def syncOtherPerms(self, *args, **options):
        for app_config in apps.get_app_configs():
            app_config.models_module = True
            print('try create_permissions app_config %s' % app_config)
            create_permissions(app_config, apps=apps, verbosity=2)
            app_config.models_module = None

    def syncCustomPermissions(self):
        content_type = ContentType.objects.get_for_model(BookUser)
        for app_config in apps.get_app_configs():
            try:
                perms = importlib.import_module(app_config.name+'.perms', None)
            except ImportError as e:
                continue
            print('start create permission for %s' % app_config.name)
            for name, permcls in perms.__dict__.items():
                if name != 'Permissions': continue
                print('got Permissions class')
                for key, val in permcls.__dict__.items():
                    if not key.startswith('perm_'): continue
                    for permname, permdesc in val:
                        self._createPerm(content_type, permname, permdesc)
                        
    def _createPerm(self, content_type, permname, permdesc):
        ContentType.objects
        # if it doesn't exist..
        if not Permission.objects.filter(content_type=content_type, codename=permname):
            # add it
            Permission.objects.create(content_type=content_type,
                                      codename=permname,
                                      name=permdesc)
            print("Added permission(%s) for %s" % (permname, content_type.name))
