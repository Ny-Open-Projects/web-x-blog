// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145053587
package main // 引入依赖
import (
	"fmt"
	"os"
) // 引入依赖
type TreeNode struct {
	Val         int
	Left, Right *TreeNode
} // 定义类型
func buildBST(vals []interface{}) *TreeNode { // 定义函数/方法 buildBST
	if len(vals) == 0 {
		return nil
	} // 若 长度(vals) 等于 0 { return nil }
	v, _ := vals[0].(int)     // 把 vals[0].(int) 写入 v, _ :
	root := &TreeNode{Val: v} // 把 按位与 TreeNode{Val:值} 写入 root :
	q := []*TreeNode{root}    // 把 [] 乘 TreeNode{根节点} 写入 q :
	i := 1                    // 把 1 写入 i :
	for i < len(vals) {       // for 下标 i 小于 长度(vals) {
		node := q[0]
		q = q[1:]          // 把 节点[0]; 节点 赋值为 节点[1:] 写入 node :
		if i < len(vals) { // 若 下标 i 小于 长度(vals
			if x, ok := vals[i].(int); ok {
				node.Left = &TreeNode{Val: x}
				q = append(q, node.Left)
			}
		}
		i++                // 下标 i 加一
		if i < len(vals) { // 若 下标 i 小于 长度(vals
			if x, ok := vals[i].(int); ok {
				node.Right = &TreeNode{Val: x}
				q = append(q, node.Right)
			}
		}
		i++ // 下标 i 加一
	}
	return root // 返回 根节点
}
func kthSmallest(root *TreeNode, k int) int { // 定义函数/方法 kthSmallest
	stack := []*TreeNode{}              // 把 [] 乘 TreeNode{} 写入 stack :
	for root != nil || len(stack) > 0 { // 把 nil 或 长度(栈) 超过 0 { 写入 for root !
		for root != nil {
			stack = append(stack, root)
			root = root.Left
		}
		root = stack[len(stack)-1]
		stack = stack[:len(stack)-1] // 把 栈[长度(栈) 减 1]; 栈 赋值为 栈[:长度(栈) 减 1] 写入 根节点
		k--                          // 下标 k 减一
		if k == 0 {
			return root.Val
		} // 若 下标 k 等于 0 { return 根节点.Val }
		root = root.Right // 把 根节点.Right 写入 根节点
	}
	return -1 // 返回 减 1
}
func main() { // 程序入口：跑内嵌自测用例
	root := buildBST([]interface{}{3, 1, 4, nil, 2}) // 把 buildBST([]interface{}{3,1,4,nil,2}) 写入 root :
	ok := true                                       // 把 true 写入 ok :
	if kthSmallest(root, 1) != 1 {
		ok = false
		fmt.Println("FAIL1")
	}
	if kthSmallest(root, 2) != 2 {
		ok = false
		fmt.Println("FAIL2")
	}
	if kthSmallest(root, 3) != 3 {
		ok = false
		fmt.Println("FAIL3")
	}
	if kthSmallest(root, 4) != 4 {
		ok = false
		fmt.Println("FAIL4")
	}
	if !ok {
		os.Exit(1)
	} // 若 取反 ok { os.Exit(1) }
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
