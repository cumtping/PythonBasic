# http://www.runoob.com/python/python-reg-expressions.html

# re.match(pattern, string, flags=0)
# how many flags are there?
# group(num=0) ?
# groups() ?
# 

import re

print (re.match('www', 'www.baidu.com').span() ) # what is span? ret:(0, 3)
print (re.match('com', 'www.baidu.com')) # ret: None

line = "Cats are smarter than dogs"

# 1. What does r mean? no escape character.
# 2. What is re.M and re.I ? re.I, ignore case; re.M, multiple mode;
#    re.L, depend on locale; re.S, match all characters;
#    re.U, depend on Unicode; re.X, detail mode;
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

if matchObj:
   print ("matchObj.group() : ", matchObj.group())
   print ("matchObj.group(1) : ", matchObj.group(1))
   print ("matchObj.group(2) : ", matchObj.group(2))
else:
   print ("No match!!")

# search
searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)
 
if searchObj:
   print ("searchObj.group() : ", searchObj.group())
   print ("searchObj.group(1) : ", searchObj.group(1))
   print ("searchObj.group(2) : ", searchObj.group(2))
else:
   print ("Nothing found!!")

# what's the difference between match and search?
# match only match the start of the string; while search match the whole string;


# re.sub(pattern, repl, string, count=0, flags=0)
phone = "2004-959-559"
 
num = re.sub(r'#.*$', "", phone)
print ("num=", num)
 
num = re.sub(r'\D', "", phone)
print ("num2=", num)

def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)
 
s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))

#模式	描述
#^	匹配字符串的开头
#$	匹配字符串的末尾。
#.	匹配任意字符，除了换行符，当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符。
#[...]	用来表示一组字符,单独列出：[amk] 匹配 'a'，'m'或'k'
#[^...]	不在[]中的字符：[^abc] 匹配除了a,b,c之外的字符。
#re*	匹配0个或多个的表达式。
#re+	匹配1个或多个的表达式。
#re?	匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式
#re{ n}	
#re{ n,}	精确匹配n个前面表达式。
#re{ n, m}	匹配 n 到 m 次由前面的正则表达式定义的片段，贪婪方式
#a| b	匹配a或b
#(re)	G匹配括号内的表达式，也表示一个组
#(?imx)	正则表达式包含三种可选标志：i, m, 或 x 。只影响括号中的区域。
#(?-imx)	正则表达式关闭 i, m, 或 x 可选标志。只影响括号中的区域。
#(?: re)	类似 (...), 但是不表示一个组
#(?imx: re)	在括号中使用i, m, 或 x 可选标志
#(?-imx: re)	在括号中不使用i, m, 或 x 可选标志
#(?#...)	注释.
#(?= re)	前向肯定界定符。如果所含正则表达式，以 ... 表示，在当前位置成功匹配时成功，否则失败。但一旦所含表达式已经尝试，匹配引擎根本没有提高；模式的剩余部分还要尝试界定符的右边。
#(?! re)	前向否定界定符。与肯定界定符相反；当所含表达式不能在字符串当前位置匹配时成功
#(?> re)	匹配的独立模式，省去回溯。
#\w	匹配字母数字及下划线
#\W	匹配非字母数字及下划线
#\s	匹配任意空白字符，等价于 [\t\n\r\f].
#\S	匹配任意非空字符
#\d	匹配任意数字，等价于 [0-9].
#\D	匹配任意非数字
#\A	匹配字符串开始
#\Z	匹配字符串结束，如果是存在换行，只匹配到换行前的结束字符串。c
#\z	匹配字符串结束
#\G	匹配最后匹配完成的位置。
#\b	匹配一个单词边界，也就是指单词和空格间的位置。例如， 'er\b' 可以匹配"never" 中的 'er'，但不能匹配 "verb" 中的 'er'。
#\B	匹配非单词边界。'er\B' 能匹配 "verb" 中的 'er'，但不能匹配 "never" 中的 'er'。
#\n, \t, 等.	匹配一个换行符。匹配一个制表符。等
#\1...\9	匹配第n个分组的内容。
#\10	匹配第n个分组的内容，如果它经匹配。否则指的是八进制字符码的表达式。


#实例	描述
#[Pp]ython	匹配 "Python" 或 "python"
#rub[ye]	匹配 "ruby" 或 "rube"
#[aeiou]	匹配中括号内的任意一个字母
#[0-9]	匹配任何数字。类似于 [0123456789]
#[a-z]	匹配任何小写字母
#[A-Z]	匹配任何大写字母
#[a-zA-Z0-9]	匹配任何字母及数字
#[^aeiou]	除了aeiou字母以外的所有字符
#[^0-9]	匹配除了数字外的字符



