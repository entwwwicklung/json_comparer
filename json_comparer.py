def comparer(first_json, second_json, response=''):
    """
        Well this is actually comparing two dicts instead of two json strings 
        so make sure to convert json to dict before calling comparer method

        e.g. When comparing two json strings:
        import json
        comparer(json.loads(json1), json.loads(json2))

        e.g. When just comparing two dicts:
        comparer(json1, json2)
    """
	for k, v in second_json.items():
		try:
			first_json[k]
		except KeyError:
			print("{}['{}'] --- Key missing in 1st JSON".format(response,k))
		if isinstance(v,list):
			for y in range(len(v)):
				try:
					first_json[k][y]
				except IndexError:
					print("{}['{}'][{}] --- Object is missing from list in 1st JSON".format(response,k,y))

	for k, v in first_json.items():
		try:
			if v != second_json[k]:
				if isinstance(v, (str, int)) or v == None:
					print("{}['{}'] --- Value is different".format(response,k))
				elif isinstance(v, dict):
					comparer(v, second_json[k], response=response+"['{}']".format(k))
				elif isinstance(v, list):
					for y in range(len(v)):
						try:
							comparer(v[y], second_json[k][y], response=response+"['{}'][{}]".format(k,y))
						except IndexError:
							print("{}['{}'][{}] --- Object is missing from list in 2nd JSON".format(response,k,y))
		except KeyError:
			print("{}['{}'] --- Key missing in 2nd JSON".format(response,k))
