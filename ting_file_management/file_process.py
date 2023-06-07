from .file_management import txt_importer
import sys


def process(path_file, instance):
    processed_data = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(txt_importer(path_file)),
            "linhas_do_arquivo": txt_importer(path_file)
        }

    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return []

    instance.enqueue(processed_data)
    sys.stdout.write(str(processed_data))


def remove(instance):
    if instance.__len__() == 0:
        sys.stdout.write("Não há elementos\n")
    else:
        path_file = instance.dequeue()["nome_do_arquivo"]
        sys.stdout.write(f"Arquivo {path_file} removido com sucesso\n")


def file_metadata(instance, position):
    try:
        file = instance.search(position)
        sys.stdout.write(str(file))
    except IndexError:
        sys.stderr.write(str("Posição inválida"))
