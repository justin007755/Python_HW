
下面是我自己学习《learn python the hardway》的笔记，是按章节来组织的，最后有一个总结。

**Ex1（A Good First Program）**  

1）可以用单引号和双引号：  
print 'Yay! Printing.'  
print "I'd much rather you 'not'."  
print 'I "said" do not touch this.'

======  
Python 3

print("Hello World!")  
print('I "said" do not touch this.')  
print('100 + 200 =', 100 + 200)  

print()会依次打印每个字符串，遇到逗号“,”会输出一个空格，  

======

2）如果有关于ASCII encoding的问题，可以在文件最前面加上如下内容。其实这一行也会被Python忽略，但它是一个hack or workaround用来检测文件的格式。  
"# -*- coding: utf-8 -*-"  
这行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。此时还有编码问题，可以写成如下格式，强制为utf编码。
print u'好消息'

**Ex2（Comments and Pound Characters）**  

注释：  
"# A comment, this is so you can read your program later."  
"# Anything after the # is ignored by python."  
print "I could have code like this." # and the comment after is ignored
….

How do I comment out multiple lines? --> Put a # in front of each one.

**Ex3（Numbers and Math）**

为了保持计算更准确，需要用浮点数，即floating point。

1. 在Python2中: 7 / 2 == 3 , 即整数除以整数，得到的还是整数。这和C语言是一致的，是计算机的思维方式。如果要得到3.5的结果，需要用“7 / 2.0”
2. 在Python3中: 7 / 2 == 3.5 , 即整数除以整数，得到的是浮点数。这和人类的思维是一致的。


%表示取模： "X divided by Y with J remaining." For example, "100 divided by 16 with 4 remaining." The result of % is the J part, or the remaining part.

======  
Python 3

print("Hen", 25 + 30 / 6)  
print('Is it true that 3 + 2 < 5 - 7?')  
print(3 + 2 < 5 - 7) --> False  

======


**Ex4（Variables And Names）**

写成”x = 4“比”x=4“要好，易读。  
print "hey %s there" % "you"

**Ex5(More Variables and Printing)**

所有格式化字符（"format string."）：  
BTW，%r is a very useful one. It's like saying "print this no matter what."
变量必须 start with a character。 You can use the round() function like this: round(1.7333)


======  
Python 3

my_name = 'Zed A. Shaw'
print(f"Let's talk about {my_name}.")

这个f符号在Python3.5里不能用，可能在3.6里有效。

">>> print("Its fleece was white as {}.".format('snow'))  
Its fleece was white as snow.

Can I use single-quotes or double-quotes to make a string or do they do different things?  
In Python either way to make a string is acceptable, although typically you'll use single-quotes for any short strings like 'a' or 'snow'.

======

**Ex6(Strings and Text)**

%r和%s的区别：%r用来做debugging，因为它显示变量的raw data，而其他格式符则用来显示给user看。  
use a single-quote inside a string that has double-quotes

**Ex7(More Printing)**

print "." * 10 #表示打10个点  

print end1 + end2 + end3 + end4 + end5 + end6,     #逗号表示不回车换行，只有一个空格?  
print end7 + end8 + end9 + end10 + end11 + end12


	* 不是每一行都要写注释，只在一些比较难以理解的code处写注释，解释逻辑。
	* Python中可以用单引号或者双引号来写string，一般对于比较短的string我们用单引号。
	* 当print一个特别长的行时，建议用逗号分成两个print行。


**Ex8(Printing，Printing)**

	* 当用%r去print一个双引号里的字符串时，一般结果是输出单引号的字符串（原因是Python试图用最有效的方式来打印字符串，这对于用来打印debugging信息的%r来说是很好的一种方式）。但如果双引号里的字符串中带有一个单引号，那么最后的结果是输出双引号的字符串。
	* %r表示“representation”，将会给你变量的 "raw programmer's" version。
	* Python把True和False认为是keywords，代表true和false的含义，所以不用引号把它们引起来。
	* 如果要打印汉字，需要在第一行加上“# -*- coding: uft-8 -*-”，然后用（print "%s" % u"好"），不能用%r。


======  
Python 3

">>> formatter = "{} {} {} {}"  
">>> print(formatter.format(1, 2, 3, 4))  
1 2 3 4  

实际上formatter是一个string，然后调用这个string的format函数，带4个参数。。。。

======

**Ex9(Printing，Printing，Printing)**

	* 如果用%r来format \n，则不会有换行产生，因为%r就是"raw" format for debugging。
	* 用三个连续的双引号来type as much as we like。


**Ex10(What Was That?)**

	* escape sequences（转义字符）。Like："I am 6'2\" tall." # escape double-quote inside string
	* 第二种方法是用三个双引号（或单引号）来输出多行。
	* \t表示Tab；\\表示\；\'表示单引号；\n表示换行；\r是让光标回到本行的最前面。
	* 
\r （return）就是return 回到 本行 行首 这就会把这一行以前的输出 覆盖掉。

	* \a表示ASCII bell（）响铃；\b表示backspace
	* %r表示raw打印，即按你写在文件里的方式打印，而%s则是打印你想看到的样子。Always remember this: %r is for debugging, %s is for displaying.


LF，即Line Feed，中文意思“换行”；CR，即Carriage Return，中文意思“回车”。但是我们通常把这两个混为一谈。既然设置成2个，则肯定有其存在的道理，查了一下资料，与大家分享。

关于“回车”（carriage return）和“换行”（line feed）这两个概念的来历和区别。
在计算机还没有出现之前，有一种叫做电传打字机（Teletype Model 33）的玩意，每秒钟可以打10个字符。但是它有一个问题，就是打完一行换行的时候，要用去0.2秒，正好可以打两个字符。要是在这0.2秒里面，又有新的字符传过来，那么这个字符将丢失。

于是，研制人员想了个办法解决这个问题，就是在每行后面加两个表示结束的字符。一个叫做“回车”，告诉打字机把打印头定位在左边界；另一个叫做“换行”，告诉打字机把纸向下移一行。

这就是“换行”和“回车”的来历，从它们的英语名字上也可以看出一二。

后来，计算机发明了，这两个概念也就被般到了计算机上。那时，存储器很贵，一些科学家认为在每行结尾加两个字符太浪费了，加一个就可以。于是，就出现了分歧。

Unix系统里，每行结尾只有“<换行>”，即“\n”；Windows系统里面，每行结尾是“<换行><回车>”，即“\n\r”；Mac系统里，每行结尾是“<回车>”。一个直接后果是，Unix/Mac系统下的文件在Windows里打开的话，所有文字会变成一行；而Windows里的文件在Unix/Mac下打开的话，在每行的结尾可能会多出一个^M符号。

