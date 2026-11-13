// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134668646
package main // 引入依赖
import (
	"fmt"
	"os"
	"sort"
) // 引入依赖
func findContentChildren(g []int, s []int) int { // 定义函数/方法 findContentChildren
	sort.Ints(g)              // sort.Ints(g)
	sort.Ints(s)              // sort.Ints(字符串)
	j := 0                    // 把 0 写入 j :
	n := len(s)               // 把 长度(字符串) 写入 n :
	count := 0                // 把 0 写入 count :
	for _, child := range g { // 同时取 _ 与 子节点 遍历
		for j < n && s[j] < child { // for 下标 j 小于 元素个数 且 字符串[下标 j] 小于 子节点 {
			j++ // 下标 j 加一
		}
		if j < n { // 若 下标 j 小于 元素个数
			count++ // 计数 加一
			j++     // 下标 j 加一
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
