#
# Copyright (c) 2025 Airbyte, Inc., all rights reserved.
#


import sys

from airbyte_cdk.entrypoint import launch
from .source import SourceMyTestName

def run():
    source = SourceMyTestName()
    launch(source, sys.argv[1:])
