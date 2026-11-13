// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145385760
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"math"    // 「math」
	"os"      // 「os」
	"reflect" // 「reflect」
)

type Automaton struct { // 定义类型
	state string // state string
	sign  int    // sign int
	ans   int    // 答案 int
}

var autoTable = map[string][]string{ // 把 映射表[string][]string{ 存入 autoTable
	"start":     {"start", "signed", "in_number", "end"},
	"signed":    {"end", "end", "in_number", "end"},
	"in_number": {"end", "end", "in_number", "end"},
	"end":       {"end", "end", "end", "end"},
}

func (a *Automaton) getCol(c byte) int { // 定义函数/方法 getCol
	if c == ' ' { // 若 字符 等于 ' '
		return 0 // 返回 0
	}
	if c == '+' || c == '-' { // 若 字符 等于 ' 加 ' 或 字符 等于 ' 减 '
		return 1 // 返回 1
	}
	if c >= '0' && c <= '9' { // 若 字符 不低于 '0' 且 字符 不超过 '9'
		return 2 // 返回 2
	}
	return 3 // 返回 3
}

func (a *Automaton) get(c byte) { // 定义函数/方法 get
	a.state = autoTable[a.state][a.getCol(c)] // 把 autoTable[数组.state][数组.getCol(字符)] 写入 a.state
	if a.state == "in_number" {               // 若 数组.state 等于 「in_number」
		a.ans = a.ans*10 + int(c-'0') // 把 数组.答案 乘 10 加 int(字符 减 '0') 写入 答案
		if a.sign == 1 {              // 若 数组.sign 等于 1
			if a.ans > math.MaxInt32 { // 若 数组.答案 超过 math.MaxInt32
				a.ans = math.MaxInt32 // 把 math.MaxInt32 写入 答案
			}
		} else { // 否则
			if a.ans > math.MaxInt32+1 { // 若 数组.答案 超过 math.MaxInt32 加 1
				a.ans = math.MaxInt32 + 1 // 把 math.MaxInt32 加 1 写入 答案
			}
		}
	} else if a.state == "signed" { // 否则，若 数组.state 等于 「signed」
		if c == '+' { // 若 字符 等于 ' 加 '
			a.sign = 1 // 把 1 写入 a.sign
		} else { // 否则
			a.sign = -1 // 把 减 1 写入 a.sign
		}
	}
}

func myAtoi(str string) int { // 定义函数/方法 myAtoi
	auto := &Automaton{state: "start", sign: 1, ans: 0} // 把 按位与 Automaton{state: 「起点」, sign: 1, 答案: 0} 写入 auto :
	for i := 0; i < len(str); i++ {                     // 让 下标 i 从 0 开始计数
		auto.get(str[i]) // auto 查找 str[下标 i])
	}
	return auto.sign * auto.ans // 返回 auto.sign 乘 auto.答案
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		in   string // in string
		want int    // want int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{"   -42", -42},
		{"4193 with words", 4193},
		{"words and 987", 0},
		{"-91283472332", -2147483648},
		{"+1", 1},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := myAtoi(c.in); !reflect.DeepEqual(got, c.want) { // 若 got : 赋值为 myAtoi(字符.in); 取反 reflect.DeepEqual(got, 字符.want
			ok = false                                                    // 把 false 写入 ok
			fmt.Printf("FAIL myAtoi(%q)=%v want %v\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
