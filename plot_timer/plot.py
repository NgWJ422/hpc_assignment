import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('timing_data3.csv')

plt.plot(df['Iteration'], df['CPU'], label='CPU-only', marker='o')
plt.plot(df['Iteration'], df['GPU'], label='GPU-only', marker='s')
plt.plot(df['Iteration'], df['Hybrid'], label='Hybrid', marker='^')

plt.xlabel('Iteration')
plt.ylabel('Execution Time (ms)')
plt.title('SYCL Kernel Benchmark - Execution Time per Iteration')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('execution_time_plot.png')
plt.show()
