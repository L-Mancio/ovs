struct eth_addr test_mac = ETH_ADDR_C(00,00,00,00,00,01);
struct eth_addr temp_mac = ETH_ADDR_C(44,34,56,78,9a,bc);
VLOG_ERR("The Ethernet address is "ETH_ADDR_FMT"\n", ETH_ADDR_ARGS(eth_preDeaggr->eth_src));
VLOG_ERR("entro in deaggr with uint16_t port = %"PRIu16, deaggr->port);
VLOG_ERR("entro in deaggr with ofp_port_t port = %ld", (size_t) u16_to_ofp(deaggr->port));

VLOG_ERR("The src Ethernet address is "ETH_ADDR_FMT"\n", ETH_ADDR_ARGS(ctx->xin->flow.dl_src));
VLOG_ERR("The dst Ethernet address is "ETH_ADDR_FMT"\n", ETH_ADDR_ARGS(ctx->xin->flow.dl_dst));
VLOG_ERR("structure of packet before change: %s ", ofp_dp_packet_to_string(ctx->xin->packet));



//print dp_packet payloads extracted
//for testing payloads
for(int j=0; j<PACKET_BUFF_ELEMENTS; j++)
{
    VLOG_ERR("payload #%d: %.*s with size of packet %d", j, recvdpackets[j].sizeofpayload, (char *) dp_packet_get_udp_payload(&recvdpackets[j].packet),
                (int) dp_packet_size(&recvdpackets[j].packet) );

}

VLOG_ERR("structure of packet before change: %s ", ofp_dp_packet_to_string(packetAggr));

VLOG_ERR("is packet that i already sent still here %s", ofp_dp_packet_to_string(hold_to_rebuild[i_csum].to_reassemble->packet));