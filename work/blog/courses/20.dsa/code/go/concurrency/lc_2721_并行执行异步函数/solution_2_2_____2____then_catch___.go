// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145383126
package main // 引入依赖

import (
	"fmt"  // 「fmt」
	"os"   // 「os」
	"sync" // 「sync」
)

// Result 模拟 JS Promise 的 then/catch：携带成功值或错误信息。
type Result struct { // 定义类型
	Ok    bool   // Ok bool
	Value int    // Value int
	Err   string // Err string
}

// promiseAll 是 Python 参考 solution_2 的忠实翻译（并行执行并捕获各自的成功/失败结果）。
func promiseAll(fns []func() (int, error)) []Result { // 定义函数/方法 promiseAll
	results := make([]Result, len(fns)) // 把 make([]Result, 长度(fns)) 写入 results :
	var wg sync.WaitGroup               // var wg sync.WaitGroup
	for i, fn := range fns {            // 同时取 下标 i 与 fn 遍历
		wg.Add(1)                                 // wg.Add(1)
		go func(idx int, f func() (int, error)) { // 定义函数/方法 func
			defer wg.Done() // defer wg.Done()
			v, err := f()   // 把 f() 写入 v, err :
			if err != nil { // 若 err 不等于 nil
				results[idx] = Result{Ok: false, Err: err.Error()} // 把 Result{Ok: false, Err: err.Error()} 写入 results[idx]
			} else { // 否则
				results[idx] = Result{Ok: true, Value: v} // 把 Result{Ok: true, Value: 值} 写入 results[idx]
			}
		}(i, fn) // }(下标 i, fn)
	}
	wg.Wait()      // wg.Wait()
	return results // 返回 results
}

func main() { // 程序入口：跑内嵌自测用例
	success := func(value int) func() (int, error) { // 把 func(value int) func() (int, error) { 写入 success :
		return func() (int, error) { return value, nil } // 返回 func() (int, error) { return value, nil }
	}
	fail := func() (int, error) { // 把 func() (int, error) { 写入 fail :
		return 0, fmt.Errorf("boom") // 返回 0, fmt.Errorf(「boom」)
	}
	results := promiseAll([]func() (int, error){success(1), fail, success(3)})
	if len(results) != 3 { // 若 长度(results) 不等于 3
		fmt.Println("FAIL len", len(results)) // 打印输出
		os.Exit(1)                            // os.Exit(1)
	}
	if !results[0].Ok || results[0].Value != 1 { // 若 取反 results[0].Ok 或 results[0].Value 不等于 1
		fmt.Println("FAIL result0", results[0]) // 打印输出
		os.Exit(1)                              // os.Exit(1)
	}
	if results[1].Ok { // 若 results[1].Ok
		fmt.Println("FAIL result1 should fail", results[1]) // 打印输出
		os.Exit(1)                                          // os.Exit(1)
	}
	if !results[2].Ok || results[2].Value != 3 { // 若 取反 results[2].Ok 或 results[2].Value 不等于 3
		fmt.Println("FAIL result2", results[2]) // 打印输出
		os.Exit(1)                              // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
