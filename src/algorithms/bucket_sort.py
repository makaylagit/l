import math
from typing import List

def standard_bucket_sort(arr: List[float], num_buckets: int = None) -> List[float]:
    n = len(arr)
    if n <= 1:
        return arr.copy()
    
    k = num_buckets if num_buckets else n
    min_val, max_val = min(arr), max(arr)
    val_range = max_val - min_val
    
    if val_range == 0:
        return arr.copy()
        
    buckets = [[] for _ in range(k)]
    for val in arr:
        normalized = (val - min_val) / (val_range + 1e-9)
        idx = min(int(k * normalized), k - 1)
        buckets[idx].append(val)
        
    sorted_arr = []
    for bucket in buckets:
        for i in range(1, len(bucket)):
            key = bucket[i]
            j = i - 1
            while j >= 0 and bucket[j] > key:
                bucket[j + 1] = bucket[j]
                j -= 1
            bucket[j + 1] = key
        sorted_arr.extend(bucket)
        
    return sorted_arr

def log_adaptive_bucket_sort(arr: List[float], num_buckets: int = None) -> List[float]:
    n = len(arr)
    if n <= 1:
        return arr.copy()
        
    k = num_buckets if num_buckets else n
    log_vals = [math.log1p(x) for x in arr]
    min_log, max_log = min(log_vals), max(log_vals)
    log_range = max_log - min_log
    
    if log_range == 0:
        return arr.copy()
        
    buckets = [[] for _ in range(k)]
    for orig_val, l_val in zip(arr, log_vals):
        normalized = (l_val - min_log) / (log_range + 1e-9)
        idx = min(int(k * normalized), k - 1)
        buckets[idx].append(orig_val)
        
    sorted_arr = []
    for bucket in buckets:
        bucket.sort()
        sorted_arr.extend(bucket)
        
    return sorted_arr
