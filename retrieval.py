def recuperar(query, fuentes):
    return [
        f for f in fuentes
        if query.lower() in f["texto"].lower()
    ]

if __name__ == "__main__":
    datos = [
        {"texto": "RAG usa fuentes externas"},
        {"texto": "Backend y APIs"}
    ]
    print(recuperar("rag", datos))
