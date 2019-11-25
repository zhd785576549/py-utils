"""
This is validate for chinese character

Author: zhangkun
History:
    Version             Author          Email                 Date                Message
    1.0.0               zhangkun        584807419@qq.com        2019-11-23          Create
"""


def every_character_valid(check_str):
    """
    check every chinese character from string
    :param check_str:
    :return:
    """
    for index, ch in enumerate(check_str):
        if u'\u4e00' <= ch <= u'\u9fff':
            print(f'check the character {check_str[index]} of {check_str} pass')
        else:
            print(f'check the character {check_str[index]} of {check_str} failed')
            return False
    return True


def first_character_valid(check_str):
    """
    check first chinese character from string

    in:  print(first_character_valid('中文'))
    out: True

    in:  print(first_character_valid('english'))
    out: False

    :param check_str:
    :return:
    """
    for index, ch in enumerate(check_str):
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
        else:
            return False
