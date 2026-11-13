// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145371693
package main // 引入依赖

import (
	"fmt"  // 「fmt」
	"os"   // 「os」
	"time" // 「time」
)

// timeLimit 是 Python 参考 solution_1 的忠实翻译（超时即返回 "Time Limit Exceeded" 错误）。
func timeLimit(fn func(int) int, t int) func(int) (int, error) { // 定义函数/方法 func
	return func(arg int) (int, error) { // 定义函数/方法 func
		ch := make(chan int, 1)       // 把 make(chan int, 1) 写入 ch :
		go func() { ch <- fn(arg) }() // 定义函数/方法 func
		select {                      // select {
		case res := <-ch: // 把 小于 减 字符: 写入 case res :
			return res, nil // 返回 结果, nil
		case <-time.After(time.Duration(t) * time.Millisecond):
			return 0, fmt.Errorf("Time Limit Exceeded") // 返回 0, fmt.Errorf(「Time Limit Exceeded」)
		}
	}
}

func main() { // 程序入口：跑内嵌自测用例
	slow := func(ms int) int { // 把 func(ms int) int { 写入 slow :
		time.Sleep(time.Duration(ms) * time.Millisecond) // time.Sleep(time.Duration(ms) 乘 time.Millisecond)
		return ms                                        // 返回 ms
	}
	limited := timeLimit(slow, 100) // 把 timeLimit(慢指针, 100) 写入 limited :
	_, err := limited(150)          // 把 limited(150) 写入 _, err :
	if err == nil {                 // 若 err 等于 nil
		fmt.Println("FAIL: expected timeout error") // 打印输出
		os.Exit(1)                                  // os.Exit(1)
	}
	if err.Error() != "Time Limit Exceeded" { // 若 err.Error() 不等于 「Time Limit Exceeded」
		fmt.Println("FAIL: wrong error:", err.Error()) // 打印输出
		os.Exit(1)                                     // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
