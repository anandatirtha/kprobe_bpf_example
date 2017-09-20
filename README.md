# kprobe_bpf_example

First step
install bcc https://github.com/iovisor/bcc/blob/master/INSTALL.md

Second step
echo  > 1 /sys/kernel/debug/tracing/events/kprobes/enable 


This is the Hello world version of dynamic tracing of kernel functions using
eBPF.

If your environment is set up properly, executing the python script should
log all connect() and listen() calls made on your system



