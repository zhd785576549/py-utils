# py-utils

![PyPI - License](https://img.shields.io/pypi/l/py-utils)

py-utils is a collector of python tools.Welcome all people come in this project, and provide normal and usual tools for python.We record in this page.
    
# Feature

Include bellow categories:

- Time
- Validator

# Usage

Just import package or module in your project, you must not write these again and again in each project, like this:

```python

from py_utils.validator.phone import cn
cn.mobile_valid("13XXXXXXXXX")
```

This will return True

```python

from py_utils.validator.phone import cn
cn.mobile_valid("13XXXX")
```

This will return False

# History

|Module|Author|Date|Version|Description|
|------|------|-----|------|-----------|
|py_utils.validator.phone.cn|Winter|2019-10-10|1.0.0|Validator for phone number in China|
|py_utils.valodator.email.global|zhangkun|2019-10-10|1.0.0|Validator for email address|

# Requirement

# License

MIT License
