// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130450957
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
)

func gcd(a, b int) int { // 定义函数/方法 gcd
	for b != 0 { // 把 0 { 写入 for b !
		a, b = b, a%b // 把 b, 数组 对…取模 b 写入 a, b
	}
	return a // 返回 数组
}

func hasGroupsSizeX(deck []int) bool { // 定义函数/方法 hasGroupsSizeX
	if len(deck) < 2 { // 若 长度(deck) 小于 2
		return false // 返回 false
	}
	count := map[int]int{}   // 把 映射表[int]int{} 写入 count :
	for _, c := range deck { // 同时取 _ 与 字符 遍历
		count[c]++ // 计数[字符] 加一
	}
	g := 0                    // 把 0 写入 g :
	for _, c := range count { // 同时取 _ 与 字符 遍历
		g = gcd(g, c) // 把 gcd(g, 字符) 写入 g
	}
	return g >= 2 // 返回 g 不低于 2
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		in   []int // in []int
		want bool  // want bool
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{[]int{1, 2, 3, 4, 4, 3, 2, 1}, true},
		{[]int{1, 1, 1, 2, 2, 2, 3, 3}, false},
		{[]int{1, 1}, true},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := hasGroupsSizeX(c.in); !reflect.DeepEqual(got, c.want) {
			ok = false                                                            // 把 false 写入 ok
			fmt.Printf("FAIL hasGroupsSizeX(%v)=%v want %v\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
