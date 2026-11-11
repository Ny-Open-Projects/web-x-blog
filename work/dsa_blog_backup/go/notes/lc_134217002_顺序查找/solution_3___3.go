// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134217002
package main // 引入依赖
import (
	"fmt"
	"os"
) // 引入依赖
func seqSearch(arr []int, target int) int { // 定义函数/方法 seqSearch
	for i, v := range arr {
		if v == target {
			return i
		}
	} // 同时取 下标 i 与 值 遍历
	return -1 // 返回 减 1
}
func main() { // 程序入口：跑内嵌自测用例
	cases := []struct {
		arr  []int
		t    int
		want int
	}{ // 把 []struct{ 数组 []int; 另一字符串 int; want int }{ 写入 cases :
		{[]int{1, 2, 3}, 1, 0}, {[]int{1, 2, 3}, 3, 2}, {[]int{1, 2, 3}, 5, -1},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := seqSearch(c.arr, c.t); got != c.want {
			ok = false
			fmt.Printf("FAIL=%v want %v\n", got, c.want)
		}
	}
	if !ok {
		os.Exit(1)
	} // 若 取反 ok { os.Exit(1) }
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
