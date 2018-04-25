import uuid
import unittest
from djcom.basemodels import MemModel
from django.db import models
from django.utils import timezone
from django.utils.datetime_safe import datetime, time
from django.core.exceptions import ValidationError

class TestMemModel(MemModel):
    pkey = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50, verbose_name='Title')
    content = models.TextField(blank=True, null=True)
    floatval = models.FloatField()
    urlval = models.URLField()
    boolval = models.BooleanField(default=False)
    bintval = models.BigIntegerField(verbose_name='BigIntegerField')
    dateval = models.DateField(default=datetime.today)
    dtval = models.DateTimeField(default=timezone.now)
    timeval = models.TimeField(default=time(16, 0))
    emailval = models.EmailField()
    pintval = models.PositiveIntegerField(default=200)
    psintval = models.PositiveSmallIntegerField()
    sintval = models.SmallIntegerField()
    uuidval = models.UUIDField(default=uuid.uuid4)
    
    def __str__(self):
        result = []
        for field in self._meta.local_fields:
            result.append('%s(%s)' % (field.name, getattr(self, field.name)))
        return ', '.join(result)

class TcMemModel(unittest.TestCase):
    def test_createMemModel(self):
        obj = TestMemModel.objects.create(pkey=1, bintval=100, content='test content')
        print(obj)
        validationErr = None
        try:
            obj.full_clean()
        except ValidationError as e:
            validationErr = e
        self.assertTrue(validationErr is not None)
        objok = TestMemModel.objects.create(pkey=1, title='test title', floatval=1.0,
                                            urlval='http://ebook.yuewen.com',
                                            bintval=-2000000, emailval='zhangyang@yuewen.com',
                                            psintval=200, sintval=10)
        print(objok)
        validationErr = None
        try:
            objok.full_clean()
        except ValidationError as e:
            validationErr = e
            
        self.assertTrue(validationErr is None)
