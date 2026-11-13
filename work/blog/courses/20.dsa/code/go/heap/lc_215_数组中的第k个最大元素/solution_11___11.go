// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133471440
package main // 引入依赖

import (
	"fmt"
	"os"
	"sort"
) // 引入依赖

func findKthLargest(nums []int, k int) int { // 定义函数/方法 findKthLargest
	s := make([]int, len(nums)) // 把 make([]int, 长度(数组)) 写入 s :
	copy(s, nums)               // copy(字符串, 数组)
	sort.Slice(s, func(i, j int) bool { return s[i] > s[j] })
	return s[k-1] // 返回 字符串[下标 k 减 1]
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []struct {
		nums []int
		k    int
		want int
	}{ // 把 []struct{ 数组 []int; 下标 k int; want int }{ 写入 cases :
		{[]int{1, 2, 3}, 1, 3},
		{[]int{3, 2, 1, 5, 6, 4}, 2, 5},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := findKthLargest(c.nums, c.k); got != c.want { // 若 got : 赋值为 findKthLargest(字符.数组, 字符.下标 k); got 不等于 字符.want
			ok = false                                                                      // 把 false 写入 ok
			fmt.Printf("FAIL findKthLargest(%v,%d)=%d want %d\n", c.nums, c.k, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
