import sys
from sys import platform

from pwntk.utils.io import get_output_from_cmd, execute_cmd, kill_processes
from pwntk.utils.logger import print_check, print_error


def ensure_port_fwd():
    proccesses = []
    fwd_var = "net.ipv4.ip_forward"
    print(f"Checking ip forwarding for arquitecture: {platform}")
    if platform == "darwin":
        fwd_var = "net.inet.ip.forwarding"
    cmd_red = f"sysctl -n {fwd_var}"
    sysctl_read_out = get_output_from_cmd(cmd_red)
    fwd = int(chr(sysctl_read_out[0]))
    if fwd == 1:
        print_check("Ip forward value is 1")
    else:
        print_error(f"""Ip forwarding value is 0

Try to run this command:
        
    sudo sysctl -w {fwd_var}=1
    
        """)
        sys.exit(1)
