// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145385760
package main // 引入依赖
import (
	"fmt"
	"os"
	"strconv"
	"strings"
) // 引入依赖
func compareVersion(v1, v2 string) int { // 定义函数/方法 compareVersion
	a := strings.Split(v1, ".") // 把 strings.Split(v1, 「.」) 写入 a :
	b := strings.Split(v2, ".") // 把 strings.Split(v2, 「.」) 写入 b :
	n := len(a)
	if len(b) > n {
		n = len(b)
	} // 把 长度(数组); if 长度(b) 超过 元素个数 { 元素个数 赋值为 长度(b) } 写入 n :
	for i := 0; i < n; i++ { // 让 下标 i 从 0 开始计数
		x, y := 0, 0 // 把 0, 0 写入 x, y :
		if i < len(a) {
			x, _ = strconv.Atoi(a[i])
		} // 若 下标 i 小于 长度(数组) { x, _ 赋值为 strconv.Atoi(数组[下标 i]) }
		if i < len(b) {
			y, _ = strconv.Atoi(b[i])
		} // 若 下标 i 小于 长度(b) { y, _ 赋值为 strconv.Atoi(b[下标 i]) }
		if x > y {
			return 1
		} // 若 x 超过 y { return 1 }
		if x < y {
			return -1
		} // 若 x 小于 y { return 减 1 }
	}
	return 0 // 返回 0
}
func main() { // 程序入口：跑内嵌自测用例
	cases := []struct {
		a, b string
		want int
	}{ // 把 []struct{ 数组, b string; want int }{ 写入 cases :
		{"1.01", "1.001", 0}, {"1.0", "1.0.0", 0}, {"0.1", "1.1", -1}, {"1.0.1", "1", 1},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := compareVersion(c.a, c.b); got != c.want {
			ok = false
			fmt.Printf("FAIL=%v want %v\n", got, c.want)
		}
	}
	if !ok {
		os.Exit(1)
	} // 若 取反 ok { os.Exit(1) }
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
