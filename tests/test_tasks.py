import json
import os
import tempfile


# ---------------------------
# Test Add Task
# ---------------------------
def test_add_task():
    tasks = []
    tasks.append({"text": "Study", "completed": False})

    assert len(tasks) == 1
    assert tasks[0]["text"] == "Study"
    assert tasks[0]["completed"] is False


# ---------------------------
# Test Mark Complete
# ---------------------------
def test_mark_complete():
    tasks = [{"text": "Study", "completed": False}]

    tasks[0]["completed"] = True

    assert tasks[0]["completed"] is True


# ---------------------------
# Test Save and Load JSON
# ---------------------------
def test_save_and_load():
    sample_tasks = [{"text": "Test Task", "completed": False}]

    # Open file in write mode (IMPORTANT FIX)
    with tempfile.NamedTemporaryFile(delete=False, mode="w") as tmp:
        json.dump(sample_tasks, tmp)
        tmp.close()

        # Now read the file
        with open(tmp.name, "r") as f:
            loaded = json.load(f)

        assert loaded == sample_tasks

        os.remove(tmp.name)


# ---------------------------
# Test Corrupted JSON
# ---------------------------
def test_corrupted_json():
    with tempfile.NamedTemporaryFile(delete=False, mode="w") as tmp:
        tmp.write("INVALID JSON")
        tmp.close()

        try:
            with open(tmp.name, "r") as f:
                json.load(f)
        except json.JSONDecodeError:
            assert True
        finally:
            os.remove(tmp.name)