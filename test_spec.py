import subprocess
import os
import shutil

def run_cmd(args):
    result = subprocess.run(
        ["python", "miniquiz.py"] + args,
        capture_output=True,
        text=True
    )
    return result.stdout.strip()

def setup_function():
    if os.path.exists(".miniquiz"):
        shutil.rmtree(".miniquiz")

def test_init():
    run_cmd(["init"])
    assert os.path.exists(".miniquiz")

def test_init_again():
    run_cmd(["init"])
    output = run_cmd(["init"])
    assert "Already initialized" in output

def test_add_question():
    run_cmd(["init"])
    output = run_cmd(["add", "2+2?", "4"])
    assert "Added question #1" in output

def test_add_multiple():
    run_cmd(["init"])
    run_cmd(["add", "Q1", "A1"])
    output = run_cmd(["add", "Q2", "A2"])
    assert "#2" in output

def test_list_empty():
    run_cmd(["init"])
    output = run_cmd(["list"])
    assert "No questions found" in output

def test_list_has_data():
    run_cmd(["init"])
    run_cmd(["add", "2+2?", "4"])
    output = run_cmd(["list"])
    assert "2+2?" in output

def test_not_initialized():
    output = run_cmd(["add", "Q", "A"])
    assert "Not initialized" in output

def test_unknown_command():
    run_cmd(["init"])
    output = run_cmd(["fly"])
    assert "Unknown command" in output