Ex11（Asking Questions）
1）在print语句后加一个逗号，表示print还未完成本行。
2）raw_input()函数读取控制台的输入。
3）input()函数也可以读取控制台的输入，它试图像Python代码一样转换你输入的东西（比如3+4被转换为7），但是有安全问题，所以应该避免使用它。
raw_input() 将所有输入作为字符串看待，返回字符串类型。而 input() 在对待纯数字输入时具有自己的特性，它返回所输入的数字的类型（int, float甚至是tuple,list等）。

======  
Python 3

raw_input()函数和input()函数合并为input()函数了。

======

这两个函数均能接收 字符串 ，但 raw_input() 直接读取控制台的输入（任何类型的输入它都可以接收）。而对于 input() ，它希望能够读取一个合法的 python 表达式，即你输入字符串的时候必须使用引号将它括起来，否则它会引发一个 SyntaxError 。

raw_input() 将所有输入作为字符串看待，返回字符串类型。而 input() 在对待纯数字输入时具有自己的特性，它返回所输入的数字的类型（ int, float ）；同时在例子 1 知道，input() 可接受合法的 python 表达式，举例：input( 1 + 3 ) 会返回 int 型的 4 。

4）在Python编程中，每一行最好不应该超过80个字符串，这是编程style。

**Ex12（Prompting People）**

1）在raw_input()里可以加一些prompt，比如：age = raw_input("How old are you? ")，这样就可把Ex11中的print()语句省略了，直接prompt，然后把控制台输入的值放到age变量里。  
2）如何查帮助？两种方式：第一，可以在python命令行输入help()，进入帮助模式，然后再输入要查看的函数，比如raw_input；或者，直接在powershell里输入：python -m pydoc raw_input，即可

**Ex13（Parameters, Unpacking, Variables）**

1）"from sys import argv"：相当于Python不会把所有库都加载，只加载你import的东西，这样可以保证你的程序比较小，也可以对那些读你程序的人有所帮助。  
2）argv表示“argument variable”，用来存储所有要传递给你的Python脚本的参数。  
3）“script, first, second, third = argv”用来unpack argv给各个单独的变量。

E**x14（Prompting and Passing）**

1）用一个变量 prompt = '> ' 来纪录提示符。如果想改为其他的提示符，只需要改这个变量即可。  
2）三个双引号：  
print """
Alright, so you said %r about liking me.  
You live in %r.  Not sure where that is.  
And you have a %r computer.  Nice.  
""" % (likes, lives, computer)

**Ex15（Reading Files）**  

1）You know how to get input from a user with raw_input or argv。  
2）需要注意：在操作文件时，很容易导致文件误操作，如果不仔细的话。  
3）可以这样在google上查找帮助：“python open“  
4）txt = open(filename)只是返回了“file object”，而不是文件内容。 The DVD player is not the DVD the same way the file object is not the file's contents.  
5）用open()方法打开文件后，还需要用close()方法关闭文件。  
6）用open()方法打开文件，可以打开多次，Python不会报错。

**Ex16（Reading and Writing Files）**  

1）各种有关文件操作的方法/函数：close，read，readline，truncate，write('stuff')  
2）seek(offset,where):  where=0从起始位置移动，1从当前位置移动，2从结束位置移动。当有换行时，会被换行截断。seek（）无返回值，故值为None。  
3）tell():  文件的当前位置,即tell是获得文件指针位置，受seek、readline、read、readlines影响，不受truncate影响  
4）read( )：表示读取全部内容  
5）readline(n )：读入若干行，n表示读入的最长字节数。其中读取的开始位置为tell()+1。当n为空时，默认只读当前行的内容  
6）readlines读入所有行内容  
7）truncate(n):  从文件的首行首字符开始截断，截断文件为n个字符；无n表示从当前位置起截断；截断之后n后面的所有字符被删除。如果前面有readline函数已经执行过了，那么当前的光标已经移到当前行了，所以truncate()的结果是该行后面的内容全部被删除了。

二、以下以1个例子说明以上各个函数的作用  
 
fso = open("f:\\a.txt",'w+')    '以w+方式，并非a方式打开文件，故文件原内容被清空  
print fso.tell()    '文件原内容被清空，故此时tell()=0  
fso.write("abcde\n")  '写入文件abcde\n，因为换行\n占两个字符，故共写入7个字符  
print fso.tell()  '此时tell()=7  

fso.write("fghwm")  '又写入文件fghwm，故此时文件共写入7+5 =142个字符
print fso.tell()  '此时tell()=12 

fso.seek(1, 0)  '从起始位置即文件首行首字符开始移动1个字符  
print fso.tell()   ‘此时tell() =1  
print  fso.readline()  '读取当前行，即文件的第1行，但是从第二个字符（tell（）+1）开始读，结果为:bcde。'若换成for读取整个文件或read读取整个文件则结为bcdefghwm       
print fso.tell()   ‘因为readline此时tell() =7,  
fso.truncate(8)  '从写入后文件的首行首字符开始阶段，截断为8个字符，即abcde\nf，即文件的内容为：abcde\nf

print fso.tell()   ‘tell() 依旧为7,并为受truncate(8)影响，但是此时文件内容为abcde\nf  
print  fso.readline()  ‘从tell（）+1=8开始读取，读取当前行内容：

三、参数Mode的基本取值  
r、w、a为打开文件的基本模式，对应着只读、只写、追加模式；  
b、t、+、U这四个字符，与以上的文件打开模式组合使用，二进制模式，文本模式，读写模式、通用换行符，根据实际情况组合使用。最重要的是“+”，加上“+”号，则表示可以用读写的方式打开文件。缺省打开模式是只读。

四、 常见的mode取值组合  
1、r或rt    默认模式，文本模式读  
2、rb      二进制文件  
3、w或wt    文本模式写，打开前文件存储被清空  
4、wb    二进制写，文件存储同样被清空  
5、a   追加模式，只能写在文件末尾  
6、a+  可读写模式，写只能写在文件末尾  
7、w+ 可读写，与a+的区别是要清空文件内容  
8、r+   可读写，与a+的区别是可以写到文件任何位置  

**Ex17（More Files）**

1）“from os.path import exists”，然后用函数exists(to_file)去判断文件是否存在，返回值为布尔值。  
2）下面的代码表示等待控制台的回车。  
print "Ready, hit RETURN to continue, CTRL-C to abort."  
raw_input()  
3）echo "This is a test file." > test.txt # 生成一个新文件。  
4）len(indata) # 返回string的长度。  
5）indata = open(from_file).read() # 这行执行完毕，则文件已经被Python自动关了，所以不需要in_file.close()关文件了。  

