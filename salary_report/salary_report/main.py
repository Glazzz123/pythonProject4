import argparse
import sys
from salary_report.parser import parse_files
from salary_report.reports import REPORTS


def main():
    parser = argparse.ArgumentParser(
        description="CSV-based employee report generator."
    )
    parser.add_argument(
        "--report",
        type=str,
        required=True,
        help="Name of the report (for example: payout)",
    )
    parser.add_argument(
        "files",
        nargs="+",
        help="Paths to one or more CSV files"
    )

    args = parser.parse_args()

    report_name = args.report.lower()
    if report_name not in REPORTS:
        print(f"  Unknown report: {report_name}", file=sys.stderr)
        print(f"Available reports: {', '.join(REPORTS)}", file=sys.stderr)
        sys.exit(1)

    try:
        employee_data = parse_files(args.files)
        report_fn = REPORTS[report_name]
        report_output = report_fn(employee_data)
        print(report_output)
    except Exception as e:
        print(f"🚨 Error: {e}", file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
