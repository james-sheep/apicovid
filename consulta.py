import requests

import pandas as pd


def busca_api(cidade):
    
    url = "https://elastic-leitos.saude.gov.br/leito_ocupacao/_search"
    payload = {"size": 500, "query": {"match": {"municipio": cidade}}}

    r = requests.post(url, auth=('user-api-leitos', 'aQbLL3ZStaTr38tj'), json=payload)
    a = r.json()

    lista_unidades = []
    lista_obito = []
    lista_respiradores = []
    lista_uti = []
    lista_ocupacao_uti = []
    lista_oferta_srga_cli = []
    lista_ocupacao_srga_cli = []
    lista_oferta_hosp_cli = []
    lista_data_ultima_notificao = []

    for n in a['hits'].values():

        if type(n) == list:

            for i in n:

                resumo = i["_source"]

                if "nomeCnes" in resumo:
                    obito = str(resumo["obitos"])
                    lista_obito.append(obito)

                    unidade = resumo["nomeCnes"]
                    lista_unidades.append(unidade)

                    respiradores = str(resumo["ofertaRespiradores"])
                    lista_respiradores.append(respiradores)

                    uti = str(resumo["ofertaHospUti"])
                    lista_uti.append(uti)

                    ocupacao_uti = str(resumo["ocupHospUti"])
                    lista_ocupacao_uti.append(ocupacao_uti)

                    ofertaSRAGCli = str(resumo["ofertaSRAGCli"])
                    lista_oferta_srga_cli.append(ofertaSRAGCli)

                    ocupSRAGCli = str(resumo["ocupSRAGCli"])
                    lista_ocupacao_srga_cli.append(ocupSRAGCli)

                    ofertaHospCli = str(resumo["ofertaHospCli"])
                    lista_oferta_hosp_cli.append(ofertaHospCli)

                    data_notificacao = str(resumo['dataNotificacaoOcupacao'])
                    lista_data_ultima_notificao.append(data_notificacao)

            
    return  {"Unidade": lista_unidades, "Obitos": lista_obito, "Qtd Respiradores": lista_respiradores,
             "Leitos UTI": lista_uti, "Ocupacao UTI": lista_ocupacao_uti,
             "Oferta Leitos Clinicos": lista_oferta_srga_cli, "Ocupacao Leitos Cli": lista_ocupacao_srga_cli,
             "Data da notificacao": lista_data_ultima_notificao}

    
    
