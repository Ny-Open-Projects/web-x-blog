// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144821546
package main // 引入依赖

// 忠实翻译自 python/dp/lc_674_最长连续递增序列/solution_3_3_____3______.py
import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
)

func findLengthOfLCIS(nums []int) int { // 定义函数/方法 findLengthOfLCIS
	n := len(nums) // 把 长度(数组) 写入 n :
	if n <= 1 {    // 若 元素个数 不超过 1
		return n // 返回 元素个数
	}
	count := 1           // 把 1 写入 count :
	dp := make([]int, n) // 把 make([]int, 元素个数) 写入 dp :
	for i := range dp {  // 把 range DP 表 { 写入 for i :
		dp[i] = 1 // 把 1 写入 dp[i]
	}
	for i := 1; i < n; i++ { // 让 下标 i 从 1 开始计数
		if nums[i-1] < nums[i] { // 若 数组[下标 i 减 1] 小于 数组[下标 i]
			dp[i] = dp[i-1] + 1 // 把 DP 表[下标 i 减 1] 加 1 写入 dp[i]
		}
		if count < dp[i] { // 若 计数 小于 DP 表[下标 i]
			count = dp[i] // 把 DP 表[下标 i] 写入 计数
		}
	}
	return count // 返回 计数
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []struct { // 把 []struct { 写入 cases :
		in   []int // in []int
		want int   // want int
	}{ // }{
		{[]int{1, 3, 5, 4, 7}, 3}, // normal: 最长连续递增 [1,3,5]
		{[]int{2, 2, 2, 2, 2}, 1}, // boundary: 全部相等
		{[]int{}, 0},              // boundary: 空数组
		{[]int{1}, 1},             // boundary: 单元素
		{[]int{1, 2, 3}, 3},       // normal: 整段递增
		{[]int{5, 4, 3, 2, 1}, 1}, // boundary: 严格递减
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := findLengthOfLCIS(c.in); !reflect.DeepEqual(got, c.want) {
			ok = false                                                              // 把 false 写入 ok
			fmt.Printf("FAIL findLengthOfLCIS(%v)=%v want %v\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
