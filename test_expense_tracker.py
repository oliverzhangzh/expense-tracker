from expense_tracker import total_by_category, total_by_month


def sample():
    return [
        {"date": "2026-10-03", "category": "food", "amount": 12.5, "note": ""},
        {"date": "2026-10-20", "category": "food", "amount": 7.5, "note": ""},
        {"date": "2026-11-02", "category": "books", "amount": 40.0, "note": ""},
    ]


def test_total_by_category():
    assert total_by_category(sample()) == {"food": 20.0, "books": 40.0}


def test_total_by_month():
    assert total_by_month(sample()) == {"2026-10": 20.0, "2026-11": 40.0}


def test_empty_list():
    assert total_by_category([]) == {}
