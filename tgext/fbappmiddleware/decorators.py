#! /usr/bin/python
# -*- coding: utf-8 -*-
"""
Copyright (C) 2011 by Martin Thorsen Ranang <mtr@ranang.org>

This file is part of tgext.FBAppMiddleware.

tgext.FBAppMiddleware is free software: you can redistribute it and/or
modify it under the terms of the Lesser GNU General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

tgext.FBAppMiddleware is distributed in the hope that it will be
useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the Lesser
GNU General Public License for more details.

You should have received a copy of the Lesser GNU General Public
License along with tgext.FBAppMiddleware.  If not, see
<http://www.gnu.org/licenses/>.
"""
__author__ = "Martin Thorsen Ranang"

from tg import request, config
from tg.decorators import Decoration

class expose_fb_app(object):
    def __init__(self, template, content_type='text/html'):
        if template in config.get('renderers', []):
            engine, template = template, ''
        elif ':' in template:
            engine, template = template.split(':', 1)
        elif template:
            engine = config.get('default_renderer')
        else:
            engine, template = None, None

        self.template = template
        self.engine = engine
        self.content_type = content_type

    def hook_func(self, *args, **kwargs):
        if request.is_fb_app:
            try:
                override_mapping = request._override_mapping
            except:
                override_mapping = request._override_mapping = {}
                
            override_mapping[self.func] = {self.content_type:
                                           (self.engine, self.template, [])}
            
    def __call__(self, func):
        self.func = func
        deco = Decoration.get_decoration(func)
        deco.register_hook('before_render', self.hook_func)
        return func
