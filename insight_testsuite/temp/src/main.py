# -*- coding: utf-8 -*-
"""
@author: tran
"""
# Main program
from utilities import *
import json
#batch_log_file = '../log_input/batch_log.json'
#stream_log_file = '../log_input/stream_log.json'
#flagged_file = '../log_output/flagged_purchases.json'
in_folder='../temp/log_input'#'sample_dataset'
out_folder='../temp/log_output'
print('Process data in the folder:'+in_folder)
batch_log_file = in_folder+'/batch_log.json'
stream_log_file = in_folder+'/stream_log.json'
flagged_file = out_folder+'/flagged_purchases.json'
g=open(batch_log_file,'r')
file = open(flagged_file,'w')
file.close()
l, vertex_list,amount,timestamp,T,D=initialize_nw(batch_log_file)
with open(stream_log_file) as f1:
    for line in f1:
        if len(line)>1:
            item=json.loads(line)
            l,amount,timestamp=anomalous_detection(l,amount,timestamp,item,D,T,flagged_file)

print('Process data in the folder:'+in_folder)
in_folder='../tests/test_1/log_input'#'sample_dataset'
out_folder='../tests/test_1/log_output'
batch_log_file = in_folder+'/batch_log.json'
stream_log_file = in_folder+'/stream_log.json'
flagged_file = out_folder+'/flagged_purchases.json'
file = open(flagged_file,'w')
file.close()
l, vertex_list,amount,timestamp,T,D=initialize_nw(batch_log_file)
with open(stream_log_file) as f1:
    for line in f1:
        if len(line)>1:
            item=json.loads(line)
            l,amount,timestamp=anomalous_detection(l,amount,timestamp,item,D,T,flagged_file)
print('finished')
