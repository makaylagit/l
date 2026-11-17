import time
import tracemalloc
import pandas as pd
from src.algorithms.bucket_sort import standard_bucket_sort, log_adaptive_bucket_sort

def profile_algorithm(func, data):
    tracemalloc.start()
    start_time = time.perf_counter()
    
    result = func(data)
    
    elapsed = (time.perf_counter() - start_time) * 1000  # ms
    _, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    return elapsed, peak_mem / 1024  # ms, KB

def run_suite(csv_path="data/raw/vgsales.csv"):
    if not pd.io.common.file_exists(csv_path):
        print(f"Dataset not found at {csv_path}. Please place vgsales.csv to run benchmarks.")
        return
        
    df = pd.read_csv(csv_path)
    sales = df["Global_Sales"].dropna().tolist()
    
    sizes = [500, 1000, 5000, 10000, len(sales)]
    records = []

    for size in sizes:
        subset = sales[:size]
        for name, algo in [
            ("Standard Bucket Sort", standard_bucket_sort),
            ("Log-Adaptive Bucket Sort", log_adaptive_bucket_sort),
            ("Python Timsort (sorted)", sorted),
        ]:
            ms, kb = profile_algorithm(algo, subset)
            records.append({
                "Dataset_Size": size,
                "Algorithm": name,
                "Time_ms": round(ms, 4),
                "Peak_Memory_KB": round(kb, 2)
            })

    results_df = pd.DataFrame(records)
    results_df.to_csv("results/benchmark_metrics.csv", index=False)
    print(results_df.to_string(index=False))

if __name__ == "__main__":
    run_suite()
