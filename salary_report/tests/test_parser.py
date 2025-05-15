import pytest
from salary_report.parser import parse_csv_file, normalize_employee_data


def test_parse_csv_file(csv_file):
    file = csv_file("""
        name,department,hours,salary
        Alice,Dev,160,20
        Bob,Sales,150,15
    """)
    rows = parse_csv_file(str(file))
    assert len(rows) == 2
    assert rows[0]["name"] == "Alice"
    assert rows[1]["department"] == "Sales"


def test_normalize_employee_data():
    rows = [
        {"name": "John", "department": "QA", "rate": "30", "hours": "120"},
        {"name": "Lana", "department": "UX", "hourly_rate": "40", "hours": "100"},
        {"name": "Mike", "department": "Support", "salary": "25", "hours": "80"},
    ]
    normalized = normalize_employee_data(rows)
    assert normalized[0]["rate"] == 30.0
    assert normalized[1]["rate"] == 40.0
    assert normalized[2]["rate"] == 25.0
