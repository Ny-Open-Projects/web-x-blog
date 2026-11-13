-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134191965
-- 数据结构与算法之排序: 基数排序 — Lua 版（方案1）
local function radix_sort(nums) -- local function radix_sort(数组)
	if #nums == 0 then
		return nums
	end -- 若 #数组 等于 0 then return 数组 终点
	local mn, mx = nums[1], nums[1] -- 把 数组[1], 数组[1] 写入 local mn, mx
	for _, v in ipairs(nums) do -- 遍历取 值
		if v < mn then
			mn = v
		end -- 若 值 小于 mn then mn 赋值为 值 终点
		if v > mx then
			mx = v
		end -- 若 值 超过 mx then mx 赋值为 值 终点
	end -- 终点
	local offset = mn < 0 and -mn or 0 -- 把 mn 小于 0 and 减 mn or 0 写入 local offset
	local adj = {} -- 把 {} 写入 local adj
	for i, v in ipairs(nums) do
		adj[i] = v + offset
	end -- 遍历取 值
	local max_adj = adj[1] -- 把 邻接表[1] 写入 local max_adj
	for _, v in ipairs(adj) do
		if v > max_adj then
			max_adj = v
		end
	end -- 遍历取 值
	local radix = 1 -- 把 1 写入 local radix
	local tmp = {} -- 把 {} 写入 local tmp
	while max_adj >= radix do -- 把 radix do 写入 while max_adj >
		local bucket = {} -- 把 {} 写入 local bucket
		for i = 0, 9 do
			bucket[i] = 0
		end -- 让 下标 i 从 0 走到 9（Lua 1 基）
		for _, v in ipairs(adj) do -- 遍历取 值
			local d = math.floor(v / radix) % 10 -- 把 math.floor(值 除以 radix) 对…取模 10 写入 local d
			bucket[d] = bucket[d] + 1 -- 把 bucket[d] 加 1 写入 bucket[d]
		end -- 终点
		for i = 1, 9 do
			bucket[i] = bucket[i] + bucket[i - 1]
		end -- 让 下标 i 从 1 走到 9（Lua 1 基）
		for i = #adj, 1, -1 do -- 把 #邻接表, 1, 减 1 do 写入 for i
			local d = math.floor(adj[i] / radix) % 10 -- 把 math.floor(邻接表[下标 i] 除以 radix) 对…取模 10 写入 local d
			tmp[bucket[d]] = adj[i] -- 把 邻接表[下标 i] 写入 tmp[bucket[d]]
			bucket[d] = bucket[d] - 1 -- 把 bucket[d] 减 1 写入 bucket[d]
		end -- 终点
		for i = 1, #adj do
			adj[i] = tmp[i]
		end -- 把 1, #邻接表 do 邻接表[下标 i] 赋值为 临时变量[下标 i] 终点 写入 for i
		radix = radix * 10 -- 把 radix 乘 10 存入 radix
	end -- 终点
	for i, v in ipairs(adj) do
		adj[i] = v - offset
	end -- 遍历取 值
	return adj -- 返回 邻接表
end -- 终点
assert(table.concat(radix_sort({ 1, 2, 3 }), ",") == "1,2,3") -- 打印输出
assert(table.concat(radix_sort({ 5, 4, 3, 2, 1 }), ",") == "1,2,3,4,5") -- 打印输出
assert(table.concat(radix_sort({ 3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5 }), ",") == "1,1,2,3,3,4,5,5,5,6,9") -- 打印输出
print("PASS") -- 全部用例通过，输出 PASS
