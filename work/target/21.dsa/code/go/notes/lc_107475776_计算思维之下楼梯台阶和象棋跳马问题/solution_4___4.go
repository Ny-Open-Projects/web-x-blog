// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107475776
package main // 引入依赖
import (
	"fmt"
	"os"
) // 引入依赖
func horseJumpCount() int { // 定义函数/方法 horseJumpCount
	dx := []int{1, 2, 2, 1}   // 把 []int{1, 2, 2, 1} 写入 dx :
	dy := []int{2, 1, -1, -2} // 把 []int{2, 1, 减 1, 减 2} 写入 dy :
	count := 0                // 把 0 写入 count :
	var jump func(int, int)   // var jump func(int, int)
	jump = func(x, y int) {   // 把 func(x, y int) { 写入 jump
		if x == 8 && y == 4 { // 若 x 等于 8 且 y 等于 4
			count++ // 计数 加一
			return  // return
		}
		for k := 0; k < 4; k++ { // 让 下标 k 从 0 开始计数
			nx, ny := x+dx[k], y+dy[k]                    // 把 x 加 dx[下标 k], y 加 dy[下标 k] 写入 nx, ny :
			if nx >= 0 && nx <= 8 && ny >= 0 && ny <= 4 { // 若 nx 不低于 0 且 nx 不超过 8 且 ny 不低于 0 且 ny 不超过 4
				jump(nx, ny) // jump(nx, ny)
			}
		}
	}
	jump(0, 0)   // jump(0, 0)
	return count // 返回 计数
}
func main() { // 程序入口：跑内嵌自测用例
	cases := []struct{ want int }{{37}, {37}} // 把 []struct{ want int }{ {37}, {37} } 写入 cases :
	got := horseJumpCount()                   // 把 horseJumpCount() 写入 got :
	ok := true                                // 把 true 写入 ok :
	for _, c := range cases {                 // 同时取 _ 与 字符 遍历
		if got != c.want {
			ok = false
			fmt.Printf("FAIL got %d want %d\n", got, c.want)
		}
	}
	if !ok {
		os.Exit(1)
	} // 若 取反 ok { os.Exit(1) }
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
