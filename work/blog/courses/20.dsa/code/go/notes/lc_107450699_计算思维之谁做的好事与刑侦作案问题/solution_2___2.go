// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107450699
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// whoDidGood 思路二：通过数字表示人 (0=A,1=B,2=C,3=D)
func whoDidGood() int { // 定义函数/方法 whoDidGood
	for k := 0; k < 4; k++ { // 让 下标 k 从 0 开始计数
		s := 0      // 把 0 写入 s :
		if k != 0 { // 若 下标 k 不等于 0
			s++ // 字符串 加一
		}
		if k == 2 { // 若 下标 k 等于 2
			s++ // 字符串 加一
		}
		if k == 3 { // 若 下标 k 等于 3
			s++ // 字符串 加一
		}
		if k != 3 { // 若 下标 k 不等于 3
			s++ // 字符串 加一
		}
		if s == 3 { // 若 字符串 等于 3
			return k // 返回 下标 k
		}
	}
	return -1 // 返回 减 1
}

func main() { // 程序入口：跑内嵌自测用例
	got := whoDidGood() // 把 whoDidGood() 写入 got :
	if got != 2 {       // 若 got 不等于 2
		fmt.Printf("FAIL got=%d want=2 (C)\n", got) // 打印输出
		os.Exit(1)                                  // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
