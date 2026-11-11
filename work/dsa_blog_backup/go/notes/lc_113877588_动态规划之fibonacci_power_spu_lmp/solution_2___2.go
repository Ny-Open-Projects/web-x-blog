// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/113877588
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// power 快速幂 (Fast Power) - O(log n)
func power(base, exp int) int { // 定义函数/方法 power
	if exp == 0 { // 若 exp 等于 0
		return 1 // 返回 1
	}
	half := power(base, exp>>1) // 把 power(base, exp 超过 超过 1) 写入 half :
	if exp%2 == 0 {             // 若 exp 对…取模 2 等于 0
		return half * half // 返回 half 乘 half
	}
	return half * half * base // 返回 half 乘 half 乘 base
}

func main() { // 程序入口：跑内嵌自测用例
	if power(2, 10) != 1024 { // 若 power(2, 10) 不等于 1024
		fmt.Println("FAIL power(2,10)") // 打印输出
		os.Exit(1)                      // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
