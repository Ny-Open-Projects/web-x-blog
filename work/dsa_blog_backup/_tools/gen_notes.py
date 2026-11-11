import os

base = "/Users/Wang/Code/webfault-ai/dsa/java/notes/lc_93536806_数据结构与算法笔记_复杂度"

# (classname, solve body, main body)
files = {}

files["solution_3___3.java"] = r'''package com.webfault.dsa;

class Ns3 {
    int[] bubble_sort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) { int t = arr[j]; arr[j] = arr[j + 1]; arr[j + 1] = t; }
            }
        }
        return arr;
    }
    public static void main(String[] args) {
        Ns3 s = new Ns3();
        Object[][] cases = {{new int[]{3, 1, 4, 1, 5, 9, 2, 6}, new int[]{1, 1, 2, 3, 4, 5, 6, 9}}};
        boolean ok = true;
        for (Object[] c : cases) {
            int[] got = s.bubble_sort((int[]) c[0]);
            if (!java.util.Arrays.equals(got, (int[]) c[1])) { ok = false; System.out.println("FAIL got=" + java.util.Arrays.toString(got)); }
        }
        if (!ok) throw new RuntimeException("FAILED");
        System.out.println("PASS");
    }
}
'''

files["solution_4___4.java"] = r'''package com.webfault.dsa;

class Ns4 {
    int partition(int[] arr, int left, int right) {
        int pivot = arr[right];
        int i = left;
        for (int j = left; j < right; j++) {
            if (arr[j] < pivot) { int t = arr[i]; arr[i] = arr[j]; arr[j] = t; i++; }
        }
        int t = arr[i]; arr[i] = arr[right]; arr[right] = t;
        return i;
    }
    void quick_sort(int[] arr, int left, int right) {
        if (left < right) {
            int p = partition(arr, left, right);
            quick_sort(arr, left, p - 1);
            quick_sort(arr, p + 1, right);
        }
    }
    int[] quick_sort(int[] arr) {
        if (arr.length > 0) quick_sort(arr, 0, arr.length - 1);
        return arr;
    }
    public static void main(String[] args) {
        Ns4 s = new Ns4();
        Object[][] cases = {{new int[]{3, 1, 4, 1, 5, 9, 2, 6}, new int[]{1, 1, 2, 3, 4, 5, 6, 9}}};
        boolean ok = true;
        for (Object[] c : cases) {
            int[] got = s.quick_sort((int[]) c[0]);
            if (!java.util.Arrays.equals(got, (int[]) c[1])) { ok = false; System.out.println("FAIL got=" + java.util.Arrays.toString(got)); }
        }
        if (!ok) throw new RuntimeException("FAILED");
        System.out.println("PASS");
    }
}
'''

files["solution_5___5.java"] = r'''package com.webfault.dsa;

class Ns5 {
    int[] selection_sort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n; i++) {
            int min_idx = i;
            for (int j = i + 1; j < n; j++) if (arr[j] < arr[min_idx]) min_idx = j;
            int t = arr[i]; arr[i] = arr[min_idx]; arr[min_idx] = t;
        }
        return arr;
    }
    public static void main(String[] args) {
        Ns5 s = new Ns5();
        Object[][] cases = {{new int[]{3, 1, 4, 1, 5, 9, 2, 6}, new int[]{1, 1, 2, 3, 4, 5, 6, 9}}};
        boolean ok = true;
        for (Object[] c : cases) {
            int[] got = s.selection_sort((int[]) c[0]);
            if (!java.util.Arrays.equals(got, (int[]) c[1])) { ok = false; System.out.println("FAIL got=" + java.util.Arrays.toString(got)); }
        }
        if (!ok) throw new RuntimeException("FAILED");
        System.out.println("PASS");
    }
}
'''

