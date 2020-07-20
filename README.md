<p align="center">
    <p align="center">
        <img alt="spy image" src="assets/spy.png" >
    </p>
    <p align="center">
        <a href="https://www.python.org/">
            <img alt="built with python" src="https://img.shields.io/badge/built%20with-python-blue.svg?style=plastic" >
        </a>
        <a href="https://github.com/ziord/spy/blob/master/LICENSE.txt">
            <img alt="Spy License" src="https://img.shields.io/github/license/ziord/spy?style=plastic" >
        </a>
        <a href="https://www.python.org/downloads/">
            <img alt="python versions (3.6+)" src="https://img.shields.io/badge/python-3.6+-blue.svg?style=plastic">
        </a>
        <a href="https://github.com/ziord/spy/issues" >
            <img alt="issues" src="https://img.shields.io/github/issues/ziord/spy?style=plastic">
        </a>
        <a href="https://github.com/ziord/spy/stargazers">
            <img alt="stars" src="https://img.shields.io/github/stars/ziord/spy?style=plastic">
        </a>
        <a href="https://github.com/ziord/spy/network/members">
            <img alt="forks" src="https://img.shields.io/github/forks/ziord/spy?style=plastic">
        </a>
    </p>
</p>
<br/>

# spy

spy is a package that enables automated _cloning_ of **user-defined** Python classes.

### Example

```python
from spy.cc import clone

class SimpleOriginal:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name})"

    def foo(self):
        return self.name + 'foo'
    
    def bar(self):
        return self.name + 'bar'


@clone(SimpleOriginal)
class SimpleClone:
    pass


# tests
sc_obj = SimpleClone('test')
print(sc_obj.foo())  # testfoo
print(sc_obj.bar())  # testbar
print(sc_obj)  # SimpleClone(test)
print(type(sc_obj))  # <class '__main__.SimpleClone'>
print(sc_obj.foo, sc_obj.bar)  
# <bound method SimpleClone.foo of SimpleClone(test)> <bound method SimpleClone.bar of SimpleClone(test)>
```

### Tests
Tested for Python 3.7, compatible with Python 3.6+.
See the [tests](https://github.com/ziord/spy/blob/master/tests) folder.


### Installation
Clone this repo, and do:

`cd spy` <br/> `python setup.py install`


### Caution
spy does not work for built-in types. See [tests](https://github.com/ziord/spy/blob/master/tests) for more information.


### License
[MIT](https://github.com/ziord/spy/blob/master/LICENSE.txt)