**Ex18（Names, Variables, Code, Functions）**

1）“def print_two(*args):" --> *args (asterisk args) which is a lot like your argv parameter but for functions. This has to go inside () parentheses to work. 其中的星号表示告诉Python：把所有参数取出，放到args里做为一个list。对于这种参数，需要用“arg1, arg2 = args”unpack参数为不同的单个参数。  
 
**Ex19（Functions and Variables）**

1）可以有不同的方式来生成函数的参数，比如：直接传值给参数，传变量给参数，传数学公式给参数，或者传数学公式和变量的combination给参数。  
2）如何分析一个函数？加注释；大声读出代码；把函数用纸打印出来，在纸上画流程图。  
3）如何想要把raw_input()的输入转为整数型输出，那么可以用int()函数。  
4）定义一个全局变量，在函数内外使用，这是一个很不好的做法，需要尽量避免。  
5）关于参数的个数，取决于Python和电脑的版本，但一般不要超过5个。  
6）可以在函数里面调用函数。

**Ex20（Functions and Files）** 

1）用“f.seek(0)”让文件指针回到最开始。
2）每次执行完“f.readline”，则文件指针跳到下一行。
3）“x = x + y”等同于：“x += y”
4）readline()函数里面的代码会扫描文件de每一个byte，直到遇到\n（表示换行），并且它还会return一个\n，这将产生一个空行。为了去掉这个空行，可以在“print line_count, f.readline()”语句后面加一个逗号。
5）文件对象本身负责维护文件当前的指针位置。

**Ex21（Functions Can Return Something）**

1）在函数的返回中可以用公式，比如：return a + b  
2）可以把一个函数的返回值做为另一个函数的参数  
3）int(raw_input()) or float(raw_input())  

**Ex22（What Do You Know So Far?）**

	* 注释 --〉用#号，井号后面空一格
	* print --〉可以用单引号或双引号；可以用格式符：%s, %r, %d
	* 可以用连续3个双引号来print一些长句
	* raw_input(), input()
	* int(), float(), len() 
	* 调用模块 --〉from sys import argv
	* def, return,
	* 文件操作 --〉fso = open("f:\\a.txt",'w+')，fso.read, tell, seek, readline


**Ex23（Read Some Code）**

1）string split()函数， 返回一个字符串中的所有单词的列表。  
比如：st0 = ' song wen zhang '; print "st0.split()"，结果为：['song','wen','zhang']； 当不带参数时，默认是以空格作为参数，不管空格在哪，或者有几个全部被镐掉了！另一个例子如下：  
">>> str="hello boy<[www.doiido.com]>byebye"  
">>> str.split("[")[1].split("]")[0]  
'www.doiido.com'
">>> str.split("[")[1].split("]")[0].split(".")  
['www', 'doiido', 'com']

2）Python有两种格式化输出语法，一种类似C语言的printf，用%，比如：

	* >>> '%s %d-%d' % ('hello', 7, 1)  
	* 'hello 7-1' 


另一种类似C#的方式，比如：

	* >>> '{0} {1}:{2}'.format('hello', '1', '7')  
	* 'hello 1:7' 


wordfreq = [wordlist.count(w) for w in wordlist]；其中wordlist.count(w)是输出wordlist中的w字窜有几个。

**Ex24（More Practice）**

1）函数的返回可以有多种形式，如下：  

def secret_formula(started):  
    jelly_beans = started * 500  
    jars = jelly_beans / 1000  
    crates = jars / 100  
    return jelly_beans, jars, crates  

print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)  
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)

**Ex25（Even More Practice）**

1）字符串函数  
words.split;  
sort(words);  

">>> sorted('4356712')  
['1', '2', '3', '4', '5', '6', '7']

def sort_words(words):  
    """Sorts the words."""  
    return sorted(words)  

2）List函数  
words.pop(0); 第一个字串，str类型不支持这个函数，所以要先把str转为list类型，用words.split函数。  
words.pop(-1); 

