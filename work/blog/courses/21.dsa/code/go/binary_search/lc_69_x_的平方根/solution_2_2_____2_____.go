// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145233215
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// x 的平方根：二分查找（记录符合条件的最大 mid）
// 忠实于 Python ref_mySqrt 的二分思想
func mySqrt(x int) int { // 定义函数/方法 mySqrt
	if x < 2 { // 若 x 小于 2
		return x // 返回 x
	}
	lo, hi := 1, x/2 // 把 1, x 除以 2 写入 lo, hi :
	ans := 0         // 把 0 写入 ans :
	for lo <= hi {   // 把 右边界 { 写入 for lo <
		m := (lo + hi) / 2 // 把 (左边界 加 右边界) 除以 2 写入 m :
		if m*m <= x {      // 若 映射表 乘 映射表 不超过 x
			ans = m    // 把 映射表 写入 答案
			lo = m + 1 // 把 映射表 加 1 写入 左边界
		} else { // 否则
			hi = m - 1 // 把 映射表 减 1 写入 右边界
		}
	}
	return ans // 返回 答案
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct{ x, want int } // 定义类型
	cases := []tc{{4, 2}, {8, 2}, {16, 4}, {2147395599, 46339}}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		got := mySqrt(c.x) // 把 mySqrt(字符.x) 写入 got :
		if got != c.want { // 若 got 不等于 字符.want
			fmt.Printf("FAIL: mySqrt(%d)=%d want %d\n", c.x, got, c.want) // 打印输出
			ok = false                                                    // 把 false 写入 ok
		}
	}
	if !ok { // 若 取反 ok
		fmt.Println("FAIL") // 打印输出
		os.Exit(1)          // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
