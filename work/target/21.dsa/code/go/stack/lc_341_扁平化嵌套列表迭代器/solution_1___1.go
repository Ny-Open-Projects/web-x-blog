// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145345560
package main // 引入依赖
import (
	"fmt"
	"os"
	"reflect"
) // 引入依赖

type NestedInteger struct { // 定义类型
	isInt  bool            // isInt bool
	intVal int             // intVal int
	list   []NestedInteger // 列表 []NestedInteger
}

func NewInt(v int) NestedInteger                  { return NestedInteger{isInt: true, intVal: v} } // 定义函数/方法 NewInt
func NewList(items []NestedInteger) NestedInteger { return NestedInteger{list: items} }            // 定义函数/方法 NewList
func (n NestedInteger) IsInteger() bool           { return n.isInt }                               // 定义函数/方法 IsInteger
func (n NestedInteger) GetInteger() int           { return n.intVal }                              // 定义函数/方法 GetInteger
func (n NestedInteger) GetList() []NestedInteger  { return n.list }                                // 定义函数/方法 GetList

func flatten(nestedList []NestedInteger) []int { // 定义函数/方法 flatten
	res := []int{}                  // 把 []int{} 写入 res :
	var dfs func([]NestedInteger)   // var dfs func([]NestedInteger)
	dfs = func(l []NestedInteger) { // 把 func(左指针 []NestedInteger) { 写入 dfs
		for _, nest := range l { // 同时取 _ 与 nest 遍历
			if nest.IsInteger() {
				res = append(res, nest.GetInteger())
			} else {
				dfs(nest.GetList())
			}
		}
	}
	dfs(nestedList) // dfs(nestedList)
	return res      // 返回 结果
}

func main() { // 程序入口：跑内嵌自测用例
	in1 := []NestedInteger{NewList([]NestedInteger{NewInt(1), NewList([]NestedInteger{NewInt(2), NewInt(3)})})}
	in2 := []NestedInteger{NewList([]NestedInteger{NewInt(1), NewInt(1)}), NewInt(2), NewList([]NestedInteger{NewInt(1), NewInt(1)})}
	ok := true // 把 true 写入 ok :
	if got := flatten(in1); !reflect.DeepEqual(got, []int{1, 2, 3}) {
		ok = false
		fmt.Printf("FAIL flatten1=%v\n", got)
	}
	if got := flatten(in2); !reflect.DeepEqual(got, []int{1, 1, 2, 1, 1}) {
		ok = false
		fmt.Printf("FAIL flatten2=%v\n", got)
	}
	if !ok {
		os.Exit(1)
	} // 若 取反 ok { os.Exit(1) }
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
