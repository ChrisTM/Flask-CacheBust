from setuptools import setup
setup(
    name='Flask-CacheBust',
    version='1.0.0',
    description='Flask extension that cache-busts static files',
    packages=['flask_cache_bust'],
    license='MIT',
    url='https://github.com/ChrisTM/Flask-CacheBust',
    install_requires=[
        'Flask',
    ],
)
