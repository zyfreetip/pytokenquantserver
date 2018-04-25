import sys
import platform
import l5sys
from time import time
from datetime import timedelta
from urllib.request import urlopen

if sys.platform == 'win32':
    cmdencode = 'gbk'
else:
    cmdencode = 'utf8'

def isWindowsSystem():
    return 'Windows' in platform.system()

def isLinuxSystem():
    return 'Linux' in platform.system()


def dateRange(start, end, filterFunc=None, reverse=False):
    delta = end - start
    if not reverse:
        for idx in range(delta.days+1):
            dtobj = (start + timedelta(days=idx))
            if filterFunc and not filterFunc(dtobj):
                continue
            yield dtobj
    else:
        for idx in range(delta.days+1):
            dtobj = (end - timedelta(days=idx))
            if filterFunc and not filterFunc(dtobj):
                continue
            yield dtobj

def L5GetRoute(modId, cmdId, timeout=0.2):
    ret,qos = l5sys.ApiGetRoute({'modId':modId,'cmdId':cmdId}, timeout)
    if ret < 0:
        return ret
    tmstart = time()
    iret = 0
    use_time = int((time() - tmstart) * 1000000)
    l5sys.ApiRouteResultUpdate(qos,iret,use_time)
    addr = 'http://' + qos['hostIp'].decode() + ':' + str(qos['hostPort'])
    return addr

def CheckUrlAvailable(url=None, timeout=5):
    try:
        if url == None:
            return False
        ret = urlopen(url, timeout=timeout)
        if ret.code == 200:
            return True
        else:
            return False
    except:
            return False

