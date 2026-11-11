// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144821546
package main // 引入依赖

// 忠实翻译自 python/dp/lc_674_最长连续递增序列/solution_1_1_____1____.py
import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
)

func findLengthOfLCIS(nums []int) int { // 定义函数/方法 findLengthOfLCIS
	if len(nums) == 0 { // 若 长度(数组) 等于 0
		return 0 // 返回 0
	}
	ans := 1                         // 把 1 写入 ans :
	cur := 1                         // 把 1 写入 cur :
	for i := 1; i < len(nums); i++ { // 让 下标 i 从 1 开始计数
		if nums[i] > nums[i-1] { // 若 数组[下标 i] 超过 数组[下标 i 减 1]
			cur++          // 当前值 加一
			if cur > ans { // 若 当前值 超过 答案
				ans = cur // 把 当前值 写入 答案
			}
		} else { // 否则
			cur = 1 // 把 1 写入 当前值
		}
	}
	return ans // 返回 答案
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
