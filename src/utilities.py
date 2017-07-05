
#This file contains the following functions
#1. add_to_list: to add value(node id, time stamp, amount purchase) to 
#the corresponding list l
#2. remove_edge: to remove edge
#3. purchase(new_purchase,log_file,time_stamp,qnw,s): what needs to be done
#when a purchase is made.
#4. def bfs(s,i,D,T): find the D-netowrk of the node i using breath first seach
#5. initialize_nw(batch_log_file): to generate network, amount purchased from each node and timestamp form batch_log_file
# 
def add_to_list(l,id1,value):
    # To add to list of vertices, edges or purchases 
    if len(l)>id1:#9994  
        if len(l[id1])==0:
            l[id1].append(id1)
        l[id1].append(value)
    else:         
        for i in range(len(l),id1+1):
            l.append([])
        l[id1].append(id1)
        l[id1].append(value)
    return l   

def remove_edge(l,id1uf,id2uf):
    # To remove edge from list of vertices that are adjacent to a node
    if len(l)>id1uf:
           if id2uf in l[id1uf]: 
               l[id1uf].remove(id2uf)
    if len(l)>id2uf:
           if id1uf in l[id2uf]: 
               l[id2uf].remove(id1uf)
    return l
def purchase(new_purchase,log_file,time_stamp,qnw,s):
    #from datetime import datetime as dt
    import numpy as np
    mean_s=np.mean(s)
    sd_s=np.std(s)
    #new_purchase is good send everyon on qnw.
    if (np.abs(new_purchase-mean_s)>3*sd_s):
        file = open(log_file,'a')
        for id in qnw[1:]:
            str1="{\"event_type\":\"purchase\", \"timestamp\":\""
            str1=str1+time_stamp+"\",\"id\":"+"\"" + str(id) + "\", \"amount\": \""+str(new_purchase)+"\", \"mean\": \""
            str1=str1+str(round(mean_s,2))+"\", \"sd\": \""+str(round(sd_s,2))+"\"}\n"
            file.write(str1)
        file.close()
# In[]
def bfs(s,i,D,T):
    #This function will find the tree by breadth first search
    #print('newnewnew')
    depth=0;stop=0;current_element=0;last_element=0;q=[i];
    while stop==0:
        if last_element==len(q) and len(s[q[-1]])==1:
            stop =1;break #stop at leaft node
        if current_element==last_element:
            if last_element<len(q):
                depth+=1
                last_element=len(q)
                if depth==D+1:
                    stop =1;break
            else:
                stop=1;break
        tem=s[q[current_element]]
        if len(tem)>1:
            #must remove all vertex already in the nw before adding
            for i in tem:
                if i not in q:
                    q.append(i)
            current_element +=1;
    return q
# In[4]
def initialize_nw(batch_log_file):
    import json
    with open(batch_log_file) as f:
        objects = [json.loads(line) for line in f]
    l=[];
    vertex_list=[];
    D=int(objects[0]['D'])
    T=int(objects[0]['T'])
    objects1=objects[1:]
    amount=[];
    timestamp=[];
    for item in objects1:
        if (item['event_type']=='purchase'):
            id=int(item['id'])
            amount=add_to_list(amount,id,float(item['amount']))
            timestamp=add_to_list(timestamp,id,item['timestamp'])
            if len(l)>id:
                if len(l[id])==0:
                    l[id].append(id)
        if (item['event_type']=='befriend'):
            id1bf=int(item['id1'])
            id2bf=int(item['id2'])
            l=add_to_list(l,id1bf,id2bf)
            l=add_to_list(l,id2bf,id1bf)
        if (item['event_type']=='unfriend'):
            id1uf=int(item['id1'])
            id2uf=int(item['id2'])
            l=remove_edge(l,id1uf,id2uf)         
    return l, vertex_list,amount,timestamp,T,D;
# In[6]
def anomalous_detection(l,amount,timestamp,item,D,T,flagged_file):
    #Need to modify the code to be able to update the D-networks quick/automatically
    #when new edge is added or an edge is removed.
        #if new edge
    if (item['event_type']=='befriend'):
        id1bf=int(item['id1'])
        id2bf=int(item['id2'])
        l=add_to_list(l,id1bf,id2bf)
        l=add_to_list(l,id2bf,id1bf)
        #If new purchase:
    if (item['event_type']=='purchase'):#if (item['event_type']=='purchase'):            
        id=int(item['id'])
        amount=add_to_list(amount,id,float(item['amount']))
        timestamp=add_to_list(timestamp,id,item['timestamp'])
        qnw = bfs(l,id,D,T)
        purchase(float(item['amount']),flagged_file,item['timestamp'],qnw,amount[id][-1*min(T,len(amount[id])-1):])
    if (item['event_type']=='ufriend'):
        id1bf=int(item['id1'])
        id2bf=int(item['id2'])
        l=remove_edge(l,id1bf,id2bf)
        l=remove_edge(l,id2bf,id1bf)
    return l,amount,timestamp
