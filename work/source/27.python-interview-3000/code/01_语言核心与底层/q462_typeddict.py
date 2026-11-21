from typing import TypedDict

class Movie(TypedDict):
    title: str
    year: int

class MoviePartial(TypedDict, total=False):
    """所有字段可选"""
    title: str
    year: int

def print_movie(m: Movie) -> None:
    print(f"{m['title']} ({m['year']})")

if __name__ == "__main__":
    m: Movie = {"title": "Inception", "year": 2010}
    print_movie(m)
    p: MoviePartial = {"title": "Untitled"}     # 缺 year:total=False 允许
    print(p)
    print(type(m).__name__)                     # dict:运行时就是普通字典
    m["extra"] = 1                              # 运行时不拦,mypy 会报错
    print("runtime is permissive:", m)
