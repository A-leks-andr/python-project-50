from gendiff.data import read_data


def miks_dict(file1, file2):
    diff_dict = {}
    data1 = read_data(file1)
    data2 = read_data(file2)
    def inner(data1=None, data2=None):
        if not data1:
            data1 = {}
        if not data2:
            data2 = {}
        all_keys = sorted(list(data1.keys() | data2.keys()))
        for k in all_keys:
            if k in data1 and k in data2:
                if data1[k] == data2[k] and (not isinstance(data1[k], dict)
                                        and not isinstance(data2[k], dict)):
                    diff_dict[f'  {k}'] = data1[k]
                elif data1[k] == data2[k] and (isinstance(data1[k], dict)
                                        or isinstance(data2, dict)):
                    if f'  {k}' not in diff_dict:
                        diff_dict[f'  {k}'] = {}
                    diff_dict[f'  {k}'] = inner(data1[k], data2[k])
                elif data1[k] != data2[k] and (not isinstance(data1[k], dict)
                                        and not isinstance(data2[k], dict)):
                    diff_dict[f'- {k}'] = data1[k]
                    diff_dict[f'+ {k}'] = data2[k]
                elif data1[k] != data2[k] and (isinstance(data1[k], dict)
                                        or isinstance(data2, dict)):
                    if f'- {k}' not in diff_dict:
                        diff_dict[f'- {k}'] = {}
                    diff_dict[f'- {k}'].update(inner(data1[k], data2[k]))
            elif k in data1 and k not in data2:
                if isinstance(data1[k], dict):
                    diff_dict[f'- {k}'] = inner(data1[k], None)
                else:
                    diff_dict[f'- {k}'] = data1[k]
            elif k not in data1 and k in data2:
                if isinstance(data2[k], dict):
                    diff_dict[f'+ {k}'] = inner(None, data2[k])
                else:
                    diff_dict[f'+ {k}'] = data2[k]
        return diff_dict

    inner(data1, data2)
    return diff_dict


print(6, miks_dict('tests/test_data/file5.json', 
                   'tests/test_data/file6.json'))