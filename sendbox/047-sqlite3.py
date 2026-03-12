import sqlite3
import time


def with_cursor(original_func):
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('blog.db')
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        rv = original_func(c, *args, **kwargs)
        conn.commit()
        conn.close()
        return rv
    return wrapper


@with_cursor
def get_blog_list(c):
    c.execute("SELECT * FROM blog")
    return c.fetchall()


@with_cursor
def add_blog(c, subject, content):
    c.execute("INSERT INTO blog (subject, content, date) VALUES (?, ?, ?)",
        (subject, content, time.strftime('%Y%m%d')))


@with_cursor
def read_blog(c, _id):
    c.execute("SELECT * FROM blog WHERE id=?", (_id,))
    return c.fetchone()


@with_cursor
def modify_blog(c, _id, subject, content):
    c.execute("UPDATE blog SET subject=?, content=? WHERE id=?",
        (subject, content, _id))


@with_cursor
def remove_blog(c, _id):
    c.execute("DELETE FROM blog WHERE id=?", (_id,))


if __name__ == "__main__":
    # 1. 블로그 포스트 추가 테스트
    # print("--- 포스트 추가 중 ---")
    # add_blog("첫 번째 포스트", "안녕하세요, SQLite와 파이썬 테스트입니다.")
    # add_blog("두 번째 포스트", "데코레이터를 사용하니 코드가 깔끔하네요!")

    # 2. 전체 목록 조회 테스트
    print("\n--- 전체 블로그 목록 ---")
    blogs = get_blog_list()
    for blog in blogs:
        # sqlite3.Row 설정을 했으므로 컬럼명으로 접근 가능합니다.
        print(f"ID: {blog['id']} | 제목: {blog['subject']} | 날짜: {blog['date']}")

    # 3. 특정 포스트 읽기 (ID가 1인 데이터가 있다고 가정)
    # if blogs:
    #     target_id = blogs[0]['id']
    #     print(f"\n--- ID {target_id}번 포스트 상세 내용 ---")
    #     post = read_blog(target_id)
    #     if post:
    #         print(f"제목: {post['subject']}\n내용: {post['content']}")

    # 4. 포스트 수정 테스트
    # modify_blog(target_id, "수정된 제목", "내용도 수정되었습니다.")

    # 5. 포스트 삭제 테스트
    # remove_blog(target_id)