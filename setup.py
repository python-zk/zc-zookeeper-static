#  Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

name, version = 'zookeeper-static', '3.3.3a1'

install_requires = ['setuptools']
extras_require = dict(test=[])

entry_points = """
"""

import distutils.command.build_ext
import distutils.core
import os
import shutil
import time

def do_system(cmd):
    print cmd
    if os.system(cmd):
        raise SystemError("Failed: %s" % cmd)

class build_ext(distutils.command.build_ext.build_ext):

    def run(self):
        # Hack to build C sources first
        if os.path.exists('c'):
            print "Removing old c directory"
            shutil.rmtree('c')
        do_system("tar xzf c.tgz")
        os.utime("c/config.h.in", (time.time(), time.time()))
        do_system("cd c; ./configure; make")

        distutils.command.build_ext.build_ext.run(self)

distutils.core.setup(
    author = 'Henry Robinson',
    author_email = 'henry@cloudera.com',
    license = 'Apache',

    name = name, version = version,
    long_description=open('README.txt').read(),
    description = open('README.txt').read().strip().split('\n')[0],
    cmdclass={'build_ext': build_ext},
    ext_modules=[
        distutils.core.Extension(
            "zookeeper",
            sources=["zookeeper.c"],
            include_dirs=["c/include",
                          "c/generated"],
            extra_objects=["c/.libs/libzookeeper_mt.a"],
            )
        ],
    )

