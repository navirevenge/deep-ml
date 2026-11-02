def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	index = 0
	summ = 0 
	array_output = []

	for a_list in a: 
		if len(a_list) != len(b):
			return -1
		else:
			for component in a_list:
				summ += component * b[index]
				index += 1
			array_output.append(summ)
			index = 0
			summ = 0
	
	return array_output
			

		
			
		



	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	pass