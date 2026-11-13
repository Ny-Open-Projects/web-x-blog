// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145241347
package main // 引入依赖

import (
	"fmt"
	"os"
) // 引入依赖

func canJump(nums []int) bool { // 定义函数/方法 canJump
	maxReach := 0               // 把 0 写入 maxReach :
	for i, step := range nums { // 同时取 下标 i 与 步数 遍历
		if i > maxReach { // 若 下标 i 超过 maxReach
			return false // 返回 false
		}
		if i+step > maxReach { // 若 下标 i 加 步数 超过 maxReach
			maxReach = i + step // 把 下标 i 加 步数 写入 maxReach
		}
	}
	return true // 返回 true
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		in   []int // in []int
		want bool  // want bool
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{[]int{2, 3, 1, 1, 4}, true},
		{[]int{3, 2, 1, 0, 4}, false},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := canJump(c.in); got != c.want { // 若 got : 赋值为 canJump(字符.in); got 不等于 字符.want
			ok = false                                                     // 把 false 写入 ok
			fmt.Printf("FAIL canJump(%v)=%v want %v\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
