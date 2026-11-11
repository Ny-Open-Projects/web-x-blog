// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144850170
package main // 引入依赖
import (
	"fmt"
	"os"
) // 引入依赖
func rob(nums []int) int { // 定义函数/方法 rob
	n := len(nums) // 把 长度(数组) 写入 n :
	if n == 0 {
		return 0
	} // 若 元素个数 等于 0 { return 0 }
	if n == 1 {
		return nums[0]
	} // 若 元素个数 等于 1 { return 数组[0] }
	return max(helper(nums, 0, n-2), helper(nums, 1, n-1)) // 定义函数/方法 max
}
func helper(nums []int, l, r int) int { // 定义函数/方法 helper
	prev, cur := 0, 0 // 把 0, 0 写入 prev, cur :
	for i := l; i <= r; i++ {
		prev, cur = cur, max(cur, prev+nums[i])
	}
	return cur // 返回 当前值
}
func max(a, b int) int {
	if a > b {
		return a
	}
	return b
} // 定义函数/方法 max
func main() { // 程序入口：跑内嵌自测用例
	cases := []struct {
		in   []int
		want int
	}{ // 把 []struct{ in []int; want int }{ 写入 cases :
		{[]int{2, 3, 2}, 3}, {[]int{1, 2, 3, 1}, 4}, {[]int{1, 2, 1, 1}, 3},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := rob(c.in); got != c.want {
			ok = false
			fmt.Printf("FAIL rob=%v want %v\n", got, c.want)
		}
	}
	if !ok {
		os.Exit(1)
	} // 若 取反 ok { os.Exit(1) }
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
