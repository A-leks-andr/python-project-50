def search_diff(value1, value2):  # noqa: C901
    def inner(value1=None, value2=None):  # noqa: C901
        diff_dict = {}
        if not value1 or not isinstance(value1, dict):
            value1 = {}
        if not value2 or not isinstance(value2, dict):
            value2 = {}
        all_keys = sorted(list(value1.keys() | value2.keys()))
        for k in all_keys:
            if k in value1 and k in value2:
                if value1[k] == value2[k] and (
                    not isinstance(value1[k], dict)
                    and not isinstance(value2[k], dict)
                ):
                    diff_dict[f"  {k}"] = value1[k]
                elif value1[k] == value2[k] and (
                    isinstance(value1[k], dict) or isinstance(value2, dict)
                ):
                    if f"  {k}" not in diff_dict:
                        diff_dict[f"  {k}"] = {}
                    diff_dict[f"  {k}"] = inner(value1[k], value2[k])
                elif value1[k] != value2[k] and (
                    not isinstance(value1[k], dict)
                    and not isinstance(value2[k], dict)
                ):
                    diff_dict[f"- {k}"] = value1[k]
                    diff_dict[f"+ {k}"] = value2[k]
                elif value1[k] != value2[k] and (
                    isinstance(value1[k], dict) and isinstance(value2[k], dict)
                ):
                    if f"  {k}" not in diff_dict:
                        diff_dict[f"  {k}"] = {}
                    diff_dict[f"  {k}"].update(inner(value1[k], value2[k]))
                elif value1[k] != value2[k] and (
                    isinstance(value1[k], dict)
                    and not isinstance(value2[k], dict)
                ):
                    if f"- {k}" not in diff_dict:
                        diff_dict[f"- {k}"] = {}
                    diff_dict[f"- {k}"].update(inner(value1[k], None))
                    diff_dict[f"+ {k}"] = value2[k]
                elif value1[k] != value2[k] and (
                    not isinstance(value1[k], dict)
                    and isinstance(value2[k], dict)
                ):
                    diff_dict[f"- {k}"] = value1[k]
                    if f"+ {k}" not in diff_dict:
                        diff_dict[f"+ {k}"] = {}
                    diff_dict[f"+ {k}"].update(inner(None, value1[k]))
            elif k in value1 and k not in value2:
                if isinstance(value1[k], dict):
                    diff_dict[f"  {k}"] = inner(value1[k], None)
                else:
                    diff_dict[f"- {k}"] = value1[k]
            elif k not in value1 and k in value2:
                if isinstance(value2[k], dict):
                    diff_dict[f"  {k}"] = inner(None, value2[k])
                else:
                    diff_dict[f"+ {k}"] = value2[k]
        return diff_dict

    return inner(value1, value2)
