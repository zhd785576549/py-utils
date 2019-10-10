"""
This is validate for email

Author: zhangkun
History:
    Version             Author          Email                 Date                Message
    1.0.0               zhangkun      584807419@qq.com        2019-10-10          Create
"""
import re


def email_valid(email_address):
    """
    email validator
    :param email_address: [str] email_address
    :return:
    """
    r = re.match(r"[^@]+@[^@]+\.[^@]+", email_address)
    if r:
        return True
    else:
        return False
