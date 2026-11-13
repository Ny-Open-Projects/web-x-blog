// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145355207
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

func verifyPostorder(postorder []int) bool { // 定义函数/方法 verifyPostorder
	var helper func(seq []int) bool // var helper func(seq []int) bool
	helper = func(seq []int) bool { // 把 func(seq []int) bool { 写入 helper
		if len(seq) <= 1 { // 若 长度(seq) 不超过 1
			return true // 返回 true
		}
		root := seq[len(seq)-1]               // 把 seq[长度(seq) 减 1] 写入 root :
		i := 0                                // 把 0 写入 i :
		for i < len(seq)-1 && seq[i] < root { // for 下标 i 小于 长度(seq) 减 1 且 seq[下标 i] 小于 根节点 {
			i++ // 下标 i 加一
		}
		for j := i; j < len(seq)-1; j++ { // 把 下标 i; 下标 j 小于 长度(seq) 减 1; 下标 j 加一 { 写入 for j :
			if seq[j] <= root { // 若 seq[下标 j] 不超过 根节点
				return false // 返回 false
			}
		}
		return helper(seq[:i]) && helper(seq[i:len(seq)-1]) // 定义函数/方法 helper
	}
	return helper(postorder) // 定义函数/方法 helper
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		in   []int // in []int
		want bool  // want bool
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{[]int{1, 6, 3, 2, 5}, false},
		{[]int{1, 3, 2, 6, 5}, true},
		{[]int{4, 8, 6, 12, 10, 9}, true},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := verifyPostorder(c.in); got != c.want { // 若 got : 赋值为 verifyPostorder(字符.in); got 不等于 字符.want
			ok = false                                                             // 把 false 写入 ok
			fmt.Printf("FAIL verifyPostorder(%v)=%v want %v\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
