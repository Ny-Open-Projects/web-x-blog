// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145397820
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

func pow10(k int) int { // 定义函数/方法 pow10
	r := 1                   // 把 1 写入 r :
	for i := 0; i < k; i++ { // 让 下标 i 从 0 开始计数
		r *= 10 // 把 10 写入 r *
	}
	return r // 返回 右指针
}

func nextGreaterElement(n int) int { // 定义函数/方法 nextGreaterElement
	MAX := 2147483647                  // 把 2147483647 写入 MAX :
	x := n                             // 把 元素个数 写入 x :
	cnt := 1                           // 把 1 写入 cnt :
	for x >= 10 && (x/10)%10 >= x%10 { // 把 10 且 (x 除以 10) 对…取模 10 不低于 x 对…取模 10 { 写入 for x >
		x = x / 10 // 把 x 除以 10 写入 x
		cnt++      // 计数 加一
	}
	x = x / 10  // 把 x 除以 10 写入 x
	if x == 0 { // 若 x 等于 0
		return -1 // 返回 减 1
	}
	targetDigit := x % 10      // 把 x 对…取模 10 写入 targetDigit :
	x2 := n                    // 把 元素个数 写入 x2 :
	cnt2 := 0                  // 把 0 写入 cnt2 :
	for x2%10 <= targetDigit { // 把 targetDigit { 写入 for x2%10 <
		x2 = x2 / 10 // 把 x2 除以 10 写入 x2
		cnt2++       // cnt2 加一
	}
	d := x2 % 10 // 把 x2 对…取模 10 写入 d :
	result := n/pow10(cnt)*pow10(cnt) + d*pow10(cnt-1) + n%pow10(cnt2-1)
	if result > MAX || result <= n { // 若 结果 超过 MAX 或 结果 不超过 元素个数
		return -1 // 返回 减 1
	}
	return result // 返回 结果
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		in   int // in int
		want int // want int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{1, -1},
		{9, -1},
		{21, -1},
		{10, -1},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := nextGreaterElement(c.in); got != c.want { // 若 got : 赋值为 nextGreaterElement(字符.in); got 不等于 字符.want
			ok = false                                                                // 把 false 写入 ok
			fmt.Printf("FAIL nextGreaterElement(%d)=%d want %d\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
