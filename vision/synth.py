# Copyright 2018 Google LLC
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

"""This script is used to synthesize generated parts of this library."""

import synthtool as s
from synthtool import gcp

gapic = gcp.GAPICGenerator()

versions = ['v1', 'v1p1beta1', 'v1p2beta1']


for version in versions:
    library = gapic.py_library('vision', version)

    s.move(library / f'google/cloud/vision_{version}/gapic')
    # Don't move over __init__.py, as we modify it to make ImageAnnotatorClient
    # use vision_helpers.
    s.move(library / f'google/cloud/vision_{version}/types.py')
    s.move(library / f'google/cloud/vision_{version}/proto')
    s.move(library / f'tests/unit/gapic/{version}')
