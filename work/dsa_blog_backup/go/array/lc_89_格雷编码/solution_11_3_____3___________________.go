// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130456218
package main // 引入依赖
import (
	"fmt"
	"os"
) // 引入依赖
func grayCode(n int) []int { // 定义函数/方法 grayCode
	res := make([]int, 1<<n) // 把 make([]int, 1 小于 小于 元素个数) 写入 res :
	for i := 0; i < (1 << n); i++ {
		res[i] = i ^ (i >> 1)
	} // 让 下标 i 从 0 开始计数
	return res // 返回 结果
}
func main() { // 程序入口：跑内嵌自测用例
	cases := []struct {
		in   int
		want []int
	}{ // 把 []struct{ in int; want []int }{ 写入 cases :
		{0, []int{0}}, {1, []int{0, 1}}, {2, []int{0, 1, 3, 2}},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		got := grayCode(c.in) // 把 grayCode(字符.in) 写入 got :
		if len(got) != len(c.want) {
			ok = false
			fmt.Printf("FAIL len\n")
			continue
		}
		for i := range got {
			if got[i] != c.want[i] {
				ok = false
				fmt.Printf("FAIL grayCode(%v)=%v want %v\n", c.in, got, c.want)
				break
			}
		} // 打印输出
	}
	if !ok {
		os.Exit(1)
	} // 若 取反 ok { os.Exit(1) }
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
