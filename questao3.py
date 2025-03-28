import mysql.connector
import os
import csv
from datetime import datetime

# Função para conectar ao MySQL
def conectar_ao_mysql():
    try:
        conn = mysql.connector.connect(
            host="localhost",       # Altere para o host do seu banco
            user="root",            # Seu usuário do MySQL
            password="senha",       # Sua senha do MySQL
            database="seu_banco"    # Nome do banco de dados
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Erro ao conectar ao MySQL: {err}")
        return None

# Função para criar a tabela no banco de dados
def criar_tabela(conn):
    try:
        cursor = conn.cursor()
        query = """
        CREATE TABLE IF NOT EXISTS demonstrativos_contabeis (
            id INT AUTO_INCREMENT PRIMARY KEY,
            data DATE,
            reg_ans VARCHAR(255),
            cd_conta_contabil VARCHAR(255),
            descricao VARCHAR(255),
            vl_saldo_inicial DECIMAL(15,2) DEFAULT 0.00,
            vl_saldo_final DECIMAL(15,2) DEFAULT 0.00
        );
        """
        cursor.execute(query)
        conn.commit()
        print("Tabela criada com sucesso!")
    except mysql.connector.Error as err:
        print(f"Erro ao criar tabela: {err}")

# Função para importar dados de arquivos CSV para a tabela
def importar_csv_para_tabela(conn, pasta_csv):
    try:
        cursor = conn.cursor()
        arquivos_csv = [f for f in os.listdir(pasta_csv) if f.endswith('.csv')]

        for arquivo in arquivos_csv:
            if arquivo.startswith(('1T2023', '2T2023', '3T2023', '4T2023', '1T2024', '2T2024', '3T2024', '4T2024')):
                caminho_arquivo = os.path.join(pasta_csv, arquivo)
                with open(caminho_arquivo, 'r', encoding='utf-8') as f:
                    csv_reader = csv.reader(f, delimiter=',')
                    next(csv_reader)  # Pular o cabeçalho do CSV
                    for row in csv_reader:
                        query = """
                        INSERT INTO demonstrativos_contabeis (data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
                        VALUES (%s, %s, %s, %s, %s, %s);
                        """
                        cursor.execute(query, (row[0], row[1], row[2], row[3], row[4], row[5]))
                conn.commit()
                print(f"Dados do arquivo {arquivo} importados com sucesso!")
    except mysql.connector.Error as err:
        print(f"Erro ao importar dados: {err}")
    except Exception as e:
        print(f"Erro inesperado ao importar os dados: {e}")

# Função para criar a tabela de operadoras_ativas
def criar_tabela_operadoras(conn):
    try:
        cursor = conn.cursor()
        query = """
        CREATE TABLE IF NOT EXISTS operadoras_ativas (
            id_operadora INT PRIMARY KEY,
            nome_operadora VARCHAR(255),
            cnpj VARCHAR(14),
            status VARCHAR(50)
        );
        """
        cursor.execute(query)
        conn.commit()
        print("Tabela de operadoras criada com sucesso!")
    except mysql.connector.Error as err:
        print(f"Erro ao criar tabela de operadoras: {err}")

# Função para responder à primeira consulta (último trimestre)
def consultar_top_10_trimestre(conn):
    try:
        cursor = conn.cursor()
        query = """
        SELECT
            o.nome_operadora,
            SUM(d.vl_saldo_final) AS total_despesas
        FROM
            demonstrativos_contabeis d
        JOIN
            operadoras_ativas o ON d.reg_ans = o.cnpj
        WHERE
            d.descricao = "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MÉDICO HOSPITALAR"
            AND d.data >= CURDATE() - INTERVAL 3 MONTH
        GROUP BY
            o.nome_operadora
        ORDER BY
            total_despesas DESC
        LIMIT 10;
        """
        cursor.execute(query)
        resultados = cursor.fetchall()
        print("Top 10 Operadoras no Último Trimestre:")
        for row in resultados:
            print(f"{row[0]}: {row[1]:,.2f} de despesas")
    except mysql.connector.Error as err:
        print(f"Erro ao consultar o top 10 do trimestre: {err}")

# Função para responder à segunda consulta (último ano)
def consultar_top_10_ano(conn):
    try:
        cursor = conn.cursor()
        query = """
        SELECT
            o.nome_operadora,
            SUM(d.vl_saldo_final) AS total_despesas
        FROM
            demonstrativos_contabeis d
        JOIN
            operadoras_ativas o ON d.reg_ans = o.cnpj
        WHERE
            d.descricao = "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MÉDICO HOSPITALAR"
            AND d.data >= CURDATE() - INTERVAL 1 YEAR
        GROUP BY
            o.nome_operadora
        ORDER BY
            total_despesas DESC
        LIMIT 10;
        """
        cursor.execute(query)
        resultados = cursor.fetchall()
        print("Top 10 Operadoras no Último Ano:")
        for row in resultados:
            print(f"{row[0]}: {row[1]:,.2f} de despesas")
    except mysql.connector.Error as err:
        print(f"Erro ao consultar o top 10 do ano: {err}")

# Função principal para executar as consultas
def main():
    pasta_csv = r"C:\Users\fabio\OneDrive\Área de Trabalho\Testes_Nivelamento"
    conn = conectar_ao_mysql()
    if conn is None:
        print("Falha na conexão com o banco de dados. Abortando execução.")
        return

    criar_tabela(conn)
    criar_tabela_operadoras(conn)
    importar_csv_para_tabela(conn, pasta_csv)
    consultar_top_10_trimestre(conn)
    consultar_top_10_ano(conn)

    conn.close()

if __name__ == "__main__":
    main()
