// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145244562
package main // 引入依赖
import (
	"fmt"
	"os"
) // 引入依赖
func predictPartyVictory(senate string) string { // 定义函数/方法 predictPartyVictory
	n := len(senate)            // 把 长度(senate) 写入 n :
	var radiant, dire []int     // var radiant, dire []int
	for i, ch := range senate { // 同时取 下标 i 与 字符 遍历
		if ch == 'R' {
			radiant = append(radiant, i)
		} else {
			dire = append(dire, i)
		}
	}
	for len(radiant) > 0 && len(dire) > 0 { // for 长度(radiant) 超过 0 且 长度(dire) 超过 0 {
		if radiant[0] < dire[0] {
			radiant = append(radiant, radiant[0]+n)
		} else {
			dire = append(dire, dire[0]+n)
		}
		radiant = radiant[1:] // 把 radiant[1:] 写入 radiant
		dire = dire[1:]       // 把 dire[1:] 写入 dire
	}
	if len(radiant) > 0 {
		return "Radiant"
	} // 若 长度(radiant) 超过 0 { return 「Radiant」 }
	return "Dire" // 返回 「Dire」
}
func main() { // 程序入口：跑内嵌自测用例
	ok := true // 把 true 写入 ok :
	if predictPartyVictory("RD") != "Radiant" {
		ok = false
		fmt.Println("FAIL1")
	}
	if predictPartyVictory("RRRDDD") != "Radiant" {
		ok = false
		fmt.Println("FAIL2")
	}
	if predictPartyVictory("DDR") != "Dire" {
		ok = false
		fmt.Println("FAIL3")
	}
	if !ok {
		os.Exit(1)
	} // 若 取反 ok { os.Exit(1) }
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
