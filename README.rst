**Deprecated**

This module has been moved into [canonicalwebteam.yaml-responses](https://github.com/canonical-webteam/yaml-responses), and will no longer be maintained. You should now import the relevant functions from that module instead.

---

A helper function for creating views from a YAML file of URL paths
==================================================================

Installation
------------

.. code:: bash

    pip install canonicalwebteam.views-from-yaml

Usage
-----

E.g. create a YAML file:

.. code:: yaml
    # url-settings.yaml
    some/url/path: {"content": "Hello world!"}
    another/path: {"content": "Different content"}

And edit your Django app's ``urls.py``\:

.. code:: python

    # django_app/urls.py

    from canonicalwebteam.views_from_yaml import load_views_from_file

    def url_view(request, url_settings):
        return HttpResponse(url_settings['content'])

    urlpatterns = load_views_from_file(
        yaml_filepath="url-settings.yaml",
        view_callback=url_view
    )

Now if you visit `http://your-django-site/some/url/path` you should see
"Hello world!".
