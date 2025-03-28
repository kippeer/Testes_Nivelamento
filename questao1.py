import os
import requests
from urllib.parse import urljoin
import zipfile
from bs4 import BeautifulSoup
import logging

# Configuração do logging
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def download_pdf(url, filename):
    """Baixar um arquivo PDF da URL fornecida"""
    try:
        logging.info(f"Iniciando o download de {filename}...")
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        logging.info(f"Download concluído: {filename}")
        return True
    except Exception as e:
        logging.error(f"Erro ao baixar {filename}: {e}")
        return False

def create_zip(pdf_files, zip_filename):
    """Criar um arquivo ZIP contendo os PDFs baixados"""
    try:
        logging.info(f"Criando arquivo ZIP: {zip_filename}...")
        with zipfile.ZipFile(zip_filename, 'w') as zipf:
            for pdf_file in pdf_files:
                if os.path.exists(pdf_file):
                    zipf.write(pdf_file, os.path.basename(pdf_file))
        logging.info(f"Arquivo ZIP criado com sucesso: {zip_filename}")
        return True
    except Exception as e:
        logging.error(f"Erro ao criar o arquivo ZIP: {e}")
        return False

def main():
    # URL da página da ANS
    url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

    try:
        # Obter o conteúdo da página
        logging.info(f"Acessando a página: {url}")
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        # Encontrar links de PDF contendo "Anexo I" e "Anexo II"
        pdf_files = []
        logging.info("Procurando links de PDF...")
        for link in soup.find_all('a'):
            href = link.get('href', '')
            text = link.get_text().lower()
            
            if href.endswith('.pdf') and ('anexo i' in text or 'anexo ii' in text):
                pdf_url = urljoin(url, href)
                filename = os.path.basename(href)  # Baixar na mesma pasta sem subdiretórios
                
                logging.info(f"Preparando para baixar: {filename}")
                if download_pdf(pdf_url, filename):
                    pdf_files.append(filename)

        if pdf_files:
            # Criar arquivo ZIP
            zip_filename = 'anexos.zip'
            if create_zip(pdf_files, zip_filename):
                logging.info(f"\nArquivos baixados e compactados com sucesso para {zip_filename}")
                
                # Limpar os arquivos PDF individuais
                for pdf_file in pdf_files:
                    os.remove(pdf_file)
                    logging.info(f"Arquivo PDF removido: {pdf_file}")
            else:
                logging.error("Falha ao criar o arquivo ZIP")
        else:
            logging.warning("Nenhum arquivo PDF encontrado para Anexo I e Anexo II")

    except Exception as e:
        logging.error(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()
