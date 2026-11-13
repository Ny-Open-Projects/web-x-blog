// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107450699
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// whoDidGood 思路一：通过字符表示人 (A/B/C/D)
// A说:不是我  -> thisman != 'A'
// B说:是C     -> thisman == 'C'
// C说:是D     -> thisman == 'D'
// D说:他胡说  -> thisman != 'D'
// 已知三人说真话一人说假话：sum == 3
func whoDidGood() byte { // 定义函数/方法 whoDidGood
	for k := 0; k < 4; k++ { // 让 下标 k 从 0 开始计数
		thisman := byte('A' + k) // 把 byte('A' 加 下标 k) 写入 thisman :
		s := 0                   // 把 0 写入 s :
		if thisman != 'A' {      // 若 thisman 不等于 'A'
			s++ // 字符串 加一
		}
		if thisman == 'C' { // 若 thisman 等于 'C'
			s++ // 字符串 加一
		}
		if thisman == 'D' { // 若 thisman 等于 'D'
			s++ // 字符串 加一
		}
		if thisman != 'D' { // 若 thisman 不等于 'D'
			s++ // 字符串 加一
		}
		if s == 3 { // 若 字符串 等于 3
			return thisman // 返回 thisman
		}
	}
	return 0 // 返回 0
}

func main() { // 程序入口：跑内嵌自测用例
	got := whoDidGood() // 把 whoDidGood() 写入 got :
	if got != 'C' {     // 若 got 不等于 'C'
		fmt.Printf("FAIL got=%c want=C\n", got) // 打印输出
		os.Exit(1)                              // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
