from flask import Flask, jsonify, request
from .gpt_service import generate_sparql_query, interpret_sparql_query
from .kg_service import fetch_from_graphdb
from api import app

@app.route('/generate', methods=['POST'])
def generate():

    # Generate SPARQL query
    question = request.json['question']

    # Execute SPARQL query
    sparql_query = generate_sparql_query(question)
    return jsonify({"sparql_query": sparql_query})

@app.route('/execute', methods=['POST'])
def exectute():
    question = request.json['question']

    # Generate SPARQL query
    sparql_query = generate_sparql_query(question)

    # Execute SPARQL query
    results = fetch_from_graphdb(sparql_query)

    return jsonify(results)

@app.route('/answer', methods=['POST'])
def answer():
    question = request.json['question']

    # Generate SPARQL query
    sparql_query = generate_sparql_query(question)

    # Execute SPARQL query
    results = fetch_from_graphdb(sparql_query)

    # Interpret SPARQL query
    answer = interpret_sparql_query(question, results)

    return jsonify(answer)

@app.route('/test', methods=['GET'])
def test_route():
    return "Test successful!"