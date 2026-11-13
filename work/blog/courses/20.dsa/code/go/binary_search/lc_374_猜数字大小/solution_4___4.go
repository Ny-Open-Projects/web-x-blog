// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134359782
package main // 引入依赖

import (
	"fmt"
	"os"
) // 引入依赖

var pick = 6 // 把 6 存入 pick

func guess(num int) int { // 定义函数/方法 guess
	if num == pick { // 若 num 等于 pick
		return 0 // 返回 0
	}
	if num < pick { // 若 num 小于 pick
		return 1 // 返回 1
	}
	return -1 // 返回 减 1
}

func guessNumber(n int) int { // 定义函数/方法 guessNumber
	left, right := 1, n // 把 1, 元素个数 写入 left, right :
	for left <= right { // 把 右边界 { 写入 for left <
		mid := (left + right) / 2 // 把 (左边界 加 右边界) 除以 2 写入 mid :
		g := guess(mid)           // 把 guess(中点) 写入 g :
		if g == 0 {               // 若 g 等于 0
			return mid // 返回 中点
		}
		if g == 1 { // 若 g 等于 1
			left = mid + 1 // 把 中点 加 1 写入 左边界
		} else { // 否则
			right = mid - 1 // 把 中点 减 1 写入 右边界
		}
	}
	return -1 // 返回 减 1
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []struct { // 把 []struct { 写入 cases :
		n    int // 元素个数 int
		want int // want int
	}{ // }{
		{10, 6},
		{100, 6},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := guessNumber(c.n); got != c.want { // 若 got : 赋值为 guessNumber(字符.元素个数); got 不等于 字符.want
			ok = false                                                        // 把 false 写入 ok
			fmt.Printf("FAIL guessNumber(%d)=%d want %d\n", c.n, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
