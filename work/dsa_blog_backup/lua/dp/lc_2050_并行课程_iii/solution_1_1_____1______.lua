-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134859971
-- LeetCode 2050. 并行课程III — Lua 版（方案1）
local function minimum_time(n, relations, time) -- local function minimum_time(元素个数, relations, time)
	local next_ = {} -- 把 {} 写入 local next_
	local indeg = {} -- 把 {} 写入 local indeg
	for i = 1, n do
		indeg[i] = 0
	end -- 让 下标 i 从 1 走到 元素个数（Lua 1 基）
	for _, r in ipairs(relations) do -- 遍历取 右指针
		next_[r[1]] = next_[r[1]] or {} -- 把 next_[右指针[1]] or {} 写入 next_[r[1]]
		next_[r[1]][#next_[r[1]] + 1] = r[2] -- 把 右指针[2] 写入 next_[r[1]][#next_[r[1]] + 1]
		indeg[r[2]] = indeg[r[2]] + 1 -- 把 indeg[右指针[2]] 加 1 写入 indeg[r[2]]
	end -- 终点
	local finish = {} -- 把 {} 写入 local finish
	for i = 1, n + 1 do
		finish[i] = 0
	end -- 让 下标 i 从 1 走到 元素个数（Lua 1 基）
	local queue = {} -- 把 {} 写入 local queue
	for c = 1, n do -- 让 字符 从 1 走到 元素个数（Lua 1 基）
		if indeg[c] == 0 then
			queue[#queue + 1] = c
		end -- 若 indeg[字符] 等于 0 then 队列[#队列 加 1] 赋值为 字符 终点
	end -- 终点
	local total = 0 -- 把 0 写入 local total
	while #queue > 0 do -- while #队列 超过 0 do
		local nq = {} -- 把 {} 写入 local nq
		for _, c in ipairs(queue) do -- 遍历取 字符
			finish[c] = finish[c] + time[c] -- 把 finish[字符] 加 time[字符] 写入 finish[c]
			if finish[c] > total then
				total = finish[c]
			end -- 若 finish[字符] 超过 总和 then 总和 赋值为 finish[字符] 终点
			for _, nx in ipairs(next_[c] or {}) do -- 遍历取 nx
				if finish[nx] < finish[c] then
					finish[nx] = finish[c]
				end -- 若 finish[nx] 小于 finish[字符] then finish[nx] 赋值为 finish[字符] 终点
				indeg[nx] = indeg[nx] - 1 -- 把 indeg[nx] 减 1 写入 indeg[nx]
				if indeg[nx] == 0 then
					nq[#nq + 1] = nx
				end -- 若 indeg[nx] 等于 0 then nq[#nq 加 1] 赋值为 nx 终点
			end -- 终点
		end -- 终点
		queue = nq -- 把 nq 存入 队列
	end -- 终点
	return total -- 返回 总和
end -- 终点
assert(minimum_time(3, { { 1, 3 }, { 2, 3 } }, { 3, 2, 5 }) == 8) -- 断言校验
assert(minimum_time(5, { { 1, 2 }, { 2, 3 }, { 3, 4 }, { 4, 5 } }, { 1, 2, 3, 4, 5 }) == 15) -- 断言校验
assert(minimum_time(1, {}, { 5 }) == 5) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
