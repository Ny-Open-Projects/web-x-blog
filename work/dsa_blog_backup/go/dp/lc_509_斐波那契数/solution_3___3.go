// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130660242
package main // 引入依赖
import (
	"fmt"
	"os"
) // 引入依赖
func fib(n int) int { // 定义函数/方法 fib
	if n < 2 {
		return n
	} // 若 元素个数 小于 2 { return 元素个数 }
	a, b := 0, 1 // 把 0, 1 写入 a, b :
	for i := 2; i <= n; i++ {
		a, b = b, a+b
	} // 让 下标 i 从 2 开始计数
	return b // 返回 b
}
func main() { // 程序入口：跑内嵌自测用例
	cases := []struct {
		in   int
		want int
	}{{0, 0}, {1, 1}, {2, 1}, {10, 55}}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := fib(c.in); got != c.want {
			ok = false
			fmt.Printf("FAIL fib(%v)=%v want %v\n", c.in, got, c.want)
		}
	}
	if !ok {
		os.Exit(1)
	} // 若 取反 ok { os.Exit(1) }
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
