import math

data = {
	'Manas Hira': {
		'Networking': 1.46,
		'Theory of Computation': 5.0,
		'Software engineering': 3.34,
		'DBMS': 2.32
	},

	'Jaya Sil': {
		'Networking': 5.0,
		'Theory of Computation': 2.54,
		'Machine Learning': 4.32,
		'Algorithms': 2.76
	},

	'Abhik Mukherjee': {
		'Networking': 5.0,
		'Operating Systems': 4.72,
		'Theory of Computation': 3.25,
		'Compiler Design': 3.61,
		'Microprocessor': 3.58,
		'Machine Learning': 3.23,
		'Algorithms': 3.03
	},

	'Ashish Kumar Layek': {
		'Operating Systems': 4.34,
		'Theory of Computation': 4.52,
		'Software engineering': 4.04,
		'Compiler Design': 3.97,
		'Microprocessor': 5.0,
		'Algorithms': 4.92
	},

	'Apurba Sarkar': {
		'Operating Systems': 4.33,
		'Theory of Computation': 3.57,
		'Machine Learning': 4.39,
		'Algorithms': 5.0
	},

	'Sulata Mitra': {
		'Operating Systems': 4.58,
		'Theory of Computation': 4.43,
		'Software engineering': 4.38,
		'Microprocessor': 2.42,
		'DBMS': 2.80
	},

	'Amit Kumar Das': {
		'Operating Systems': 4.24,
		'Theory of Computation': 2.17,
		'Compiler Design': 2.92,
		'Microprocessor': 5.0,
		'Machine Learning': 3.18,
		'Algorithms': 5.0
	},

	'Malay Kule': {
		'Operating Systems': 4.64,
		'Theory of Computation': 4.38,
		'Software engineering': 3.62,
		'Compiler Design': 4.88,
		'Microprocessor': 4.72,
		'Algorithms': 4.38
	},

	'Asit Kumar Das': {
		'Theory of Computation': 4.60,
		'Software engineering': 3.54,
		'Compiler Design': 4.28,
		'Microprocessor': 1.53,
		'DBMS': 5.0
	},

	'Susanta Chakraborty': {
		'Operating Systems': 3.45,
		'Theory of Computation': 5.0,
		'Software engineering': 4.83,
	},

	'Tamal Pal': {
		'Operating Systems': 4.23,
		'Theory of Computation': 4.22,
		'Software engineering': 4.74,
		'Microprocessor': 3.83,
		'Algorithms': 3.95
	},

	'Sipra Das Bit': {
		'Operating Systems': 5.0,
		'Theory of Computation': 1.66,
		'Compiler Design': 4.62,
		'Microprocessor': 3.94,
	},

	'Uma Bhattacharya': {
		'Operating Systems': 1.5,
		'Theory of Computation': 2.76,
		'Software engineering': 3.76,
		'Compiler Design': 5.0,
		'Microprocessor': 4.93,
		'Algorithms': 4.63
	},

	'Sekhar Kumar Mandal': {
		'Theory of Computation': 4.67,
		'Software engineering': 3.86,
		'Compiler Design': 4.14,
		'DBMS': 5.0,
	},
}

def euclidean_similarity(person1, person2):

	common_ranked_items = [itm for itm in data[person1] if itm in data[person2]]
	rankings = [(data[person1][itm], data[person2][itm]) for itm in common_ranked_items]
	distance = [pow(rank[0] - rank[1], 2) for rank in rankings]

	return 1 / (1 + sum(distance))

def pearson_similarity(person1, person2):

	common_ranked_items = [itm for itm in data[person1] if itm in data[person2]]

	n = len(common_ranked_items)

	s1 = sum([data[person1][item] for item in common_ranked_items])
	s2 = sum([data[person2][item] for item in common_ranked_items])

	ss1 = sum([pow(data[person1][item], 2) for item in common_ranked_items])
	ss2 = sum([pow(data[person2][item], 2) for item in common_ranked_items])

	ps = sum([data[person1][item] * data[person2][item] for item in common_ranked_items])

	num = n * ps - (s1 * s2)

	den = math.sqrt((n * ss1 - math.pow(s1, 2)) * (n * ss2 - math.pow(s2, 2)))

	return (num / den) if den != 0 else 0



def recommend(person, bound, similarity=pearson_similarity):
	scores = [(similarity(person, other), other) for other in data if other != person]

	scores.sort()
	scores.reverse()
	scores = scores[0:bound]

	print (scores)

	recomms = {}

	for sim, other in scores:
		ranked = data[other]

		for itm in ranked:
			if itm not in data[person]:
				weight = sim * ranked[itm]

				if itm in recomms:
					s, weights = recomms[itm]
					recomms[itm] = (s + sim, weights + [weight])
				else:
					recomms[itm] = (sim, [weight])

	for r in recomms:
		sim, item = recomms[r]
		recomms[r] = sum(item) / sim

	return recomms


print(recommend("Manas Hira", 5, euclidean_similarity))
print("--------------------------------------")
print(recommend("Manas Hira", 5, pearson_similarity))
