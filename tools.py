#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import re

def remove_markdown_toc(content=''):
    """

    """
    pat = re.compile(r'<div class="toc">.*?<\/div>', re.S)
    return pat.sub('', content)

def pip_upgrade_outdated():
    """
    https://blog.csdn.net/yuzhucu/article/details/80287307
    升级所有的库，不够合理，还是应该升级过期的库
    """
    import pip
    from subprocess import call
    from pip._internal.utils.misc import get_installed_distributions

    for dist in get_installed_distributions():
        call("pip install --upgrade " + dist.project_name, shell=True)



if __name__ == "__main__":
    # pip_upgrade_outdated()
