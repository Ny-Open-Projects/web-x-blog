# 8-Linux的shell脚本2

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day01-Hadoop介绍和环境搭建
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day01-Hadoop介绍和环境搭建\8-Linux的shell脚本2【海量资源尽在 ubkz.com】.mp4
- 时长 12分6秒（音频 726s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 我们继续看摄要编程我们来看一下摄要中的运算符这个摄要中的运算符呢也就是加减乘除去磨等好在这里呢我给大家举了一个例子比如说呢在这里呢我定义两个变量然后呢这个变量里边呢我去实现两个数的求和这个求两个数的和有三种方式第一种方式我们可以用一个关键字叫XPR然后呢$A
[00:29] 加上$b注意它外边要包裹一个这个符号叫反引号它不是单引号它是反引号这是第一种方式第二种方式我们可以用$两个小括号然后a加上b第三种是$一个中括号a加上b这三种方式都可以我们来演示一下好在这里我们来建一个test3
[01:01] 在sh好放在这里放在这里之后呢我要说一点的是大家在定义这个变量的时候这个等号两边呢你是不能留空格的你比如说我留个空格你看它颜色就变了所以说复制语句两边不能留空格这是第一点还有呢这个分号问题就是每一行后面这个分号你可以加也可以不加如果说一行上它就一条命令那你呢不用加
[01:32] 如果一行上有两条命令你别说了我还可以让他A B等于2我把它放在一行上那前面这个分号是必须要加的好了接下来呢我们来看第一个我们要执行两个数求和啊$A$B那这个地方大家注意这个XPR呢它是一个关键字这个$A$B呀这个加号两边要留空格你看我把这个空格去掉
[02:02] 那这个时候它就不好使所以说加号两边要留空格也就是复制一句两边不能留空格但是这个运算符两边要留空格这是这个第二种呢是一个dollar符小括号里边的A加B这个时候呢对这个空格呢没什么要求第三种是dollar符中号这个和上面的差不多来我们来演示一下这个地方SHTES3跟SHZ你会发现三个都可以了
[02:34] 好我们再回到代码如果说这个时候呢我求的不是加我求的是乘大家请注意比如说我求乘法来我们再来走一遍你会发现第一个呢他说语法错误这个syntax error语法错误什么原因呢这个乘号你需要对它进行转移需要加个反斜杠反斜杠之后呢我们再来试一下走你会发现
[03:05] 这个时候一乘以二那它是二那这个就没问题了所以这个乘号啊一定要对它进行转移好这是它的一个运算符我们就先说到这里好说完运算符之后呢咱们来向下看还有一个义辅语句这个义辅语句呢它呢它的语法呢也比较特殊你看啊这个咱们来看这么一个例子我把这个代码呢直接拷贝过来
[03:35] test这个地方我想vmtest4我写if.sh我们把它粘过来粘过来之后我们来阅读一下这个代码这个代码其实很简单第一个是固定的好那大家注意个问题在这个shell里边呢这个井号呢表示一个注释这个你看我在这个比如说我在这个后面呢我加一个注释随便来加一个注释我写个井号
[04:06] 它后面的就是注释但是在第一行呀就这个位置这个井号呢不是注释它有它有特殊的含义也可以说是一个固定的写法在其他位置出现的井号呢都是注释来我们来先看这一行read-pplease input your name这个什么意思呢这个表示呢我们需要从键盘获取一个获取一个数据把这个数据呢复制给内幕那就有点像我们加尔中的
[04:36] scanf有点像加尔姆的scannerscannerokscanner system in输入一个数据给name然后呢给name了之后呢我来去做一个if判断if呢如果说这个name的值啊是rote也就是你是rote用户then呢表示然后我就干嘛呢我就执行这么一句话把这个name呢输出hello然后呢你的名字welcome好如果说呢
[05:05] 你不是rote而你是什么呢你是idcast那我就执行什么呢我就执行hello idcastwelcome那如果说你既不是rote也不是idcast那就走最后一个else就是get out please请出去这是这么一个义父语句非常简单大家在写这个义父的时候一定要注意这个义父呢他的语法要求比较严格这个中框号两边呢要留空格
[05:35] 这个等号呢它不是一个复职它是一个判断两边也要留空格否则它会报错来我们来试一下我们来保存推出一下我来运行这个程序比如说呢我们来sh test然后这一方4eaf好后面回车这个时候呢它程序停在这里让你输你的用户名比如说我输一个什么呢我输一个我输一个itcast它说呢
[06:09] 那我要说个别的这时候呢他说改套的好这是一个非常典型的一个if语句那么if的结束呢是fi他是if的一个把这个单词呢反过来好注意if呢有很多种写法那这个就是一种写法就是if else if当然还可以有别的你比如说还可以if直接是一个if然后还有if else
[06:39] 那这个是第三种if else if我希望大家能理解这个和我们加吧差不多好这是if语句接下来我们再看它的一个for语句这个for语句呢它的写法有两种第一种呢是一个for然后呢一个一个这个in这句话合在一起什么意思呢这句话合在一起就是说它在执行一个循环每循环一次呀会将后面这个列表的数据
[07:10] 一次的给n然后呢去执行下面这个也就是说这个复活循环会执行几次呢会执行三次第一次这个n是1第二次呢这个n是2第三次n是3然后呢度就是执行下面的一句结束呢是但这是一个复活循环那这种方式呢好像和我们加码的差别比较大还有一种方式呢就是我们可以指定它的循环次数
[07:39] 这个呢和加尔差不多是一个4i等0这表示初始条件i小于等于5i加加那这个和加尔看起来很像了然后呢度就是执行下面这句话然后呢但那这个循环呢就会被执行六次那执行六次我们来简单来试一下把它拿过来好这地方呢test-4.sh把它粘过来
[08:09] 我们来运行一下test然后呢test5test然后忘记编号了falldsh走你会发现这个循环已经执行了这是一个fall一句fall一句好最后呢咱说一下这个shell中的一个函数这个shell里面呢也可以定义函数那么这个函数呢它需要一个函数的名字
[08:42] 前面呢什么也不写直接写函数的名字这个形态呢也不需要写好这个大括号里面呢是函数的一个函数体好这个函数是干嘛的呢你比如说呢他说呢我这里呢让你输入第一个数字read呢表示从键盘呢获取一个数字来读给这个a number然后再输入第二个数字呢读给another number然后输入两个数接下来我要求两个数的和
[09:11] 那return那么让第一个数呢加上第二个数这就是求和好求和完之后呢我怎么去调这个函数呢我直接写上函数的名字就行了连括号都不用加这就是函数的调用那最后呢输出一个结果我怎么去获取这个函数的结果呢有个$问号这个呢就可以获取上一次的返回值
[09:39] 也就是函数的返回值来我们把它复制一下放在这位置test函数f1c.sh把它粘过来粘过来之后呢我们再来看一下这是一个函数这个函数呢让我们输入两个数字第一个数字给a number第二个数字给another number然后呢分别输出这两个数字接下来return就是返回这两个函数的这两个
[10:13] 变量的和这个求和的时候呢来咱们看一下这个地方呢dollar for number这是一个变量dollar for another number这也是个变量这是两个变量的和外面又为什么又加一个dollar呢这其实是一个运算符的一种格式我要求和那这个时候呢我们必须再加两个小括号才能去进行运算这个函数定义完之后呢这一话是在定义这个函数
[10:43] 那这个echo啊表示呢我去输出这两个函数执行的结果用一个$问号这个$问号呢我们向上翻有一个表$问号是显示最后命令的退出状态这个呢一般是用来获取函数的返回值来我们来试一下好这个是sh test-func回车一下它让我们输入第一个数字我输个100第二个数字输个200
[11:16] 你发现这两个数字的它的这个值呢是100和200那么它的求和数字是44这是为什么呢我要给大家说一件事这个求和的时候呢这个数字呢它默认大小是一个字节你这个数字的大小呢你不能超过一个字节你看我比如说我把这个数字呢调小一点10 20
[11:45] 这个时候你发现了这个数字大小呢是正常的这个一个字节呢是120最大是多少118是不是你不能超过118这个大家注意一下好了那么关于share编程呢我们就先说到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解 Linux Shell 脚本中的算术运算、if 判断、for 循环和函数定义与调用。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 展示了算术运算符示例代码：`a=1; b=2; echo expr $a + $b; echo $(($a+$b)); echo $((a+b));`
- 画面标题为“4.3 运算符”。

