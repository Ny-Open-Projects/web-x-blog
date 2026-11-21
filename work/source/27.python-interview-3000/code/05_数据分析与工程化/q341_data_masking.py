import hashlib
import os

SALT = os.environ.get("MASK_SALT", "dev-only-salt")

def mask_phone(phone):
    """展示用掩码:保留前 3 后 4。"""
    s = str(phone)
    return s[:3] + "****" + s[-4:] if len(s) == 11 else "invalid"

def hash_id(id_no):
    """分析用确定性哈希:同输入同输出,可 join 不可逆。"""
    return hashlib.sha256((SALT + str(id_no)).encode()).hexdigest()[:16]

def mask_name(name):
    return name[0] + "**" if name else name

if __name__ == "__main__":
    users = [{"phone": "13812345678", "name": "王大力", "cid": "110101199001011234"}]
    masked = [{**u,
               "phone": mask_phone(u["phone"]),
               "name": mask_name(u["name"]),
               "cid": hash_id(u["cid"])} for u in users]
    assert masked[0]["cid"] == hash_id("110101199001011234")  # 可复现可 join
    print(masked)
