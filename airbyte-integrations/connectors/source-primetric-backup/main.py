#
# Copyright (c) 2022 Airbyte, Inc., all rights reserved.
#


#import sys

#from airbyte_cdk.entrypoint import launch
#from source_primetric import SourcePrimetric
from source_my_test_name.run import run


if __name__ == "__main__":
    run()
    #source = SourcePrimetric()
    #launch(source, sys.argv[1:])
