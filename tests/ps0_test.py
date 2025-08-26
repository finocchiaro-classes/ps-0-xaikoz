import pytest
from io import StringIO
import sys
import os

# Helper function to capture printed output from script execution
def capture_script_output(script_path):
    captured_output = StringIO()
    sys.stdout = captured_output
    sys.stdin = StringIO()  # Ensure no input is required
    with open(script_path) as script_file:
        exec(script_file.read())
    sys.stdout = sys.__stdout__
    return captured_output.getvalue().strip()

# Test cases for ps0.py
def test_hello_boston_college():
    script_path = os.path.join(os.path.dirname(__file__), "../ps0.py")
    output = capture_script_output(script_path)
    assert "Hello, Boston College!" in output

def test_addition():
    script_path = os.path.join(os.path.dirname(__file__), "../ps0.py")
    output = capture_script_output(script_path)
    assert "22" in output

# Additional tests
def test_output_order():
    script_path = os.path.join(os.path.dirname(__file__), "../ps0.py")
    output = capture_script_output(script_path)
    lines = output.split("\n")
    assert lines[0] == "Hello, Boston College!"
    assert lines[1] == "22"

def test_extra_output():
    script_path = os.path.join(os.path.dirname(__file__), "../ps0.py")
    output = capture_script_output(script_path)
    lines = output.split("\n")
    assert len(lines) == 3  # Ensure there are exactly two lines of outputimport pytest