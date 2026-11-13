-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145078849
-- LeetCode 341. 扁平化嵌套列表迭代器 — Lua 版（方案3）
local function flatten(nested) -- local function flatten(nested)
	local out = {} -- 把 {} 写入 local out
	local function go(items) -- local function go(items)
		for _, it in ipairs(items) do -- 遍历取 it
			if type(it) == "number" then -- 若 type(it) 等于 「number」 then
				out[#out + 1] = it -- 把 it 写入 out[#out + 1]
			else -- 否则
				go(it) -- go(it)
			end -- 终点
		end -- 终点
	end -- 终点
	go(nested) -- go(nested)
	return out -- 返回 out
end -- 终点
assert(table.concat(flatten({ 1, { 2, { 3, 4 } } }), ",") == "1,2,3,4") -- 打印输出
assert(table.concat(flatten({ { 1, 1 }, 2, { 1, 1 } }), ",") == "1,1,2,1,1") -- 打印输出
print("PASS") -- 全部用例通过，输出 PASS
