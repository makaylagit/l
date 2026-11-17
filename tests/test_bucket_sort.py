import pytest
from src.algorithms.bucket_sort import standard_bucket_sort, log_adaptive_bucket_sort

@pytest.mark.parametrize("sort_fn", [standard_bucket_sort, log_adaptive_bucket_sort])
def test_sorting_correctness(sort_fn):
    sample_sales = [82.74, 0.01, 40.24, 15.32, 0.01, 3.14, 0.0]
    assert sort_fn(sample_sales) == sorted(sample_sales)

@pytest.mark.parametrize("sort_fn", [standard_bucket_sort, log_adaptive_bucket_sort])
def test_edge_cases(sort_fn):
    assert sort_fn([]) == []
    assert sort_fn([5.0]) == [5.0]
    assert sort_fn([2.5, 2.5, 2.5]) == [2.5, 2.5, 2.5]
