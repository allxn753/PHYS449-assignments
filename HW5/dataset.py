import numpy as np
import pandas as pd
from tqdm import tqdm

L =  14 # Lattice size
num_T = 40  # Number of temperature values
N_samples_per_T = 2500  # So total ≈ 10,000
T_values = np.linspace(1.0, 3.5, num_T)
D = []

def metropolis_step(state, T, n_steps=1000):
    for _ in range(n_steps):
        i, j = np.random.randint(L), np.random.randint(L)
        s = state[i, j]
        nb = state[(i+1)%L, j] + state[(i-1)%L, j] + state[i, (j+1)%L] + state[i, (j-1)%L]
        dE = 2 * s * nb
        if dE <= 0 or np.random.rand() < np.exp(-dE / T):
            state[i, j] *= -1
    return state

print("Generating Ising dataset...")
for T in tqdm(T_values, desc="Temperatures"):
    for _ in tqdm(range(N_samples_per_T), leave=False, desc=f"Sampling T={T:.2f}"):
        state = np.random.choice([-1, 1], size=(L, L))
        state = metropolis_step(state, T, n_steps=2000)
        state = metropolis_step(state, T, n_steps=500)
        flat = state.flatten()
        label = "FM" if T < 2.269 else "PM"
        D.append(np.concatenate([flat, [T], [label]]))

columns = ["s" + str(i) for i in range(L*L)] + ["T", "label"]
df = pd.DataFrame(D, columns=columns)

df = df.sample(frac=1, random_state=42).reset_index(drop=True)
N = len(df)
train_N = int(0.8 * N)
train_df = df.iloc[:train_N]
val_df = df.iloc[train_N:]

train_df.to_csv("ising_train2.csv", index=False)
val_df.to_csv("ising_val2.csv", index=False)
print(f"Train and validation CSVs created: {train_N} train, {N-train_N} val, total {N} samples")