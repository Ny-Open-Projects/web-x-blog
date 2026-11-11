// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145116019
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
)

func minSubArrayLen(target int, nums []int) int { // 定义函数/方法 minSubArrayLen
	n := len(nums) // 把 长度(数组) 写入 n :
	if n == 0 {    // 若 元素个数 等于 0
		return 0 // 返回 0
	}
	ans := int(^uint(0) >> 1) // 把 int( 按位异或 uint(0) 超过 超过 1) 写入 ans :
	for i := 0; i < n; i++ {  // 让 下标 i 从 0 开始计数
		s := 0                   // 把 0 写入 s :
		for j := i; j < n; j++ { // 把 下标 i; 下标 j 小于 元素个数; 下标 j 加一 { 写入 for j :
			s += nums[j]     // 字符串累加 数组[下标 j]
			if s >= target { // 若 字符串 不低于 目标值
				if j-i+1 < ans { // 若 下标 j 减 下标 i 加 1 小于 答案
					ans = j - i + 1 // 把 下标 j 减 下标 i 加 1 写入 答案
				}
				break // 跳出循环
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
	_ = reflect.DeepEqual // 把 reflect.DeepEqual 写入 _
	if !ok {              // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
