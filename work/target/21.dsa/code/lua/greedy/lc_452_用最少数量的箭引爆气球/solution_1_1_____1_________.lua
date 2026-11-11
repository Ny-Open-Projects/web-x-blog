-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135949307
-- LeetCode 452. 用最少数量的箭引爆气球 — Lua 版（方案1）
local function find_min_arrow_shots(points) -- local function find_min_arrow_shots(points)
	if #points == 0 then
		return 0
	end -- 若 #points 等于 0 then return 0 终点
	local arr = {} -- 把 {} 写入 local arr
	for i, p in ipairs(points) do
		arr[i] = { p[1], p[2] }
	end -- 遍历取 节点
	table.sort(arr, function(a, b)
		return a[2] < b[2]
	end) -- 排序
	local arrows, end_ = 1, arr[1][2] -- 把 1, 数组[1][2] 写入 local arrows, end_
	for k = 2, #arr do -- 把 2, #数组 do 写入 for k
		if arr[k][1] > end_ then -- 若 数组[下标 k][1] 超过 end_ then
			arrows = arrows + 1 -- 把 arrows 加 1 存入 arrows
			end_ = arr[k][2] -- 把 数组[下标 k][2] 存入 end_
		end -- 终点
	end -- 终点
	return arrows -- 返回 arrows
end -- 终点
assert(find_min_arrow_shots({ { 10, 16 }, { 2, 8 }, { 1, 6 }, { 7, 12 } }) == 2) -- 断言校验
assert(find_min_arrow_shots({}) == 0) -- 断言校验
assert(find_min_arrow_shots({ { 1, 2 }, { 3, 4 }, { 5, 6 }, { 7, 8 } }) == 4) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
