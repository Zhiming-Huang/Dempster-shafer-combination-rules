# Depster-shafer-combination-rules
A very simple script to realize the basic DS combination rules with just 10 lines codes

# Usage
The input is 2 Diction sets, the keys can be number or strings, whatever you like.
for example


```
a={1:0.5, 12:0.5}
b={1:0.3, 2:0.6, 12:0.1}
DSCombination(a,b)
```
The results would be
```
{1: 0.5, 2: 0.4285714285714286, 12: 0.071428571428571438}
```

or use keys with strings

```
a={'a':0.5, 'ab':0.5}
b={'b':0.3, 'abc':0.6, 'c':0.1}
DSCombination(a,b)
```
The results would be
```
{'a': 0.39999999999999997,
 'ab': 0.39999999999999997,
 'abc': 0.0,
 'b': 0.19999999999999998,
 'c': 0.0}
```
Following editions will consider the situation of confliction. 
