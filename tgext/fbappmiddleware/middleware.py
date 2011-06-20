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

from webob import Request
import re

class DetectFBAppRequest(object):
    """Detect Facebook application request
    """
    
    def __init__(self, application, config):
        super(DetectFBAppRequest, self).__init__()
        
        self.fb_host_prefix_re = re.compile(r'^fb\..+$', re.IGNORECASE)
        
    def _recognize_fb_hostname_prefix(self, hostname):
        return bool(self.fb_host_prefix_re.match(hostname))
    
    def perform_detection(self, request):
        hostname = request.headers.get('Host', None)
        
        return hostname and self._recognize_fb_hostname_prefix(hostname)
    
    def __call__(self, request):
        return self.perform_detection(request)
    
class FBAppMiddleware(object):
    def __init__(self, application, config,
                 fb_app_request_detector=DetectFBAppRequest):
        self.application = application
        
        if isinstance(fb_app_request_detector, type):
            self.detect_fb_app = fb_app_request_detector(application, config)
        else:
            self.detect_fb_app = fb_app_request_detector
            
    def __call__(self, environ, start_response):
        request = Request(environ)
        
        request.is_fb_app = bool(self.detect_fb_app(request))
        
        response = request.get_response(self.application)
        
        return response(environ, start_response)
