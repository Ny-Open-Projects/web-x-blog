// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145383126
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
	"sync"    // 「sync」
	"time"    // 「time」
)

// promiseAll 是 Python 参考 solution_1 的忠实翻译（并行执行并收集结果，保持顺序）。
func promiseAll(fns []func() int) []int { // 定义函数/方法 promiseAll
	results := make([]int, len(fns)) // 把 make([]int, 长度(fns)) 写入 results :
	var wg sync.WaitGroup            // var wg sync.WaitGroup
	for i, fn := range fns {         // 同时取 下标 i 与 fn 遍历
		wg.Add(1)                        // wg.Add(1)
		go func(idx int, f func() int) { // 定义函数/方法 func
			defer wg.Done()    // defer wg.Done()
			results[idx] = f() // 把 f() 写入 results[idx]
		}(i, fn) // }(下标 i, fn)
	}
	wg.Wait()      // wg.Wait()
	return results // 返回 results
}

func main() { // 程序入口：跑内嵌自测用例
	delay := func(seconds time.Duration, value int) func() int {
		return func() int { // 返回 func() int {
			time.Sleep(seconds) // time.Sleep(seconds)
			return value        // 返回 value
		}
	}
	results := promiseAll([]func() int{ // 把 promiseAll([]func() int{ 写入 results :
		delay(50*time.Millisecond, 1),
		delay(50*time.Millisecond, 2),
		delay(50*time.Millisecond, 3),
	}) // })
	if !reflect.DeepEqual(results, []int{1, 2, 3}) { // 若 取反 reflect.DeepEqual(results, []int{1, 2, 3}
		fmt.Println("FAIL:", results) // 打印输出
		os.Exit(1)                    // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
