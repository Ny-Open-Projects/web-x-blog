// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144850170
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

func max2(a, b int) int { // 定义函数/方法 max2
	if a > b { // 若 数组 超过 b
		return a // 返回 数组
	}
	return b // 返回 b
}

// rob 是 Python 参考 solution_1 的忠实翻译（两条 DP 线：dp1 不抢最后一个，dp2 不抢第一个）。
func rob(nums []int) int { // 定义函数/方法 rob
	n := len(nums) // 把 长度(数组) 写入 n :
	if n == 0 {    // 若 元素个数 等于 0
		return 0 // 返回 0
	}
	if n == 1 { // 若 元素个数 等于 1
		return nums[0] // 返回 数组[0]
	}
	dp1 := make([]int, n)           // 把 make([]int, 元素个数) 写入 dp1 :
	dp2 := make([]int, n)           // 把 make([]int, 元素个数) 写入 dp2 :
	dp1[0] = nums[0]                // 把 数组[0] 写入 dp1[0]
	dp1[1] = max2(nums[0], nums[1]) // 把 max2(数组[0], 数组[1]) 写入 dp1[1]
	dp2[1] = nums[1]                // 把 数组[1] 写入 dp2[1]
	for i := 2; i < n; i++ {        // 让 下标 i 从 2 开始计数
		dp1[i] = max2(dp1[i-1], dp1[i-2]+nums[i]) // 把 max2(dp1[下标 i 减 1], dp1[下标 i 减 2] 加 数组[下标 i]) 写入 dp1[i]
	}
	for i := 2; i < n; i++ { // 让 下标 i 从 2 开始计数
		dp2[i] = max2(dp2[i-1], dp2[i-2]+nums[i]) // 把 max2(dp2[下标 i 减 1], dp2[下标 i 减 2] 加 数组[下标 i]) 写入 dp2[i]
	}
	return max2(dp1[n-2], dp2[n-1]) // 定义函数/方法 max2
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		nums []int // 数组 []int
		want int   // want int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{[]int{2, 3, 2}, 3},
		{[]int{1, 2, 3, 1}, 4},
		{[]int{5}, 5},
		{[]int{3, 2, 4, 1}, 7},
		{[]int{2, 1, 1, 2}, 3},
	}
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := rob(c.nums); got != c.want { // 若 got : 赋值为 rob(字符.数组); got 不等于 字符.want
			fmt.Printf("FAIL %v got=%d want=%d\n", c.nums, got, c.want) // 打印输出
			os.Exit(1)                                                  // os.Exit(1)
		}
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
