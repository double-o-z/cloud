import subprocess


def get_ip_address(port):
    output = subprocess.check_output("ipconfig", shell=True)
    for row in output.split('\n'):
        if 'IPv4 Address' in row:
            ip_address = row.split(": ")[-1].rstrip()
            return "{}:{}".format(ip_address, port)
