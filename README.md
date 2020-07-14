<div align="center">
<img alt="spy image" src="assets/spy.png"/>
</div>

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
See the [tests](https://github.com/ziord/spy/blob/master/tests) folder.


### Caution
spy does not work for built-in types. See [tests](https://github.com/ziord/spy/blob/master/tests) for more information.


### License
[MIT](https://github.com/ziord/spy/blob/master/LICENSE.txt)