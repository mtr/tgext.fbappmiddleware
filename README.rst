About Facebook Application Middleware
-------------------------------------

Facebook App Middleware is a middleware for WSGI applications.

The planned usage is for TurboGears 2, where it can detect whether the
browser request is made to a Facebook application version of the site.
How detection is performed can be customized.  

The middleware provides an @expose_fb that can be used to
conditionally render a special Facebook application version of
decorated controller methods.  In addition, it is possible to observe
the detector's descision by inspecting the *request.is_fb_app*
attribute::

    from tg import request
    request.is_fb_app


Installation
------------

tgext.fbappmiddleware can be installed both from pypi or from bitbucket::

    easy_install tgext.fbappmiddleware

or 

    pip install tgext.fbappmiddleware

should work for most users.

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
