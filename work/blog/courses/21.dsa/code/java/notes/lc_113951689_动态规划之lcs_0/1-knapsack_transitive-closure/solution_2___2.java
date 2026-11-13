// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/113951689
package com.webfault.dsa;
import java.util.*;
class Main {
    // faithful translation of python solution_2___2.py (0/1 knapsack: max value + chosen indices)
        static Object[] knapsack(int[] weights, int[] values, int capacity){
        int n=weights.length;
        int[][] dp=new int[n+1][capacity+1];
            for(int i=1;i<=n;i++){
            int w=weights[i-1], v=values[i-1];
                for(int c=0;c<=capacity;c++){
                dp[i][c]=dp[i-1][c];
                if(c>=w) dp[i][c]=Math.max(dp[i][c],dp[i-1][c-w]+v);
            }
        }
        // 回溯所选物品
        int c=capacity;
        List<Integer> chosen=new ArrayList<>();
            for(int i=n;i>0;i--){
                if(dp[i][c]!=dp[i-1][c]){
                chosen.add(i-1);
                c-=weights[i-1];
            }
        }
        Collections.reverse(chosen);
        return new Object[]{dp[n][capacity], chosen};
    }
        public static void main(String[] args) {
        int[][] ws={{1,3,4,5},{2,2,6,5,4},{1}};
        int[][] vs={{1,4,5,7},{6,3,5,4,6},{2}};
        int[] caps={7,10,0};
        String[] wants={"9,[1, 2]","15,[0, 1, 4]","0,[]"};
        boolean ok=true;
            for(int ci=0;ci<ws.length;ci++){
            Object[] got=knapsack(ws[ci],vs[ci],caps[ci]);
            String gs=got[0]+","+got[1];
                if(!gs.equals(wants[ci])){
                ok=false; System.out.println("FAIL knapsack case "+ci+" got="+gs+" want="+wants[ci]);
            }
        }
        if(!ok) throw new RuntimeException("FAILED");
        System.out.println("PASS");
    }
}
