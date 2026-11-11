// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130455100
package main // 引入依赖
import (
	"fmt"
	"os"
) // 引入依赖
func canPlaceFlowers(flowerbed []int, n int) bool { // 定义函数/方法 canPlaceFlowers
	cnt := 0                 // 把 0 写入 cnt :
	m := len(flowerbed)      // 把 长度(flowerbed) 写入 m :
	for i := 0; i < m; i++ { // 让 下标 i 从 0 开始计数
		if flowerbed[i] == 0 && (i == 0 || flowerbed[i-1] == 0) && (i == m-1 || flowerbed[i+1] == 0) {
			flowerbed[i] = 1 // 把 1 写入 flowerbed[i]
			cnt++            // 计数 加一
			if cnt >= n {
				return true
			} // 若 计数 不低于 元素个数 { return true }
		}
	}
	return cnt >= n // 返回 计数 不低于 元素个数
}
func main() { // 程序入口：跑内嵌自测用例
	cases := []struct {
		bed  []int
		n    int
		want bool
	}{ // 把 []struct{ bed []int; 元素个数 int; want bool }{ 写入 cases :
		{[]int{1, 0, 0, 0, 1}, 1, true},
		{[]int{1, 0, 0, 0, 1}, 2, false},
		{[]int{0}, 1, true},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := canPlaceFlowers(c.bed, c.n); got != c.want {
			ok = false
			fmt.Printf("FAIL canPlaceFlowers(%v,%d)=%v want %v\n", c.bed, c.n, got, c.want) // 打印输出
		}
	}
	if !ok {
		os.Exit(1)
	} // 若 取反 ok { os.Exit(1) }
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
