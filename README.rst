About TurboGears 2 Facebook Application Middleware
--------------------------------------------------

TurboGears 2 Facebook Application Middleware is a piece of WSGI
middleware to conditionally render FB application versions of a Web
application's pages.

The planned usage is for TurboGears 2, where it can detect whether the
browser request is made to a Facebook application version of the site.
How detection is performed can be customized.  

The middleware provides an *@expose_fb_app* decorator that can be used
to conditionally render a special Facebook application version of
decorated controller methods.  In addition, it is possible to observe
the detector's descision by inspecting the *request.is_fb_app*
attribute::

    from tg import request
    request.is_fb_app


Installation
------------

tgext.fbappmiddleware can be installed both from pypi or from bitbucket::

    easy_install tgext.fbappmiddleware

or with pip (http://www.pip-installer.org/)::

    pip install tgext.fbappmiddleware

should work for most users.  To install from Github::

    pip install -e git://github.com/mtr/tgext.fbappmiddleware.git#egg=tgext.fbappmiddleware

Enabling Mobile Agents Detection
----------------------------------

In your application *config/middleware.py* import **FBAppMiddleware**:: 

    from tgext.fbappmiddleware import FBAppMiddleware

Change your **make_app** method::

    app = make_base_app(global_conf, full_stack=True, **app_conf)
    return FBAppMiddleware(app, app_conf)

Exposing FB Application Templates
---------------------------------

**tgext.fbappmiddleware** implements a *@expose_fb_app* decorator that
works like the TurboGears 2 *@expose* decorator and can be used to
specify which template to expose for Facebook application requests.

The detection may typically be done by checking the request's server
hostname.  One could for example make requests to
http://fb.example.com/ trigger the middleware's detector.

Example::

    @expose('app.templates.index')
    @expose_fb_app('app.templates.fb_app.index')
    def index(self, *args, **kw):
        return dict()


Customizing Request Type Detection
----------------------------------

You may create your own subclass of **DetectFBAppRequest**, 
or callable object and supply it as an argument to **FBAppMiddleware**, like::

    return FBAppMiddleware(app, app_conf, mobile_browser_detector=YourClass)

**DetectFBAppRequest** behaviour can be changed by any subclass by
overridding the **DetectFBAppRequest.perform_detection** method.

Acknowledgement
---------------

This WSGI extension was based on the same structure as Alessandro
Molina's https://bitbucket.org/_amol_/tgext.mobilemiddleware/src

Disclaimer
----------

Neither the authour nor this WSGI middleware extension is in any way
sponsored, endorsed or administered by, or associated with, `Facebook
<http://facebook.com/>`_.

License
-------

This software is free software: you can redistribute it and/or modify
it under the terms of the Lesser GNU General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

Please see the files COPYING and COPYING.LESSER for more information
about licensing.
