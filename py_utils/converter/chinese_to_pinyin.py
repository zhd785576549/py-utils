"""
Convert Chinese characters to Pinyin acronyms

Author: zhangkun
History:
    Version             Author          Email                 Date                Message
    1.0.0               zhangkun        584807419@qq.com      2019-11-23          Create
"""


def single_get_first(unicode1):
    str1 = unicode1.encode('gbk')
    try:
        ord(str1)
        return str1.decode('gbk')
    except:
        asc = str1[0] * 256 + str1[1] - 65536
        if -20319 <= asc <= -20284:
            return 'a'
        if -20283 <= asc <= -19776:
            return 'b'
        if -19775 <= asc <= -19219:
            return 'c'
        if -19218 <= asc <= -18711:
            return 'd'
        if -18710 <= asc <= -18527:
            return 'e'
        if -18526 <= asc <= -18240:
            return 'f'
        if -18239 <= asc <= -17923:
            return 'g'
        if -17922 <= asc <= -17418:
            return 'h'
        if -17417 <= asc <= -16475:
            return 'j'
        if -16474 <= asc <= -16213:
            return 'k'
        if -16212 <= asc <= -15641:
            return 'l'
        if -15640 <= asc <= -15166:
            return 'm'
        if -15165 <= asc <= -14923:
            return 'n'
        if -14922 <= asc <= -14915:
            return 'o'
        if -14914 <= asc <= -14631:
            return 'p'
        if -14630 <= asc <= -14150:
            return 'q'
        if -14149 <= asc <= -14091:
            return 'r'
        if -14090 <= asc <= -13119:
            return 's'
        if -13118 <= asc <= -12839:
            return 't'
        if -12838 <= asc <= -12557:
            return 'w'
        if -12556 <= asc <= -11848:
            return 'x'
        if -11847 <= asc <= -11056:
            return 'y'
        if -11055 <= asc <= -10247:
            return 'z'
        return ''


def trans_chinese_to_pinyin_arabic(string):
    """
    in：  print(trans_chinese_to_pinyin_arabic('得到拼音首字母缩写'))
    out:  ddpyszmsx
    :param string:
    :return:
    """
    if not string:
        return None
    lst = list(string)
    char_list = []
    for l in lst:
        char_list.append(single_get_first(l))
    return ''.join(char_list)
