import os
import yaml

# Caminho do script, pq ele vai ficar em authors
authors_dir = os.path.join(os.path.dirname(__file__))


def update_weights():
    # Lista os arquivos
    authors = [f for f in os.listdir(authors_dir) if f.endswith('_index.md')]
    # Ordena os arquivos alfabeticamente
    authors.sort()

    # Atualiza os pesos nos arquivos _index.md
    for weight, author_file in enumerate(authors, start=1):
        index_file = os.path.join(authors_dir, author_file)

        if os.path.exists(index_file):
            with open(index_file, 'r', encoding='utf-8') as file:
                content = next(yaml.safe_load_all(file), None)

            if content is not None:
                content['weight'] = weight

                with open(index_file, 'w', encoding='utf-8') as file:
                    yaml.dump(content, file, default_flow_style=False, allow_unicode=True)

                print(f"Atualizado: {author_file} -> peso: {weight}")
            else:
                raise FileNotFoundError(f"Conteúdo não encontrado no arquivo: {index_file}")
        else:
            raise FileNotFoundError(f"Arquivo não encontrado: {index_file}")


if __name__ == "__main__":
    update_weights()
