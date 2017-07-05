# -*- coding: utf-8 -*-
"""
@author: tran
"""
# Main program, process data in the folder in_folder='../log_input' and store output in the folder out_folder='../log_output'
from utilities import *
import json
in_folder='../log_input'#'sample_dataset'
out_folder='../log_output'
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
print('finished')
