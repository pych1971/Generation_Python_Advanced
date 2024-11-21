def merge(values):  # values - это список словарей
    new_dict = dict()
    for i in values:
        for j in i.keys():
            new_dict[j] = new_dict.get(j, set())
            new_dict[j].add(i[j])
    return new_dict
