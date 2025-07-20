from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from scholarly import scholarly, ProxyGenerator
from datetime import date

pg = ProxyGenerator()
pg.FreeProxies()
scholarly.use_proxy(pg)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/pesquisar")
def pesquisar(tema: str):
    hoje = date.today().strftime("%d/%m/%Y")
    search_query = scholarly.search_pubs(tema)
    resultados = []

    for i in range(5):
        try:
            artigo = next(search_query)
            titulo = artigo.get("bib", {}).get("title", "Sem título")
            autores = artigo.get("bib", {}).get("author", "Desconhecido")
            ano = artigo.get("bib", {}).get("pub_year", "Desconhecido")
            resumo = artigo.get("bib", {}).get("abstract", "Sem resumo")
            link = artigo.get("pub_url", "Sem link")

            autores_str = autores if isinstance(autores, str) else ", ".join(autores)
            abnt = f"{autores_str.upper()}. {titulo}. {ano}. Disponível em: {link}. Acesso em: {hoje}."

            resultados.append({
                "titulo": titulo,
                "autor(es)": autores_str,
                "ano": ano,
                "resumo": resumo,
                "link": link,
                "referencia_abnt": abnt
            })

        except StopIteration:
            break
        except Exception as e:
            resultados.append({"erro": str(e)})
            break

    return {"resultados": resultados}
