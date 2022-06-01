def findLIS(arr):

	if not arr:
		return []

	# LIS[i] menyimpan panjang LIS dari sublist
	LIS = [[] for _ in range(len(arr))]
	# print(LIS)
	LIS[0].append(arr[0])
	# print(LIS)

	# Dimulai dari elemen kedua dari list
	for i in range(1, len(arr)):

		# Lakukan untuk tiap elemen di sublist arr[0..i-1]
		for j in range(i):

			# Mencari LIS dari iterator j dengan syarat nilai pada arr[j] kurang dari arr[i] 
			if arr[j] < arr[i] and len(LIS[j]) > len(LIS[i]):
				LIS[i] = LIS[j].copy()
				print(LIS)

		# Tambahkan nilai pada arr[i] di array LIS[i]
		LIS[i].append(arr[i])

	# membandingkan panjang LIS pada index j dan index i
	j = 0
	for i in range(len(arr)):
		if len(LIS[j]) < len(LIS[i]):
			j = i

	panjangLIS = LIS[j]
	print(panjangLIS)
	print(len(panjangLIS))


if __name__ == '__main__':

	arr = [4, 1, 13, 7, 0, 2, 8, 11, 3]
	findLIS(arr)

