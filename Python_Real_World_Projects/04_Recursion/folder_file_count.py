"""Challenge 12 - Nested Folder File Count (recursion)."""


def count_files(folder):
    """Count files in a folder and every descendant folder."""
    if not isinstance(folder, dict):
        raise TypeError("A folder must be a dictionary.")
    files = folder.get("files", [])
    subfolders = folder.get("subfolders", [])
    return len(files) + sum(count_files(sub) for sub in subfolders)


if __name__ == "__main__":
    example = {"files": ["a.pdf"],
               "subfolders": [{"files": ["b.csv", "c.txt"], "subfolders": []}]}
    empty = {"files": [], "subfolders": []}
    deep = {"files": ["root.txt"], "subfolders": [
        {"files": ["l1.txt"], "subfolders": [
            {"files": [], "subfolders": [
                {"files": ["l3a.txt", "l3b.txt"], "subfolders": []}]}]},
        {"files": [], "subfolders": []}]}
    assert count_files(example) == 3
    assert count_files(empty) == 0
    assert count_files(deep) == 4
    print("example:", count_files(example))
    print("empty:  ", count_files(empty))
    print("deep:   ", count_files(deep))
