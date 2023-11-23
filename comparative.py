def compare_files(file1_path, file2_path):
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        lines1 = file1.readlines()
        lines2 = file2.readlines()

        # Certificar-se de que ambas as listas tenham o mesmo comprimento
        min_length = min(len(lines1), len(lines2))
        lines1 = lines1[:min_length]
        lines2 = lines2[:min_length]

        # Comparar linha a linha
        different_lines = sum(1 for line1, line2 in zip(lines1, lines2) if line1 != line2)

    return different_lines

# Exemplo de uso:
file1_path = 'outputs.txt'
file2_path = 'saidas_trab2.txt'
result = compare_files(file1_path, file2_path)

print(f"Número de linhas diferentes entre {file1_path} e {file2_path}: {result}")