3）自定义模块  
可以这样运行python模块。比如自定义python模块ex25.py，然后运行“python ex25.py”，再直接运行python进入交互Cli，然后敲“import ex25”即把ex25模块载入内存。然后可以在命令行里直接调用“ex25.break_words(sentence)”。  
查看ex25的帮助，可以用help(ex25)，也可以用help(ex25.break_words)。help打印出来的函数前面用两个"""写的东西： documentation comments  

但是每次调用都要写ex25.func()比较麻烦，还有一种简单的方式：from ex25 import *

4）函数返回None：如果你的函数没有定义return，那么会出现这种情况

5）“ImportError: No module named ex25.py”：不要用“import ex25.py”，要用“import ex25”

6）“SyntaxError: invalid syntax”：可能是忘了（ or “


**Ex27（Memorizing Logic）**

1）Learning logic has to come after you do some memorization.
2）The Truth Terms，布尔逻辑运算符：

	* and
	* or
	* not
	* !=
	* ==
	* >=
	* <=
	* +=
	* -=
	* *=
	* /=
	* %=
	* **=(Exponent AND) c**=a is equivalent to c=c**a
	* //=(Floor Division)
	* True
	* False


======  
Python 3

/除法计算结果是浮点数，即使是两个整数恰好整除，结果也是浮点数  
">>> 10 / 33.3333333333333335

/除法计算结果是浮点数，即使是两个整数恰好整除，结果也是浮点数：  
">>> 9 / 3
3.0

还有一种除法是//，称为地板除，两个整数的除法仍然是整数：  
">>> 10 // 3
3

在Python中，除法只有在被除数为float型时才是精确的，否则和地板除没什么差别。  
">>> x=123
">>> x%10  
3  
">>> x/10  
12  
">>> x//10  
12  
">>> x/10.0  
12.3  
">>>

=======

">>> test and test  
Traceback (most recent call last):  
  File "<stdin>", line 1, in <module>  
NameError: name 'test' is not defined  
">>>  
">>>  
">>> "test" and "test"    
'test'  
">>> 1 and 1  
1  
">>> False and 1  
False  
">>> True and 1  
1  
">>>  

**Ex30（Else and If）**  

What happens if multiple elif blocks are True?
Python starts and the top runs the first block that is True, so it will run only the first one.

**Ex31（Making Decisions）**  

1）用“if-else“代替“elif”？这样Python将检查每一对“if-else”，而不是“if-elif-else”里的第一个True。
2）如何判断一个数字在一个范围里？可以用： 0 < x < 10 or 1 <= x < 10 or  x in range(1, 10)

**Ex32（Loops and Lists）**  

1）定义列表，可以在一个列表里定义不同类型的量，也可以定义一个空列表。
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']
elements = [ ] 

2）for循环引用如下：
for number in the_count:   
    print "This is count %d" % number

for i in range(0, 6):   
    print "Adding %d to the list." % i    # append is a function that lists understand   
    elements.append(i)

3）range函数：
The range() function only does numbers from the first to the last, not including the last.  
">>> range(1,5) #代表从1到5(不包含5)  
[1, 2, 3, 4]  
">>> range(1,5,2) #代表从1到5，间隔2(不包含5)  
[1, 3]  
">>> range(5) #代表从0到5(不包含5)   
[0, 1, 2, 3, 4]  

array = [1, 2, 5, 3, 6, 8, 4]  
"#其实这里的顺序标识是  
[1, 2, 5, 3, 6, 8, 4]  
(0，1，2，3，4，5，6)  
(-7,-6,-5,-4,-3,-2,-1)  

">>> array[0:] #列出0以后的  
[1, 2, 5, 3, 6, 8, 4]  
">>> array[1:] #列出1以后的  
[2, 5, 3, 6, 8, 4]  
">>> array[:-1] #列出-1之前的  
[1, 2, 5, 3, 6, 8]  
">>> array[3:-3] #列出3到-3之间的  
[3]   

">>> array[::2]  
[1, 5, 6, 4]  
">>> array[2::]  
[5, 3, 6, 8, 4]  
">>> array[::3]  
[1, 3, 4]  
">>> array[::4]  
[1, 6]  

如果想让他们颠倒形成reverse函数的效果  
">>> array[::-1]  
[4, 8, 6, 3, 5, 2, 1]  
">>> array[::-2]  
[4, 6, 5, 1]  

range可以直接给list变量赋值：  
elements = range(0, 6)  

List所支持的方法：append(), count(), pop(), remove(), index(), insert(), reverse(), sort(), extend()

4）How do you make a 2-dimensional (2D) list?  
That's a list in a list like this: [[1,2,3],[4,5,6]]  

**Ex33（While Loops）**  

1） A while-loop runs until the expression is False.  
2）While Loop容易导致死循环，所以：a) 尽量用 for-loop；b) 检查你的while 表达式，确保某个条件下其为 False；c) 如果有疑问，可以把test变量打印出来。  
3）while语句，提供了编写通用循环的一种方法，而for语句是用来遍历序列对象内的元素，并对每个元素运行一个代码块。break,continue用在循环内，跳出整个循环或者跳出一次循环。

**Ex34（Accessing Elements of Lists）**  

1）Python starts its lists at 0 rather than 1
2） 要随机地抓取列表里的内容，列表的每一个元素都应该有一个地址，或者一个 “index（索引）”，而最好的方式是使用以 0 开头的索引。相信我说的这一点吧，这种方式获取元素会更容易。这类的数字被称为“基数(cardinal number)”，它意味着你可以任意抓取元素，所以我们需要一个 0 号元素。
记住: ordinal == 有序，以 1 开始；cardinal == 随机选取, 以 0 开始。

**Ex35（Branches and Functions）**  

1）调用exit(0)推出整个程序。 from sys import exit  
2）函数可以递归调用自己。  
3）一般把所有自定义函数写在程序文件的最前面，然后在主程序调用。  
4）if "0" in choice or "1" in choice。  
5）On many operating systems a program can abort with exit(0), and the number passed in will indicate an error or not. If you do exit(1) then it will be an error, but exit(0) will be a good exit.  在很多类型的操作系统里，``exit(0)`` 可以中断某个程序，而其中的数字参数则用来表示程序是否是碰到错误而中断。 exit(1) 表示发生了错误，而 exit(0) 则表示程序是正常退出的。这和我们学的布尔逻辑 0==False 正好相反，不过你可以用不一样的数字表示不同的错误结果。比如你可以用 exit(100) 来表示另一种和 exit(2) 或 exit(1) 不同的错误。  

**Ex36（Designing and Debugging）**   

一些If-statements的规则：  
1）每个If-statements都必须有一个else。  
2）如果else是不必要的，那么应该在else里用一个die函数去指出错误消息并退出。  
3）不要嵌套If-statements超过2层。  
4）用 if-elif-else象一组句子一样。  
5）你的布尔测试应该保持简洁，如果比较复杂，则可以把计算移到函数比较靠前的某个变量上。  

一些Loops的规则：  
1） Use a while-loop only to loop forever  
2） Use a for-loop for all other kinds of looping, especially if there is a fixed or limited number of things to loop over.  

关于Debugging：  
1）不用debugger  
2）The best way to debug a program is to use print to print out the values of variables at points in the program to see where they go wrong.  
3）不要一次写太多行代码再调试，要逐步调试。 Code a little, run a little, fix a little.  

**Ex37（Symbol Review）**  

1）Keywords:
and, as, assert, break, class, continue, def, del, elif, else, except, exec, finally, for, from, global, if, import, in, is, lambda, not, or, pass, print, raise, return, try, while, with, yield, 

as, with: 

有一些任务，可能事先需要设置，事后做清理工作。对于这种场景，Python的with语句提供了一种非常方便的处理方式。一个很好的例子是文件处理，你需要获取一个文件句柄，从文件中读取数据，然后关闭文件句柄。  

如果不用with语句，代码如下：  

file = open("/tmp/foo.txt")  
data = file.read()  
file.close()  

这里有两个问题。一是可能忘记关闭文件句柄；二是文件读取数据发生异常，没有进行任何处理。下面是处理异常的加强版本：
file = open("/tmp/foo.txt")
try:
    data = file.read()
finally:
    file.close()

虽然这段代码运行良好，但是太冗长了。这时候就是with一展身手的时候了。除了有更优雅的语法，with还可以很好的处理上下文环境产生的异常。下面是with版本的代码：

with open("/tmp/foo.txt") as file:
    data = file.read()

http://blog.csdn.net/wusuopubupt/article/details/29369601

assert:

使用assert断言是学习python一个非常好的习惯，python assert 断言句语格式及用法很简单。在没完善一个程序之前，我们不知道程序在哪里会出错，与其让它在运行最崩溃，不如在出现错误条件时就崩溃，这时候就需要assert断言的帮助。
Python的assert是用来检查一个条件，如果它为真，就不做任何事。如果它为假，则会抛出AssertError并且包含错误信息。
">>> assert 2 == 1, '2 != 1'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>

break:
Stop this loop right now.  while True: break

continue:
Don't process more of the loop, do it again.  while True: continue

del: 
Delete from dictionary.  del X[Y]

except:
If an exception happens, do this.

way 1 ->
try:  
    a=b  
    b=c  
except Exception,e:  
    print Exception,":",e

way 2 ->
"#引入python中的traceback模块，跟踪错误
import traceback  
try:  
    a=b  
    b=c  
except:  
    traceback.print_exc()

way 3 ->
"#引入sys模块
import sys  
try:  
    a=b  
    b=c  
except:  
    info=sys.exc_info()  
    print info[0],":",info[1]

exec:
Run a string as Python.  exec 'print "hello"'

finally:
Exceptions or not, finally do this no matter what.  finally: pass
在 try 中 raise一个异常，就立刻转入 except 中执行，在except 中遇到 return 时，就强制转到 finally 中执行， 在 finally 中遇到 return 时就返回

from:
Importing specific parts of a module.  from x import Y
这样可以把指定模块的某个部分导入到当前的名字空间


global:
Declare that you want a global variable.  global X

is:
Like == to test equality.  1 is 1 == True

lambda:
Create a short anonymous function.  lambda的一般形式是关键字lambda后面跟一个或多个参数，紧跟一个冒号，以后是一个表达式。lambda是一个表达式而不是一个语句。它能够出 现在Python语法不允许def出现的地方。作为表达式，lambda返回一个值（即一个新的函数）。lambda用来编写简单的函数，而def用来处 理更强大的任务。

	* f = lambda x,y,z : x+y+z  
	* print f(1,2,3)  
	*   
	* g = lambda x,y=2,z=3 : x+y+z  
	* print g(1,z=4,y=5) 


yield:
Pause here and return to caller. 

生成斐波那契數列
def fab(max): 
    n, a, b = 0, 0, 1 
    while n < max: 
        yield b 
        # print b 
        a, b = b, a + b 
        n = n + 1 
简单地讲，yield 的作用就是把一个函数变成一个 generator，带有 yield 的函数不再是一个普通函数，Python 解释器会将其视为一个 generator，调用 fab(5) 不会执行 fab 函数，而是返回一个 iterable 对象！在 for 循环执行时，每次循环都会执行 fab 函数内部的代码，执行到 yield b 时，fab 函数就返回一个迭代值，下次迭代时，代码从 yield b 的下一条语句继续执行，而函数的本地变量看起来和上次中断执行前是完全一样的，于是函数继续执行，直到再次遇到 yield。
一个带有 yield 的函数就是一个 generator，它和普通函数不同，生成一个 generator 看起来像函数调用，但不会执行任何函数代码，直到对其调用 next()（在 for 循环中会自动调用 next()）才开始执行。虽然执行流程仍按函数的流程执行，但每执行到一个 yield 语句就会中断，并返回一个迭代值，下次执行时从 yield 的下一个语句继续执行。看起来就好像一个函数在正常执行的过程中被 yield 中断了数次，每次中断都会通过 yield 返回当前的迭代值。
yield 的好处是显而易见的，把一个函数改写为一个 generator 就获得了迭代能力，比起用类的实例保存状态来计算下一个 next() 的值，不仅代码简洁，而且执行流程异常清晰。
https://www.ibm.com/developerworks/cn/opensource/os-cn-python-yield/

2）Data Types:
True, False, None, strings, numbers, floats, lists, dicts
None: x = None
string: x = "hello"
list: j = [1,2,3,4]
dict: e = {'x': 1, 'y': 2}

3) String escape sequences:
\\Backslash\'Single-quote\"Double-quote\aBell\bBackspace\fFormfeed\nNewline\rCarriage\tTab\vVertical tab

4) String formats:
%dDecimal integers (not floating point)."%d" % 45 == '45'%iSame as %d."%i" % 45 == '45'%oOctal number."%o" % 1000 == '1750'%uUnsigned decimal."%u" % -1000 == '-1000'%xHexadecimal lowercase."%x" % 1000 == '3e8'%XHexadecimal uppercase."%X" % 1000 == '3E8'%eExponential notation, lowercase 'e'."%e" % 1000 == '1.000000e+03'%EExponential notation, uppercase 'E'."%E" % 1000 == '1.000000E+03'%fFloating point real number."%f" % 10.34 == '10.340000'%FSame as %f."%F" % 10.34 == '10.340000'%gEither %f or %e, whichever is shorter."%g" % 10.34 == '10.34'%GSame as %g but uppercase."%G" % 10.34 == '10.34'%cCharacter format."%c" % 34 == '"'%rRepr format (debugging format)."%r" % int == "<type 'int'>"%sString format."%s there" % 'hi' == 'hi there'%%A percent sign."%g%%" % 10.34 == '10.34%'

5) Operators:
+Addition2 + 4 == 6-Subtraction2 - 4 == -2*Multiplication2 * 4 == 8**Power of2 ** 4 == 16/Division2 / 4.0 == 0.5//Floor division2 // 4.0 == 0.0%String interpolate or modulus2 % 4 == 2<Less than4 < 4 == False>Greater than4 > 4 == False<=Less than equal4 <= 4 == True>=Greater than equal4 >= 4 == True==Equal4 == 5 == False!=Not equal4 != 5 == True<>Not equal4 <> 5 == True( )Parenthesislen('hi') == 2[ ]List brackets[1,3,4]{ }Dict curly braces{'x': 5, 'y': 10}@At (decorators)@classmethod,Commarange(0, 10):Colondef X():.Dotself.x = 10=Assign equalx = 10;semi-colonprint "hi"; print "there"+=Add and assignx = 1; x += 2-=Subtract and assignx = 1; x -= 2*=Multiply and assignx = 1; x *= 2/=Divide and assignx = 1; x /= 2//=Floor divide and assignx = 1; x //= 2%=Modulus assignx = 1; x %= 2**=Power assignx = 1; x **= 2

读别人的代码，用如下方法：
First, print out the code you want to understand. Yes, print it out, because your eyes and brain are more used to reading paper than computer screens. Make sure you print a few pages at a time.
Second, go through your printout and take notes of the following:

	1. Functions and what they do.
	2. Where each variable is first given a value.
	3. Any variables with the same names in different parts of the program. These may be trouble later.
	4. Any if-statements without else clauses. Are they right?
	5. Any while-loops that might not end.
	6. Any parts of code that you can't understand for whatever reason.

Third, once you have all of this marked up, try to explain it to yourself by writing comments as you go. Explain the functions, how they are used, what variables are involved and anything you can to figure this code out.
Lastly, on all of the difficult parts, trace the values of each variable line by line, function by function. In fact, do another printout and write in the margin the value of each variable that you need to "trace."

**Ex38（Doing Things to Lists）**  

1）当一个List调用其方法，比如mystuff.append('hello')，其实Python是在调用append(mystuff, 'hello')，而不是你看到的mystuff.append('hello')。
2）more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]
     more_stuff.pop()
     pop方法是从最后一个item开始往外pop的。
3）print ' '.join(stuff)
     join()是把list连起来，“.“的前面是连接字符。

List:  They are simply ordered lists of facts you want to store and access randomly or linearly by an index.
Every concept in programming usually has some relationship to the real world.

4）什么时候用List？

	* If you need to maintain order. Remember, this is listed order, not sorted order. Lists do not sort for you.
	* If you need to access the contents randomly by a number. Remember, this is using cardinal numbers starting at 0.
	* If you need to go through the contents linearly (first to last). Remember, that's what for-loops are for.


**Ex39（Dictionarires, Oh Lovely Dictionaries）**  

1）可以把dict看成一个数据库来存储和组织数据。 "mapping" or "associating" is the key concept in a dictionary.  
2）对于List，其索引只能是数字，但是dict的索引不仅仅是数字。比如：  
stuff = {'name': 'Zed', 'age': 39, 'height': 6 * 12 + 2}  
print stuff['name']  
3）还可以用这种方法添加新的元素到dict：stuff[1] = "Wow"。  
4）删除元素：del stuff['city']; del stuff[1]  
5）dict所支持的方法：  
D.get(k[,d]):  D[k] if k in D, else d.  d defaults to None.  
D.has_key(k):  True if D has a key k, else False  
D.items(): list of D's (key, value) pairs, as 2-tuples  
D.keys(): list of D's keys  
D.pop(k[,d]): v, remove specified key and return the corresponding value.
If key is not found, d is returned if given, otherwise KeyError is raised  

6）For dict type a big one is that they do not have order.  
7）A list is for an ordered list of items. A dictionary (or dict) is for matching some items (called "keys") to other items (called "values").  
8） What if I need a dictionary, but I need it to be in order?  
Take a look at the collections.OrderedDict data structure in Python. Search for it online to find the documentation.
collections是Python内建的一个集合模块，提供了许多有用的集合类。  
使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。  

如果要保持Key的顺序，可以用OrderedDict：
">>> from collections import OrderedDict
">>> d = dict([('a', 1), ('b', 2), ('c', 3)])
">>> d # dict的Key是无序的
{'a': 1, 'c': 3, 'b': 2}
">>> od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
">>> od # OrderedDict的Key是有序的
OrderedDict([('a', 1), ('b', 2), ('c', 3)])

**Ex40（Modules, Classes, and Objects）**  

1）dict Vs Module
它们的定义和调用模式其实是一致的。先定义一个key=value的容器，然后用key来调用。
You can think about a module as a specialized dictionary that can store Python code so you can access it with the . operator.  

2） Python also has another construct that serves a similar purpose called a class. A class is a way to take a grouping of functions and data and place them inside a container so you can access them with the . (dot) operator.  

class MyStuff(object):   
    def __init__(self):       
        self.tangerine = "And now a thousand years between"   

    def apple(self):       
        print "I AM CLASSY APPLES!"

这种定义很像模块，只是__init__()和self.tangerine有点不同，这就是为什么class被引入的原因。你可以用类做无数个对象，它们之间互不干扰，但是import a module，整个程序都只有这么一个module而已。


	* 注意到__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
	* 有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传，Python解释器自己会把实例变量传进去
	* 和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数。除此之外，类的方法和普通函数没有什么区别，所以，你仍然可以用默认参数、可变参数和关键字参数。


Why do I need self when I make __init__ or other functions for classes?
If you don't have self, then code like cheese = 'Frank' is ambiguous. That code isn't clear about whether you mean the instance's cheese attribute, or a local variable named cheese. With self.cheese = 'Frank' it's very clear you mean the instance attribute self.cheese.

一个class像一个 "mini-module"，那么module的import操作在类里对应就是实例化 "instantiate"。比如：

thing = MyStuff()
thing.apple()
print thing.tangerine

Python实例化对象的过程如下：


目前我们有三种方法 get things from things：
"# dict style  
mystuff['apples']  

"# module style  
mystuff.apples()  
print mystuff.tangerine  

"# class style  
thing = MyStuff()  
thing.apples()  
print thing.tangerine  

=========================================================================
在Python用 import或者from...import来导入相应的模块。模块其实就是一些函数和类的集合文件，它能实现一些相应的功能，当我们需要使用这些功能的 时候，直接把相应的模块导入到我们的程序中，我们就可以使用了。这类似于C语言中的include头文件，Python中我们用import导入我们需要 的模块。  
eg:  
import sys  
print('================Python import mode==========================');  
print ('The command line arguments are:')  
for i in sys.argv:  
    print (i)  
print ('\n The python path',sys.path)  

from sys import argv,path  #  导入特定的成员  
print('================python from   import===================================')  
print('path:',path) # 因为已经导入path成员，所以此处引用时不需要加sys.path
如果你要使用所有sys模块使用的名字，你可以这样：  
from sys import *  
print('path:',path)  
从以上我们可以简单看出：  

"############################  
"#导入modules，import与from...import的不同之处在于，简单说：
"# 如果你想在程序中用argv代表sys.argv，
"# 则可使用：from sys import argv
"# 一般说来，应该避免使用from..import而使用import语句，
"# 因为这样可以使你的程序更加易读，也可以避免名称的冲突  
"###########################

**Ex41（Learning To Speak Object Oriented）**  

1）术语。
class:  Tell Python to make a new type of thing.
object:  Two meanings: the most basic type of thing, and any instance of some thing.
instance:  What you get when you tell Python to create a class.
def:  How you define a function inside a class.
self:  Inside the functions in a class, self is a variable for the instance/object being accessed.
inheritance:  The concept that one class can inherit traits from another class, much like you and your parents.
composition（组合）:  The concept that a class can be composed of other classes as parts, much like how a car has wheels.
attribute： A property classes have that are from composition and are usually variables.
is-a： A phrase to say that something inherits from another, as in a "salmon" is-a "fish."
has-a： A phrase to say that something is composed of other things or has a trait, as in "a salmon has-a mouth."

class X(Y)： “Make a class named X that is-a Y."
class X(object): def __init__(self, J)： class X has-a __init__ that takes self and J parameters."
class X(object): def M(self, J)： "class X has-a function named M that takes self and J parameters."
foo = X()： "Set foo to an instance of class X."
foo.M(J)： "From foo get the M function, and call it with parameters self, J."
foo.K = Q： "From foo get the K attribute and set it to Q."

2）判断命令行参数：
if len(sys.argv) == 2 and sys.argv[1] == "english":

3）Python strip() 方法用于移除字符串头尾指定的字符（默认为空格）。

4）从列表a中以随机顺序取出3个元素(一个元素只能取出一次,所以取出的个数不能大于列表所含元素的个数)：
a=[1,2,3,4,5]
random.sample(a,3)

5） 获取一个从1到10的整数：
random.randint(1,10)

6） Python replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。
str.replace(old, new[, max])

**Ex42（Is-A, Has-A, Objects, and Classes）**  

1）一个类 Is-A 另一个类，比如，Salmon Is-A Fish, but Salmon Has-A Gills（即类里有的属性attribute）。
object: 是一个具体的类实例。
Confusing point: 对于 class X(object): def __init__(self, J)，class is-a object
http://www.cafepy.com/article/python_types_and_objects/python_types_and_objects.html

2）self.pet = None： That makes sure that the self.pet attribute of that class is set to a default of None.

3） Python中对象方法的定义很怪异，第一个参数一般都命名为self（相当于其它语言的this），用于传递对象本身，而在调用的时候则不必显式传递，系统会自动传递。

Example: 

">>> class Foo:  
...     def bar(self, message):  
...         print(message)  
...  
">>> Foo().bar("Hello, World")  
Hello, World  
">>> fo = Foo()  
">>> fo.bar("haha")  
haha  
">>> type(fo)  
<type 'instance'>  
">>> type(Foo)  
<type 'classobj'>  
">>>  

4）Python中用super()来做父类调用。
http://www.cnblogs.com/dkblog/archive/2011/02/24/1980654.html

Ex43（Basic Object-Oriented Analysis and Design）
1）用Python解决问题的参考流程：

Top-Down的方法 --〉



问题？
1）在一个类的函数里，如何调用本类所定义的变量？类名.变量名？
2）在什么情况下定义类需要加上__init__函数？
3）在什么情况下，类里面的函数的参数要加self？

**Ex44（Inheritance Versus Composition） ** 

1） In object-oriented programming, Inheritance is the evil forest. Experienced programmers know to avoid this evil because they know that deep inside the Dark Forest Inheritance is the Evil Queen Multiple Inheritance.
2） Most of the uses of inheritance can be simplified or replaced with composition, and multiple inheritance should be avoided at all costs.
3） Inheritance is used to indicate that one class will get most or all of its features from a parent class. This happens implicitly whenever you write class Foo(Bar), which says "Make a class Foo that inherits from Bar."

Implicit Inheritance:  implicit actions that happen when you define a function in the parent, but not in the child.

class Parent(object):   
    def implicit(self):       
        print "PARENT implicit()"
class Child(Parent):
    pass
    dad = Parent()
    son = Child()

    dad.implicit()
    son.implicit()

Override Explicitly:  In this case you want to override the function in the child, effectively replacing the functionality.

class Parent(object):

    def override(self):
        print "PARENT override()"

class Child(Parent):

    def override(self):
        print "CHILD override()"

dad = Parent()
son = Child()

dad.override()
son.override()

$ python ex44b.py
PARENT override()
CHILD override()

Alter Before or After: first overriding like last one, then use "super"  to get the Parent version to call.

class Parent(object):

    def altered(self):
        print "PARENT altered()"

class Child(Parent):

    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

dad.altered()
son.altered()

4）Multiple inheritance is when you define a class that inherits from one or more classes, like this:

class SuperFun(Child, BadStuff):
    pass

The most common use of super() is actually in __init__ functions in base classes.

class Child(Parent):

    def __init__(self, stuff):
        self.stuff = stuff
        super(Child, self).__init__()

5）Composition:  Inheritance is useful, but another way to do the exact same thing is just to use other classes and modules, rather than rely on implicit inheritance.

class Other(object):

    def override(self):
        print "OTHER override()"

    def implicit(self):
        print "OTHER implicit()"

    def altered(self):
        print "OTHER altered()"

class Child(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print "CHILD override()"

    def altered(self):
        print "CHILD, BEFORE OTHER altered()"
        self.other.altered()
        print "CHILD, AFTER OTHER altered()"

son = Child()

son.implicit()
son.override()
son.altered()

$ python ex44e.py
OTHER implicit()
CHILD override()
CHILD, BEFORE OTHER altered()
OTHER altered()
CHILD, AFTER OTHER altered()


6） You don't want to have duplicated code all over your software, since that's not clean and efficient. Inheritance solves this problem by creating a mechanism for you to have implied features in base classes. Composition solves this by giving you modules and the ability to call functions in other classes.

If both solutions solve the problem of reuse, then which one is appropriate in which situations?

	* Avoid multiple inheritance at all costs, as it's too complex to be reliable. If you're stuck with it, then be prepared to know the class hierarchy and spend time finding where everything is coming from.
	* Use composition to package code into modules that are used in many different unrelated places and situations.
	* Use inheritance only when there are clearly related reusable pieces of code that fit under a single common concept or if you have to because of something you're using.

Do not be a slave to these rules.
The thing to remember about object-oriented programming is that it is entirely a social convention programmers have created to package and share code. Because it's a social convention, but one that's codified in Python, you may be forced to avoid these rules because of the people you work with. In that case, find out how they use things and then just adapt to the situation.

**Ex45（You Make a Game）**  

1）Function Style

	* When you work with classes much of your time is spent talking about making the class "do things." Instead of naming your functions after what the function does, instead name it as if it's a command you are giving to the class. Same as pop is saying "Hey list, pop this off." It isn't called remove_from_end_of_list because even though that's what it does, that's not a command to a list.
	* Keep your functions small and simple.


2）Class Style

	* Your class should use "camel case" like SuperGoldFactory rather than super_gold_factory.
	* Try not to do too much in your __init__ functions. It makes them harder to use.
	* Try not to use variables that come from the module or globals. They should be fairly self-contained.
	* Always, always have class Name(object) format or else you will be in big trouble.


3）Code Style

	* Give your code vertical space so people can read it.
	* If you can't read it out loud, it's probably hard to read. it also helps you find difficult passages and things to change for readability.
	* Try to do what other people are doing in Python until you find your own style.
	* If you find someone who writes code in a style you like, try writing something that mimics that style.


4）Good Comments

	* When you write comments, describe why you are doing what you are doing.
	* When you write doc comments for your functions, make the comments documentation for someone who will have to use your code.
	* Keep your comments relatively short and to the point, and if you change a function, review the comment to make sure it's still correct.


**Ex46（A Project Skeleton）**  

1）Install the following Python packages using pip(有时候pip对proxy比较敏感，最好不用proxy上网):  

2）Creating the Skeleton Project Directory  
$ mkdir projects  
$ cd projects/  
$ mkdir skeleton  
$ cd skeleton  
$ mkdir bin NAME tests docs  

3）在windows PowerShell：  
$ new-item -type file NAME/__init__.py  
$ new-item -type file tests/__init__.py  

单元测试工具nose:
在命令行下，直接运行nosetests(注意要把nosetests.exe所在的目录加入到环境变量Path里面)，它就会自动查找当前目录下包含"Test"字符串的目录和文件进行测试。这样我们可以把所有测试case放在一起，然后让测试自己去运行，我们最后看结果就可以了。我们可以指定具体如何输出结果，也可以指定如何搜索文件和文件夹，还可以把测试结果输入到指定的文件。

setup.py：
https://docs.python.org/3/distutils/setupscript.html
Distutils属于python中的标准库，而setuptools工具针对Python官方的distutils做了很多针对性的功能增强，比如依赖检查，动态扩展等。

Distutils is the standard tool used for packaging. It works rather well for simple needs, but is limited and not trivial to extend.

Setuptools is a project born from the desire to fill missing distutils functionality and explore new directions. In some subcommunities, it’s a de facto standard. It uses monkey-patching and magic that is frowned upon by Python core developers.

Example:
https://gitorious.org/python-modargs/python-modargs.git/?p=python-modargs:python-modargs.git;a=blob;f=setup.py;h=6e2072645b002a8373fd9a02e67e8fa95886e287;hb=HEAD

**Ex47（Automated Testing）**  

1）The automated tests won't catch all your bugs, but they will cut down on the time you spend repeatedly typing and running your code.

2） The important functions here are assert_equal which makes sure that variables you have set or paths you have built in a Room are actually what you think they are. If you get the wrong result, then nosetests will print out an error message so you can go figure it out.

def test_room():
    gold = Room("GoldRoom",
                """This room has gold in it you can grab. There's a
                door to the north.""")
    assert_equal(gold.name, "GoldRoom")
    assert_equal(gold.paths, {})

Testing Guidelines：


	1. Test files go in tests/ and are named BLAH_tests.py otherwise nosetests won't run them. This also keeps your tests from clashing with your other code.
	2. Write one test file for each module you make.
	3. Keep your test cases (functions) short, but do not worry if they are a bit messy. Test cases are usually kind of messy.
	4. Even though test cases are messy, try to keep them clean and remove any repetitive code you can. Create helper functions that get rid of duplicate code. You will thank me later when you make a change and then have to change your tests. Duplicated code will make changing your tests more difficult.
	5. Finally, do not get too attached to your tests. Sometimes, the best way to redesign something is to just delete it and start over.


关于assert:

1、assert语句用来声明某个条件是真的。
2、如果你非常确信某个你使用的列表中至少有一个元素，而你想要检验这一点，并且在它非真的时候引发一个错误，那么assert语句是应用在这种情形下的理想语句。
3、当assert语句失败的时候，会引发一AssertionError。

">>> mylist = ['1']  
">>> print len(mylist)  
1  
">>> assert len(mylist) >= 1  
">>> mylist.pop()  
'1'  
">>> print len(mylist)  
0  
">>> assert len(mylist) >= 1  
Traceback (most recent call last):  
  File "<stdin>", line 1, in <module>  
AssertionError  
">>>  

**Ex48（Advanced User Input）**  

1）Breaking Up a Sentence using:
stuff = raw_input('> ')
words = stuff.split()

tuple type: A tuple is nothing more than a list that you can't modify.

2）This method of writing code is called "psuedo code"：if you don't know how to implement something, but you can describe it in your own words.

3） Combining the "test first" with the "psuedo code" tactics we have this simple process for programming:


@staticmethod 的用法：
Python中3种方式定义类方法, 常规方式, @classmethod修饰方式, @staticmethod修饰方式.

class A(object):
    def foo(self, x):
        print("executing foo(%s,%s)" % (self, x))
        print('self:', self)
    @classmethod
    def class_foo(cls, x):
        print("executing class_foo(%s,%s)" % (cls, x))
        print('cls:', cls)
    @staticmethod
    def static_foo(x):
        print("executing static_foo(%s)" % x)   
a = A()

普通的类方法foo()需要通过self参数隐式的传递当前类对象的实例。 @classmethod修饰的方法class_foo()需要通过cls参数传递当前类对象。@staticmethod修饰的方法定义与普通函数是一样的。 @staticmethod是把函数嵌入到类中的一种方式，函数就属于类，同时表明函数不需要访问这个类。通过子类的继承覆盖，能更好的组织代码。
http://stackoverflow.com/questions/136097/what-is-the-difference-between-staticmethod-and-classmethod-in-python
http://stackoverflow.com/questions/12179271/meaning-of-classmethod-and-staticmethod-for-beginner

import的用法：
一 module
通常模块为一个文件，直接使用import来导入就好了。可以作为module的文件类型有".py"、".pyo"、".pyc"、".pyd"、".so"、".dll"。
二 package
通常包总是一个目录，可以使用import导入包，或者from + import来导入包中的部分模块。包目录下为首的一个文件便是 __init__.py。然后是一些模块文件和子目录，假如子目录中也有 __init__.py 那么它就是这个包的子包了。

用逗号分割模块名称就可以同时导入多个模块。 import socket, os, regex模块导入时可以使用 as 关键字来改变模块的引用对象名字: 
import os as system
import socket as net, thread as threads
system.chdir("..")
net.gethostname()

使用from语句可以将模块中的对象直接导入到当前的名字空间. from语句不创建一个到模块名字空间的引用对象，而是把被导入模块的一个或多个对象直接放入当前的名字空间:

from socket import gethostname         # 将gethostname放如当前名字空间
print gethostname()            # 直接调用
socket.gethostname()           # 引发异常NameError: socket

另外, as 也可以和 from 联合使用:
from socket import gethostname as hostname
h = hostname()

http://blog.csdn.net/appleheshuang/article/details/7602499

**Ex49（Making Sentences）**

1）注意：所有的函数都是定义在类外的，除了__init__以外。

http://stackoverflow.com/questions/34517392/cannot-import-python-class


**Ex50（Your First Website）**

1）The term "framework" generally means "some package that makes it easier for me to do something."

2）web应用的流程：
a）浏览器建立网络连接到web服务器，这里是localhost的8080端口
b）连接建立以后，浏览器将发送HTTP request给bin/app.py应用，app.py应用将请求 / URL。
c）在app.py应用中，“/”被映射到“index”class。
d）现在lpthw.web发现了 class index，它调用了 index.GET方法来处理HTTP request。本例中知识简单地回了一个字符串给浏览器。
e）浏览器负责解析回来的HTML页面。

3）如果采用template来订制HTML页面的话，需要用到一个 web.template.render对象。
render = web.template.render('templates/')
This render.index method is kind of a magic function where the render object sees that you're asking for index, goes into the templates/ directory, looks for a page named index.html, and then "renders" it, or converts it.
