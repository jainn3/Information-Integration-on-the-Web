import json
import ast

ignore_list = ['_type','_template','_cached_page_id']
final_list = []

with open('output.jl','w') as op:
	with open('input.jl','r') as ip:
		for line in ip:
			try:
				old_dic = ast.literal_eval(line)
			except Exception as e:
				print 'malformed',
				print line
				continue
			new_dic = dict()
			for key, value in old_dic.items():
				if key not in ignore_list:
					if key == 'url':
						if isinstance(value, list):
							new_dic['URL'] = value[0]
						else:
							new_dic['URL'] = value.strip()
					else:
						if isinstance(value, list):
							new_dic[key] = value[0].strip()
						else:
							new_dic[key] = value.strip()
			final_list.append(new_dic)
		json.dump(final_list, op)
		ip.close
	op.close