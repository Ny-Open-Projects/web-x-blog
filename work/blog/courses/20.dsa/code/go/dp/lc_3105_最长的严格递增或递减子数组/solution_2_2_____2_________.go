// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144829935
package main // 引入依赖

import (
	"fmt"
	"os"
) // 引入依赖

func longestMonotonicSubarray(nums []int) int { // 定义函数/方法 longestMonotonicSubarray
	if len(nums) == 0 { // 若 长度(数组) 等于 0
		return 0 // 返回 0
	}
	n := len(nums) // 把 长度(数组) 写入 n :
	ans := 1       // 把 1 写入 ans :
	i := 0         // 把 0 写入 i :
	for i < n {    // for 下标 i 小于 元素个数 {
		j := i                               // 把 下标 i 写入 j :
		for j+1 < n && nums[j+1] > nums[j] { // for 下标 j 加 1 小于 元素个数 且 数组[下标 j 加 1] 超过 数组[下标 j] {
			j++ // 下标 j 加一
		}
		if ans < j-i+1 { // 若 答案 小于 下标 j 减 下标 i 加 1
			ans = j - i + 1 // 把 下标 j 减 下标 i 加 1 写入 答案
		}
		j = i                                // 把 下标 i 写入 下标 j
		for j+1 < n && nums[j+1] < nums[j] { // for 下标 j 加 1 小于 元素个数 且 数组[下标 j 加 1] 小于 数组[下标 j] {
			j++ // 下标 j 加一
		}
		if ans < j-i+1 { // 若 答案 小于 下标 j 减 下标 i 加 1
			ans = j - i + 1 // 把 下标 j 减 下标 i 加 1 写入 答案
		}
		i++ // 下标 i 加一
	}
	return ans // 返回 答案
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		in   []int // in []int
		want int   // want int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{[]int{1, 4, 3, 3, 2}, 2},
		{[]int{1, 2, 3, 4, 5}, 5},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := longestMonotonicSubarray(c.in); got != c.want { // 若 got : 赋值为 longestMonotonicSubarray(字符.in); got 不等于 字符.want
			ok = false                                                                      // 把 false 写入 ok
			fmt.Printf("FAIL longestMonotonicSubarray(%v)=%v want %v\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
