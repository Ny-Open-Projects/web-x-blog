// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130450957
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
)

func hasGroupsSizeX(deck []int) bool { // 定义函数/方法 hasGroupsSizeX
	count := map[int]int{}   // 把 映射表[int]int{} 写入 count :
	for _, v := range deck { // 同时取 _ 与 值 遍历
		count[v]++ // 计数[值] 加一
	}
	N := len(deck)            // 把 长度(deck) 写入 N :
	for X := 2; X <= N; X++ { // 让 X 从 2 开始计数
		if N%X == 0 { // 若 N 对…取模 X 等于 0
			all := true               // 把 true 写入 all :
			for _, v := range count { // 同时取 _ 与 值 遍历
				if v%X != 0 { // 若 值 对…取模 X 不等于 0
					all = false // 把 false 写入 all
					break       // 跳出循环
				}
			}
			if all { // 若 all
				return true // 返回 true
			}
		}
	}
	return false // 返回 false
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		in   []int // in []int
		want bool  // want bool
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{[]int{1, 1, 1, 2, 2, 2, 3, 3}, false},
		{[]int{1, 2, 3, 4, 4, 3, 2, 1}, true},
		{[]int{1, 1}, true},
		{[]int{1}, false},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := hasGroupsSizeX(c.in); !reflect.DeepEqual(got, c.want) {
			ok = false                                                            // 把 false 写入 ok
			fmt.Printf("FAIL hasGroupsSizeX(%v)=%v want %v\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
