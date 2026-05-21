import pandas as pd
from utils import clean_demand_per_group, extend_promotions_days, merge, read_demand, read_promotions


def test_extend_promotions(promotion_path):
    p = read_promotions(promotion_path)
    n_days = 7
    ext_p = extend_promotions_days(p, n_days)
    durations = ext_p.groupby("promotion_id").apply(lambda df: (df.index.max() - df.index.min()).days ) + 1
    assert (durations == n_days).all()
    first_promotion_date = ext_p.reset_index().groupby('promotion_id').first().set_index("promotion_date")
    pd.testing.assert_frame_equal(p, first_promotion_date)

def test_read_demand(demand_path):
    d = read_demand(demand_path)
    assert len(d) > 0
    assert d.columns.tolist() == ["demand", "sku", "supermarket"]

def test_clean_demand_no_null(demand_path):
    d = read_demand(demand_path)
    d = clean_demand_per_group(d)
    assert d.demand.isnull().sum() == 0

def test_merge_contains_all_promotion_dates(demand_path, promotion_path):
    d = read_demand(demand_path)
    p = read_promotions(promotion_path)
    m = merge(d, p)
    assert p.index.isin(m.index).all()

def test_merge_has_promotions(demand_path, promotion_path):
    d = read_demand(demand_path)
    p = read_promotions(promotion_path)
    m = merge(d, p)
    assert m.promotion.sum() == len(p)

def run_tests():
    print("runs tests")
    demand_path = "demand.csv"
    promotion_path = "promotions.csv"
    test_read_demand(demand_path)
    test_clean_demand_no_null(demand_path)
    test_merge_contains_all_promotion_dates(demand_path, promotion_path)
    test_merge_has_promotions(demand_path, promotion_path)
    test_extend_promotions(promotion_path)
    print("finished tests")

if __name__ == "__main__":
    run_tests()