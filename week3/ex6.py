import numpy as np

scores = np.array([55, 62, 71, 48, 90, 77, 68, 82])
print("Original scores:", scores)

# TODO 1: Create 'curved' scores by adding 5 points to every score
curved = scores + 5

# TODO 2: Use np.clip to cap scores between 0 and 100 (just in case)
curved = np.clip(curved, 0, 100)

# TODO 3: Print original and curved summaries: mean, min, max, std
print("\nOriginal stats:")
print("  Mean:", np.mean(scores))
print("  Min:", np.min(scores))
print("  Max:", np.max(scores))
print("  Std dev:", np.std(scores))

print("\nCurved stats:")
print("  Mean:", np.mean(curved))
print("  Min:", np.min(curved))
print("  Max:", np.max(curved))
