# KEPT: covers empty list edge case
def test_filter_empty_list() -> None:
    result = filter_by_max_item_id([], 2)
    assert result == []


# KEPT: ensures all items below max remain
def test_filter_all_below_max() -> None:
    interactions = [_make_log(1,1,1), _make_log(2,1,2)]
    result = filter_by_max_item_id(interactions, 5)
    assert len(result) == 2


# DISCARDED: duplicates boundary test
# def test_duplicate_boundary():
#     ...