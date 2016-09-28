#coding=utf-8
# ELSEVIER에서 Scopus 정보 얻어오기

"""https://api.elsevier.com/content/abstract/citations
?pubmed_id= / &apiKey= / &httpAccept=application%2Fjson"""

import requests, json

def get_scopus_citation(pmid, apikey):
    """
    Get scopus citation overview of paper of input PMID.
    """
    url = "https://api.elsevier.com/content/abstract/citations?pubmed_id="\
        + pmid + "&apiKey=" + apikey + "&httpAccept=application%2Fjson"
    res_dict = json.loads(requests.get(url).text)
    return res_dict

if __name__ == "__main__":
    get_scopus_citation("22733444",
     "97181d71fab5186c8bdbb2cd176092ce")
