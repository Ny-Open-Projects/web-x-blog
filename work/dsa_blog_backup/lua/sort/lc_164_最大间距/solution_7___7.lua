-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135003383
-- LeetCode 164. 最大间距 — Lua 版（方案7）
local function maximum_gap(nums) -- local function maximum_gap(数组)
	local n = #nums -- 把 #数组 写入 local n
	if n < 2 then
		return 0
	end -- 若 元素个数 小于 2 then return 0 终点
	local min_val, max_val = math.huge, -math.huge -- 把 math.huge, 减 math.huge 写入 local min_val, max_val
	for _, x in ipairs(nums) do -- 遍历取 x
		if x < min_val then
			min_val = x
		end -- 若 x 小于 min_val then min_val 赋值为 x 终点
		if x > max_val then
			max_val = x
		end -- 若 x 超过 max_val then max_val 赋值为 x 终点
	end -- 终点
	if min_val == max_val then
		return 0
	end -- 若 min_val 等于 max_val then return 0 终点
	local d = math.max(1, math.floor((max_val - min_val) / (n - 1)))
	local bucket_size = math.floor((max_val - min_val) / d) + 1
	local buckets = {} -- 把 {} 写入 local buckets
	for i = 1, bucket_size do
		buckets[i] = { -1, -1 }
	end -- 让 下标 i 从 1 走到 bucket_size（Lua 1 基）
	for _, x in ipairs(nums) do -- 遍历取 x
		local idx = math.floor((x - min_val) / d) + 1 -- 把 math.floor((x 减 min_val) 除以 d) 加 1 写入 local idx
		if buckets[idx][1] == -1 then
			buckets[idx] = { x, x } -- 若 buckets[idx][1] 等于 减 1 then buckets[idx] 赋值为 {x, x}
		else -- 否则
			if x < buckets[idx][1] then
				buckets[idx][1] = x
			end -- 若 x 小于 buckets[idx][1] then buckets[idx][1] 赋值为 x 终点
			if x > buckets[idx][2] then
				buckets[idx][2] = x
			end -- 若 x 超过 buckets[idx][2] then buckets[idx][2] 赋值为 x 终点
		end -- 终点
	end -- 终点
	local ans, prev_max = 0, -1 -- 把 0, 减 1 写入 local ans, prev_max
	for _, b in ipairs(buckets) do -- 遍历取 b
		if b[1] ~= -1 then -- 若 b[1] ~ 赋值为 减 1 then
			if prev_max ~= -1 and b[1] - prev_max > ans then
				ans = b[1] - prev_max
			end
			prev_max = b[2] -- 把 b[2] 存入 prev_max
		end -- 终点
	end -- 终点
	return ans -- 返回 答案
end -- 终点
assert(maximum_gap({ 1, 2, 3 }) == 1) -- 断言校验
assert(maximum_gap({ 3, 6, 9, 1 }) == 3) -- 断言校验
assert(maximum_gap({ 10 }) == 0) -- 断言校验
assert(maximum_gap({}) == 0) -- 断言校验
assert(maximum_gap({ 1, 10000000 }) == 9999999) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
