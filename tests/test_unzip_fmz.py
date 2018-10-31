import os,os.path
import zipfile
import shutil
 
def zip_dir(dirname,zipfilename):
    filelist = []
    if os.path.isfile(dirname):
        filelist.append(dirname)
    else :
        for root, dirs, files in os.walk(dirname):
            for name in files:
                filelist.append(os.path.join(root, name))
        
    zf = zipfile.ZipFile(zipfilename, "w", zipfile.zlib.DEFLATED)
    for tar in filelist:
        arcname = tar[len(dirname):]
        #print arcname
        zf.write(tar,arcname)
    zf.close()
 
 
def unzip_file(zipfilename, unziptodir):
    if not os.path.exists(unziptodir): os.mkdir(unziptodir, 0o777)
    zfobj = zipfile.ZipFile(zipfilename)
    for name in zfobj.namelist():
        name = name.replace('\\','/')
       
        if name.endswith('/'):
            os.mkdir(os.path.join(unziptodir, name))
        else:            
            ext_filename = os.path.join(unziptodir, name)
            ext_dir= os.path.dirname(ext_filename)
            if not os.path.exists(ext_dir) : os.mkdir(ext_dir,0o777)
            outfile = open(ext_filename, 'wb')
            outfile.write(zfobj.read(name))
            outfile.close()
 
if __name__ == '__main__':
    #zip_dir(r'E:/python/learning',r'E:/python/learning/zip.zip')
    #unzip_file(r'E:/python/learning/zip.zip',r'E:/python/learning2')
    path = '/Users/qiaoxiaofeng/Downloads/2018-02/'
    dst_path = '/Users/qiaoxiaofeng/Downloads/bitfinex/2018-02'
    files = os.listdir(path)
    for file in files:
        if not os.path.isdir(file):
            if file.endswith('.zip'):
                filepath = path+'/'+file
                unzip_file(filepath,dst_path)
    
    # 将BTCUSDT的TICK数据拷贝到BTCUSDT目录
    dst_btcusd_path = '/Users/qiaoxiaofeng/Downloads/bitfinex/BTCUSD/2018-02'
    for root, dirs, files in os.walk(dst_path):
        for dir in dirs:
            if dir == 'BTCUSD':
                path = os.path.join(root, dir)
                files = os.listdir(path)
                for file in files:
                    if file.endswith('.csv'):
                        #filepath = path + '/' + file
                        filepath = os.path.join(path,file)
                        dstfilepath = os.path.join(dst_btcusd_path,file)
                        shutil.copyfile(filepath, dstfilepath)
            elif dir.startswith('bitfinex'):
                d_path = os.path.join(path,dir)
                for root1, dirs1, files1 in os.walk(d_path):
                    for dir in dirs1:
                        if dir == 'BTCUSD':
                            path = os.path.join(root1, dir)
                            files = os.listdir(path)
                            for file in files:
                                filepath = os.path.join(path, file)
                                dstfilepath = os.path.join(dst_btcusd_path,file)
                                shutil.copyfile(filepath, dstfilepath)
                            