files["solution_6___6.java"] = r'''package com.webfault.dsa;

class Ns6 {
    int[] insertion_sort(int[] arr) {
        for (int i = 1; i < arr.length; i++) {
            int key = arr[i];
            int j = i - 1;
            while (j >= 0 && arr[j] > key) { arr[j + 1] = arr[j]; j--; }
            arr[j + 1] = key;
        }
        return arr;
    }
    public static void main(String[] args) {
        Ns6 s = new Ns6();
        Object[][] cases = {{new int[]{3, 1, 4, 1, 5, 9, 2, 6}, new int[]{1, 1, 2, 3, 4, 5, 6, 9}}};
        boolean ok = true;
        for (Object[] c : cases) {
            int[] got = s.insertion_sort((int[]) c[0]);
            if (!java.util.Arrays.equals(got, (int[]) c[1])) { ok = false; System.out.println("FAIL got=" + java.util.Arrays.toString(got)); }
        }
        if (!ok) throw new RuntimeException("FAILED");
        System.out.println("PASS");
    }
}
'''

files["solution_7___7.java"] = r'''package com.webfault.dsa;

class Ns7 {
    int[] merge(int[] left, int[] right) {
        int[] result = new int[left.length + right.length];
        int i = 0, j = 0, k = 0;
        while (i < left.length && j < right.length) {
            if (left[i] <= right[j]) result[k++] = left[i++];
            else result[k++] = right[j++];
        }
        while (i < left.length) result[k++] = left[i++];
        while (j < right.length) result[k++] = right[j++];
        return result;
    }
    int[] merge_sort(int[] arr) {
        if (arr.length <= 1) return arr;
        int mid = arr.length / 2;
        int[] left = merge_sort(java.util.Arrays.copyOfRange(arr, 0, mid));
        int[] right = merge_sort(java.util.Arrays.copyOfRange(arr, mid, arr.length));
        return merge(left, right);
    }
    public static void main(String[] args) {
        Ns7 s = new Ns7();
        Object[][] cases = {{new int[]{3, 1, 4, 1, 5, 9, 2, 6}, new int[]{1, 1, 2, 3, 4, 5, 6, 9}}};
        boolean ok = true;
        for (Object[] c : cases) {
            int[] got = s.merge_sort((int[]) c[0]);
            if (!java.util.Arrays.equals(got, (int[]) c[1])) { ok = false; System.out.println("FAIL got=" + java.util.Arrays.toString(got)); }
        }
        if (!ok) throw new RuntimeException("FAILED");
        System.out.println("PASS");
    }
}
'''

files["solution_8___8.java"] = r'''package com.webfault.dsa;

class Ns8 {
    void heapify(int[] arr, int size, int root) {
        int largest = root;
        int left = 2 * root + 1;
        int right = 2 * root + 2;
        if (left < size && arr[left] > arr[largest]) largest = left;
        if (right < size && arr[right] > arr[largest]) largest = right;
        if (largest != root) { int t = arr[root]; arr[root] = arr[largest]; arr[largest] = t; heapify(arr, size, largest); }
    }
    int[] heap_sort(int[] arr) {
        int n = arr.length;
        for (int i = n / 2 - 1; i >= 0; i--) heapify(arr, n, i);
        for (int i = n - 1; i > 0; i--) { int t = arr[0]; arr[0] = arr[i]; arr[i] = t; heapify(arr, i, 0); }
        return arr;
    }
    public static void main(String[] args) {
        Ns8 s = new Ns8();
        Object[][] cases = {{new int[]{3, 1, 4, 1, 5, 9, 2, 6}, new int[]{1, 1, 2, 3, 4, 5, 6, 9}}};
        boolean ok = true;
        for (Object[] c : cases) {
            int[] got = s.heap_sort((int[]) c[0]);
            if (!java.util.Arrays.equals(got, (int[]) c[1])) { ok = false; System.out.println("FAIL got=" + java.util.Arrays.toString(got)); }
        }
        if (!ok) throw new RuntimeException("FAILED");
        System.out.println("PASS");
    }
}
'''

