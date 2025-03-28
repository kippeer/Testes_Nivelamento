import csv
import zipfile
import pdfplumber
from pathlib import Path

# Função para extrair dados de uma tabela de um PDF
def extract_table_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        all_data = []
        # Itera sobre todas as páginas do PDF
        for page in pdf.pages:
            # Extrai a tabela da página
            table = page.extract_table()
            if table:
                all_data.extend(table)  # Adiciona a tabela extraída à lista de dados
        return all_data

def transform_data(data):
    # Transform OD e AMB
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
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(data)

def create_zip(csv_filename, zip_filename):
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(csv_filename)

def main():
    # 1. Defina o caminho do arquivo PDF
    pdf_path = "teste_procedimentos.pdf"  # Substitua com o caminho real do seu PDF

    # 2. Extração de dados do PDF
    data = extract_table_from_pdf(pdf_path)
    
    # 3. Transforme os dados
    transformed_data = transform_data(data)
    
    # 4. Salve os dados em um arquivo CSV
    csv_filename = "teste_procedimentos.csv"
    save_to_csv(transformed_data, csv_filename)
    
    # 5. Crie o arquivo ZIP
    zip_filename = "Teste_Dados_reais.zip"
    create_zip(csv_filename, zip_filename)
    
    print(f"Process completed. Data saved to {zip_filename}")

if __name__ == "__main__":
    main()
