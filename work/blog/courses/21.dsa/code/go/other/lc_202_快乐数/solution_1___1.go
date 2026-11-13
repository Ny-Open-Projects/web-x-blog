// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145355335
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

func bitSquareSum(n int) int { // 定义函数/方法 bitSquareSum
	total := 0  // 把 0 写入 total :
	for n > 0 { // for 元素个数 超过 0 {
		digit := n % 10        // 把 元素个数 对…取模 10 写入 digit :
		total += digit * digit // 总和累加 digit 乘 digit
		n /= 10                // 把 10 写入 n /
	}
	return total // 返回 总和
}

func main() { // 程序入口：跑内嵌自测用例
	ok := true       // 把 true 写入 ok :
	tc := []struct { // 把 []struct { 写入 tc :
		in   int // in int
		want int // want int
	}{ // }{
		{1, 1}, {2, 4}, {19, 82}, {7, 49},
	}
	for _, c := range tc { // 同时取 _ 与 字符 遍历
		if got := bitSquareSum(c.in); got != c.want { // 若 got : 赋值为 bitSquareSum(字符.in); got 不等于 字符.want
			ok = false                                                          // 把 false 写入 ok
			fmt.Printf("FAIL bitSquareSum(%d)=%d want %d\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
