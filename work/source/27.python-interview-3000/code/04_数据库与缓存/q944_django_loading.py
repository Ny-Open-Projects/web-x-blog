"""用原生 SQL 演示 select_related 与 prefetch_related 的形态差异"""
import sqlite3

if __name__ == "__main__":
    conn = sqlite3.connect(":memory:")
    conn.executescript("""
        CREATE TABLE author (id INTEGER PRIMARY KEY, name TEXT);
        CREATE TABLE book (id INTEGER PRIMARY KEY, author_id INT, title TEXT);
        INSERT INTO author VALUES (1, 'Ada'), (2, 'Alan');
        INSERT INTO book VALUES (1, 1, 'Notes'), (2, 1, 'Engine'),
                                (3, 2, 'Machine');
    """)
    print("select_related 形态: 一条 JOIN")
    for r in conn.execute(
            "SELECT b.title, a.name FROM book b "
            "LEFT JOIN author a ON a.id = b.author_id"):
        print("  ", r)
    print("prefetch_related 形态: 两条 SQL + 内存拼装")
    authors = conn.execute("SELECT id, name FROM author").fetchall()
    books = conn.execute(
        f"SELECT id, author_id, title FROM book "
        f"WHERE author_id IN ({','.join(str(a[0]) for a in authors)})").fetchall()
    print("   作者:", authors, "\n   批量书籍:", books)
    print("Django: FK/OneToOne 用 select_related, M2M/反向用 prefetch_related")