画面2：
- 展示了 if 语句示例代码：`read -p "please input your name:" NAME ... if [ $NAME = root ] then ... elif [ $NAME = itcast ] then ... else ... fi`
- 画面标题为“4.4 if语句”。

画面3：
- 在 SecureCRT 中显示了 if 语句脚本内容，光标位于 `fi` 后。
- 画面标题为“4.4 if语句”。

画面4：
- 在 SecureCRT 中执行了脚本，输出了“你有新邮件”提示，光标在命令行等待输入。
- 画面标题为“4.4 if语句”。

画面5：
- 展示了 for 循环的两种写法：方式1为 `for i in 1 2 3; do echo $i; done`，方式2为 `for ((i=0; i<=5; i++)); do echo "welcome $i times"; done`。
- 画面标题为“4.5 for语句”。

画面6：
- 在 SecureCRT 中打开一个新文件，准备编写脚本。
- 画面标题为“4.5 for语句”。

画面7：
- 展示了函数定义示例代码：`funWithReturn(){ echo "这个函数会对输入的两个数字进行相加运算..."; read aNum; read anotherNum; return $(($aNum+$anotherNum)); }`
- 画面标题为“4.6 函数”。

画面8：
- 展示了函数定义示例代码：`funWithReturn(){ echo "这个函数会对输入的两个数字进行相加运算..."; read aNum; read anotherNum; return $(($aNum+$anotherNum)); }`
- 画面标题为“4.6 函数”。

