// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107475776
package main // 引入依赖
import (
	"fmt"
	"os"
) // 引入依赖
func horseJumpCount() int { // 定义函数/方法 horseJumpCount
	type Position struct{ x, y int }                      // 定义类型
	moves := []Position{{1, 2}, {2, 1}, {2, -1}, {1, -2}} // 把 []Position{{1, 2}, {2, 1}, {2, 减 1}, {1, 减 2}} 写入 moves :
	count := 0                                            // 把 0 写入 count :
	var jump func(Position)                               // var jump func(Position)
	jump = func(pos Position) {                           // 把 func(pos Position) { 写入 jump
		if pos.x == 8 && pos.y == 4 { // 若 pos.x 等于 8 且 pos.y 等于 4
			count++ // 计数 加一
			return  // return
		}
		for _, mv := range moves { // 同时取 _ 与 mv 遍历
			nxt := Position{pos.x + mv.x, pos.y + mv.y}               // 把 Position{pos.x 加 mv.x, pos.y 加 mv.y} 写入 nxt :
			if nxt.x >= 0 && nxt.x <= 8 && nxt.y >= 0 && nxt.y <= 4 { // 若 nxt.x 不低于 0 且 nxt.x 不超过 8 且 nxt.y 不低于 0 且 nxt.y 不超过 4
				jump(nxt) // jump(nxt)
			}
		}
	}
	jump(Position{0, 0}) // jump(Position{0, 0})
	return count         // 返回 计数
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
