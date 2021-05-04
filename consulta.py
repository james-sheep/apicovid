import requests


def busca_api(cidade):
        
    url = "https://elastic-leitos.saude.gov.br/leito_ocupacao/_search"
    payload = {"size": 500, "query": {"match": {"municipio": cidade}}}

    r = requests.post(url, auth=('user-api-leitos', 'aQbLL3ZStaTr38tj'), json=payload)
    a = r.json()

    lista_de_dict = []

    for n in a['hits'].values():

        if type(n) == list:

            for i in n:
                resumo = i["_source"]
                if "nomeCnes" in resumo:
                    lista_de_dict.append(resumo)

    return lista_de_dict
                    

                

               
    

                    