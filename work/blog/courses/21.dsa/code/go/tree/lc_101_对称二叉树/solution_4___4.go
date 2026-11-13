// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134623793
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

func isSymmetric(root *TreeNode) bool { // 定义判定函数 isSymmetric
	if root == nil { // 若 根节点 等于 nil
		return true // 返回 true
	}
	if root.Left == nil && root.Right == nil { // 若 根节点.Left 等于 nil 且 根节点.Right 等于 nil
		return true // 返回 true
	}
	queue := []*TreeNode{root.Left, root.Right} // 把 [] 乘 TreeNode{根节点.Left, 根节点.Right} 写入 queue :
	for len(queue) > 0 {                        // for 长度(队列) 超过 0 {
		left := queue[0]                 // 把 队列[0] 写入 left :
		queue = queue[1:]                // 把 队列[1:] 写入 队列
		right := queue[0]                // 把 队列[0] 写入 right :
		queue = queue[1:]                // 把 队列[1:] 写入 队列
		if left == nil && right == nil { // 若 左边界 等于 nil 且 右边界 等于 nil
			continue // 跳过本轮，进入下一次
		}
		if left == nil || right == nil { // 若 左边界 等于 nil 或 右边界 等于 nil
			return false // 返回 false
		}
		if left.Val != right.Val { // 若 左边界.Val 不等于 右边界.Val
			return false // 返回 false
		}
		queue = append(queue, left.Left, right.Right, left.Right, right.Left) // 把 append(队列, 左边界.Left, 右边界.Right, 左边界.Right, 右边界.Left) 写入 队列
	}
	return true // 返回 true
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []struct { // 把 []struct { 写入 cases :
		vals []interface{} // vals []interface{}
		want bool          // want bool
	}{ // }{
		{nil, true},
		{[]interface{}{1, 2, 2, 3, 4, 4, 3}, true},
		{[]interface{}{1, 2, 2, nil, 3, nil, 3}, false},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if g := isSymmetric(buildTree(c.vals)); g != c.want { // 若 g : 赋值为 isSymmetric(buildTree(字符.vals)); g 不等于 字符.want
			ok = false                                            // 把 false 写入 ok
			fmt.Printf("FAIL %v=%v want %v\n", c.vals, g, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
