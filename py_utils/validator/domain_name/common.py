"""
This is validate for domain_name

Author: zhangkun
History:
    Version             Author          Email                 Date                Message
    1.0.0               zhangkun      584807419@qq.com        2019-10-10          Create
"""
import re


def domain_name_valid(domain_name):
    """
    domain name validator
    :param domain_name: [str] domain_name
    :return:
    """
    r = re.match(r"(?i)^([a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{2,}$", domain_name)
    if r:
        return True
    else:
        return False
