from py_utils.validator.phone import cn

mobile_phone_seeds = [
    # China Mobile
    "139",
    "138",
    "137",
    "136",
    "135",
    "134",
    "159",
    "158",
    "157",
    "150",
    "151",
    "152",
    "147",
    "188",
    "187",
    "182",
    "183",
    "184",
    "178",
    # China Unicom
    "130",
    "131",
    "132",
    "156",
    "155",
    "186",
    "185",
    "145",
    "176",
    # China Telecom
    "133",
    "153",
    "189",
    "180",
    "181",
    "177",
    "173"
]


def test_mobile_phone():
    for mobile_phone in mobile_phone_seeds:
        mobile_phone = mobile_phone + "11111111"
        valid = cn.mobile_valid(mobile_phone)
        if valid is False:
            print("Mobile phone number : {} unpass".format(mobile_phone))
        assert valid == True
