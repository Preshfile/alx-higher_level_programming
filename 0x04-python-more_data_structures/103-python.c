def square_matrix_simple(matrix=[]i):
	new_list = matrix.copy()
	for i in range(len(matrix)):
		new_list[i] = list(map(lambda x: x**2, matrix[i]))
		return new_list
