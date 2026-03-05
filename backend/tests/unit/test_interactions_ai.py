from backend.app.routers.interactions import filter_by_max_item_id
from backend.tests.unit.test_interactions import _make_log


# KEPT: covers the edge case when the input list is empty
def test_filter_returns_empty_list_when_no_interactions() -> None:
    interactions = []
    result = filter_by_max_item_id(interactions=interactions, max_item_id=5)
    assert result == []


# KEPT: ensures interactions with item_id greater than max_item_id are removed
def test_filter_excludes_items_above_max() -> None:
    interactions = [
        _make_log(1, 1, 1),
        _make_log(2, 1, 5),
        _make_log(3, 1, 10),
    ]

    result = filter_by_max_item_id(interactions=interactions, max_item_id=5)

    assert len(result) == 2
    assert all(i.item_id <= 5 for i in result)


# KEPT: verifies behavior when all interactions are above the threshold
def test_filter_returns_empty_when_all_items_exceed_max() -> None:
    interactions = [
        _make_log(1, 1, 6),
        _make_log(2, 1, 7),
    ]

    result = filter_by_max_item_id(interactions=interactions, max_item_id=5)

    assert result == []


# FIXED: original generated test used incorrect expected count
def test_filter_keeps_items_below_max() -> None:
    interactions = [
        _make_log(1, 1, 1),
        _make_log(2, 1, 2),
        _make_log(3, 1, 3),
    ]

    result = filter_by_max_item_id(interactions=interactions, max_item_id=3)

    assert len(result) == 3
    assert result[0].id == 1
    assert result[1].id == 2
    assert result[2].id == 3


# DISCARDED: duplicates the boundary test already present in test_interactions.py
# def test_filter_boundary_duplicate() -> None:
#     interactions = [_make_log(1, 1, 2)]
#     result = filter_by_max_item_id(interactions=interactions, max_item_id=2)
#     assert len(result) == 1