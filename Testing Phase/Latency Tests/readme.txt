Latency tests are a bit tricky, i reduced the topology to only the parts needed for this experiment.

1. copy the customTopo and flows directories to the mininet home directory
2. copy the contents of the home dir in the mininet home directory
3. go to /root/ovs run "sh restartDB.sh"
4. open another terminal and run "ps -e | grep ovs-vswitchd" command and then "gdb ovs-vswitchd #pid", once in gdb run
5. from another terminal in the mininet home dir, run sh startmyefftopo.sh
6. from the mininet CLI then run the command "sh sh flows/myefftestnormflows.sh" for regular flows or "sh sh flows/myefftestaggrflows.sh" for the aggregation flows
7. in the latry.py script comment out in lines 190-210 the host threads we wish to start
8. in the mininet cli open xterms for h7 and h8 with command "xterm h7 h8", and in each of them start a server on localhost:80 (can be a python or php server, doesn't really matter)
9. in the mininet CLI run the command "px execfile('latry.py')", you should notice h7 and h8 receiving requests. If you are testing with aggregation flows
    gdb will start outputting logs really fast.
10. when the execution terminates, in a terminal run the command "python calcavg.py", the resulting output is the average time it took for one request


NOTE: remember to make sure the ofproto/ofproto-dpif-xlate.c variable PACKET_BUFF_ELEMENTS is set to the number of packets we want to aggregate,
if this number is changed remember to make, make install and rerun gdb, mininet only needs to rerun the flow installation with the command:
NOTE: it also might occurr when aggregation flows install that packets keep coming even after the program execution has terminated. best way i found to avoid
this issue for now was to restart gdb waiting for the requests to complete. This is especially weird considering i kill the curl processes when the timer
in latry.py expires.
NOTE: To significantly improve this experiment I recommend finding a way to run one ovs instance for each switch, and modifying the aggregation action to
remove the use of the dictionary. This problematic is also addressed in the thesis and should be the first thing to consider in a continuation of this
reaserch project.