#!/usr/bin/env python
#
# Copyright (C) 2017 The Android Open Source Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import sys

def main(argv):
    original_file = 'manifest.xml'

    if len(argv) != 4:
        raise ValueError("Wrong number of arguments %s" % len(argv))

    output_file_path = argv[1]
    override_file_path = argv[2]
    original_file = argv[3]
    fallbackPlaceholderFound = False
    with open(original_file, 'r') as input_file:
        with open(output_file_path, 'w') as output_file:
            for line in input_file:
                # If we've found the spot to add additional fonts, add them.
                if line.strip() == '</manifest>':
                    fallbackPlaceholderFound = True
                    with open(override_file_path) as override_file:
                        for override_line in override_file:
                            output_file.write(override_line)
                output_file.write(line)
    if not fallbackPlaceholderFound:
        raise ValueError('</manifest>not found in source file: %s' % original_file)

if __name__ == '__main__':
    main(sys.argv)
