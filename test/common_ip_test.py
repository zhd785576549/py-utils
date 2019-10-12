from py_utils.validator.ip_address import common

ipv4_list = [
    "113.194.30.119",
    "120.83.105.162",
    "49.70.89.67",
    "1.197.204.72",
    "0.0.0.0",
    "255.255.255.255",
    "127.0.0.1"
]


def test_ipv4():
    for i in ipv4_list:
        valid = common.ipv4_valid(i)
        if valid is False:
            print("IPv4 address : {} unpass".format(i))
        assert valid == True


ipv6_list = [
    "0000:0000:0000:0000:0000:0000:0000:0000",
    "ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff",
    "1050:0000:0000:0000:0005:0600:300c:326b",
    "1050:0:0:0:5:600:300c:326b",
    "2001:0db8:85a3:08d3:1319:8a2e:0370:7344",
    "2001:0db8:85a3:0000:1319:8a2e:0370:7344",
    "2001:0DB8:0000:0000:0000:0000:1428:57ab",
    "2001:0DB8:0:0:0:0:1428:57ab",
    "0000:0000:0000:0000:0000:0000:874B:2B34",
]


def test_ipv6():
    for i in ipv6_list:
        valid = common.ipv6_valid(i)
        if valid is False:
            print("IPv6 address : {} unpass".format(i))
        assert valid == True