画面9：
- 在 SecureCRT 中执行了 for 循环脚本，输出了“welcome 0 times”到“welcome 5 times”。
- 画面标题为“4.5 for语句”。

画面10：
- 在 SecureCRT 中显示了函数定义脚本内容，光标位于 `return $(($aNum+$anotherNum));` 后。
- 画面标题为“4.6 函数”。

画面11：
- 在 SecureCRT 中显示了函数定义脚本内容，光标位于 `return $(($aNum+$anotherNum));` 后。
- 画面标题为“4.6 函数”。

画面12：
- 在 SecureCRT 中执行了函数脚本，提示输入第一个数字“100”，光标在等待输入第二个数字。
- 画面标题为“4.6 函数”。

画面13：
- 在 SecureCRT 中执行了函数脚本，提示输入第一个数字“10”，光标在等待输入第二个数字。
- 画面标题为“4.6 函数”。

画面14：
- 展示了算术运算符示例代码：`a=1; b=2; echo expr $a + $b; echo $(($a+$b)); echo $((a+b));`
- 画面标题为“4.3 运算符”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```bash
#!/bin/bash
a=1;
b=2;
echo expr $a + $b;
echo $(($a+$b));
echo $((a+b));
```

画面2：
```bash
#!/bin/bash
read -p "please input your name:" NAME # read命令用于从控制台读取输入数据
## printf '%s\n' $NAME
if [ $NAME = root ]
then
echo "hello $NAME, welcome !"
elif [ $NAME = itcast ]
then
echo "hello $NAME, welcome !"
else
echo "Get out Please!"
fi
```

画面3：
```bash
#!/bin/bash
read -p "please input your name:" NAME # read命令用于从控制台读取输入数据
## printf '%s\n' $NAME
if [ $NAME = root ]
then
echo "hello $NAME, welcome !"
elif [ $NAME = itcast ]
then
echo "hello $NAME, welcome !"
else
echo "Get out Please!"
fi
```

