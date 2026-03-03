import os
from todo_logic import TodoManager

def test_add_task(tmp_path):
    file = tmp_path / "test.json"
    manager = TodoManager(file)
    manager.add_task("Test Task")
    assert len(manager.tasks) == 1
    assert manager.tasks[0]["task"] == "Test Task"

def test_delete_task(tmp_path):
    file = tmp_path / "test.json"
    manager = TodoManager(file)
    manager.add_task("Task")
    manager.delete_task(0)
    assert len(manager.tasks) == 0

def test_save_and_load(tmp_path):
    file = tmp_path / "test.json"
    manager = TodoManager(file)
    manager.add_task("Save Test")
    manager.save_tasks()

    new_manager = TodoManager(file)
    assert len(new_manager.tasks) == 1

def test_corrupted_json(tmp_path):
    file = tmp_path / "bad.json"
    with open(file, "w") as f:
        f.write("INVALID JSON")

    manager = TodoManager(file)
    assert manager.tasks == []