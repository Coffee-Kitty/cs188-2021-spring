

# cs188 Project 0 spring 2021

## 包括的大致内容

> 1.unix教程

> 2.如何启动正确python版本

> 3.Python教程

> 4.成绩评定（运行在自己机器上！！！）



要编辑和提交的文件：

您将在作业期间在tutorial.zip中填写addition.py、buyLotsOfFruit.py和shopSmart.py的部分内容。

评估：

请不要更改代码中任何提供的函数或类的名称，否则会对autorader造成严重破坏。然而，你执行的正确性——而不是自动评分者的判断——将是你得分的最终判断。如有必要，我们将单独审查和评分作业，以确保您的工作获得应有的学分

 

由于用的windows教程，课程unix指令不做学习



### anconda环境搭建



conda易于管理多环境。避免python版本冲突等



然后本人安装的是anaconda5.3.0，据此网址：[(200条消息) Anaconda超详细安装教程（Windows环境下）_windows安装conda_菜鸟1号！！的博客-CSDN博客](https://blog.csdn.net/fan18317517352/article/details/123035625)

![image-20230421232420156](C:\Users\86185\AppData\Roaming\Typora\typora-user-images\image-20230421232420156.png)

 

Creating a Conda Environment

The command for creating a conda environment with Python 3.6 is:

```
conda create --name <env-name> python=3.6
```

For us, we decide to name our environment `cs188`, so we run the following command, and press `y` to confirm installing any missing packages.

```
[cs188-ta@nova ~/python_basics]$ conda create --name cs188 python=3.6
```

我就也创建一个cs188命名的吧！



Entering the Environment

To enter the conda environment that we just created, do the following. Note that the Python version within the environment is 3.6, just what we want.

```
[cs188-ta@nova ~/python_basics]$ source activate cs188
(cs188) [cs188-ta@nova ~/python_basics]$ python -V
Python 3.6.6 :: Anaconda, Inc.
```

Note: the tag `(<env-name>)` shows you the name of the conda environment that is active. In our case, we have `(cs188)`, as what we’d expect.

Leaving the Environment

Leaving the environment is just as easy.

```
(cs188) [cs188-ta@nova ~/python_basics]$ source deactivate
[cs188-ta@nova ~/python_basics]$ python -V
Python 3.5.2 :: Anaconda custom (x86_64)
```

Our python version has now returned to whatever the system default is!

 也就是说source activate激活虚拟环境cs188，而source deactivate退出呗！

在windows中，咱这个这样用

![image-20230421235659684](C:\Users\86185\AppData\Roaming\Typora\typora-user-images\image-20230421235659684.png)





使用实验室机器目前，学生没有在实验室机器上下载Python 3.6或Conda的正确权限。对于P0，Python 3.5（已经安装）就足够了。

 ### Python教程

Table of Contents

- [Invoking the Interpreter](https://inst.eecs.berkeley.edu/~cs188/sp21/project0/#Invoking_the_Interpreter)
- [Operators](https://inst.eecs.berkeley.edu/~cs188/sp21/project0/#Operators)
- [Strings](https://inst.eecs.berkeley.edu/~cs188/sp21/project0/#Strings)
- [Dir and Help](https://inst.eecs.berkeley.edu/~cs188/sp21/project0/#Dir_and_Help)
- Built-in Data Structures
  - [Lists](https://inst.eecs.berkeley.edu/~cs188/sp21/project0/#Lists)
  - [Tuples](https://inst.eecs.berkeley.edu/~cs188/sp21/project0/#Tuples)
  - [Sets](https://inst.eecs.berkeley.edu/~cs188/sp21/project0/#Sets)
  - [Dictionaries](https://inst.eecs.berkeley.edu/~cs188/sp21/project0/#Dictionaries)
- [Writing Scripts](https://inst.eecs.berkeley.edu/~cs188/sp21/project0/#Writing_Scripts)
- [Indentation](https://inst.eecs.berkeley.edu/~cs188/sp21/project0/#Indentation)
- [Tabs vs Spaces](https://inst.eecs.berkeley.edu/~cs188/sp21/project0/#TabsSpaces)
- [Writing Functions](https://inst.eecs.berkeley.edu/~cs188/sp21/project0/#Writing_Functions)
- Object Basics
  - [Defining Classes](https://inst.eecs.berkeley.edu/~cs188/sp21/project0/#Defining_Classes)
  - [Using Objects](https://inst.eecs.berkeley.edu/~cs188/sp21/project0/#Using_Objects)
  - [Static vs Instance Variables](https://inst.eecs.berkeley.edu/~cs188/sp21/project0/#Static_vs_Instance_Variables)
- [Tips and Tricks](https://inst.eecs.berkeley.edu/~cs188/sp21/project0/#Tips_and_Tricks)
- [Troubleshooting](https://inst.eecs.berkeley.edu/~cs188/sp21/project0/#Troubleshooting)
- [More References](https://inst.eecs.berkeley.edu/~cs188/sp21/project0/#More_References)

 

这里只挑几条记录



#### 1.Dir and Help

Learn about the methods Python provides for strings. To see what methods Python provides for a datatype, use the `dir` and `help` commands:

```
>>> s = 'abc'

>>> dir(s)
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__str__', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'replace', 'rfind', 'rindex', 'rjust', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

>>> help(s.find)
Help on built-in function find:

find(...) method of builtins.str instance
    S.find(sub[, start[, end]]) -> int

    Return the lowest index in S where substring sub is found,
    such that sub is contained within S[start:end].  Optional
    arguments start and end are interpreted as in slice notation.

    Return -1 on failure.


>>> s.find('b')
1
```

Note: Ignore functions with underscores “_” around the names; these are private helper methods. Press ‘q’ to back out of a help screen.



![image-20230422000225180](C:\Users\86185\AppData\Roaming\Typora\typora-user-images\image-20230422000225180.png)



#### 2.List:

注意：+号可以用于list

​			然后就是 -1索引   从右到左第一个呗。

​			append增加

​			pop从尾部弹出

3.详细的[start:end]     其实是【start:end)介绍呗

We can also index multiple adjacent elements using the slice operator. For instance, `fruits[1:3]`, returns a list containing the elements at position 1 and 2. In general `fruits[start:stop]` will get the elements in `start, start+1, ..., stop-1`. We can also do `fruits[start:]` which returns all elements starting from the `start` index. Also `fruits[:end]` will return all elements before the element at position `end`:

```
>>> fruits[0:2]
['apple', 'orange']
>>> fruits[:3]
['apple', 'orange', 'pear']
>>> fruits[2:]
['pear', 'pineapple']
>>> len(fruits)
4
```



#### 3.Tuple

注意tuple内容不可变

A data structure similar to the list is the *tuple*, which is like a list except that it is immutable once it is created (i.e. you cannot change its content once created). Note that tuples are surrounded with parentheses while lists have square brackets.

```
>>> pair = (3, 5)
>>> pair[0]
3
>>> x, y = pair
>>> x
3
>>> y
5
>>> pair[1] = 6
TypeError: object does not support item assignment
```



#### 4.Sets

无重复的无序序列

A *set* is another data structure that serves as an unordered list with no duplicate items. Below, we show how to create a set:

```
>>> shapes = ['circle', 'square', 'triangle', 'circle']
>>> setOfShapes = set(shapes)
```



Another way of creating a set is shown below:

```
>>> setOfShapes = {‘circle’, ‘square’, ‘triangle’, ‘circle’}
```



add方法加入set，集合的交&  集合的并| 集合的差 -

Next, we show how to add things to the set, test if an item is in the set, and perform common set operations (difference, intersection, union):

```
>>> setOfShapes
set(['circle', 'square', 'triangle'])
>>> setOfShapes.add('polygon')
>>> setOfShapes
set(['circle', 'square', 'triangle', 'polygon'])
>>> 'circle' in setOfShapes
True
>>> 'rhombus' in setOfShapes
False
>>> favoriteShapes = ['circle', 'triangle', 'hexagon']
>>> setOfFavoriteShapes = set(favoriteShapes)
>>> setOfShapes - setOfFavoriteShapes
set(['square', 'polygon'])
>>> setOfShapes & setOfFavoriteShapes
set(['circle', 'triangle'])
>>> setOfShapes | setOfFavoriteShapes
set(['circle', 'square', 'triangle', 'polygon', 'hexagon'])
```



#### 5.字典

```
>>> studentIds = {'knuth': 42.0, 'turing': 56.0, 'nash': 92.0}
>>> studentIds['turing']
56.0
>>> studentIds['nash'] = 'ninety-two'
>>> studentIds
{'knuth': 42.0, 'turing': 56.0, 'nash': 'ninety-two'}
>>> del studentIds['knuth']
>>> studentIds
{'turing': 56.0, 'nash': 'ninety-two'}
>>> studentIds['knuth'] = [42.0, 'forty-two']
>>> studentIds
{'knuth': [42.0, 'forty-two'], 'turing': 56.0, 'nash': 'ninety-two'}
>>> studentIds.keys()
['knuth', 'turing', 'nash']
>>> studentIds.values()
[[42.0, 'forty-two'], 56.0, 'ninety-two']
>>> studentIds.items()
[('knuth', [42.0, 'forty-two']), ('turing',56.0), ('nash', 'ninety-two')]
>>> len(studentIds)
3
```



#### 6.函数式编程 

类似jdk stream流，嘿嘿

If you like functional programming you might also like `map` and `filter`:

```
>>> list(map(lambda x: x * x, [1, 2, 3]))
[1, 4, 9]
>>> list(filter(lambda x: x > 3, [1, 2, 3, 4, 5, 4, 3, 2, 1]))
[4, 5, 4]
```



#### 7.Tabs vs Spaces

这意味着，如果您的Python文件从使用制表符作为缩进切换到使用空格作为缩进，Python解释器将无法解决缩进级别的歧义并引发异常。



#### 8.Advanced Exercise

从未想过快排就这几行

```python
def quickSort(lis):
    if len(lis) <= 1:
        return  lis
    
    smaller = [x for x in lis[1:] if x < lis[0]]
    bigger = [x for x in lis[1:] if x >= lis[0]]
    return quickSort(smaller) + [lis[0]] + quickSort(bigger)
```



#### 9.Static vs Instance Variables

The following example illustrates how to use static and instance variables in Python.

Create the `person_class.py` containing the following code:

```
class Person:
    population = 0

    def __init__(self, myAge):
        self.age = myAge
        Person.population += 1

    def get_population(self):
        return Person.population

    def get_age(self):
        return self.age
```



We first compile the script:

```
[cs188-ta@nova ~]$ python person_class.py
```

Now use the class as follows:

```
>>> import person_class
>>> p1 = person_class.Person(12)
>>> p1.get_population()
1
>>> p2 = person_class.Person(63)
>>> p1.get_population()
2
>>> p2.get_population()
2
>>> p1.get_age()
12
>>> p2.get_age()
63
```



In the code above, `age` is an instance variable and `population` is a static variable. `population` is shared by all instances of the `Person` class whereas each instance has its own `age` variable.

就类变量和实例变量呗



## Autograding

To get you familiarized with the autograder, we will ask you to code, test, and submit a token after solving the three questions.

You can download all of the files associated the autograder tutorial as a zip archive: [tutorial.zip](https://inst.eecs.berkeley.edu/~cs188/sp21/assets/files/tutorial.zip) (note this is **different** from the zip file used in the UNIX and Python mini-tutorials, python_basics.zip). Unzip this file and examine its contents:、

This contains a number of files you’ll edit or run:

- `addition.py`: source file for question 1
- `buyLotsOfFruit.py`: source file for question 2
- `shop.py`: source file for question 3
- `shopSmart.py`: source file for question 3
- `autograder.py`: autograding script (see below)

and others you can ignore:

- `test_cases`: directory contains the test cases for each question
- `grading.py`: autograder code
- `testClasses.py`: autograder code
- `tutorialTestClasses.py`: test classes for this particular project
- `projectParams.py`: project parameters



```
[cs188-ta@nova ~/tutorial]$ python autograder.py
Starting on 1-21 at 23:39:51

Question q1
===========
*** FAIL: test_cases/q1/addition1.test
*** 	add(a, b) must return the sum of a and b
*** 	student result: "0"
*** 	correct result: "2"
*** FAIL: test_cases/q1/addition2.test
*** 	add(a, b) must return the sum of a and b
*** 	student result: "0"
*** 	correct result: "5"
*** FAIL: test_cases/q1/addition3.test
*** 	add(a, b) must return the sum of a and b
*** 	student result: "0"
*** 	correct result: "7.9"
*** Tests failed.
```



**查看问题1的结果，您可以看到它已经失败了三次测试，并显示错误消息“add（a，b）must return the sum of a and b”。代码给出的答案总是0，但正确的答案不同。我们将在下一个选项卡中解决这个问题。**





## Question 2: buyLotsOfFruit function

Implement the `buyLotsOfFruit(orderList)` function in `buyLotsOfFruit.py` which takes a list of `(fruit,numPounds)` tuples and returns the cost of your list. If there is some `fruit` in the list which doesn’t appear in `fruitPrices` it should print an error message and return `None`. Please do not change the `fruitPrices` variable.

Run `python autograder.py` until question 2 passes all tests and you get full marks. Each test will confirm that `buyLotsOfFruit(orderList)` returns the correct answer given various possible inputs. For example, `test_cases/q2/food_price1.test` tests whether:

```
 [('apples', 2.0), ('pears', 3.0), ('limes', 4.0)] is 12.25
```

------

```python
def buyLotsOfFruit(orderList):
    """
        orderList: List of (fruit, numPounds) tuples

    Returns cost of order
    """
    totalCost = 0.0
    "*** YOUR CODE HERE ***"
    for i in range(len(orderList)):
        fruit_price = fruitPrices[orderList[i][0]]
        if(fruit_price == None):
            print("%s have no price" % orderList[i][0])
            return None
        totalCost += fruit_price*orderList[i][1]
    return totalCost


```





## Question 3: shopSmart function

Fill in the function `shopSmart(orderList,fruitShops)` in `shopSmart.py`, which takes an `orderList` (like the kind passed in to `FruitShop.getPriceOfOrder`) and a list of `FruitShop` and returns the `FruitShop` where your order costs the least amount in total. Don’t change the file name or variable names, please. Note that we will provide the `shop.py` implementation as a “support” file, so you don’t need to submit yours.

Run `python autograder.py` until question 3 passes all tests and you get full marks. Each test will confirm that `shopSmart(orderList,fruitShops)` returns the correct answer given various possible inputs. For example, with the following variable definitions:

```
orders1 = [('apples', 1.0), ('oranges', 3.0)]
orders2 = [('apples', 3.0)]
dir1 = {'apples': 2.0, 'oranges': 1.0}
shop1 =  shop.FruitShop('shop1',dir1)
dir2 = {'apples': 1.0, 'oranges': 5.0}
shop2 = shop.FruitShop('shop2', dir2)
shops = [shop1, shop2]
```



```
test_cases/q3/select_shop1.test` tests whether: `shopSmart.shopSmart(orders1, shops) == shop1
```

and `test_cases/q3/select_shop2.test` tests whether: `shopSmart.shopSmart(orders2, shops) == shop2`



```python
def shopSmart(orderList, fruitShops):
    """
        orderList: List of (fruit, numPound) tuples
        fruitShops: List of FruitShops
    """
    "*** YOUR CODE HERE ***"
    index = -1
    min_cost = float("inf")
    for i in range(len(fruitShops)):
        cost = fruitShops[i].getPriceOfOrder(orderList)
        if cost <= min_cost:
            index = i
        min_cost = min(cost, min_cost) 

    return fruitShops[index]
```

