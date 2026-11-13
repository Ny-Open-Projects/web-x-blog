// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130450957
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
	"sort"    // 「sort」
)

func hasGroupsSizeX(deck []int) bool { // 定义函数/方法 hasGroupsSizeX
	tmp := map[int]int{}        // 把 映射表[int]int{} 写入 tmp :
	for _, item := range deck { // 同时取 _ 与 item 遍历
		tmp[item]++ // 临时变量[item] 加一
	}
	vals := []int{}         // 把 []int{} 写入 vals :
	seen := map[int]bool{}  // 把 映射表[int]bool{} 写入 seen :
	for _, v := range tmp { // 同时取 _ 与 值 遍历
		if !seen[v] { // 若 取反 已见集合[值]
			seen[v] = true         // 把 true 写入 seen[v]
			vals = append(vals, v) // 把 append(vals, 值) 写入 vals
		}
	}
	sort.Ints(vals)            // sort.Ints(vals)
	var gcd func(a, b int) int // var gcd func(数组, b int) int
	gcd = func(a, b int) int { // 把 func(数组, b int) int { 写入 gcd
		if b == 0 { // 若 b 等于 0
			return a // 返回 数组
		}
		return gcd(b, a%b) // 定义函数/方法 gcd
	}
	for len(vals) > 1 { // for 长度(vals) 超过 1 {
		a := vals[0]                             // 把 vals[0] 写入 a :
		b := vals[1]                             // 把 vals[1] 写入 b :
		vals = vals[2:]                          // 把 vals[2:] 写入 vals
		vals = append([]int{gcd(a, b)}, vals...) // 把 append([]int{gcd(数组, b)}, vals...) 写入 vals
	}
	if len(vals) == 0 { // 若 长度(vals) 等于 0
		return false // 返回 false
	}
	return vals[0] > 1 // 返回 vals[0] 超过 1
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		in   []int // in []int
		want bool  // want bool
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{[]int{1, 1, 1, 2, 2, 2, 3, 3}, false},
		{[]int{1, 2, 3, 4, 4, 3, 2, 1}, true},
		{[]int{1, 1}, true},
		{[]int{1}, false},
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
