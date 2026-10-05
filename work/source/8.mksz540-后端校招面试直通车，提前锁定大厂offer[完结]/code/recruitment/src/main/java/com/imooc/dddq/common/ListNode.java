package com.imooc.dddq.common;

import java.util.ArrayList;
import java.util.List;

public class ListNode {
    public int val;
    public ListNode next;
    public ListNode(){}
    public ListNode(int val) {
        this.val = val;
    }
    public ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }

    public static ListNode buildList(List<Integer> nums) {
        if (nums == null || nums.size() == 0) {
            return null;
        }
        ListNode head = new ListNode(nums.get(0), null);
        ListNode curr = head;
        for(int i = 1; i < nums.size(); i ++) {
            curr.next = new ListNode(nums.get(i), null);
            curr = curr.next;
        }
        return head;
    }

    public static void travelList(ListNode head) {
        ListNode curr = head;
        while(curr != null) {
            System.out.printf("%d->", curr.val);
            curr = curr.next;
        }
        System.out.println();
    }

    public static void main(String[] args){
        List<Integer> nums = new ArrayList<>();
        nums.add(1);
        nums.add(2);
        nums.add(3);
        nums.add(4);
        nums.add(5);
        nums.add(6);
        nums.add(7);
        ListNode head = buildList(nums);
        travelList(head);
    }
}
