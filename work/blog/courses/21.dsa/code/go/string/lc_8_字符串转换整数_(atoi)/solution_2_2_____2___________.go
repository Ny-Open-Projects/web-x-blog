// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145385760
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
	"strings" // 「strings」
)

func myAtoi(s string) int { // 定义函数/方法 myAtoi
	s = strings.TrimSpace(s) // 把 strings.TrimSpace(字符串) 写入 字符串
	if len(s) == 0 {         // 若 长度(字符串) 等于 0
		return 0 // 返回 0
	}
	i := 0           // 把 0 写入 i :
	sign := 1        // 把 1 写入 sign :
	if s[i] == '+' { // 若 字符串[下标 i] 等于 ' 加 '
		i++ // 下标 i 加一
	} else if s[i] == '-' { // 否则，若 字符串[下标 i] 等于 ' 减 '
		sign = -1 // 把 减 1 写入 sign
		i++       // 下标 i 加一
	}
	res := 0                                       // 把 0 写入 res :
	INT_MAX := 2147483647                          // 把 2147483647 写入 INT_MAX :
	for i < len(s) && s[i] >= '0' && s[i] <= '9' { // 把 '0' 且 字符串[下标 i] 不超过 '9' { 写入 for i < len(s) && s[i] >
		digit := int(s[i] - '0')                                  // 把 int(字符串[下标 i] 减 '0') 写入 digit :
		if res > INT_MAX/10 || (res == INT_MAX/10 && digit > 7) { // 若 结果 超过 INT_MAX 除以 10 或 (结果 等于 INT_MAX 除以 10 且 digit 超过 7
			if sign == 1 { // 若 sign 等于 1
				return INT_MAX // 返回 INT_MAX
			}
			return -INT_MAX - 1 // 返回 减 INT_MAX 减 1
		}
		res = res*10 + digit // 把 结果 乘 10 加 digit 写入 结果
		i++                  // 下标 i 加一
	}
	return sign * res // 返回 sign 乘 结果
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
