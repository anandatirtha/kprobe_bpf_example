from bcc import BPF

# Hello BPF Program
bpf_text = """ 
#include <net/inet_sock.h>
#include <bcc/proto.h>

// 1. Attach kprobe to "inet_listen"
int kprobe__inet_listen(struct pt_regs *ctx, struct socket *sock, int backlog)
{
    bpf_trace_printk("Hello World!\\n");
    return 0;
};
int kprobe__ip_rcv(struct pt_regs *ctx, struct sk_buff *skb)
{
    bpf_trace_printk("ip_rcv!\\n");
    return 0;
};
"""

# 2. Build and Inject program
b = BPF(text=bpf_text)

# 3. Print debug output
while True:
    print b.trace_readline()

