from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
from fuzzywuzzy import fuzz
import os

app = Flask(__name__)
CORS(app)

# Load the CSV data
csv_path = "Relatorio_cadop.csv"
df = pd.read_csv(csv_path, encoding='utf-8')

@app.route('/api/search', methods=['GET'])
def search_operators():
    query = request.args.get('q', '').lower()
    if not query:
        return jsonify([])
    
    # Search through multiple columns
    results = []
    for _, row in df.iterrows():
        # Calculate relevance score across multiple fields
        score = max(
            fuzz.partial_ratio(query, str(row['Razao_Social']).lower()),
            fuzz.partial_ratio(query, str(row['Nome_Fantasia']).lower()),
            fuzz.partial_ratio(query, str(row['Cidade']).lower()),
            fuzz.partial_ratio(query, str(row['Bairro']).lower()),
            fuzz.partial_ratio(query, str(row['Logradouro']).lower()),
            fuzz.partial_ratio(query, str(row['Representante']).lower())
        )
        
        if score > 60:  # Threshold for relevance
            results.append({
                'nome_operadora': row['Nome_Operadora'],
                'cnpj': row['CNPJ'],
                'razao_social': row['Razao_Social'],
                'nome_fantasia': row['Nome_Fantasia'],
                'modalidade': row['Modalidade'],
                'logradouro': row['Logradouro'],
                'numero': row['Numero'],
                'complemento': row['Complemento'],
                'bairro': row['Bairro'],
                'cidade': row['Cidade'],
                'uf': row['UF'],
                'cep': row['CEP'],
                'ddd': row['DDD'],
                'telefone': row['Telefone'],
                'fax': row['Fax'],
                'endereco_eletronico': row['Endereco_Eletronico'],
                'representante': row['Representante'],
                'cargo_representante': row['Cargo_Representante'],
                'regiao_de_comercializacao': row['Regiao_Comercializacao'],
                'data_registro_ans': row['Data_Registro_ANS'],
                'relevance_score': score
            })
    
    # Sort by relevance score and return top 10 results
    results.sort(key=lambda x: x['relevance_score'], reverse=True)
    return jsonify(results[:10])

if __name__ == '__main__':
    app.run(debug=True, port=5000)