from py_utils.validator.email import common

email_address = ['ymhy25@china.com', 'odge4@enet.com.cn', 'x0dqv3lr@163.net', 'gk5ivn06yb3@yahoo.com.cn',
                 'ufqjp0cu0xypb@netease.com', 'gex@xinhua.net', 'q2sxerp115@hotmail.com', 'y1hhorsq@35.com',
                 'mwq11@china.com', 'ykwvyzvrf53@qq.com', 'cyb64ieh0ikm@35.com', 'u6c1vg@etang.com',
                 'qpz6nslyhku@sina.com', '12yrqnklnhr@hotmail.com', '5j2lw2qpq@enet.com.cn', '4tfb@msn.com',
                 'ei54whv2ebsp@yahoo.com.cn', 'z4oic4mlmtxip@netease.com', 'nix1samgeaa@163.com', 'w5wn0i@etang.com',
                 'f4z3tk65fe@netease.com', 'hfy6zrieb4a4o3@yeah.net', '4301c0cvncg@tom.com', 'mzyp@265.com',
                 'bylnd6y6eohm@35.com', '2ke@163.net', 'lpb6gb@eastday.com', 'o5uw3foo50@qq.com', 'u60zvj@eastday.com',
                 'ojcwjjo34d1paj@etang.com', '3n3fskwd1cf@21cn.com', 'hicqltg@21cn.com', 'b2h10uwblknrr@163.com',
                 'o03pagburtjf@sohu.com', 'vuwqqrt4t@eyou.com', 'mrvkgdu@sina.com',
                 '6qs3g5uyltzrh@yeah.net', '1r6hngri@21cn.com', 's0z5wi0@126.com', 'qlxwozb@tom.com',
                 '1xr2b4nm@56.com', 'ofvb4sudioa1@35.com', 'jr5nq0cuo2j33@eyou.com', ]


def test_email():
    for i in email_address:
        valid = common.email_valid(i)
        if valid is False:
            print("email address : {} unpass".format(i))
        assert valid == True
