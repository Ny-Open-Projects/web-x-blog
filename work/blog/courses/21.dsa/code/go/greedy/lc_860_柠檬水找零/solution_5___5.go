// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134661209
package main // 引入依赖
import (
	"fmt"
	"os"
) // 引入依赖
func lemonadeChange(bills []int) bool { // 定义函数/方法 lemonadeChange
	five, ten := 0, 0            // 把 0, 0 写入 five, ten :
	for _, bill := range bills { // 同时取 _ 与 bill 遍历
		if bill == 5 {
			five++
		} else if bill == 10 { // 若 bill 等于 5 { five 加一 } else if bill 等于 10
			if five == 0 {
				return false
			} // 若 five 等于 0 { return false }
			five--
			ten++ // five 减一 ; ten 加一
		} else { // 否则
			if ten > 0 && five > 0 {
				ten--
				five--
			} else if five >= 3 {
				five -= 3
			} else {
				return false
			}
		}
	}
	return true // 返回 true
}
func main() { // 程序入口：跑内嵌自测用例
	ok := true // 把 true 写入 ok :
	if !lemonadeChange([]int{5, 5, 5, 10, 20}) {
		ok = false
		fmt.Println("FAIL1")
	}
	if lemonadeChange([]int{5, 5, 10, 10, 20}) {
		ok = false
		fmt.Println("FAIL2")
	}
	if !ok {
		os.Exit(1)
	} // 若 取反 ok { os.Exit(1) }
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
