from icssploit.clients.s7_client import S7Client

if __name__ == '__main__':
    target = S7Client(name="s7Test", ip="192.168.218.101", rack=0, slot=3)
    target.connect()
    target.check_privilege()
    print(target.get_target_info())
