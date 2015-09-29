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

    def test_connect(self):
        for i in range(1, 100):
            x = pexpect.spawnu('echo', ['hello'])
            x.expect_exact('hello')


if __name__ == '__main__':
    unittest.main()

