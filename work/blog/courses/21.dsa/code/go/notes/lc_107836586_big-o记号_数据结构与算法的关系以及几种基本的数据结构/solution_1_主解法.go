// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107836586
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// asymptoticT T(n) = 5n·[3n·(n+2)+4] + 6
func asymptoticT(n int) int { // 定义函数/方法 asymptoticT
	return 5*n*(3*n*(n+2)+4) + 6 // 返回 5 乘 元素个数 乘 (3 乘 元素个数 乘 (元素个数 加 2) 加 4) 加 6
}

// classify 给定各次项系数（索引为次数），返回最高次非零项对应的 Big-O 记号
func classify(coeffs []int) string { // 定义函数/方法 classify
	for deg := len(coeffs) - 1; deg >= 0; deg-- { // 把 长度(coeffs) 减 1; deg 不低于 0; deg 减一 { 写入 for deg :
		if coeffs[deg] != 0 { // 若 coeffs[deg] 不等于 0
			if deg > 1 { // 若 deg 超过 1
				return fmt.Sprintf("O(n^%d)", deg) // 返回 fmt.Sprintf(「O(元素个数 按位异或 对…取模 d)」, deg)
			} else if deg == 1 { // 否则，若 deg 等于 1
				return "O(n)" // 返回 「O(元素个数)」
			}
			return "O(1)" // 返回 「O(1)」
		}
	}
	return "O(1)" // 返回 「O(1)」
}

func main() { // 程序入口：跑内嵌自测用例
	// 验证 T(n) 增长公式
	if asymptoticT(1) != 71 { // 若 asymptoticT(1) 不等于 71
		fmt.Println("FAIL T(1)") // 打印输出
		os.Exit(1)               // os.Exit(1)
	}
	if asymptoticT(10) != 18206 { // 若 asymptoticT(10) 不等于 18206
		fmt.Println("FAIL T(10)") // 打印输出
		os.Exit(1)                // os.Exit(1)
	}
	if asymptoticT(100) != 15302006 { // 若 asymptoticT(100) 不等于 15302006
		fmt.Println("FAIL T(100)") // 打印输出
		os.Exit(1)                 // os.Exit(1)
	}
	if asymptoticT(1000) != 15030020006 { // 若 asymptoticT(1000) 不等于 15030020006
		fmt.Println("FAIL T(1000)") // 打印输出
		os.Exit(1)                  // os.Exit(1)
	}
	// 验证 classify
	if classify([]int{6, 20, 30, 35}) != "O(n^3)" { // 若 classify([]int{6, 20, 30, 35}) 不等于 「O(元素个数 按位异或 3)」
		fmt.Println("FAIL classify") // 打印输出
		os.Exit(1)                   // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
