// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107450699
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"strings" // 「strings」
)

// solveCrime 刑侦案件：六嫌疑人 A,B,C,D,E,F，1 表示作案，0 表示未作案
func solveCrime() string { // 定义函数/方法 solveCrime
	names := "ABCDEF"        // 把 「ABCDEF」 写入 names :
	found := ""              // 把 「」 写入 found :
	for a := 0; a < 2; a++ { // 让 数组 从 0 开始计数
		for b := 0; b < 2; b++ { // 让 b 从 0 开始计数
			for c := 0; c < 2; c++ { // 让 字符 从 0 开始计数
				for d := 0; d < 2; d++ { // 让 d 从 0 开始计数
					for e := 0; e < 2; e++ { // 让 e 从 0 开始计数
						for f := 0; f < 2; f++ { // 让 f 从 0 开始计数
							if (a == 1 || b == 1) &&
								((a == 1 && e == 1) || (a == 1 && f == 1) || (e == 1 && f == 1)) &&
								!(a == 1 && d == 1) &&
								((b == 1 && c == 1) || (b == 0 && c == 0)) &&
								((c == 1 && d == 0) || (c == 0 && d == 1)) &&
								(d == 1 || (d == 0 && e == 0)) { // 把 赋值为 1 或 (d 等于 0 且 e 等于 0))) { 写入 (d
								people := ""                    // 把 「」 写入 people :
								vals := []int{a, b, c, d, e, f} // 把 []int{数组, b, 字符, d, e, f} 写入 vals :
								for i, v := range vals {        // 同时取 下标 i 与 值 遍历
									if v == 1 { // 若 值 等于 1
										people += string(names[i]) // people累加 string(names[下标 i])
									}
								}
								found = people // 把 people 写入 found
							}
						}
					}
				}
			}
		}
	}
	return found // 返回 found
}

func main() { // 程序入口：跑内嵌自测用例
	got := solveCrime()                   // 把 solveCrime() 写入 got :
	if strings.TrimSpace(got) != "ABCF" { // 若 strings.TrimSpace(got) 不等于 「ABCF」
		fmt.Printf("FAIL got=%q want=ABCF\n", got) // 打印输出
		os.Exit(1)                                 // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
