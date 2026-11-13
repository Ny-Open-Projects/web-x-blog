// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145355653
package main // 引入依赖
import (
	"fmt"
	"os"
) // 引入依赖
func isPowerOfThree(n int) bool { // 定义判定函数 isPowerOfThree
	if n <= 0 {
		return false
	} // 若 元素个数 不超过 0 { return false }
	for n%3 == 0 {
		n /= 3
	} // 把 赋值为 0 { 元素个数 除以 3 } 写入 for n%3
	return n == 1 // 返回 元素个数 等于 1
}
func main() { // 程序入口：跑内嵌自测用例
	cases := []struct {
		in   int
		want bool
	}{ // 把 []struct{ in int; want bool }{ 写入 cases :
		{1, true}, {0, false}, {9, true}, {2, false}, {27, true},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := isPowerOfThree(c.in); got != c.want {
			ok = false
			fmt.Printf("FAIL=%v want %v\n", got, c.want)
		}
	}
	if !ok {
		os.Exit(1)
	} // 若 取反 ok { os.Exit(1) }
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
