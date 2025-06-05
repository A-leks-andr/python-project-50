import json

def search_diff(value1, value2):
	result = {}
	all_keys = sorted(list(value1.keys() | value2.keys()))
	for key in all_keys:
		if key in value1 and key not in value2:
			result[f'- {key}'] = value1.get(key)
		elif key in value1 and key in value2:
			if value1[key] == value2[key]:
				result[f'  {key}'] = value1.get(key)
			else:
				result[f'- {key}'] = value1.get(key)
				result[f'+ {key}'] = value2.get(key)
		elif key not in value1 and key in value2:
			result[f'+ {key}'] = value2.get(key)
	return json.dumps(result, indent=4)