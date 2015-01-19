Flask-CacheBust is a Flask extension that adds a distinct hash to the URL of
each static file. The hash changes whenever the content of the file changes,
allowing your webserver to safely declare the resource as indefinitely
cacheable.

# Usage

Install Flask-CacheBust by placing the "flask_cache_bust" file somewhere
importable from Python. Import the extension and use it to augment your app:

```python
from flask.ext import cache_bust

# ...

cache_bust.init_cache_busting(app)
```

The `url_for` function will now cache-bust your files. For example, this
template:

```html
<script src="{{ url_for('static', filename='js/main.min.js') }}"></script>
```

will render like this:

```html
<script src="/static/1fc6e32/js/main.min.js"></script>
```

and the "1fc6e32" part will change whenever "main.min.js" changes. Now you can
configure long cache expiration dates on your static files!
