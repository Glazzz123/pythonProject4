from typing import List, Dict


def generate_payout_report(data: List[Dict[str, str]]) -> str:

    if not data:
        return "No data to report."

    headers = ["Name", "Department", "Hours", "Rate", "Payout"]
    rows = []

    for row in data:
        name = row["name"]
        dept = row["department"]
        hours = row["hours"]
        rate = row["rate"]
        # noinspection PyTypeChecker
        payout = rate * hours

        rows.append([
            name,
            dept,
            f"{hours:.2f}",
            f"{rate:.2f}",
            f"{payout:.2f}"
        ])

    col_widths = [
        max(len(str(header)), *(len(str(row[i])) for row in rows))
        for i, header in enumerate(headers)
    ]

    lines = []

    header_line = " | ".join(
        header.ljust(col_widths[i]) for i, header in enumerate(headers)
    )
    lines.append(header_line)
    lines.append("-" * len(header_line))

    for row in rows:
        lines.append(" | ".join(
            row[i].ljust(col_widths[i]) for i in range(len(headers))
        ))

    return "\n".join(lines)
