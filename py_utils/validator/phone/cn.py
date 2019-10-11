"""
This is validate for phone in China

Author: Winter
History:
    Version             Author          Email                 Date                Message
    1.0.0               Winter        785576549@qq.com        2019-10-10          Create
"""
import re


def mobile_valid(mobile):
    """
    Mobile phone number validator
    :param mobile: [str] Mobile phone number
    :return:
    """
    r = re.match(r"^1[345789]\d{9}$", mobile)
    if r:
        return True
    else:
        return False


def telephone_valid(telephone):
    """
    Whole station telephone number validator
    :param telephone: [str] Telephone number
    :return:
    """
    r = re.match(r"0\d{2,3}-\d{7,8}", telephone)
    if r:
        return True
    else:
        return False


def tj_telephone_valid(telephone):
    """
    TianJin telephone number validator
    :param telephone: [str] Telephone number
    :return:
    """
    r = re.match(r"^022-\d{7,8}$", telephone)
    if r:
        return True
    else:
        return False
