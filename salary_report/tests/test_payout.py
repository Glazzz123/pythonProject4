from salary_report.reports.payout import generate_payout_report


def test_generate_payout_report_format():
    data = [
        {"name": "Alice", "department": "Dev", "rate": 20.0, "hours": 160},
        {"name": "Bob", "department": "Sales", "rate": 15.0, "hours": 150},
    ]
    report = generate_payout_report(data)
    assert "Alice" in report
    assert "3200.00" in report
    assert "2250.00" in report
