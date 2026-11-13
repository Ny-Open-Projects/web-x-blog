// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145088458
package main // 引入依赖
import (
	"fmt"
	"os"
	"reflect"
) // 引入依赖
type Node struct {
	Val      int
	Children []*Node
} // 定义类型
func levelOrder(root *Node) [][]int { // 定义函数/方法 levelOrder
	if root == nil {
		return [][]int{}
	} // 若 根节点 等于 nil { return [][]int{} }
	res := [][]int{}
	q := []*Node{root} // 把 [][]int{}; 节点 : 赋值为 [] 乘 Node{根节点} 写入 res :
	for len(q) > 0 {   // for 长度(节点) 超过 0 {
		lvl := []int{}
		n := len(q)              // 把 []int{}; 元素个数 : 赋值为 长度(节点) 写入 lvl :
		for k := 0; k < n; k++ { // 让 下标 k 从 0 开始计数
			node := q[0]
			q = q[1:]
			lvl = append(lvl, node.Val)
			for _, ch := range node.Children {
				q = append(q, ch)
			} // 同时取 _ 与 字符 遍历
		}
		res = append(res, lvl) // 把 append(结果, lvl) 写入 结果
	}
	return res // 返回 结果
}
func main() { // 程序入口：跑内嵌自测用例
	c5 := &Node{Val: 5}
	c6 := &Node{Val: 6} // 把 按位与 Node{Val: 5}; c6 : 赋值为 按位与 Node{Val: 6} 写入 c5 :
	c3 := &Node{Val: 3, Children: []*Node{c5, c6}}
	c2 := &Node{Val: 2}
	c4 := &Node{Val: 4}
	root := &Node{Val: 1, Children: []*Node{c3, c2, c4}}
	if got := levelOrder(root); !reflect.DeepEqual(got, [][]int{{1}, {3, 2, 4}, {5, 6}}) {
		fmt.Println("FAIL", got)
		os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
