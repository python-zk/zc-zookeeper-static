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

3.4.4-1 (unreleased)
--------------------


3.4.4 (2012-09-25)
------------------

Based on Zookeeper 3.4.4.

- Include patch https://issues.apache.org/jira/browse/ZOOKEEPER-1398:
  zkpython corrupts session passwords that contain nulls.


3.4.3-5 (2012-08-23)
--------------------

Based on Zookeeper 3.4.3.

- Include patch https://issues.apache.org/jira/browse/ZOOKEEPER-1398:
  zkpython corrupts session passwords that contain nulls.

3.4.3-4 (2012-08-16)
--------------------

Based on Zookeeper 3.4.3.

- Include patch https://issues.apache.org/jira/browse/ZOOKEEPER-1339:
  C client didn't build with `--enable-debug`.

3.4.3-3 (2012-06-06)
--------------------

Based on Zookeeper 3.4.3.

- Include patch https://issues.apache.org/jira/browse/ZOOKEEPER-1318:
  In Python binding, get_children (and get and exists, and probably others)
  with expired session doesn't raise exception properly.

- Include patch https://issues.apache.org/jira/browse/ZOOKEEPER-1431:
  zkpython: async calls leak memory

3.4.3 (2012-04-20)
------------------

Based on Zookeeper 3.4.3.

3.3.5 (2012-03-24)
------------------

Based on Zookeeper 3.3.5.
