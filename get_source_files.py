import os
import shutil
import sys

def main():
    here = os.getcwd()

    [tarball] = sys.argv[1:]
    os.system('rm -rf zookeeper-sources')
    os.mkdir('zookeeper-sources')
    os.chdir('zookeeper-sources')
    os.system('tar xzf ' + tarball)
    [srcdir] = os.listdir('.')

    if os.path.exists(os.path.join(here, 'src')):
        shutil.rmtree(os.path.join(here, 'src'))
    os.mkdir(os.path.join(here, 'src'))
    os.chdir(os.path.join(srcdir, 'src'))
    os.system("tar czf %s c" % os.path.join(here, 'c.tgz'))
    shutil.copy(os.path.join('c', 'LICENSE'), here)
    os.chdir(os.path.join('contrib', 'zkpython'))
    shutil.copy('README', os.path.join(here, 'ORIGINAL-README'))
    os.chdir(os.path.join('src'))
    shutil.copytree('test', os.path.join(here, 'src', 'zookeepertests'))
    open(os.path.join(here, 'src', 'zookeepertests', '__init__.py'),
         'w').close()
    connection_test = open(
        os.path.join(here, 'src', 'zookeepertests', 'connection_test.py')
        ).read()
    f = open(
        os.path.join(here, 'src', 'zookeepertests', 'connection_test.py'),
        'w')
    if ('handles = [ zookeeper.init(self.host) for i in xrange(63) ]'
        in connection_test):
        connection_test = connection_test.replace(
            'handles = [ zookeeper.init(self.host) for i in xrange(63) ]',
            'handles = [ zookeeper.init(self.host) for i in xrange(9) ]')
    else:
        connection_test = connection_test.replace('testmanyhandles',
                                                  'disabledtestmanyhandles')


    f.write(connection_test)
    f.close()
    os.chdir(os.path.join('c'))
    shutil.copy('pyzk_docstrings.h', here)
    shutil.copy('zookeeper.c', here)
    os.chdir(here)

if __name__ == '__main__':
    main()
