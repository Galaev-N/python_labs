from src.lab05.json_csv import *


def test_json_to_csv_roundtrip(tmp_path: Path):
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"
    data = [
        {"name": "Alice", "age": 22},
        {"name": "Bob", "age": 25},
    ]
    src.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    json_to_csv(str(src), str(dst))

    with dst.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    assert len(rows) == 2
    assert {"name", "age"} <= set(rows[0].keys())


def test_csv_to_json_roundtrip(tmp_path: Path):
    src = tmp_path / "test.csv"
    dst = tmp_path / "test.json"

    src.write_text("name,age\nAlice,22\nBob,25", encoding="utf-8")
    csv_to_json(str(src), str(dst))

    result = json.loads(dst.read_text(encoding="utf-8"))
    assert result == [{"name": "Alice", "age": "22"}, {"name": "Bob", "age": "25"}]


#   Бро придумывай кейсы сам upd: лень мне
#   и тд.... upd: НЕТ СИЛ МОИХ БОЛЬШЕ!