files["solution_9___9.java"] = r'''package com.webfault.dsa;

class Ns9 {
    int fib_recursive(int n) {
        if (n < 2) return n;
        return fib_recursive(n - 1) + fib_recursive(n - 2);
    }
    int fib_iterative(int n) {
        if (n < 2) return n;
        int a = 0, b = 1;
        for (int k = 2; k <= n; k++) { int t = b; b = a + b; a = t; }
        return b;
    }
    public static void main(String[] args) {
        Ns9 s = new Ns9();
        boolean ok = true;
        if (s.fib_recursive(10) != 55) { ok = false; System.out.println("FAIL fib_recursive"); }
        if (s.fib_iterative(10) != 55) { ok = false; System.out.println("FAIL fib_iterative"); }
        if (!ok) throw new RuntimeException("FAILED");
        System.out.println("PASS");
    }
}
'''

files["solution_10___10.java"] = r'''package com.webfault.dsa;

class Ns10 {
    int[] two_sum_brute(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++)
            for (int j = i + 1; j < nums.length; j++)
                if (nums[i] + nums[j] == target) return new int[]{i, j};
        return new int[]{};
    }
    int[] two_sum_hash(int[] nums, int target) {
        java.util.Map<Integer, Integer> seen = new java.util.HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (seen.containsKey(target - nums[i])) return new int[]{seen.get(target - nums[i]), i};
            seen.put(nums[i], i);
        }
        return new int[]{};
    }
    public static void main(String[] args) {
        Ns10 s = new Ns10();
        boolean ok = true;
        if (!java.util.Arrays.equals(s.two_sum_brute(new int[]{2, 7, 11, 15}, 9), new int[]{0, 1})) { ok = false; System.out.println("FAIL two_sum_brute"); }
        if (!java.util.Arrays.equals(s.two_sum_hash(new int[]{2, 7, 11, 15}, 9), new int[]{0, 1})) { ok = false; System.out.println("FAIL two_sum_hash"); }
        if (!ok) throw new RuntimeException("FAILED");
        System.out.println("PASS");
    }
}
'''

files["solution_11___11.java"] = r'''package com.webfault.dsa;

class Ns11 {
    int[][] matrix_multiply(int[][] a, int[][] b) {
        int n = a.length;
        int[][] c = new int[n][n];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                for (int k = 0; k < n; k++)
                    c[i][j] += a[i][k] * b[k][j];
        return c;
    }
    public static void main(String[] args) {
        Ns11 s = new Ns11();
        int[][] a = {{1, 2}, {3, 4}};
        int[][] b = {{5, 6}, {7, 8}};
        int[][] want = {{19, 22}, {43, 50}};
        int[][] got = s.matrix_multiply(a, b);
        boolean ok = true;
        if (got.length != want.length) ok = false;
        else for (int i = 0; i < want.length; i++)
            if (!java.util.Arrays.equals(got[i], want[i])) ok = false;
        if (!ok) { System.out.println("FAIL"); throw new RuntimeException("FAILED"); }
        System.out.println("PASS");
    }
}
'''

files["solution_12___12.java"] = r'''package com.webfault.dsa;

import java.util.*;

class Ns12 {
    List<String> hanoi(int n, char src, char aux, char dst) {
        List<String> moves = new ArrayList<>();
        h(n, src, aux, dst, moves);
        return moves;
    }
    void h(int n, char src, char aux, char dst, List<String> moves) {
        if (n == 1) { moves.add("" + src + dst); return; }
        h(n - 1, src, dst, aux, moves);
        moves.add("" + src + dst);
        h(n - 1, aux, src, dst, moves);
    }
    public static void main(String[] args) {
        Ns12 s = new Ns12();
        List<String> got = s.hanoi(3, 'A', 'B', 'C');
        List<String> want = Arrays.asList("AC", "AB", "CB", "AC", "BA", "BC", "AC");
        boolean ok = got.equals(want);
        if (!ok) { System.out.println("FAIL got=" + got); throw new RuntimeException("FAILED"); }
        System.out.println("PASS");
    }
}
'''

for fn, content in files.items():
    with open(os.path.join(base, fn), "w") as f:
        f.write(content)
print("wrote", len(files), "files")
