# NumPy Functions & Matrix Operations

This repository contains my **NumPy learning notebook**, implemented in **Google Colab** and pushed to GitHub.  
This notebook covers **NumPy fundamentals and matrix operations**, which are **essential for Machine Learning, Artificial Intelligence, and Data Science**, including data preprocessing, vectorization, and linear algebra operations.

---

## Topics Covered

### 1. Array Creation & Random Generation
- `np.arange(1, 10, 2)`
- `np.linspace(start, end, num)`
- `np.ones()`
- `np.zeros()`
- `np.eye()`
- `np.random.rand(depth, rows, columns)`
- `np.random.randn(depth, rows, columns)`
- `np.random.randint(start, end, size)`
- `np.random.seed(42)`

---

### 2. Array Shape & Reshaping
- `array.shape`
- `array.reshape(4, 5)`
- `np.expand_dims(arr, axis=1)`
- `np.squeeze(arr)`

---

### 3. Arithmetic & Mathematical Operations
- Element-wise operations:
  - `array * array`
  - `array + 1`
  - `array * 2`
  - `array ** 2`
  - `array - 2`
- Universal functions:
  - `np.sqrt(array)`
  - `np.log(array)`
  - `np.sin(array)`
  - `np.round(array, decimals=3)`
- Aggregations:
  - `np.max(array)`
  - `np.min(array)`
  - `np.argmax(array)`
  - `np.argmin(array)`

---

### 4. Indexing, Slicing & Boolean Masking
- Indexing:
  - `array[4]`
  - `array[[0, 5, 8]]`
  - `array[0:5]`
- Assignment:
  - `array[1] = 4`
  - `array[3:7] = 400`
- 2D Indexing:
  - `array2D[:, [2, 4]]`
  - `array2D[[1, 3], [2, 4]]`
- Boolean logic:
  - `array < 5`
  - `array[array < 5]`

---

### 5. Axis-Based Statistics (CRITICAL)
- `np.sum(arr, axis=0)`
- `np.mean(arr, axis=0)`
- `np.median(arr, axis=0)`
- `np.std(arr, axis=0)`
- `np.var(arr, axis=0)`
- `np.min(arr, axis=0)`
- `np.max(arr, axis=0)`

---

### 6. Matrix Operations & Linear Algebra (CORE)
- `np.dot(A, B)`
- `A @ B`
- `A.T`
- `np.transpose(A)`
- `np.linalg.inv(A)`
- `np.linalg.det(A)`
- `np.linalg.eig(A)`
- `np.linalg.svd(A)`
- `np.linalg.solve(A, b)`
- `np.linalg.norm(A)`

---

### 7. Broadcasting Rules
- `X + 1`
- `X * np.array([1, 2, 3])`

---

### 8. Boolean Logic & Conditions
- `np.where(condition, x, y)`
- `np.any(arr)`
- `np.all(arr)`

---

### 9. Missing Values Handling
- `np.nan`
- `np.isnan(arr)`
- `np.nanmean(arr)`
- `np.nanstd(arr)`
- `np.nanmin(arr)`
- `np.nanmax(arr)`

---

### 10. Sorting & Ranking
- `np.sort(arr)`
- `np.argsort(arr)`
- `np.unique(arr)`
- `np.unique(arr, return_counts=True)`

---

### 11. Stacking, Splitting & Reshaping
- `np.concatenate((a, b), axis=0)`
- `np.vstack((a, b))`
- `np.hstack((a, b))`
- `np.split(arr, 3)`

---

### 12. Type Conversion & Memory Safety
- `arr.astype(float)`
- `arr.astype(int)`
- `arr.copy()`

---

### 13. Saving & Loading Data
- `np.save()`
- `np.savetxt()`
- `np.load()`
- `np.savez()`

---

### 14, Advanced Utility Functions
- `np.clip(arr, min, max)`
- `np.percentile(arr, 25)`
- `np.cumsum(arr)`
- `np.diff(arr)`
- `np.take(arr, indices)`
- `np.take_along_axis(arr, indices, axis)`

---

---

## Tools Used
- Python
- NumPy
- Google Colab
- Git & GitHub
