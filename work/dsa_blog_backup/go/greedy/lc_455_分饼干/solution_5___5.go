// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134668646
package main // 引入依赖
import (
	"fmt"
	"os"
	"sort"
) // 引入依赖
func findContentChildren(g []int, s []int) int { // 定义函数/方法 findContentChildren
	sort.Ints(g)               // sort.Ints(g)
	sort.Ints(s)               // sort.Ints(字符串)
	i := 0                     // 把 0 写入 i :
	for _, cookie := range s { // 同时取 _ 与 cookie 遍历
		if i < len(g) && cookie >= g[i] { // 若 下标 i 小于 长度(g) 且 cookie 不低于 g[下标 i]
			i++ // 下标 i 加一
		}
	}
	return i // 返回 下标 i
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
