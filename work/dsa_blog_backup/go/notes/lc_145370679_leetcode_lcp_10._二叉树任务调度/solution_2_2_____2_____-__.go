// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145370679
// LeetCode LCP 10. 二叉树任务调度 — Go 版（方案2：深度优先-优化）

package main

import (
	"fmt"
	"math"
	"os"
)

type TreeNode struct { // 二叉树节点：Val 为自身执行时间（用 float64 承载均摊的 0.5）
	Val         float64
	Left, Right *TreeNode
}

// buildTree 层序数组建树，nil 表示空节点
func buildTree(vals []interface{}) *TreeNode {
	if len(vals) == 0 {
		return nil
	}
	root := &TreeNode{Val: vals[0].(float64)}
	queue := []*TreeNode{root} // 队列里只放非空节点
	i := 1
	for len(queue) > 0 && i < len(vals) {
		node := queue[0] // 出队一个父节点
		queue = queue[1:]
		if i < len(vals) && vals[i] != nil { // 左孩子
			node.Left = &TreeNode{Val: vals[i].(float64)}
			queue = append(queue, node.Left)
		}
		i++
		if i < len(vals) && vals[i] != nil { // 右孩子
			node.Right = &TreeNode{Val: vals[i].(float64)}
			queue = append(queue, node.Right)
		}
		i++
	}
	return root
}

// dfs 返回 [子树总耗时, 子树最小完成时间 maxExec]
func dfs(root *TreeNode) [2]float64 {
	if root == nil {
		return [2]float64{0.0, 0.0} // 空子树
	}
	left := dfs(root.Left)   // 左子树的总耗时与最小完成时间
	right := dfs(root.Right) // 右子树的总耗时与最小完成时间
	leftSum, leftExec := left[0], left[1]
	rightSum, rightExec := right[0], right[1]
	// 当前任务自身必须独占串行跑完；孩子任务两条机器可穿插：
	// 下界取「较慢的一侧」与「两侧工作量均分到两台机器」的较大者
	parallel := (leftSum + rightSum) / 2.0 // 两台机器均摊左右子树总工作量（浮点）
	maxExec := root.Val + math.Max(math.Max(leftExec, rightExec), parallel)
	return [2]float64{leftSum + rightSum + root.Val, maxExec}
}

// minimalExecutionTime 答案 = 整棵树的最小完成时间
func minimalExecutionTime(root *TreeNode) float64 {
	return dfs(root)[1]
}

func main() { // 程序入口：跑内嵌自测用例（三个官方用例）
	cases := []struct {
		vals []interface{}
		want float64
	}{
		{[]interface{}{47.0, 74.0, 31.0}, 121.0},
		{[]interface{}{15.0, 21.0, nil, 24.0, nil, 27.0, 26.0}, 87.0},
		{[]interface{}{1.0, 3.0, 2.0, nil, nil, 4.0, 4.0}, 7.5},
	}
	for _, tc := range cases {
		got := minimalExecutionTime(buildTree(tc.vals))
		if diff := got - tc.want; diff > 1e-6 || diff < -1e-6 { // 浮点比较用 1e-6 容差
			fmt.Println("FAIL got", got, "want", tc.want) // 失败打印 FAIL
			os.Exit(1)                                    // 非零退出
		}
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
