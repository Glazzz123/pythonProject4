from typing import List, Dict

RATE_KEYS = {"rate", "hourly_rate", "salary"}


def parse_csv_file(file_path: str) -> List[Dict[str, str]]:

    with open(file_path, encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]
        if not lines:
            return []

        header = [h.strip().lower() for h in lines[0].split(",")]
        rows = []

        for line in lines[1:]:
            values = [v.strip() for v in line.split(",")]
            row = dict(zip(header, values))
            rows.append(row)

        return rows


def normalize_employee_data(rows: List[Dict[str, str]]) -> List[Dict[str, str]]:

    result = []

    for row in rows:
        normalized = {}
        rate_field = next((k for k in row if k.lower() in RATE_KEYS), None)
        if not rate_field:
            raise ValueError(f"Payment rate not found in the line: {row}")

        normalized["name"] = row.get("name", "").strip()
        normalized["department"] = row.get("department", "").strip()
        normalized["rate"] = float(row[rate_field])
        normalized["hours"] = float(row.get("hours", 0))

        result.append(normalized)

    return result


def parse_files(file_paths: List[str]) -> List[Dict[str, str]]:

    all_rows = []
    for path in file_paths:
        rows = parse_csv_file(path)
        normalized = normalize_employee_data(rows)
        all_rows.extend(normalized)

    return all_rows
