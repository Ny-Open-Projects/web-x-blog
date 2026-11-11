// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144831173
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// longestArithSeqLength 是 Python 参考 solution_1 的忠实翻译（DP dp[i][d]）。
func longestArithSeqLength(nums []int) int { // 定义函数/方法 longestArithSeqLength
	if len(nums) <= 2 { // 若 长度(数组) 不超过 2
		return len(nums) // 定义函数/方法 len
	}
	n := len(nums)               // 把 长度(数组) 写入 n :
	dp := make([]map[int]int, n) // 把 make([]映射表[int]int, 元素个数) 写入 dp :
	for i := range dp {          // 把 range DP 表 { 写入 for i :
		dp[i] = map[int]int{} // 把 映射表[int]int{} 写入 dp[i]
	}
	ans := 2                 // 把 2 写入 ans :
	for i := 0; i < n; i++ { // 让 下标 i 从 0 开始计数
		for j := 0; j < i; j++ { // 让 下标 j 从 0 开始计数
			d := nums[i] - nums[j]     // 把 数组[下标 i] 减 数组[下标 j] 写入 d :
			prev := 1                  // 把 1 写入 prev :
			if v, ok := dp[j][d]; ok { // 若 值, ok : 赋值为 DP 表[下标 j][d]; ok
				prev = v // 把 值 写入 前一个
			}
			cur := prev + 1 // 把 前一个 加 1 写入 cur :
			dp[i][d] = cur  // 把 当前值 写入 dp[i][d]
			if cur > ans {  // 若 当前值 超过 答案
				ans = cur // 把 当前值 写入 答案
			}
		}
	}
	return ans // 返回 答案
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		nums []int // 数组 []int
		want int   // want int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{[]int{9, 4, 7, 2, 10}, 3},
		{[]int{20, 1, 15, 3, 10, 5, 8}, 4},
		{[]int{1, 2, 3, 4}, 4},
		{[]int{83, 20, 17, 43, 52, 78, 68, 45}, 2},
		{[]int{3, 6, 9, 12}, 4},
	}
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := longestArithSeqLength(c.nums); got != c.want { // 若 got : 赋值为 longestArithSeqLength(字符.数组); got 不等于 字符.want
			fmt.Printf("FAIL %v got=%d want=%d\n", c.nums, got, c.want) // 打印输出
			os.Exit(1)                                                  // os.Exit(1)
		}
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
