Flask-CacheBust is a Flask extension that adds a hash to the URL of each static
file. This lets you safely declare your static resources as indefinitely
cacheable because they automatically get new URLs when their contents change.

# Usage

Install Flask-CacheBust by placing the "flask_cache_bust" folder somewhere
importable from Python. Import the extension and use it to augment your app:

```python
from flask.ext import cache_bust

# ...

cache_bust.init_cache_busting(app)
```

The `url_for` function will now cache-bust your static files. For example, this
template:

```html
<script src="{{ url_for('static', filename='js/main.min.js') }}"></script>
```

will render like this:

```html
<script src="/static/1fc6e32/js/main.min.js"></script>
```

The "1fc6e32" part will change whenever "main.min.js" changes. Now you can
configure long cache expiration dates on your static files!

# Motivation

This was originally written for www.cloudboltsoftware.com while exercising an
obsession for minimizing page load time and delivering a snappy browsing
experience. It improves over Last-Modified or ETag cache schemes by enabling an
expiration date to be set, which removes round-trip checks to see if a
browser's cached version of a resource is still valid.
