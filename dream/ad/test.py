import socket

# List of IP addresses to try
ip_addresses = ["172.16.1.1", "172.16.2.2", "172.16.3.3", "172.16.4.4", "172.16.5.5", "172.16.6.6", "172.16.7.7"]

# List of strings to try sending
strings_to_send = [
    r"%+7;ELPU]`dhmruyyurmhd`]UPLE;7+%",
    r"#+.9ADPS\biorwz~~zwroib\SPDA9.+#",
    r"*1<?ENRV\adhqwz~~zwqhda\VRNE?<1*",
    r"%,/:DJPW[_bejsv{{vsjeb_[WPJD:/,%",
    r"+3=@EIOUZ]`dgntxxtngd`]ZUOIE@=3+",
    r"#&.37CJVYchpsvy~~yvsphcYVJC73.&#",
    r"*-2:@IRVZ]ehoty||ytohe]ZVRI@:2-*",
    r"$*/7:@ISX[gkou{~~{uokg[XSI@:7/*$",
    r"'+.29?CIS^cipux||xupic^SIC?92.+'",
    r"(-7?CFKOSVZcinqxxqnicZVSOKFC?7-(",
    r"'+.:>FMU\\cgmqvy||yvqmgc\\UMF>:.+'",
    r"%,17>CJTW[`djmp{{pmjd`[WTJC>71,%",
    r"&25:=AHOXbgoswz~~zwsogbXOHA=:52&",
    r"#+148>BFPV^akps||spka^VPFB>841+#"
]

def try_netcat(ip, port, data):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((ip, port))
            s.sendall(data.encode())
            response = s.recv(1024).decode()
            return response.strip()
    except (socket.timeout, socket.error):
        return None

def main():
    port = 10058  # Change this to the appropriate port number

    for ip in ip_addresses:
        print(f"Trying IP address: {ip}")
        for data in strings_to_send:
            response = try_netcat(ip, port, data)
            if response:
                print(f"Response from {ip}: {response}")
                break
            else:
                print(f"Failed to connect or no response for string: {data}")

if __name__ == "__main__":
    main()
