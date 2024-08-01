# language-knowledge

install requirements
```
pip install -r requirements.txt
```

make a configs/secret.py
```
# GPT-4 API Key
OPENAI_API_KEY = "YOUR_KEY"

# GraphDB Endpoint
GRAPHDB_ENDPOINT = "YOUR_ENDPOINT"

DBPEDIA_SPARQL_ENDPOINT = "http://dbpedia.org/sparql"

```

to run the app on local
```
run.py
```

to test if your endpoints exist
```
curl http://127.0.0.1:5000/test
```

to generate a query
```
curl -X POST -H "Content-Type: application/json" -d '{"question": "Who is Albert Einstein?"}' http://127.0.0.1:5000/generate
```

to execture a query
```
curl -X POST -H "Content-Type: application/json" -d '{"question": "Who is Albert Einstein?"}' http://127.0.0.1:5000/execute
```

to use the query response to help answer the original question
```
curl -X POST -H "Content-Type: application/json" -d '{"question": "Who is Albert Einstein?"}' http://127.0.0.1:5000/answer
```


```
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX res: <http://dbpedia.org/resource/>

SELECT ?abstract
WHERE {
    res:Albert_Einstein dbo:abstract ?abstract .
    FILTER (lang(?abstract) = 'en') .
}

```