画面4：
```bash
#!/bin/bash
read -p "please input your name:" NAME # read命令用于从控制台读取输入数据
## printf '%s\n' $NAME
if [ $NAME = root ]
then
echo "hello $NAME, welcome !"
elif [ $NAME = itcast ]
then
echo "hello $NAME, welcome !"
else
echo "Get out Please!"
fi
```

画面5：
```bash
方式1：
#!/bin/bash
for i in 1 2 3
do
echo $i
done

方式2：
#!/bin/bash
for ((i=0; i<=5; i++))
do
echo "welcome $i times"
done
```

画面6：
```bash
#!/bin/bash
```

画面7：
```bash
#!/bin/bash
funWithReturn(){
echo "这个函数会对输入的两个数字进行相加运算..."
read aNum
echo "输入第二个数字："
read anotherNum
echo "两个数字分别为 $aNum 和 $anotherNum !"
return $(($aNum+$anotherNum));
}
funWithReturn
echo "输入的两个数字之和为 $?"
```

画面8：
```bash
#!/bin/bash
funWithReturn(){
echo "这个函数会对输入的两个数字进行相加运算..."
read aNum
echo "输入第二个数字："
read anotherNum
echo "两个数字分别为 $aNum 和 $anotherNum !"
return $(($aNum+$anotherNum));
}
funWithReturn
echo "输入的两个数字之和为 $?"
```

画面9：
```bash
#!/bin/bash
for ((i=0; i<=5; i++))
do
echo "welcome $i times"
done
```

画面10：
```bash
#!/bin/bash
funWithReturn(){
echo "这个函数会对输入的两个数字进行相加运算..."
read aNum
echo "输入第二个数字："
read anotherNum
echo "两个数字分别为 $aNum 和 $anotherNum !"
return $(($aNum+$anotherNum));
}
funWithReturn
echo "输入的两个数字之和为 $?"
```

画面11：
```bash
#!/bin/bash
funWithReturn(){
echo "这个函数会对输入的两个数字进行相加运算..."
read aNum
echo "输入第二个数字："
read anotherNum
echo "两个数字分别为 $aNum 和 $anotherNum !"
return $(($aNum+$anotherNum));
}
funWithReturn
echo "输入的两个数字之和为 $?"
```

画面12：
```bash
#!/bin/bash
funWithReturn(){
echo "这个函数会对输入的两个数字进行相加运算..."
read aNum
echo "输入第二个数字："
read anotherNum
echo "两个数字分别为 $aNum 和 $anotherNum !"
return $(($aNum+$anotherNum));
}
funWithReturn
echo "输入的两个数字之和为 $?"
```

画面13：
```bash
#!/bin/bash
funWithReturn(){
echo "这个函数会对输入的两个数字进行相加运算..."
read aNum
echo "输入第二个数字："
read anotherNum
echo "两个数字分别为 $aNum 和 $anotherNum !"
return $(($aNum+$anotherNum));
}
funWithReturn
echo "输入的两个数字之和为 $?"
```

画面14：
```bash
#!/bin/bash
a=1;
b=2;
echo expr $a + $b;
echo $(($a+$b));
echo $((a+b));
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：
- PPT 标题：4.3 运算符

画面2：
- PPT 标题：4.4 if语句

画面3：
- PPT 标题：4.4 if语句

画面4：
- PPT 标题：4.4 if语句

画面5：
- PPT 标题：4.5 for语句

画面6：
- PPT 标题：4.5 for语句

画面7：
- PPT 标题：4.6 函数

画面8：
- PPT 标题：4.6 函数

画面9：
- PPT 标题：4.5 for语句

画面10：
- PPT 标题：4.6 函数

画面11：
- PPT 标题：4.6 函数

画面12：
- PPT 标题：4.6 函数

画面

