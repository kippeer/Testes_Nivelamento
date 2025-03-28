import csv
import zipfile
from pathlib import Path

def extract_table_from_pdf():
   # aplicação mock_data
    mock_data = [
        ["CÓDIGO", "PROCEDIMENTO", "OD", "AMB"],
        ["10101", "Consulta médica", "S", "S"],
        ["10102", "Exame laboratorial", "N", "S"],
    ]
    return mock_data

def transform_data(data):
    # Transformar as colunas OD e AMB
    od_map = {
        "S": "Segmentação Obrigatória",
        "N": "Segmentação Não Obrigatória"
    }
    
    amb_map = {
        "S": "Procedimento Ambulatorial",
        "N": "Procedimento Não Ambulatorial"
    }
    
    transformed_data = []
    for row in data:
        if row[0] == "CÓDIGO":  # Linha de cabeçalho
            transformed_data.append(row)
            continue
            
        transformed_row = row.copy()
        transformed_row[2] = od_map.get(row[2], row[2])
        transformed_row[3] = amb_map.get(row[3], row[3])
        transformed_data.append(transformed_row)
    
    return transformed_data

def save_to_csv(data, filename):
    # Salvar os dados no formato CSV
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(data)

def create_zip(csv_filename, zip_filename):
    # Criar arquivo ZIP contendo o CSV
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(csv_filename)

def main():
    # 1. Extrair dados do PDF
    data = extract_table_from_pdf()
    
    # 2. Transformar os dados
    transformed_data = transform_data(data)
    
    # 3. Salvar os dados em um arquivo CSV
    csv_filename = "procedimentos.csv"
    save_to_csv(transformed_data, csv_filename)
    
    # 4. Criar o arquivo ZIP
    zip_filename = "Teste_Mock.zip"
    create_zip(csv_filename, zip_filename)
    
    print(f"Process completed. Data saved to {zip_filename}")

if __name__ == "__main__":
    main()
