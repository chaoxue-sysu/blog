# Python基础
## 杂记
**2021.4.29: collections.defaultdict()的使用**
>Python中通过Key访问字典，当Key不存在时，会引发‘KeyError’异常。为了避免这种情况的发生，可以使用collections类中的defaultdict()方法来为字典提供默认值。<br>
语法格式：
collections.defaultdict([default_factory[, …]])<br>
该函数返回一个类似字典的对象。defaultdict是Python内建字典类（dict）的一个子类，它重写了方法_missing_(key)，增加了一个可写的实例变量default_factory,实例变量default_factory被missing()方法使用，如果该变量存在，则用以初始化构造器，如果没有，则为None。其它的功能和dict一样。<br>
第一个参数为default_factory属性提供初始值，默认为None；其余参数包括关键字参数（keyword arguments）的用法，和dict构造器用法一样。<br>
————————————————
原文链接：https://blog.csdn.net/yangsong95/article/details/82319675


Example:
```python
import collections
dt=collections.defaultdict(list)
dt['a'].append('b')

## 相当于普通字典
dt={}
if not dt.has_key('a'):
    dt['a']=[]
dt['a'].append('b')
```