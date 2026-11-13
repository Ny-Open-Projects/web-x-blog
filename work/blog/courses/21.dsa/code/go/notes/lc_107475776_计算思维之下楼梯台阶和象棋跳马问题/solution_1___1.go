// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107475776
package main // 引入依赖
import (
	"fmt"
	"os"
	"reflect"
) // 引入依赖
func climbStairs(h int) [][]int { // 定义函数/方法 climbStairs
	var plans [][]int           // var plans [][]int
	var path []int              // var 当前路径 []int
	var dfs func(int)           // var dfs func(int)
	dfs = func(remaining int) { // 把 func(remaining int) { 写入 dfs
		if remaining == 0 { // 若 remaining 等于 0
			p := make([]int, len(path)) // 把 make([]int, 长度(当前路径)) 写入 p :
			copy(p, path)               // copy(节点, 当前路径)
			plans = append(plans, p)    // 把 append(plans, 节点) 写入 plans
			return                      // return
		}
		for _, step := range []int{3, 2, 1} { // 同时取 _ 与 步数 遍历
			if remaining >= step { // 若 remaining 不低于 步数
				path = append(path, step) // 把 append(当前路径, 步数) 写入 当前路径
				dfs(remaining - step)     // dfs(remaining 减 步数)
				path = path[:len(path)-1] // 把 当前路径[:长度(当前路径) 减 1] 写入 当前路径
			}
		}
	}
	dfs(h)       // dfs(h)
	return plans // 返回 plans
}
func main() { // 程序入口：跑内嵌自测用例
	plans := climbStairs(6) // 把 climbStairs(6) 写入 plans :
	ok := true              // 把 true 写入 ok :
	if len(plans) != 24 {   // 若 长度(plans) 不等于 24
		ok = false
		fmt.Printf("FAIL len plans=%d want 24\n", len(plans)) // 打印输出
	}
	if !(len(plans) > 0 && reflect.DeepEqual(plans[0], []int{3, 3})) {
		ok = false
		fmt.Printf("FAIL first plan=%v want [3 3]\n", plans[0]) // 打印输出
	}
	if !ok {
		os.Exit(1)
	} // 若 取反 ok { os.Exit(1) }
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
