// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145007192
package main // 引入依赖

import (
	"fmt"
	"os"
) // 引入依赖

type TreeNode struct { // 定义类型
	Val   int       // Val int
	Left  *TreeNode // Left 乘 TreeNode
	Right *TreeNode // Right 乘 TreeNode
}

func buildTree(vals []interface{}) *TreeNode { // 定义函数/方法 buildTree
	if len(vals) == 0 || vals[0] == nil { // 若 长度(vals) 等于 0 或 vals[0] 等于 nil
		return nil // 返回 nil
	}
	root := &TreeNode{Val: vals[0].(int)} // 把 按位与 TreeNode{Val: vals[0].(int)} 写入 root :
	q := []*TreeNode{root}                // 把 [] 乘 TreeNode{根节点} 写入 q :
	i := 1                                // 把 1 写入 i :
	for i < len(vals) {                   // for 下标 i 小于 长度(vals) {
		node := q[0]        // 把 节点[0] 写入 node :
		q = q[1:]           // 把 节点[1:] 写入 节点
		if vals[i] != nil { // 若 vals[下标 i] 不等于 nil
			node.Left = &TreeNode{Val: vals[i].(int)} // 把 按位与 TreeNode{Val: vals[下标 i].(int)} 写入 node.Left
			q = append(q, node.Left)                  // 把 append(节点, 节点.Left) 写入 节点
		}
		i++                // 下标 i 加一
		if i < len(vals) { // 若 下标 i 小于 长度(vals
			if vals[i] != nil { // 若 vals[下标 i] 不等于 nil
				node.Right = &TreeNode{Val: vals[i].(int)} // 把 按位与 TreeNode{Val: vals[下标 i].(int)} 写入 node.Right
				q = append(q, node.Right)                  // 把 append(节点, 节点.Right) 写入 节点
			}
			i++ // 下标 i 加一
		}
	}
	return root // 返回 根节点
}

func flatten(root *TreeNode) { // 定义函数/方法 flatten
	if root == nil { // 若 根节点 等于 nil
		return // return
	}
	stack := []*TreeNode{root} // 把 [] 乘 TreeNode{根节点} 写入 stack :
	var prev *TreeNode         // var 前一个 乘 TreeNode
	for len(stack) > 0 {       // for 长度(栈) 超过 0 {
		curr := stack[len(stack)-1]  // 把 栈[长度(栈) 减 1] 写入 curr :
		stack = stack[:len(stack)-1] // 把 栈[:长度(栈) 减 1] 写入 栈
		if prev != nil {             // 若 前一个 不等于 nil
			prev.Left = nil   // 把 nil 写入 prev.Left
			prev.Right = curr // 把 当前值 写入 prev.Right
		}
		if curr.Right != nil { // 若 当前值.Right 不等于 nil
			stack = append(stack, curr.Right) // 把 append(栈, 当前值.Right) 写入 栈
		}
		if curr.Left != nil { // 若 当前值.Left 不等于 nil
			stack = append(stack, curr.Left) // 把 append(栈, 当前值.Left) 写入 栈
		}
		prev = curr // 把 当前值 写入 前一个
	}
}

func main() { // 程序入口：跑内嵌自测用例
	root := buildTree([]interface{}{1, 2, 5, 3, 4, nil, 6}) // 把 buildTree([]interface{}{1, 2, 5, 3, 4, nil, 6}) 写入 root :
	flatten(root)                                           // flatten(根节点)
	spine := []int{}                                        // 把 []int{} 写入 spine :
	leftOK := true                                          // 把 true 写入 leftOK :
	cur := root                                             // 把 根节点 写入 cur :
	for cur != nil {                                        // 把 nil { 写入 for cur !
		spine = append(spine, cur.Val) // 把 append(spine, 当前值.Val) 写入 spine
		if cur.Left != nil {           // 若 当前值.Left 不等于 nil
			leftOK = false // 把 false 写入 leftOK
		}
		cur = cur.Right // 把 当前值.Right 写入 当前值
	}
	want := []int{1, 2, 3, 4, 5, 6}                       // 把 []int{1, 2, 3, 4, 5, 6} 写入 want :
	if !leftOK || fmt.Sprint(spine) != fmt.Sprint(want) { // 若 取反 leftOK 或 fmt.Sprint(spine) 不等于 fmt.Sprint(want
		fmt.Printf("FAIL spine=%v want %v leftOK=%v\n", spine, want, leftOK) // 打印输出
		os.Exit(1)                                                           // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
