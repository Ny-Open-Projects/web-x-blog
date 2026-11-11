// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145344295
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

func containsDuplicate(nums []int) bool { // 定义函数/方法 containsDuplicate
	seen := make(map[int]bool) // 把 make(映射表[int]bool) 写入 seen :
	for _, v := range nums {   // 同时取 _ 与 值 遍历
		if seen[v] { // 若 已见集合[值]
			return true // 返回 true
		}
		seen[v] = true // 把 true 写入 seen[v]
	}
	return false // 返回 false
}

func main() { // 程序入口：跑内嵌自测用例
	ok := true       // 把 true 写入 ok :
	tc := []struct { // 把 []struct { 写入 tc :
		in   []int // in []int
		want bool  // want bool
	}{ // }{
		{[]int{1, 2, 3}, false},
		{[]int{1, 2, 3, 1}, true},
		{[]int{5, 5}, true},
	}
	for _, c := range tc { // 同时取 _ 与 字符 遍历
		if got := containsDuplicate(c.in); got != c.want { // 若 got : 赋值为 containsDuplicate(字符.in); got 不等于 字符.want
			ok = false                                                               // 把 false 写入 ok
			fmt.Printf("FAIL containsDuplicate(%v)=%v want %v\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
