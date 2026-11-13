// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107475776
package main // 引入依赖
import (
	"fmt"
	"os"
) // 引入依赖
func horseJumpCount() int { // 定义函数/方法 horseJumpCount
	type Position struct{ x, y int }                      // 定义类型
	moves := []Position{{1, 2}, {2, 1}, {2, -1}, {1, -2}} // 把 []Position{{1, 2}, {2, 1}, {2, 减 1}, {1, 减 2}} 写入 moves :
	start := Position{0, 0}                               // 把 Position{0, 0} 写入 start :
	goal := Position{8, 4}                                // 把 Position{8, 4} 写入 goal :
	isValid := func(p Position) bool { return p.x >= 0 && p.x <= 8 && p.y >= 0 && p.y <= 4 }
	isGoal := func(p Position) bool { return p.x == goal.x && p.y == goal.y }
	count := 0                  // 把 0 写入 count :
	var jump func(Position)     // var jump func(Position)
	jump = func(pos Position) { // 把 func(pos Position) { 写入 jump
		if isGoal(pos) { // 定义判定函数 isGoal
			count++ // 计数 加一
			return  // return
		}
		for _, mv := range moves { // 同时取 _ 与 mv 遍历
			nxt := Position{pos.x + mv.x, pos.y + mv.y} // 把 Position{pos.x 加 mv.x, pos.y 加 mv.y} 写入 nxt :
			if !isValid(nxt) {                          // 若 取反 isValid(nxt
				continue // 跳过本轮，进入下一次
			}
			jump(nxt) // jump(nxt)
		}
	}
	jump(start)  // jump(起点)
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
