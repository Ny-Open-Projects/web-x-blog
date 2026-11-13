-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/136236962
-- LeetCode 1685. 有序数组中差绝对值之和 — Lua 版（方案3）
local function get_sum_absolute_differences(nums) -- local function get_sum_absolute_differences(数组)
	local n = #nums -- 把 #数组 写入 local n
	local total = 0 -- 把 0 写入 local total
	for _, v in ipairs(nums) do
		total = total + v
	end -- 遍历取 值
	local prefix = 0 -- 把 0 写入 local prefix
	local out = {} -- 把 {} 写入 local out
	for i = 1, n do -- 让 下标 i 从 1 走到 元素个数（Lua 1 基）
		local v = nums[i] -- 把 数组[下标 i] 写入 local v
		local cnt_left = i - 1 -- 把 下标 i 减 1 写入 local cnt_left
		local cnt_right = n - i -- 把 元素个数 减 下标 i 写入 local cnt_right
		local left = v * cnt_left - prefix -- 把 值 乘 cnt_left 减 prefix 写入 local left
		local right = (total - prefix - v) - v * cnt_right -- 把 (总和 减 prefix 减 值) 减 值 乘 cnt_right 写入 local right
		out[i] = left + right -- 把 左边界 加 右边界 写入 out[i]
		prefix = prefix + v -- 把 prefix 加 值 存入 prefix
	end -- 终点
	return out -- 返回 out
end -- 终点
assert(table.concat(get_sum_absolute_differences({ 2, 3, 5 }), ",") == "4,3,5") -- 打印输出
assert(table.concat(get_sum_absolute_differences({ 1, 4, 6, 8, 10 }), ",") == "24,15,13,15,21") -- 打印输出
print("PASS") -- 全部用例通过，输出 PASS
