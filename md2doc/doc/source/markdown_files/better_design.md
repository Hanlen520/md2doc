

### 归类
#### 优先级 A：非常重要的
这些规则会帮你规避错误，这里面可能存在例外，但应该非常少，且只有你同时精通 Python 和 Appium 才可以这样做。

#### 优先级 B：强烈推荐
这些规则能够改善可读性和开发体验。即使你违反了，代码还是能照常运行，但例外应该有合理的理由。

#### 优先级 C：推荐
当存在多个同样好的选项，选任意一个都可以确保一致性。在这些规则里，我们描述了每个选项并建议一个默认的选择。也就是说只要保持一致且理由充分，你可以随意在你的代码中做出不同的选择。请务必给出一个好的理由！



### 优先级 A

#### 异常捕获与处理

捕获异常时应声明异常类型，并作出对该异常的适当处理。如不需要做特殊处理，也需打印到log中，这样方便了错误处理。

###### 不好的例子
```
try:
    # ...
except Exception:
    # ...
```

```
try:
    # ...
except AttributeError:
    pass
```

###### 好例子

```
try:
    # ...
except AttributeError:
    self.log.W('Ignore but still print in log')
```


### 优先级 B

#### 布尔返回值

通常API中会带有布尔的返回值标志操作是否成功。返回时通常带有判断条件，若判断条件本来就是布尔表达式，则推荐直接返回布尔表达式；若判断条件不是布尔表达式，则可以使用bool转换表达式（Python中` if some_statement `等价于`if bool(some_statement)`）。

###### 不好的例子
```
if a == b:
    return True
else:
    return False
```

```
if self.driver.wait_element_by_name(name):
    return True
else:
    return False
```

###### 好例子
```
return a and b
```

```
return bool(self.driver.wait_element_by_name(name))
```

### 优先级 C