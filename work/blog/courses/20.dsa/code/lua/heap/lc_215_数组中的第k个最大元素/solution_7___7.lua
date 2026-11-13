-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133471440
-- LeetCode 215. 数组中的第K个最大元素 — Lua 版（方案7）
local function quickselect(a, l, r, k) -- local function quickselect(数组, 左指针, 右指针, 下标 k)
	if l >= r then
		return a[k]
	end -- 若 左指针 不低于 右指针 then return 数组[下标 k] 终点
	local i, j = l, r -- 把 左指针, 右指针 写入 local i, j
	local pivot = a[math.floor((l + r) / 2)] -- 把 数组[math.floor((左指针 加 右指针) 除以 2)] 写入 local pivot
	while i <= j do -- 把 下标 j do 写入 while i <
		while a[i] > pivot do
			i = i + 1
		end -- 把 下标 i 加 1 终点 写入 while a[i] > pivot do i
		while a[j] < pivot do
			j = j - 1
		end -- 把 下标 j 减 1 终点 写入 while a[j] < pivot do j
		if i <= j then -- 若 下标 i 不超过 下标 j then
			a[i], a[j] = a[j], a[i] -- 把 数组[下标 j], 数组[下标 i] 写入 a[i], a[j]
			i, j = i + 1, j - 1 -- 把 下标 i 加 1, 下标 j 减 1 写入 i, j
		end -- 终点
	end -- 终点
	if k <= j then
		return quickselect(a, l, j, k)
	end
	if k >= i then
		return quickselect(a, i, r, k)
	end
	return a[k] -- 返回 数组[下标 k]
end -- 终点
local function find_kth_largest(nums, k) -- local function find_kth_largest(数组, 下标 k)
	local a = { table.unpack(nums) } -- 把 {table.unpack(数组)} 写入 local a
	return quickselect(a, 1, #a, k) -- 返回 quickselect(数组, 1, #数组, 下标 k)
end -- 终点
assert(find_kth_largest({ 3, 2, 1, 5, 6, 4 }, 2) == 5) -- 断言校验
assert(find_kth_largest({ 3, 2, 3, 1, 2, 4, 5, 5, 6 }, 4) == 4) -- 断言校验
assert(find_kth_largest({ 1 }, 1) == 1) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
