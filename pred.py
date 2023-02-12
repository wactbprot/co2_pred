import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set_theme()
sns.set_context("poster")

def emission(year, m_e, c_e):
    return m_e * year + c_e

def reduction(year, m_n, c_r, eff):
    return  (m_n * c_r * year  + c_r) * (1 + year * eff)

start_year = 2024
end_year = 2050
N = end_year - start_year
year = np.linspace(start_year, end_year, N)

c_e = 38e9              # t ... CO2 Emmission start_year
m_e = 1e3               # t/a ... CO2 Zuwachs Emmission pro Jahr
E = emission(y, m_e, c_e)

c_r = 34e4              # t ... CO2 Reduktion pro Anlage start_year (Mamuth)
m_n = [1, 5, 10]        # n/a ... CO2 Reduktion durch Anzahl pro Jahr
eff = [0.1, 0.25, 0.5]  # 1/a ... CO2 Reduktion durch Effizienz pro Jahr

marker = ["o", "s", "v"]
color = ["tab:blue", "tab:orange", "tab:purple"]

for ce, e in enumerate(eff):
    for mm, m in enumerate(m_n):
        for i, y in enumerate(year):
            r = reduction(i, m, c_r, e)
            if i == 0:
                R = [r]
            else:
                R.append(R[i - 1 ] + r)
    
        label = "{} = {}, {} = {} in %".format("$\\frac{N}{a}$", m,"$\epsilon$", e*100)
        
        plt.plot(year, R/E * 100,
                 label=label,
                 color=color[ce],
                 marker=marker[mm],
                 markersize = 20,
                 linestyle = ':',
                 alpha=0.5)

## 10% Grenze
plt.axhline(y = 10, color = 'g', linestyle = '-', alpha=0.5)
plt.text(year[0], 10, "10% Grenze", size=50, color="g", alpha=0.5)

plt.ylim([0, 15])

plt.ylabel("Reduction in %")

plt.xlabel("Jahr")
plt.legend(ncol=3)

#plt.yscale("log")

plt.show()
