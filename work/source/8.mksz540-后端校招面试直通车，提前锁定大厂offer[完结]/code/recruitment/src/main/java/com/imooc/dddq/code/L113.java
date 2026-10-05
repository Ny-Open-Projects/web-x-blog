package com.imooc.dddq.code;

import com.imooc.dddq.common.TreeNode;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class L113 {

    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        List<List<Integer>> result = new ArrayList<>();
        // preOrder(root, result, new ArrayList<>(), targetSum);
        bfs(root, result, targetSum);
        return result;
    }

    // 深搜
    public void preOrder(TreeNode head, List<List<Integer>> result, List<Integer> path, int targetNum) {
        if (head == null) {
            return;
        }
        path.add(head.val);
        targetNum -= head.val;
        if(head.leftNode == null && head.rightNode == null && targetNum == 0) {
            result.add(new ArrayList<>(path));
        }
        preOrder(head.leftNode, result, new ArrayList<>(path), targetNum);
        preOrder(head.rightNode, result, new ArrayList<>(path), targetNum);
    }

    // 广度优先搜索
    public void bfs(TreeNode head, List<List<Integer>> result, int targetNum) {
        if (head == null) {
            return;
        }
        // 1. 初始化路径
        Queue<List<TreeNode>> queue = new LinkedList<>();
        List<TreeNode> initPath = new ArrayList<>();
        initPath.add(head);
        queue.offer(initPath);
        // 2. 队列
        while (! queue.isEmpty()) {
            // 2.1 当前路径取出来
            List<TreeNode> path = queue.poll();
            TreeNode tail = path.get(path.size()-1);
            // 2.2 判断叶子节点（完整路径）
            if (tail.rightNode == null && tail.leftNode == null) {
                List<Integer> pathInt = new ArrayList<>();
                int sum = 0;
                // 2.2.1 和 == targetNum
                for(int i = 0; i < path.size(); i ++) {
                    int val = path.get(i).val;
                    pathInt.add(val);
                    sum += path.get(i).val;
                }
                if (sum == targetNum) {
                    result.add(pathInt);
                }
            } else { // 2.3 不是叶子节点
                if (tail.leftNode != null) {
                    List<TreeNode> newPath = new ArrayList<>(path);
                    newPath.add(tail.leftNode);
                    queue.offer(newPath);
                }
                if (tail.rightNode != null) {
                    List<TreeNode> newPath = new ArrayList<>(path);
                    newPath.add(tail.rightNode);
                    queue.offer(newPath);
                }
            }
        }
    }
}
