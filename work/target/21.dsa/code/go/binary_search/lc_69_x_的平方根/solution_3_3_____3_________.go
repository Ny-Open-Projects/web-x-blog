// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145233215
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// x 的平方根：牛顿迭代法
// 忠实于 Python ref_mySqrt 求整数平方根的等价结果
func mySqrt(x int) int { // 定义函数/方法 mySqrt
	if x < 2 { // 若 x 小于 2
		return x // 返回 x
	}
	r := x        // 把 x 写入 r :
	for r*r > x { // for 右指针 乘 右指针 超过 x {
		r = (r + x/r) / 2 // 把 (右指针 加 x 除以 右指针) 除以 2 写入 右指针
	}
	return r // 返回 右指针
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
