Coffee Compressor Compiler
=========================

[![Build Status](https://travis-ci.org/Juvenal1228/coffee-compressor-compiler.png?branch=master)](https://travis-ci.org/Juvenal1228/coffee-compressor-compiler)

Purpose
-------

This tool is meant to be used as an extension to [django-compressor](https://github.com/jezdez/django_compressor)

It precompiles [coffee-script](http://coffeescript.org/)


Features
--------

- platform independent
- no need to install node.js packages
- 100% test coverage
- [PEP 8](http://www.python.org/dev/peps/pep-0008/) compliance
- [semver](http://semver.org/) compliance


Installing
----------

Install with pip/easy_install from the pypi

`pip install coffee-compressor-compiler`

or clone the latest source

    git clone https://github.com/Juvenal1228/coffee-compressor-compiler.git
    cd coffee-compressor-compiler
    python setup.py install

You must also install [node.js](http://nodejs.org/) or [PyV8](https://code.google.com/p/pyv8/)

The latest versions of node.js can be found [here](http://nodejs.org/download/)

Using
-----

Using this tool is as simple as installing it and adding it to the `COMPRESS_PRECOMPILERS` django setting

```python
COMPRESS_PRECOMPILERS = (
    ('text/coffeescript', 'coffeecompressorcompiler.filter.CoffeeScriptCompiler'),
)
```

Then, in your django templates you can embed coffee-script templates like so
```html+django
{% load staticfiles %}
{% load compress %}

{% compress js %}
<script type="text/coffeescript" src="{% static 'app/main.coffee' %}" ></script>
<script type="text/coffeescript">
    console.log 'Hello!'
    alert 'Hello!'
</script>
{% endcompress %}
```
