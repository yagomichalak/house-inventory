from typing import List, Dict

def group_item_dicts_by_cat(*dicts: List[Dict], category: str = 'category') -> Dict[str, List[str]]:
	""" Groups a list of dictionaries by item category.
	:param dicts: The list of dictionaries. """

	d = {}
	for dct in dicts:
		try:
			d[getattr(dct, category)].append(dct)
		except KeyError:
			d[getattr(dct, category)] = [dct]

	return d