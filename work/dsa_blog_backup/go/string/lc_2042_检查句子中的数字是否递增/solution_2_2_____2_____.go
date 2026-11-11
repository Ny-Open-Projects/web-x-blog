// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145374488
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
	"strconv" // 「strconv」
	"strings" // 「strings」
)

func areNumbersAscending(s string) bool { // 定义函数/方法 areNumbersAscending
	words := strings.Fields(s)   // 把 strings.Fields(字符串) 写入 words :
	prev := 0                    // 把 0 写入 prev :
	for _, word := range words { // 同时取 _ 与 单词 遍历
		if word[0] >= '0' && word[0] <= '9' { // 若 单词[0] 不低于 '0' 且 单词[0] 不超过 '9'
			num, _ := strconv.Atoi(word) // 把 strconv.Atoi(单词) 写入 num, _ :
			if num <= prev {             // 若 num 不超过 前一个
				return false // 返回 false
			}
			prev = num // 把 num 写入 前一个
		}
	}
	return true // 返回 true
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		in   string // in string
		want bool   // want bool
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{"abc", true},
		{"1 2 3", true},
		{"1 box has 3 blue 4 red 6 green and 12 yellow", true},
		{"sunset 13 sunset 11", false},
		{"hello world 5 x 5", false},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := areNumbersAscending(c.in); !reflect.DeepEqual(got, c.want) {
			ok = false                                                                 // 把 false 写入 ok
			fmt.Printf("FAIL areNumbersAscending(%q)=%v want %v\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
