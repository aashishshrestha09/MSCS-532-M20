from sorting_algorithms import merge_sort_algorithm, quick_sort_algorithm
from utils import dataset_utils, metrics_utils, plot_utils


def main():
    dataset_sizes = [500, 1000, 2000, 5000]
    dataset_types = ["Sorted", "Reverse", "Random"]

    for dtype in dataset_types:
        print(f"\nDataset Type: {dtype}")
        print(f"{'Size':<8} {'Algorithm':<12} {'Time (ms)':<12} {'Memory (KB)':<12}")
        print("=" * 60)

        results_time = {"Merge Sort": [], "Quick Sort": []}
        results_memory = {"Merge Sort": [], "Quick Sort": []}

        for size in dataset_sizes:
            if dtype == "Sorted":
                data = dataset_utils.generate_sorted_dataset(size)
            elif dtype == "Reverse":
                data = dataset_utils.generate_reverse_sorted_dataset(size)
            else:
                data = dataset_utils.generate_random_dataset(size)

            # Merge Sort
            time_ms, memory_kb = metrics_utils.measure_performance(
                merge_sort_algorithm.merge_sort, data
            )
            print(f"{size:<8} {'Merge Sort':<12} {time_ms:<12.2f} {memory_kb:<12.2f}")
            results_time["Merge Sort"].append(time_ms)
            results_memory["Merge Sort"].append(memory_kb)

            # Quick Sort
            time_ms, memory_kb = metrics_utils.measure_performance(
                quick_sort_algorithm.quick_sort, data
            )
            print(f"{size:<8} {'Quick Sort':<12} {time_ms:<12.2f} {memory_kb:<12.2f}")
            results_time["Quick Sort"].append(time_ms)
            results_memory["Quick Sort"].append(memory_kb)

        plot_utils.plot_performance(
            dataset_sizes,
            results_time,
            results_memory,
            title_suffix=f"({dtype} Data)",
            output_file=f"img/sorting_performance_{dtype.lower()}.png",
        )


if __name__ == "__main__":
    main()
