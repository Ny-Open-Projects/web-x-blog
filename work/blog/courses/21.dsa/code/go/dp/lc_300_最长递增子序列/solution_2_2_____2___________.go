// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144823912
package main // 引入依赖

import (
	"fmt"
	"os"
) // 引入依赖

func lengthOfLIS(nums []int) int { // 定义函数/方法 lengthOfLIS
	n := len(nums) // 把 长度(数组) 写入 n :
	if n == 0 {    // 若 元素个数 等于 0
		return 0 // 返回 0
	}
	dp := []int{}              // 把 []int{} 写入 dp :
	for _, num := range nums { // 同时取 _ 与 num 遍历
		lo, hi := 0, len(dp) // 把 0, 长度(DP 表) 写入 lo, hi :
		for lo < hi {        // for 左边界 小于 右边界 {
			mid := (lo + hi) / 2 // 把 (左边界 加 右边界) 除以 2 写入 mid :
			if dp[mid] < num {   // 若 DP 表[中点] 小于 num
				lo = mid + 1 // 把 中点 加 1 写入 左边界
			} else { // 否则
				hi = mid // 把 中点 写入 右边界
			}
		}
		i := lo           // 把 左边界 写入 i :
		if i == len(dp) { // 若 下标 i 等于 长度(DP 表
			dp = append(dp, num) // 把 append(DP 表, num) 写入 DP 表
		} else { // 否则
			dp[i] = num // 把 num 写入 dp[i]
		}
	}
	return len(dp) // 定义函数/方法 len
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		in   []int // in []int
		want int   // want int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{[]int{10, 9, 2, 5, 3, 7, 101, 18}, 4},
		{[]int{}, 0},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := lengthOfLIS(c.in); got != c.want { // 若 got : 赋值为 lengthOfLIS(字符.in); got 不等于 字符.want
			ok = false                                                         // 把 false 写入 ok
			fmt.Printf("FAIL lengthOfLIS(%v)=%v want %v\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
