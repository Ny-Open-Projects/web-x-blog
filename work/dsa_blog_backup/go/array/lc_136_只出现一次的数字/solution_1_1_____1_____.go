// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145029963
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// singleNumber 位运算解法：所有元素异或，成对数字抵消，剩下只出现一次的数字。
// 忠实翻译自 Python 参考实现（方案1: 位运算）。
func singleNumber(nums []int) int { // 定义函数/方法 singleNumber
	res := 0                 // 把 0 写入 res :
	for _, v := range nums { // 同时取 _ 与 值 遍历
		res ^= v // 把 值 写入 res ^
	}
	return res // 返回 结果
}

func selfCheck() bool { // 定义函数/方法 selfCheck
	// (args, expected) 取自 _tools/correctness_check.py 的 lc_136_只出现一次的数字 cases
	cases := []struct { // 把 []struct { 写入 cases :
		name string // name string
		in   []int  // in []int
		want int    // want int
	}{ // }{
		{"case1", []int{2, 2, 1}, 1},
		{"case2", []int{4, 1, 2, 1, 2}, 4},
		{"case3", []int{1}, 1},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		got := singleNumber(c.in) // 把 singleNumber(字符.in) 写入 got :
		if got != c.want {        // 若 got 不等于 字符.want
			ok = false                                                   // 把 false 写入 ok
			fmt.Printf("FAIL %s: got %d want %d\n", c.name, got, c.want) // 打印输出
		}
	}
	return ok // 返回 ok
}

func main() { // 程序入口：跑内嵌自测用例
	if !selfCheck() { // 若 取反 selfCheck(
		fmt.Println("FAIL") // 打印输出
		os.Exit(1)          // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
