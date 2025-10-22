from app.app import dedupe_header

def test_unique_columns():
    # 测试：如果所有列名本来就是唯一的，函数是否会保持它们不变。

    assert dedupe_header(["id", "name", "age"]) == ["id", "name", "age"]

def test_duplicate_columns():
    #测试：如果所有列名都是重复的，函数是否能正确添加后缀。
    assert dedupe_header(["id", "id", "id"]) == ["id", "id.1", "id.2"]

def test_mixed_columns():
   # 测试：文档中给出的混合示例 [cite: 23, 46, 48]。
    cols = ["id", "name", "id", "name", "name"]

    expected = ["id", "name", "id.1", "name.1", "name.2"]

    assert dedupe_header(cols) == expected

def test_empty_list():
    # 测试：如果输入是一个空列表，函数是否能正确返回一个空列表。
    assert dedupe_header([]) == []