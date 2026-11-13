// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134668646
package main // 引入依赖
import (
	"fmt"
	"os"
	"sort"
) // 引入依赖
func bisectLeft(s []int, x int, lo int) int { // 定义函数/方法 bisectLeft
	for lo < len(s) && s[lo] < x { // for 左边界 小于 长度(字符串) 且 字符串[左边界] 小于 x {
		lo++ // 左边界 加一
	}
	return lo // 返回 左边界
}
func findContentChildren(g []int, s []int) int { // 定义函数/方法 findContentChildren
	sort.Ints(g)              // sort.Ints(g)
	sort.Ints(s)              // sort.Ints(字符串)
	j := 0                    // 把 0 写入 j :
	count := 0                // 把 0 写入 count :
	for _, child := range g { // 同时取 _ 与 子节点 遍历
		k := bisectLeft(s, child, j) // 把 bisectLeft(字符串, 子节点, 下标 j) 写入 k :
		if k < len(s) {              // 若 下标 k 小于 长度(字符串
			count++   // 计数 加一
			j = k + 1 // 把 下标 k 加 1 写入 下标 j
		} else { // 否则
			break // 跳出循环
		}
	}
	return count // 返回 计数
}
func main() { // 程序入口：跑内嵌自测用例
	cases := []struct {
		g    []int
		s    []int
		want int
	}{ // 把 []struct{ g []int; 字符串 []int; want int }{ 写入 cases :
		{[]int{1, 2, 3}, []int{1, 1}, 1},
		{[]int{1, 2}, []int{1, 2, 3}, 2},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := findContentChildren(c.g, c.s); got != c.want {
			ok = false
			fmt.Printf("FAIL got %d want %d\n", got, c.want) // 打印输出
		}
	}
	if !ok {
		os.Exit(1)
	} // 若 取反 ok { os.Exit(1) }
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
