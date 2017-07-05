This program is will identify anomalous purchase made by an user and notify all people in his/her network. The main idea is to construct the network from the batch file and store in a list of adjacency edges for each node.

Each time when a new purchase is made by a node i, decide if this purchase is anomalous or not, run breath first search with starting point from node i to find the D-network of i and notify everyone in this network.

To run the code on the test sets: change the folder to anomaly_detection-master_Hoang and run run.sh, this will run the file test.py

To run the code on other data set:

1. Store data in the folder: in_folder='../log_input' and change this correspondingly in the file main.py

2. Prepare the output folder: out_folder='../log_output'
