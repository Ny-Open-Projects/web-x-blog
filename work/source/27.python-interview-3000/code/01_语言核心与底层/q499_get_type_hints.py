from typing import Dict, List, get_type_hints

def parse(data: "bytes") -> "Dict[str, int]":
    """字符串注解:运行时延迟求值"""
    return {}

def summarize(rows: List[Dict[str, float]], title: str = "report") -> str:
    return f"{title}: {len(rows)} rows"

if __name__ == "__main__":
    print("raw annotations:", parse.__annotations__)
    print("resolved:", get_type_hints(parse))
    hints = get_type_hints(summarize)
    print("rows origin:", hints["rows"].__origin__)
    print("title default preserved:", summarize.__defaults__)
