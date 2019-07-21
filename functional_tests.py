#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Teddy' in browser.title

