-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133471440
-- LeetCode 215. 数组中的第K个最大元素 — Lua 版（方案3）
local function find_kth_largest(nums, k) -- local function find_kth_largest(数组, 下标 k)
	local a = { table.unpack(nums) } -- 把 {table.unpack(数组)} 写入 local a
	local length = #a -- 把 #数组 写入 local length
	for i = length, length - k + 1, -1 do -- 把 长度, 长度 减 下标 k 加 1, 减 1 do 写入 for i
		for j = 1, i - 1 do -- 让 下标 j 从 1 走到 下标 i（Lua 1 基）
			if a[j] > a[j + 1] then
				a[j], a[j + 1] = a[j + 1], a[j]
			end
		end -- 终点
	end -- 终点
	return a[length - k + 1] -- 返回 数组[长度 减 下标 k 加 1]
end -- 终点
assert(find_kth_largest({ 3, 2, 1, 5, 6, 4 }, 2) == 5) -- 断言校验
assert(find_kth_largest({ 3, 2, 3, 1, 2, 4, 5, 5, 6 }, 4) == 4) -- 断言校验
assert(find_kth_largest({ 1 }, 1) == 1) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
