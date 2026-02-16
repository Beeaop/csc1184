import numpy as np

# TODO 1: Set a random seed so results are repeatable (pick any integer)
np.random.seed(69)

# TODO 2: Simulate 1000 exam scores between 40 and 100
# Hint: np.random.random(1000) gives values between 0 and 1
# You can then scale and shift them: 40 + 60 * np.random.random(1000)
sim_scores = 40 + 60 * np.random.random(1000)

print("First 10 simulated scores:", sim_scores[:10])

# TODO 3: Compute and print mean and standard deviation
mean = np.mean(sim_scores)
std = np.std(sim_scores)
print("Mean:", round(mean, 2))
print("Std dev:", round(std, 2))

# TODO 4: What percentage of students score at least 60?
mask = sim_scores >= 60
fraction_passing = np.sum(mask) / len(sim_scores) * 100
print("Percentage with score >= 60:", round(fraction_passing, 1), "%")
