-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133278676
-- LeetCode 133278676. 使用链表（指针链）获取 JSON 节点值 — Lua 版（方案A：安全遍历（单用例），缺失返回 nil）
local function get_value(data, path) -- local function get_value(data, 当前路径)
	local node = data -- 把 data 写入 local node
	for _, key in ipairs(path) do -- 遍历取 key
		if type(node) ~= "table" or node[key] == nil then
			return nil
		end
		node = node[key] -- 把 节点[key] 存入 节点
	end -- 终点
	return node -- 返回 节点
end -- 终点

local data = { a = { b = { c = 1 } }, d = { e = 2 } }
assert(get_value(data, { "a", "b", "c" }) == 1, "p1") -- 断言校验
assert(get_value(data, { "a", "z" }) == nil, "p2") -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
