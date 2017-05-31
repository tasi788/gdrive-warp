import subprocess
import sys

dirname = sys.argv[1]


def upload(dir,dirid):
    pi = subprocess.Popen(['gdrive','sync','upload',dir,dirid],stdout=subprocess.PIPE)
    out, err = pi.communicate()
    print (out.decode('utf-8'))
def mkdir(dir):
    pi = subprocess.Popen(['gdrive','mkdir',dir],stdout=subprocess.PIPE)
    out, err = pi.communicate()
    try:
        dirid = out.decode('utf-8').split(' ')[1]
    except:
        print (out.decode('utf-8'))
        return
    upload(dir,dirid)


mkdir(dirname)

