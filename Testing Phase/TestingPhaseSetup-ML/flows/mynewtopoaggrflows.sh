#s1 flows
#deaggr
ovs-ofctl add-flow s1 dl_type=2048,dl_src=12:34:56:78:9a:bc,nw_dst=99.99.99.99,action=deaggr
#DNS
ovs-ofctl add-flow s1 dl_type=2048,nw_dst=192.168.1.254,action=output:3 
ovs-ofctl add-flow s1 dl_type=2048,nw_proto=6,action=aggrs:3,1
ovs-ofctl add-flow s1 dl_type=2048,nw_proto=17,action=aggrs:3,1
#resub flows
ovs-ofctl add-flow s1 dl_type=2048,nw_dst=10.0.0.1,action=output:1
ovs-ofctl add-flow s1 dl_type=2048,nw_dst=10.0.0.2,action=output:2
#ARP 
ovs-ofctl add-flow s1 dl_type=2054,dl_dst=00:00:00:00:00:01,action=output:1
ovs-ofctl add-flow s1 dl_type=2054,dl_dst=00:00:00:00:00:02,action=output:2

#s3 flows
#deaggr             
ovs-ofctl add-flow s3 in_port=1,dl_type=2048,dl_src=12:34:56:78:9a:bc,nw_dst=99.99.99.99,action=output:2
ovs-ofctl add-flow s3 in_port=2,dl_type=2048,dl_src=12:34:56:78:9a:bc,nw_dst=99.99.99.99,action=output:1
#DNS
ovs-ofctl add-flow s3 dl_type=2048,nw_dst=192.168.1.254,action=output:2
#resub flows        
ovs-ofctl add-flow s3 dl_type=2048,nw_dst=10.0.0.0/24,action=output:1
#ARP 
ovs-ofctl add-flow s3 dl_type=2054,dl_dst=00:00:00:00:00:01,action=output:1
ovs-ofctl add-flow s3 dl_type=2054,dl_dst=00:00:00:00:00:02,action=output:1

#s7 flows
#deaggr             
ovs-ofctl add-flow s7 dl_type=2048,dl_src=12:34:56:78:9a:bc,nw_dst=99.99.99.99,action=deaggr
#DNS
ovs-ofctl add-flow s7 dl_type=2048,nw_dst=192.168.1.254,action=output:eth2
ovs-ofctl add-flow s7 dl_type=2048,nw_src=192.168.1.254,nw_dst=10.0.0.1,action=output:1
ovs-ofctl add-flow s7 dl_type=2048,nw_src=192.168.1.254,nw_dst=10.0.0.2,action=output:1
#resub flows        
ovs-ofctl add-flow s7 dl_type=2048,nw_dst=10.0.0.0/24,action=aggrs:1,2           
ovs-ofctl add-flow s7 dl_type=2048,nw_src=10.0.0.0/24,action=output:eth2
#ARP                
ovs-ofctl add-flow s7 dl_type=2054,dl_dst=00:00:00:00:00:01,action=output:1
ovs-ofctl add-flow s7 dl_type=2054,dl_dst=00:00:00:00:00:02,action=output:1






#s4 flows
#deaggr             
ovs-ofctl add-flow s4 in_port=1,dl_type=2048,dl_src=12:34:56:78:9a:bc,nw_dst=99.99.99.99,action=output:2
ovs-ofctl add-flow s4 in_port=2,dl_type=2048,dl_src=12:34:56:78:9a:bc,nw_dst=99.99.99.99,action=output:1
#DNS
ovs-ofctl add-flow s4 dl_type=2048,nw_dst=192.168.1.254,action=output:2

#resub flows        
ovs-ofctl add-flow s4 dl_type=2048,nw_dst=10.0.0.0/24,action=output:1                   
#ARP 
ovs-ofctl add-flow s4 dl_type=2054,dl_dst=00:00:00:00:00:01,action=output:1
ovs-ofctl add-flow s4 dl_type=2054,dl_dst=00:00:00:00:00:02,action=output:1


#s5 flows
#deaggr             
ovs-ofctl add-flow s5 in_port=1,dl_type=2048,dl_src=12:34:56:78:9a:bc,nw_dst=99.99.99.99,action=output:2
ovs-ofctl add-flow s5 in_port=2,dl_type=2048,dl_src=12:34:56:78:9a:bc,nw_dst=99.99.99.99,action=output:1
#DNS
ovs-ofctl add-flow s5 dl_type=2048,nw_dst=192.168.1.254,action=output:2
#resub flows        
ovs-ofctl add-flow s5 dl_type=2048,nw_dst=10.0.0.0/24,action=output:1
                                    
#ARP                
ovs-ofctl add-flow s5 dl_type=2054,dl_dst=00:00:00:00:00:01,action=output:1
ovs-ofctl add-flow s5 dl_type=2054,dl_dst=00:00:00:00:00:02,action=output:1



