from scholarly import scholarly

def buscar_artigo_google_scholar(tema):
    print(f"\n🔎 Buscando artigo sobre: {tema}...\n")

    resultados = scholarly.search_pubs(tema)
    try:
        artigo = next(resultados)

        titulo = artigo['bib'].get('title', 'Sem título')
        autores = artigo['bib'].get('author', 'Autores não identificados')
        ano = artigo['bib'].get('pub_year', 'Ano não informado')
        resumo = artigo['bib'].get('abstract', 'Resumo não disponível')
        link = artigo.get('pub_url', 'Link não disponível')

        print(f"📄 Título: {titulo}")
        print(f"👥 Autores: {autores}")
        print(f"📅 Ano: {ano}")
        print(f"🔗 Link: {link}")
        print(f"\n📝 Resumo: {resumo}")

    except StopIteration:
        print("❌ Nenhum artigo encontrado.")

if __name__ == "__main__":
    tema = input("Digite o tema da pesquisa: ")
    buscar_artigo_google_scholar(tema)
