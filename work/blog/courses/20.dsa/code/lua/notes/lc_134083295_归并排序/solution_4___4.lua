-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134083295
-- 数据结构与算法之排序: 归并排序 — Lua 版（方案4）
local function merge_sort(nums) -- local function merge_sort(数组)
	if #nums <= 1 then
		return nums
	end -- 若 #数组 不超过 1 then return 数组 终点
	local mid = #nums // 2 -- 把 #数组 写入 local mid
	local left, right = {}, {} -- 把 {}, {} 写入 local left, right
	for i = 1, mid do
		left[i] = nums[i]
	end -- 让 下标 i 从 1 走到 中点（Lua 1 基）
	for i = mid + 1, #nums do
		right[i - mid] = nums[i]
	end -- 把 中点 加 1, #数组 do 右边界[下标 i 减 中点] 赋值为 数组[下标 i] 终点 写入 for i
	left = merge_sort(left) -- 把 merge_sort(左边界) 存入 左边界
	right = merge_sort(right) -- 把 merge_sort(右边界) 存入 右边界
	local out, i, j = {}, 1, 1 -- 把 {}, 1, 1 写入 local out, i, j
	while i <= #left and j <= #right do -- 把 #左边界 and 下标 j 不超过 #右边界 do 写入 while i <
		if left[i] <= right[j] then
			out[#out + 1] = left[i]
			i = i + 1
		else
			out[#out + 1] = right[j]
			j = j + 1
		end -- 否则
	end -- 终点
	while i <= #left do
		out[#out + 1] = left[i]
		i = i + 1
	end
	while j <= #right do
		out[#out + 1] = right[j]
		j = j + 1
	end
	return out -- 返回 out
end -- 终点
assert(table.concat(merge_sort({ 5, 4, 3, 2, 1 }), ",") == "1,2,3,4,5") -- 打印输出
assert(table.concat(merge_sort({ 3, 1, 4, 1, 5 }), ",") == "1,1,3,4,5") -- 打印输出
print("PASS") -- 全部用例通过，输出 PASS
