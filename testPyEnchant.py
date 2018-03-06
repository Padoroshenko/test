#! /usr/bin/env python
# -*- coding: utf-8 -*-
import enchant


print enchant.list_dicts()
d = enchant.Dict("ru_RU")
print(d.check(u"около"))
print(d.check(u"Правигепьпво"))
a = d.suggest(u"Правигепьпво")[0]
print (a)