-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145355207
-- LeetCode LCR 152. 验证二叉搜索树的后序遍历序列 — Lua 版（方案1）
local function verify_postorder(postorder) -- local function verify_postorder(postorder)
	local function check(seq, lo, hi) -- local function check(seq, 左边界, 右边界)
		if hi - lo <= 1 then
			return true
		end -- 若 右边界 减 左边界 不超过 1 then return true 终点
		local root = seq[hi] -- 把 seq[右边界] 写入 local root
		local i = lo -- 把 左边界 写入 local i
		while i < hi and seq[i] < root do
			i = i + 1
		end -- 把 下标 i 加 1 终点 写入 while i < hi and seq[i] < root do i
		for j = i, hi - 1 do -- 把 下标 i, 右边界 减 1 do 写入 for j
			if seq[j] < root then
				return false
			end -- 若 seq[下标 j] 小于 根节点 then return false 终点
		end -- 终点
		return check(seq, lo, i - 1) and check(seq, i, hi - 1) -- 返回 check(seq, 左边界, 下标 i 减 1) and check(seq, 下标 i, 右边界 减 1)
	end -- 终点
	return check(postorder, 1, #postorder) -- 返回 check(postorder, 1, #postorder)
end -- 终点
assert(verify_postorder({ 1, 6, 3, 2, 5 }) == false) -- 断言校验
assert(verify_postorder({ 1, 3, 2, 4, 5 }) == true) -- 断言校验
assert(verify_postorder({ 4, 6, 5, 9, 8, 7 }) == true) -- 断言校验
assert(verify_postorder({ 1, 2, 3 }) == true) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
