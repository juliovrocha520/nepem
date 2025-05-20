import os
import yaml

# Caminho do script, pq ele vai ficar em authors
authors_dir = os.path.join(os.path.dirname(__file__))


def update_weights():
    # Lista os diretórios
    authors = [d for d in os.listdir(authors_dir) if os.path.isdir(os.path.join(authors_dir, d))]

    # Ignora o diretório "admin"
    authors = [d for d in authors if d != "admin"]

    # Ordena os diretórios alfabeticamente
    authors.sort()

    # Atualiza os pesos nos arquivos _index.md
    for weight, author_dir in enumerate(authors, start=1):
        index_file = os.path.join(authors_dir, author_dir, '_index.md')

        if os.path.exists(index_file):
            with open(index_file, 'r', encoding='utf-8') as file:
                content = next(yaml.safe_load_all(file), None)

            if content is not None:
                content['weight'] = weight

                with open(index_file, 'w', encoding='utf-8') as file:
                    yaml.dump(content, file, default_flow_style=False, allow_unicode=True)

                print(f"Atualizado: {author_dir}/_index.md -> peso: {weight}")
            else:
                raise FileNotFoundError(f"Conteúdo não encontrado no arquivo: {index_file}")
        else:
            print(f"Aviso: Arquivo '_index.md' não encontrado no diretório: {author_dir}")


if __name__ == "__main__":
    update_weights()
