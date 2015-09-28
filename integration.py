#!/usr/bin/env python3
#
# Copyright (C) 2004-2015 ZNC, see the NOTICE file for details.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


import pexpect
import subprocess
import sys
import time
import tempfile
import unittest

from contextlib import contextmanager


class TestZNC(unittest.TestCase):

    @contextmanager
    def run_znc(self):
        znc = subprocess.Popen(['./znc', '--debug', '--datadir', self.config])
        yield
        znc.terminate()
        # TODO: bump python requirements to 3.3 and use znc.wait(timeout=30) instead.
        # Ubuntu Precise on Travis has too old python.
        self.assertEqual(0, znc.wait())


    @contextmanager
    def run_ircd(self):
        ircd = pexpect.spawnu('socat', ['stdio', 'tcp6-listen:12345,reuseaddr'])
        yield ircd
        ircd.terminate()


    @contextmanager
    def run_client(self):
        client = pexpect.spawnu('socat', ['stdio', 'tcp6:[::1]:12345'])
        yield client
        client.terminate()


    def test_connect(self):
        with self.run_ircd() as ircd:
                time.sleep(3)
                with self.run_client() as client:
                    client.sendline('PASS :hunter2')
                    ircd.expect_exact('hunter2')
                    ircd.sendline('Welcome')
                    client.expect_exact('Welcome')


if __name__ == '__main__':
    unittest.main()

