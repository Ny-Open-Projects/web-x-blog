-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135941089
-- LeetCode 435. 无重叠区间 — Lua 版（方案1）
local function erase_overlap_intervals(intervals) -- local function erase_overlap_intervals(intervals)
	if #intervals == 0 then
		return 0
	end -- 若 #intervals 等于 0 then return 0 终点
	local arr = {} -- 把 {} 写入 local arr
	for i, iv in ipairs(intervals) do
		arr[i] = { iv[1], iv[2] }
	end -- 遍历取 iv
	table.sort(arr, function(a, b)
		return a[2] < b[2]
	end) -- 排序
	local count, end_ = 1, arr[1][2] -- 把 1, 数组[1][2] 写入 local count, end_
	for i = 2, #arr do -- 把 2, #数组 do 写入 for i
		if arr[i][1] >= end_ then -- 若 数组[下标 i][1] 不低于 end_ then
			count = count + 1 -- 把 计数 加 1 存入 计数
			end_ = arr[i][2] -- 把 数组[下标 i][2] 存入 end_
		end -- 终点
	end -- 终点
	return #arr - count -- 返回 #数组 减 计数
end -- 终点
assert(erase_overlap_intervals({ { 1, 2 }, { 2, 3 }, { 3, 4 }, { 1, 3 } }) == 1) -- 断言校验
assert(erase_overlap_intervals({}) == 0) -- 断言校验
assert(erase_overlap_intervals({ { 1, 2 }, { 1, 2 }, { 1, 2 } }) == 2) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
