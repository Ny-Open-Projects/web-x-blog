-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133530983
-- 数据结构与算法之堆: 实现最大堆类及堆排序 — Lua 版（方案3）
local function max_heap_pop_all(input) -- local function max_heap_pop_all(input)
	local h = {} -- 把 {} 写入 local h
	local function up(i) -- local function up(下标 i)
		while i > 1 do -- while 下标 i 超过 1 do
			local p = i // 2 -- 把 下标 i 写入 local p
			if h[p] >= h[i] then
				break
			end -- 若 h[节点] 不低于 h[下标 i] then break 终点
			h[p], h[i] = h[i], h[p] -- 把 h[下标 i], h[节点] 写入 h[p], h[i]
			i = p -- 把 节点 存入 下标 i
		end -- 终点
	end -- 终点
	local function down(i) -- local function down(下标 i)
		local n = #h -- 把 #h 写入 local n
		while true do -- while true do
			local l, r, m = 2 * i, 2 * i + 1, i -- 把 2 乘 下标 i, 2 乘 下标 i 加 1, 下标 i 写入 local l, r, m
			if l <= n and h[l] > h[m] then
				m = l
			end -- 若 左指针 不超过 元素个数 and h[左指针] 超过 h[映射表] then 映射表 赋值为 左指针 终点
			if r <= n and h[r] > h[m] then
				m = r
			end -- 若 右指针 不超过 元素个数 and h[右指针] 超过 h[映射表] then 映射表 赋值为 右指针 终点
			if m == i then
				break
			end -- 若 映射表 等于 下标 i then break 终点
			h[i], h[m] = h[m], h[i] -- 把 h[映射表], h[下标 i] 写入 h[i], h[m]
			i = m -- 把 映射表 存入 下标 i
		end -- 终点
	end -- 终点
	for _, v in ipairs(input) do -- 遍历取 值
		h[#h + 1] = v -- 把 值 写入 h[#h + 1]
		up(#h) -- up(#h)
	end -- 终点
	local out = {} -- 把 {} 写入 local out
	while #h > 0 do -- while #h 超过 0 do
		out[#out + 1] = h[1] -- 把 h[1] 写入 out[#out + 1]
		local last = table.remove(h) -- 把 table 弹出 h) 写入 local last
		if #h > 0 then -- 若 #h 超过 0 then
			h[1] = last -- 把 last 写入 h[1]
			down(1) -- down(1)
		end -- 终点
	end -- 终点
	return out -- 返回 out
end -- 终点
assert(table.concat(max_heap_pop_all({ 3, 1, 6, 5, 2, 4 }), ",") == "6,5,4,3,2,1") -- 打印输出
print("PASS") -- 全部用例通过，输出 PASS
