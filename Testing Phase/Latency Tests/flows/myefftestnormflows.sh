#s1 flows
ovs-ofctl add-flow s1 dl_type=2048,nw_dst=10.0.0.1,action=output:1
ovs-ofctl add-flow s1 dl_type=2048,nw_dst=10.0.0.2,action=output:2
ovs-ofctl add-flow s1 dl_type=2048,nw_dst=10.0.0.3,action=output:3
ovs-ofctl add-flow s1 dl_type=2048,nw_dst=10.0.0.4,action=output:4
ovs-ofctl add-flow s1 dl_type=2048,nw_dst=10.0.0.5,action=output:5
ovs-ofctl add-flow s1 dl_type=2048,nw_dst=10.0.0.6,action=output:6
ovs-ofctl add-flow s1 dl_type=2048,nw_dst=10.0.0.7,action=output:7
ovs-ofctl add-flow s1 dl_type=2048,nw_dst=10.0.0.8,action=output:7
#ARP 
ovs-ofctl add-flow s1 dl_type=2054,dl_dst=00:00:00:00:00:01,action=output:1
ovs-ofctl add-flow s1 dl_type=2054,dl_dst=00:00:00:00:00:02,action=output:2
ovs-ofctl add-flow s1 dl_type=2054,dl_dst=00:00:00:00:00:03,action=output:3
ovs-ofctl add-flow s1 dl_type=2054,dl_dst=00:00:00:00:00:04,action=output:4
ovs-ofctl add-flow s1 dl_type=2054,dl_dst=00:00:00:00:00:05,action=output:5
ovs-ofctl add-flow s1 dl_type=2054,dl_dst=00:00:00:00:00:06,action=output:6
ovs-ofctl add-flow s1 dl_type=2054,dl_dst=00:00:00:00:00:07,action=output:7
ovs-ofctl add-flow s1 dl_type=2054,dl_dst=00:00:00:00:00:08,action=output:7

#s3 flows
#deaggr             
#resub flows        
ovs-ofctl add-flow s3 dl_type=2048,nw_dst=10.0.0.1,action=output:1
ovs-ofctl add-flow s3 dl_type=2048,nw_dst=10.0.0.2,action=output:1
ovs-ofctl add-flow s3 dl_type=2048,nw_dst=10.0.0.3,action=output:1
ovs-ofctl add-flow s3 dl_type=2048,nw_dst=10.0.0.4,action=output:1
ovs-ofctl add-flow s3 dl_type=2048,nw_dst=10.0.0.5,action=output:1
ovs-ofctl add-flow s3 dl_type=2048,nw_dst=10.0.0.6,action=output:1
ovs-ofctl add-flow s3 dl_type=2048,nw_dst=10.0.0.7,action=output:2
ovs-ofctl add-flow s3 dl_type=2048,nw_dst=10.0.0.8,action=output:2
#ARP 
ovs-ofctl add-flow s3 dl_type=2054,dl_dst=00:00:00:00:00:01,action=output:1
ovs-ofctl add-flow s3 dl_type=2054,dl_dst=00:00:00:00:00:02,action=output:1
ovs-ofctl add-flow s3 dl_type=2054,dl_dst=00:00:00:00:00:03,action=output:1
ovs-ofctl add-flow s3 dl_type=2054,dl_dst=00:00:00:00:00:04,action=output:1
ovs-ofctl add-flow s3 dl_type=2054,dl_dst=00:00:00:00:00:05,action=output:1
ovs-ofctl add-flow s3 dl_type=2054,dl_dst=00:00:00:00:00:06,action=output:1
ovs-ofctl add-flow s3 dl_type=2054,dl_dst=00:00:00:00:00:07,action=output:2
ovs-ofctl add-flow s3 dl_type=2054,dl_dst=00:00:00:00:00:08,action=output:2

#s7 flows       
#aggrs     
ovs-ofctl add-flow s7 dl_type=2048,nw_dst=10.0.0.1,action=output:1                                           
ovs-ofctl add-flow s7 dl_type=2048,nw_dst=10.0.0.2,action=output:1                                           
ovs-ofctl add-flow s7 dl_type=2048,nw_dst=10.0.0.3,action=output:1                                 
ovs-ofctl add-flow s7 dl_type=2048,nw_dst=10.0.0.4,action=output:1   
ovs-ofctl add-flow s7 dl_type=2048,nw_dst=10.0.0.5,action=output:1   
ovs-ofctl add-flow s7 dl_type=2048,nw_dst=10.0.0.6,action=output:1                              
ovs-ofctl add-flow s7 dl_type=2048,nw_dst=10.0.0.7,action=output:2
ovs-ofctl add-flow s7 dl_type=2048,nw_dst=10.0.0.8,action=output:3
#ARP                
ovs-ofctl add-flow s7 dl_type=2054,dl_dst=00:00:00:00:00:01,action=output:1
ovs-ofctl add-flow s7 dl_type=2054,dl_dst=00:00:00:00:00:02,action=output:1
ovs-ofctl add-flow s7 dl_type=2054,dl_dst=00:00:00:00:00:03,action=output:1
ovs-ofctl add-flow s7 dl_type=2054,dl_dst=00:00:00:00:00:04,action=output:1
ovs-ofctl add-flow s7 dl_type=2054,dl_dst=00:00:00:00:00:05,action=output:1
ovs-ofctl add-flow s7 dl_type=2054,dl_dst=00:00:00:00:00:06,action=output:1
ovs-ofctl add-flow s7 dl_type=2054,dl_dst=00:00:00:00:00:07,action=output:2
ovs-ofctl add-flow s7 dl_type=2054,dl_dst=00:00:00:00:00:08,action=output:3





