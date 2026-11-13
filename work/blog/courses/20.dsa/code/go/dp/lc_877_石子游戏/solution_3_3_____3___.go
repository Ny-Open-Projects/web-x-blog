// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145355902
package main // 引入依赖

import (
	"fmt"
	"os"
) // 引入依赖

func stoneGame(piles []int) bool { // 定义函数/方法 stoneGame
	return true // 返回 true
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		in   []int // in []int
		want bool  // want bool
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{[]int{5, 3, 4, 5}, true},
		{[]int{3, 7, 2, 3}, true},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := stoneGame(c.in); got != c.want { // 若 got : 赋值为 stoneGame(字符.in); got 不等于 字符.want
			ok = false                                                       // 把 false 写入 ok
			fmt.Printf("FAIL stoneGame(%v)=%v want %v\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
