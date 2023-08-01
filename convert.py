import ipaddress

def cidr_to_ip_range(cidr_block):
    network = ipaddress.IPv4Network(cidr_block, strict=False)
    return str(network.network_address), str(network.broadcast_address)

input_file = 'cidrs.txt'
output_file = 'result.txt'

with open(input_file, 'r') as infile:
    cidr_blocks = infile.read().splitlines()

with open(output_file, 'w') as outfile:
    for cidr_block in cidr_blocks:
        start_ip, end_ip = cidr_to_ip_range(cidr_block)
        outfile.write(f"{cidr_block} -> IP Range: {start_ip} - {end_ip}\n")
