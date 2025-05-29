import matplotlib.pyplot as plt
import os


def plot_performance(
    dataset_sizes,
    results_time,
    results_memory,
    title_suffix="",
    output_file="sorting_performance.png",
):
    """Plot execution time and memory usage for sorting algorithms."""

    # Ensure the directory exists
    output_dir = os.path.dirname(output_file)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    plt.figure(figsize=(12, 5))

    # 📈 Execution Time Plot
    plt.subplot(1, 2, 1)
    plt.plot(dataset_sizes, results_time["Merge Sort"], marker="o", label="Merge Sort")
    plt.plot(dataset_sizes, results_time["Quick Sort"], marker="o", label="Quick Sort")
    plt.xlabel("Dataset Size")
    plt.ylabel("Execution Time (ms)")
    plt.title(f"Execution Time {title_suffix}")
    plt.legend()
    plt.grid(True)

    # 📊 Memory Usage Plot
    plt.subplot(1, 2, 2)
    plt.plot(
        dataset_sizes, results_memory["Merge Sort"], marker="o", label="Merge Sort"
    )
    plt.plot(
        dataset_sizes, results_memory["Quick Sort"], marker="o", label="Quick Sort"
    )
    plt.xlabel("Dataset Size")
    plt.ylabel("Memory Usage (KB)")
    plt.title(f"Memory Usage {title_suffix}")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.savefig(output_file)
    plt.show()
