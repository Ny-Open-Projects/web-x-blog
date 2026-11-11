// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145116019
package main // 引入依赖
import (
	"fmt"
	"os"
) // 引入依赖
func minSubArrayLen(target int, nums []int) int { // 定义函数/方法 minSubArrayLen
	l, best, sum := 0, len(nums)+1, 0 // 把 0, 长度(数组) 加 1, 0 写入 l, best, sum :
	for r := 0; r < len(nums); r++ {  // 让 右指针 从 0 开始计数
		sum += nums[r]      // 累计和累加 数组[右指针]
		for sum >= target { // 把 目标值 { 写入 for sum >
			if r-l+1 < best {
				best = r - l + 1
			} // 若 右指针 减 左指针 加 1 小于 当前最优 { 当前最优 赋值为 右指针 减 左指针 加 1 }
			sum -= nums[l]
			l++ // 把 数组[左指针]; 左指针 加一 写入 sum -
		}
	}
	if best == len(nums)+1 {
		return 0
	} // 若 当前最优 等于 长度(数组) 加 1 { return 0 }
	return best // 返回 当前最优
}
func main() { // 程序入口：跑内嵌自测用例
	cases := []struct {
		t    int
		nums []int
		want int
	}{ // 把 []struct{ 另一字符串 int; 数组 []int; want int }{ 写入 cases :
		{7, []int{2, 3, 1, 2, 4, 3}, 2}, {4, []int{1, 4, 4}, 1}, {11, []int{1, 1, 1, 1, 1, 1, 1, 1}, 0},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := minSubArrayLen(c.t, c.nums); got != c.want {
			ok = false
			fmt.Printf("FAIL=%v want %v\n", got, c.want)
		}
	}
	if !ok {
		os.Exit(1)
	} // 若 取反 ok { os.Exit(1) }
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
