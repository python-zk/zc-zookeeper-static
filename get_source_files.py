import os
import shutil
import sys

def main():
    [srcdir] = sys.argv[1:]
    here = os.getcwd()
    os.chdir(os.path.join(srcdir, 'src'))
    os.system("tar czf %s c" % os.path.join(here, 'c.tgz'))
    shutil.copy(os.path.join('c', 'LICENSE'), here)
    os.chdir(os.path.join('contrib', 'zkpython'))
    shutil.copy('README', os.path.join(here, 'ORIGINAL-README'))
    os.chdir(os.path.join('src', 'c'))
    shutil.copy('pyzk_docstrings.h', here)
    shutil.copy('zookeeper.c', here)
    os.chdir(here)

if __name__ == '__main__':
    main()
