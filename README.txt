ZooKeeper Python bindings
=========================

This is a self-contained distribution of the ZooKeeper Python
bindings. It should build on any unix-like system by just running the
``setup.py`` script or using an install tool like pip, easy_install or
buildout. (Windows patches to the setup script are welcome. :)

For more information **except** building instructions, see the file
ORIGINAL-README included in the source distribution.

If you have setuptools or distribute in your python path, then you can
use the ``setup.py test`` command to run the tests.  Note, however,
that the tests require that a testing ZooKeeper server be running on
port 22182 of the local machine.

You can find the source code of this distribution at
https://github.com/python-zk/zc-zookeeper-static

Changelog
=========

3.4.3 (2012-04-20)
------------------

Based on Zookeeper 3.4.3.
