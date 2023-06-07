def exists_word(word, instance):
    list_1 = []

    for index in range(len(instance)):
        path_file = instance.search(index)["linhas_do_arquivo"]

        for i in range(len(path_file)):
            if word in path_file[i].lower():
                list_1.append({"linha": i + 1})

    processed_data = {
            "palavra": word,
            "arquivo": instance.search(index)["nome_do_arquivo"],
            "ocorrencias": list_1,
        }

    if len(list_1) == 0:
        return []
    return [processed_data]


def search_by_word(word, instance):
    list_1 = []

    for index in range(len(instance)):
        path_file = instance.search(index)["linhas_do_arquivo"]
        list_2 = []

        for i in range(len(path_file)):
            if word in path_file[i].lower():
                list_2.append({"linha": i + 1, "conteudo": path_file[i]})

        if len(list_2) > 0:
            list_1.append({
                "palavra": word,
                "arquivo": instance.search(index)["nome_do_arquivo"],
                "ocorrencias": list_2
            })
    return list_1
