// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134623793
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

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
	for len(q) > 0 && i < len(vals) {     // 定义函数/方法 len
		node := q[0]                         // 把 节点[0] 写入 node :
		q = q[1:]                            // 把 节点[1:] 写入 节点
		if i < len(vals) && vals[i] != nil { // 若 下标 i 小于 长度(vals) 且 vals[下标 i] 不等于 nil
			node.Left = &TreeNode{Val: vals[i].(int)} // 把 按位与 TreeNode{Val: vals[下标 i].(int)} 写入 node.Left
			q = append(q, node.Left)                  // 把 append(节点, 节点.Left) 写入 节点
		}
		i++                                  // 下标 i 加一
		if i < len(vals) && vals[i] != nil { // 若 下标 i 小于 长度(vals) 且 vals[下标 i] 不等于 nil
			node.Right = &TreeNode{Val: vals[i].(int)} // 把 按位与 TreeNode{Val: vals[下标 i].(int)} 写入 node.Right
			q = append(q, node.Right)                  // 把 append(节点, 节点.Right) 写入 节点
		}
		i++ // 下标 i 加一
	}
	return root // 返回 根节点
}

func isSymmetric(root *TreeNode) bool { // 定义判定函数 isSymmetric
	if root == nil { // 若 根节点 等于 nil
		return true // 返回 true
	}
	var isMirror func(l, r *TreeNode) bool // var isMirror func(左指针, 右指针 乘 TreeNode) bool
	isMirror = func(l, r *TreeNode) bool { // 把 func(左指针, 右指针 乘 TreeNode) bool { 写入 isMirror
		if l == nil && r == nil { // 若 左指针 等于 nil 且 右指针 等于 nil
			return true // 返回 true
		}
		if l == nil || r == nil { // 若 左指针 等于 nil 或 右指针 等于 nil
			return false // 返回 false
		}
		return l.Val == r.Val && isMirror(l.Left, r.Right) && isMirror(r.Left, l.Right)
	}
	return isMirror(root.Left, root.Right) // 定义判定函数 isMirror
}

type tc struct { // 定义类型
	root *TreeNode // 根节点 乘 TreeNode
	want bool      // want bool
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []tc{ // 把 []tc{ 写入 cases :
		{buildTree(nil), true},
		{buildTree([]interface{}{1}), true},
		{buildTree([]interface{}{1, 2, 2, 3, 4, 4, 3}), true},
		{buildTree([]interface{}{1, 2, 2, 3, 4, 4, 9}), false},
	}
	for idx, c := range cases { // 同时取 idx 与 字符 遍历
		got := isSymmetric(c.root) // 把 isSymmetric(字符.根节点) 写入 got :
		if got != c.want {         // 若 got 不等于 字符.want
			fmt.Printf("case %d failed: got %v want %v\n", idx, got, c.want) // 打印输出
			os.Exit(1)                                                       // os.Exit(1)
		}
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
