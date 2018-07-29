#encoding=utf8
from time import time
from djcom.utils import ts2dt
from blockcomm.net.exceptions import LogicErrorException, LogicAssertException
from django.utils import timezone
from random import Random
from django.core.mail import send_mail
from django.conf import settings
from blockuser.models import EmailVerifyRecord
import code

EMAIL_FROM = settings.get('EMAIL_FROM', '')
SITE_URL = settings.get('SITE_URL', '')
def dt2jsonint(dt):
    if not dt: return 0
    return int(dt.timestamp() * 1000)

def jsonint2dt(jsonint):
    return ts2dt(jsonint)

def dbtm2jsonint(dt):
    if not dt:
        return 0
    return int(timezone.localtime(dt).timestamp() * 1000)

def currentTimestamp():
    return int(time() * 1000)

class GuessParams(object):
    def __init__(self, request, jrequest):
        self.request = request
        self.jrequest = jrequest

    def _guessParam(self, keys, param=None, default=None):
        if type(param) in (int, str):
            return param
        if param is None:
            paramDict = self.jrequest
        elif isinstance(param, dict):
            paramDict = param
        else:
            raise LogicErrorException('unknown type param(%s)' % repr(param))
        for key in keys:
            param = paramDict.get(key, None)
            if param is not None:
                return param
        if default is not None:
            return default
        else:
            raise LogicErrorException('can not get param(%s)' % keys[0])

def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0, length)]
    return str

def send_register_email(email, send_type='register'):
    email_record = EmailVerifyRecord()
    code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()
    email_title = ''
    email_body = ''
    if send_type == 'register':
        email_title = '注册激活链接'
        email_body = '请点击下面的链接激活你的账号:' + SITE_URL + 'active/' + code
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email]) 
        if send_status:
            pass
        else:
            print('email send failed')
        
    