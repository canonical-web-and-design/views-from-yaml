import yaml

from django.conf.urls import url


def create_view(url_settings, view_callback):
    """
    Create a view function to execute the callback function with the
    url_settings
    """

    def url_view(request):
        return view_callback(request, url_settings)

    return url_view


def load_views_from_file(yaml_filepath, view_callback):
    """
    Givan a YAML file mapping URL paths to values, e.g.:

        path/one: {"some": "value"}
        path/two: {"another": "value"}

    Create a Django URL pattern from each value, so that when that path
    is requested, self.handle_url_path is run, passing the mapped value.
    """

    urlpatterns = []

    with open(yaml_filepath) as yaml_paths_file:
        url_paths = yaml.load(yaml_paths_file.read())
        if url_paths:
            for url_path, url_settings in url_paths.items():
                urlpatterns.append(
                    url(
                        r'^{0}$'.format(url_path),
                        create_view(url_settings, view_callback)
                    )
                )

    return urlpatterns
