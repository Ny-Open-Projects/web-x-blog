// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145029963
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// singleNumber 基于集合（map 模拟）的解法：出现则移除，未出现则加入，最后剩下的即为答案。
// 忠实翻译自 Python 参考实现（方案2: 基于 Set）。
func singleNumber(nums []int) int { // 定义函数/方法 singleNumber
	seen := make(map[int]bool) // 把 make(映射表[int]bool) 写入 seen :
	for _, num := range nums { // 同时取 _ 与 num 遍历
		if seen[num] { // 若 已见集合[num]
			delete(seen, num) // delete(已见集合, num)
		} else { // 否则
			seen[num] = true // 把 true 写入 seen[num]
		}
	}
	// 题目保证恰好有一个只出现一次的数字
	for k := range seen { // 把 range 已见集合 { 写入 for k :
		return k // 返回 下标 k
	}
	return 0 // 返回 0
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
