import matplotlib.pyplot as plt
import numpy as np

# Точні значення для Вашого Варіанту № 7[cite: 1]
n = 50
m_hat = -0.9490
var_hat = 12.4494
ss_val = 622.4700

# Обчислення функції ln L(m) під ваш варіант[cite: 1]
m_vals = np.linspace(-3.5, 1.5, 300)
ll_m = (
    -0.5 * n * np.log(2 * np.pi)
    - 0.5 * n * np.log(var_hat)
    - (ss_val + n * (m_vals - m_hat) ** 2) / (2 * var_hat)
)
max_ll = -0.5 * n * np.log(2 * np.pi) - 0.5 * n * np.log(var_hat) - 0.5 * n

# Стилізація як у методичці[cite: 3]
fig, ax = plt.subplots(figsize=(9, 4.5), dpi=150)

# Синя крива вашої функції правдоподібності
ax.plot(m_vals, ll_m, color="#1e557d", linewidth=2.5)

# Точка максимуму та вертикальна пунктирна лінія
ax.plot(m_hat, max_ll, marker="o", markersize=7, color="#ba5421")
ax.vlines(
    x=m_hat,
    ymin=ax.get_ylim()[0],
    ymax=max_ll,
    color="#ba5421",
    linestyle="--",
    linewidth=1.5,
)

# Стрілка з вашим значенням m̂ = -0.9490[cite: 1, 3]
ax.annotate(
    f"m̂ = {m_hat}",
    xy=(m_hat, max_ll),
    xytext=(m_hat + 0.5, max_ll - 8),
    color="#ba5421",
    fontsize=11,
    arrowprops=dict(
        arrowstyle="->", color="#ba5421", lw=1.2, mutation_scale=12
    ),
)

# Підписи осей для вашої лабораторної[cite: 3]
ax.set_xlabel("m", fontsize=11, fontstyle="italic")
ax.set_ylabel("ln L(m)", fontsize=11, fontstyle="italic")
ax.grid(True, color="#e1e8ed", linestyle="-", linewidth=0.8)

# Оформлення рамок[cite: 3]
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_color("#333333")
ax.spines["bottom"].set_color("#333333")

plt.tight_layout()
plt.savefig("variant7_likelihood_plot.png", dpi=300)
plt.show()