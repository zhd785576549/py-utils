"""
This is validate for IPv4、IPv6

Author: zhangkun
History:
    Version             Author          Email                 Date                Message
    1.0.0               zhangkun      584807419@qq.com        2019-10-10          Create
"""
import re


def ipv4_valid(ipv4):
    """
    IPv4 validator
    :param ipv4: [str] ipv4
    :return:
    """
    r = re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", ipv4)
    if r:
        return True
    else:
        return False


def ipv6_valid(ipv6):
    """
    IPv6 validator
    An IPv6 address is made of 128 bits divided into eight 16-bits blocks.
    Each block is then converted into 4-digit Hexadecimal numbers separated by colon symbols
    :param ipv6: [str] ipv6
    :return:
    """
    r = re.match(r"^(?:[A-F0-9]{1,4}:){7}[A-F0-9]{1,4}$", ipv6, re.I)
    if r:
        return True
    else:
        return False
