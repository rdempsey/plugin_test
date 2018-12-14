# Plugin Test
This repo shows how to create a Python application with a plugin architecture.

## Requirements

For development I've been using Python 3.7. Required Python libraries are in requirements.txt.

## Building the Packages

The main library is ptest. To build it, in the root `plugin_test` directory, run:

```
pip install --editable ptest
ptest
```

The plugin is in the spam directory. Build it and run ptest with:

```
pip install --editable spam
ptest
```


## Resources

* [Implementing a Plugin Architecture in a Python Application](https://alysivji.github.io/simple-plugin-system.html)
* [Pluggy](https://pluggy.readthedocs.io/en/latest/)