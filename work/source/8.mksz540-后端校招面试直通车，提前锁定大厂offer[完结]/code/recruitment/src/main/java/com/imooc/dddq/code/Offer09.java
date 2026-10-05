package com.imooc.dddq.code;

import java.util.Vector;

public class Offer09 {

    private Vector<Integer> vec1;
    private Vector<Integer> vec2;

    public Offer09() {
        vec1 = new Vector<>();
        // 辅助栈
        vec2 = new Vector<>();
    }

    public void appendTail(int val){
        this.vec1.add(val);
    }

    public int deleteHead(){
        if (vec1.size() == 0 && vec2.size() == 0) {
            return -1;
        }
        if (vec2.size() == 0) {
            while(!vec1.isEmpty()) {
                vec2.add(vec1.remove(vec1.size()-1));
            }
        }
        return vec2.remove(vec2.size()-1);
    }
}
