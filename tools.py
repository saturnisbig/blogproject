#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import re

def remove_markdown_toc(content=''):
    """

    """
    pat = re.compile(r'<div class="toc">.*?<\/div>', re.S)
    return pat.sub('', content)
