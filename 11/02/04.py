def build_query_string(params):
    result = ''
    for i in sorted(params):
        result += f'{i}={params[i]}&'
    return result[:-1]
