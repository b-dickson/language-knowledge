from SPARQLWrapper import SPARQLWrapper, JSON
from config.secret import DBPEDIA_SPARQL_ENDPOINT

DBPEDIA_SPARQL_ENDPOINT = "http://dbpedia.org/sparql"

sparql = SPARQLWrapper(DBPEDIA_SPARQL_ENDPOINT)

def fetch_from_graphdb(sparql_query):
    sparql.setQuery(sparql_query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    return results