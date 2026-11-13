// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130743564
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

func inorderTraversal(root *TreeNode) []int { // 定义函数/方法 inorderTraversal
	res := []int{}   // 把 []int{} 写入 res :
	cur := root      // 把 根节点 写入 cur :
	for cur != nil { // 把 nil { 写入 for cur !
		if cur.Left == nil { // 若 当前值.Left 等于 nil
			res = append(res, cur.Val) // 把 append(结果, 当前值.Val) 写入 结果
			cur = cur.Right            // 把 当前值.Right 写入 当前值
		} else { // 否则
			pred := cur.Left                             // 把 当前值.Left 写入 pred :
			for pred.Right != nil && pred.Right != cur { // 把 nil 且 pred.Right 不等于 当前值 { 写入 for pred.Right !
				pred = pred.Right // 把 pred.Right 写入 pred
			}
			if pred.Right == nil { // 若 pred.Right 等于 nil
				pred.Right = cur // 把 当前值 写入 pred.Right
				cur = cur.Left   // 把 当前值.Left 写入 当前值
			} else { // 否则
				pred.Right = nil           // 把 nil 写入 pred.Right
				res = append(res, cur.Val) // 把 append(结果, 当前值.Val) 写入 结果
				cur = cur.Right            // 把 当前值.Right 写入 当前值
			}
		}
	}
	return res // 返回 结果
}

func main() { // 程序入口：跑内嵌自测用例
	got := inorderTraversal(buildTree([]interface{}{1, nil, 2, nil, 3}))
	want := []int{1, 2, 3}                   // 把 []int{1, 2, 3} 写入 want :
	if fmt.Sprint(got) != fmt.Sprint(want) { // 若 fmt.Sprint(got) 不等于 fmt.Sprint(want
		fmt.Printf("FAIL =%v want %v\n", got, want) // 打印输出
		os.Exit(1)                                  // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
