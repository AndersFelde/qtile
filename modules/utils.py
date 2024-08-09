import socket


def has_internet(host="8.8.8.8", port=53, timeout=3) -> str:
    try:
        socket.setdefaulttimeout(timeout)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        return "󰖩 "
    except socket.error as ex:
        return "󰖪 "
    finally:
        s.close()
