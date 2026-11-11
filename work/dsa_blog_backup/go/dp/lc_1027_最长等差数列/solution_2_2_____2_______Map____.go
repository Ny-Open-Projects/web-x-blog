// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144831173
package main // 引入依赖
import (
	"fmt"
	"os"
) // 引入依赖
func longestArithSeqLength(nums []int) int { // 定义函数/方法 longestArithSeqLength
	n := len(nums) // 把 长度(数组) 写入 n :
	if n <= 2 {
		return n
	} // 若 元素个数 不超过 2 { return 元素个数 }
	best := 2                    // 把 2 写入 best :
	dp := make([]map[int]int, n) // 把 make([]映射表[int]int, 元素个数) 写入 dp :
	for i := range dp {
		dp[i] = map[int]int{}
	} // 把 range DP 表 { DP 表[下标 i] 赋值为 映射表[int]int{} } 写入 for i :
	for i := 1; i < n; i++ { // 让 下标 i 从 1 开始计数
		for j := 0; j < i; j++ { // 让 下标 j 从 0 开始计数
			d := nums[i] - nums[j] // 把 数组[下标 i] 减 数组[下标 j] 写入 d :
			v := 2                 // 把 2 写入 v :
			if dp[j][d] > 0 {
				v = dp[j][d] + 1
			} // 若 DP 表[下标 j][d] 超过 0 { 值 赋值为 DP 表[下标 j][d] 加 1 }
			if dp[i][d] < v {
				dp[i][d] = v
			} // 若 DP 表[下标 i][d] 小于 值 { DP 表[下标 i][d] 赋值为 值 }
			if dp[i][d] > best {
				best = dp[i][d]
			} // 若 DP 表[下标 i][d] 超过 当前最优 { 当前最优 赋值为 DP 表[下标 i][d] }
		}
	}
	return best // 返回 当前最优
}
func main() { // 程序入口：跑内嵌自测用例
	cases := []struct {
		in   []int
		want int
	}{ // 把 []struct{ in []int; want int }{ 写入 cases :
		{[]int{9, 4, 7, 2, 10}, 3}, {[]int{20, 1, 15, 3, 10, 5, 8}, 4}, {[]int{3, 6, 9, 12}, 4},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := longestArithSeqLength(c.in); got != c.want {
			ok = false
			fmt.Printf("FAIL=%v want %v\n", got, c.want)
		}
	}
	if !ok {
		os.Exit(1)
	} // 若 取反 ok { os.Exit(1) }
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
