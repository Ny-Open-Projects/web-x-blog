// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145116019
package main // 引入依赖

import (
	"fmt"  // 「fmt」
	"os"   // 「os」
	"sort" // 「sort」
)

func bisectLeft(arr []int, x int) int { // 定义函数/方法 bisectLeft
	return sort.Search(len(arr), func(i int) bool { return arr[i] >= x })
}

func minSubArrayLen(target int, nums []int) int { // 定义函数/方法 minSubArrayLen
	n := len(nums) // 把 长度(数组) 写入 n :
	if n == 0 {    // 若 元素个数 等于 0
		return 0 // 返回 0
	}
	ans := int(^uint(0) >> 1) // 把 int( 按位异或 uint(0) 超过 超过 1) 写入 ans :
	sums := make([]int, n+1)  // 把 make([]int, 元素个数 加 1) 写入 sums :
	for i := 1; i <= n; i++ { // 让 下标 i 从 1 开始计数
		sums[i] = sums[i-1] + nums[i-1] // 把 sums[下标 i 减 1] 加 数组[下标 i 减 1] 写入 sums[i]
	}
	for i := 1; i <= n; i++ { // 让 下标 i 从 1 开始计数
		t := sums[i-1] + target      // 把 sums[下标 i 减 1] 加 目标值 写入 t :
		bound := bisectLeft(sums, t) // 把 bisectLeft(sums, 另一字符串) 写入 bound :
		if bound <= n {              // 若 bound 不超过 元素个数
			if bound-(i-1) < ans { // 若 bound 减 (下标 i 减 1) 小于 答案
				ans = bound - (i - 1) // 把 bound 减 (下标 i 减 1) 写入 答案
			}
		}
	}
	if ans == int(^uint(0)>>1) { // 若 答案 等于 int( 按位异或 uint(0) 超过 超过 1
		return 0 // 返回 0
	}
	return ans // 返回 答案
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		target int   // 目标值 int
		nums   []int // 数组 []int
		want   int   // want int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{1, []int{1, 2, 3}, 1},
		{7, []int{2, 3, 1, 2, 4, 3}, 2},
		{11, []int{1, 2, 3, 4, 5}, 3},
		{15, []int{1, 2, 3, 4, 5}, 5},
		{100, []int{1, 2, 3}, 0},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := minSubArrayLen(c.target, c.nums); got != c.want { // 若 got : 赋值为 minSubArrayLen(字符.目标值, 字符.数组); got 不等于 字符.want
			ok = false                                                                           // 把 false 写入 ok
			fmt.Printf("FAIL minSubArrayLen(%v,%v)=%v want %v\n", c.target, c.nums, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
