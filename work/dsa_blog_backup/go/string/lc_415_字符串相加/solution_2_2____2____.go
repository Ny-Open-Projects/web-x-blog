// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145385760
package main // 引入依赖
import (
	"fmt"
	"os"
) // 引入依赖
func addStrings(num1, num2 string) string { // 定义函数/方法 addStrings
	i, j := len(num1)-1, len(num2)-1    // 把 长度(num1) 减 1, 长度(num2) 减 1 写入 i, j :
	carry := 0                          // 把 0 写入 carry :
	var result []byte                   // var 结果 []byte
	for i >= 0 || j >= 0 || carry > 0 { // 把 0 或 下标 j 不低于 0 或 carry 超过 0 { 写入 for i >
		total := carry // 把 carry 写入 total :
		if i >= 0 {
			total += int(num1[i] - '0')
			i--
		} // 若 下标 i 不低于 0 { 总和 累加 int(num1[下标 i] 减 '0'); 下标 i 减一 }
		if j >= 0 {
			total += int(num2[j] - '0')
			j--
		} // 若 下标 j 不低于 0 { 总和 累加 int(num2[下标 j] 减 '0'); 下标 j 减一 }
		result = append([]byte{byte('0' + total%10)}, result...) // 把 append([]byte{byte('0' 加 总和 对…取模 10)}, 结果...) 写入 结果
		carry = total / 10                                       // 把 总和 除以 10 写入 carry
	}
	return string(result) // 定义函数/方法 string
}
func main() { // 程序入口：跑内嵌自测用例
	cases := []struct {
		a    string
		b    string
		want string
	}{ // 把 []struct{ 数组 string; b string; want string }{ 写入 cases :
		{"11", "123", "134"},
		{"456", "77", "533"},
		{"99", "1", "100"},
		{"0", "0", "0"},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := addStrings(c.a, c.b); got != c.want { // 若 got : 赋值为 addStrings(字符.数组, 字符.b); got 不等于 字符.want
			ok = false
			fmt.Printf("FAIL addStrings(%s,%s)=%s want %s\n", c.a, c.b, got, c.want) // 打印输出
		}
	}
	if !ok {
		os.Exit(1)
	} // 若 取反 ok { os.Exit(1) }
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
