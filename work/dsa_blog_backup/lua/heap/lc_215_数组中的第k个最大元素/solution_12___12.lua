-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133471440
-- LeetCode 215. 数组中的第K个最大元素 — Lua 版（方案12）
local function find_kth_largest(nums, k) -- local function find_kth_largest(数组, 下标 k)
	local a = { table.unpack(nums) } -- 把 {table.unpack(数组)} 写入 local a
	table.sort(a, function(x, y)
		return x > y
	end) -- 排序
	return a[k] -- 返回 数组[下标 k]
end -- 终点
assert(find_kth_largest({ 3, 2, 1, 5, 6, 4 }, 2) == 5) -- 断言校验
assert(find_kth_largest({ 3, 2, 3, 1, 2, 4, 5, 5, 6 }, 4) == 4) -- 断言校验
assert(find_kth_largest({ 1 }, 1) == 1) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
