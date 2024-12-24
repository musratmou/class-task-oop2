import numpy as np

score = np.array([85, 90, 78, 92, 88])

score = score.astype(float)

a_score = score.copy()
a_score += 5

print("Original Score:", score)
print("Modified Score (a_score):", a_score)

print("Shape:", score.shape)
print("Number of Dimensions (ndim):", score.ndim)
print("Size:", score.size)
print("Itemsize:", score.itemsize)
print("Data Type (dtype):", score.dtype)

sorted_score = np.sort(score)
print("Sorted Score:", sorted_score)

indices_80_plus = np.where(score >= 80)
print("Indices of scores >= 80:", indices_80_plus)

print("Min:", np.min(score))
print("Max:", np.max(score))
print("Standard Deviation:", np.std(score))
print("Variance:", np.var(score))
print("Sum:", np.sum(score))
print("Mean:", np.mean(score))

print("Axis-wise Mean:", np.mean(score, axis=0))

print("Score [::2]:", score[::2])
print("Score [-3:-1]:", score[-3:-1])
print("Score [1:4]:", score[1:4])
