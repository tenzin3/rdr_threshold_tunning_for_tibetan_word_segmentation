import os
import sys

from ..pSCRDRtagger.RDRPOSTagger import run


#sys.argv = ['RDRPOSTagger.py', 'train', 'TIB_tagged.txt']
#sys.argv = ['RDRPOSTagger.py', 'tag', 'resources\TIB_tagged.txt.RDR', 'resources\TIB_tagged.txt.DICT', 'data\TIB_test_maxmatched.txt']


run(['RDRPOSTagger.py', 'tag', 'resources\TIB_tagged.txt.RDR', 'resources\TIB_tagged.txt.DICT', '.\data\TIB_test_maxmatched.txt'])

