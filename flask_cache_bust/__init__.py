import hashlib
import os


def init_cache_busting(app):
    """
    Configure `app` to so that `url_for` adds a unique prefix to URLs generated
    for the `'static'` endpoint. Also make the app able to serve cache-busted
    static files.

    This allows setting long cache expiration values on static resources
    because whenever the resource changes, so does its URL.
    """

    static_folder = app.static_folder  # the rooted path to the static file folder

    bust_table = {}  # map from an unbusted filename to a busted one
    unbust_table = {}  # map from a busted filename to an unbusted one

    app.logger.debug('Computing cache-busting values...')
    # compute (un)bust tables.
    for dirpath, dirnames, filenames in os.walk(static_folder):
        for filename in filenames:
            # compute version component
            rooted_filename = os.path.join(dirpath, filename)
            with open(rooted_filename, 'r') as f:
                version = hashlib.md5(f.read()).hexdigest()[:7]

            # add version
            unbusted = os.path.relpath(rooted_filename, static_folder)
            busted = os.path.join(version, unbusted)

            # save computation to tables
            bust_table[unbusted] = busted
            unbust_table[busted] = unbusted
    app.logger.debug('Finished computing cache-busting values')

    def bust_filename(filename):
        return bust_table.get(filename, filename)

    def unbust_filename(filename):
        return unbust_table.get(filename, filename)

    @app.url_defaults
    def reverse_to_cache_busted_url(endpoint, values):
        """
        Make `url_for` produce busted filenames when using the 'static' endpoint.
        """
        if endpoint == 'static':
            values['filename'] = bust_filename(values['filename'])

    def debusting_static_view(filename):
        """
        Serve a request for a static file having a busted name.
        """
        return original_static_view(filename=unbust_filename(filename))

    # Replace the default static file view with our debusting view.
    original_static_view = app.view_functions['static']
    app.view_functions['static'] = debusting_static_view
