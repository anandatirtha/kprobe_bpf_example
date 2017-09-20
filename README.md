# kprobe_bpf_example

1. Install bcc https://github.com/iovisor/bcc/blob/master/INSTALL.md

2. `echo  > 1 /sys/kernel/debug/tracing/events/kprobes/enable` 


This is the Hello world version of dynamic tracing of kernel functions using
eBPF.

If your environment is set up properly, executing the python script `sudo
./trace_tcp.py` should
log all connect() and listen() calls made on your system.


more info here https://www.kernel.org/doc/Documentation/trace/kprobetrace.txt

