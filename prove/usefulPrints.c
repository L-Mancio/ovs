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

/*
struct ofp_aggrs_output {
    ovs_be32 port;
    ovs_be16 fl_id;

};
OFP_ASSERT(sizeof(struct ofp_aggrs_output) == 8);
*/
ntohl(get_16aligned_be32(&iph->ip_dst))
static void
encode_AGGRS(const struct ofpact_aggrs *aggrs,
             enum ofp_version ofp_version OVS_UNUSED,
             struct ofpbuf *out )
{

    VLOG_ERR("sizeof ofpact %ld: ", sizeof(struct ofp_aggrs_output));
    printf("some aggr encoding stuff \n");
    struct ofp_aggrs_output *o_aggrs;
    o_aggrs = put_OFPAT_AGGRS(out);
    o_aggrs->port = htons(aggrs->port);
    o_aggrs->fl_id = htons(aggrs->flowid);
    printf("finished aggr encoding stuff \n");


}
static enum ofperr
decode_OFPAT_RAW_AGGRS(const struct ofp_aggrs_output *o_aggrs,
                       enum ofp_version ofp_version OVS_UNUSED, // //uint16_t p, int fl,
                       struct ofpbuf *out)
{
    //OFPAT_RAW_AGGRS generates an abstract action.
    struct ofpact_aggrs *aggrs;

    aggrs = ofpact_put_AGGRS(out);
    aggrs->port = ntohs(o_aggrs->port);
    aggrs->flowid = ntohs(o_aggrs->fl_id);

    return 0;
}
//helper for below
/*
static char * OVS_WARN_UNUSED_RESULT
parse_aggrs(char *arg, struct ofpbuf *ofpacts)
{

    struct ofpact_aggrs *aggrs;
    uint16_t port;
    int fl = 0;
    char *error;
    //char *errorfl;
    char *name = "error";
    //int errorint = 999999;
    error = str_to_u16(arg, name, &port);
    if (error) return error;
    //some error for parameter flowid, don't know how to set this tbh
    //errorfl = str_to_int(arg, errorint, &fl);
    //if (errorfl) return error;

    aggrs = ofpact_put_AGGRS(ofpacts);
    aggrs->port = port;
    aggrs->flowid = fl;
    return NULL;

}
 */
static char * OVS_WARN_UNUSED_RESULT
parse_AGGRS(char *arg, const struct ofpact_parse_params *pp OVS_UNUSED) //
{

    VLOG_ERR("esiste la virgola %p", strstr(arg,","));
    uint16_t port;

    char *error;
    printf("arg from parse_AGGRS, should contain port and id: %s %s %s \n", &arg[0], &arg[1], &arg[2]);
    struct ofpact_aggrs *aggrs;
    aggrs =  ofpact_put_AGGRS(pp->ofpacts);
    error = str_to_u16(&arg[0], "port_for_aggr", &port);
    aggrs->port = port;
    aggrs->flowid = atoi(&arg[2]);



    //str_to_u16
    //ofpact_put_AGGRS(pp->ofpacts);
    //struct ofpact_aggrs *ofpactaggrs;
    //ofpactaggrs = ofpact_put_AGGRS(pp->ofpacts);
    return error;//parse_aggrs(arg, pp->ofpacts);

}
static void
format_AGGRS(const struct ofpact_aggrs *aggrs,
             const struct ofpact_format_params *fp)
{
    printf("some aggr formatting stuff \n");
    //ds_put_format(fp->s , "%saggrs%s", colors.value, colors.end);
    ds_put_format(fp->s, "aggrs:%"PRIu16 ",flowid:%d", aggrs->port, aggrs->flowid);
}
static enum ofperr
check_AGGRS(const struct ofpact_aggrs *aggrs OVS_UNUSED,
            const struct ofpact_check_params *cp OVS_UNUSED)
{
    //return ofpact_check_output_port(aggrs->port, cp->max_ports);
    return 0;
}

//fake ack is equal to orioginal ack + size of payload
//ovs_16aligned_u32 *f_ack;
//put_16aligned_u32(f_ack, sizepayload);

//get_unaligned_u16(tcpHeadercopy->tcp_ack.hi)
//VLOG_ERR("tcpHeadercopy->tcp_ack %d"PRIu16, htons(tcpHeadercopy->tcp_ack.hi) );
//get_16aligned_u32
//ovs_be32 t_ack = get_16aligned_be32(&tcpHeadercopy->tcp_ack);

struct ds ds = DS_EMPTY_INITIALIZER;



int maxport = getmaxport(ctx->xin->ofproto);
int randport = 0;
if (maxport < 2)
{
    randport = 1;
}
if(maxport == 2 || maxport == 4 || maxport == 7)
{
    VLOG_ERR("PORT SHENANIGANS");
    randport = 2; //for testing purposes turn to 1 else 2
}
else if (maxport > 2)
{
    unsigned int seed = 0;
    int low = 3;
    int high = maxport;
    randport = (rand_r(&seed) % (high - low + 1)) + low;

}

ofp_port_t out_port = (randport > 0 && randport != (int) ctx->xin->flow.in_port.ofp_port) ? randport : maxport;