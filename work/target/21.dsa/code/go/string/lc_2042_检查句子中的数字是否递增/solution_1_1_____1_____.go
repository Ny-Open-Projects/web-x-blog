// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145374488
package main // 引入依赖
import (
	"fmt"
	"os"
) // 引入依赖
func areNumbersAscending(s string) bool { // 定义函数/方法 areNumbersAscending
	prev := -1                // 把 减 1 写入 prev :
	for i := 0; i < len(s); { // 让 下标 i 从 0 开始计数
		if s[i] >= '0' && s[i] <= '9' { // 若 字符串[下标 i] 不低于 '0' 且 字符串[下标 i] 不超过 '9'
			num := 0 // 把 0 写入 num :
			for i < len(s) && s[i] >= '0' && s[i] <= '9' {
				num = num*10 + int(s[i]-'0')
				i++
			}
			if prev >= num {
				return false
			} // 若 前一个 不低于 num { return false }
			prev = num // 把 num 写入 前一个
		} else {
			i++
		} // 否则
	}
	return true // 返回 true
}
func main() { // 程序入口：跑内嵌自测用例
	cases := []struct {
		in   string
		want bool
	}{ // 把 []struct{ in string; want bool }{ 写入 cases :
		{"a 1 b 2 c 3", true}, {"a 3 b 2", false}, {"abc", true},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := areNumbersAscending(c.in); got != c.want {
			ok = false
			fmt.Printf("FAIL=%v want %v\n", got, c.want)
		}
	}
	if !ok {
		os.Exit(1)
	} // 若 取反 ok { os.Exit(1) }
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
