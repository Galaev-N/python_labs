import argparse
import os
from io_txt_csv import *


def main():
    parser = argparse.ArgumentParser(description="Обработка файлов")
    parser.add_argument("--in", dest="input_file", required=True)
    parser.add_argument("--out", dest="output_file", required=True)

    args = parser.parse_args()

    # Работа с файлами
    process_files(args.input_file, args.output_file)


def process_files(input_path, output_path):
    # Создаем папку для выходного файла, если её нет
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    try:
        all_text = read_text(input_path, encoding="utf-8")

        data = []
        for i in top_n(count_freq(tokenize(all_text)), 5):
            data.append(((f"{i[0]}"), (f"{i[1]}")))

        write_csv(data, output_path, ("word", "count"))

    except FileNotFoundError:
        print(f"Файл {input_path} не найден")

    except Exception as e:
        print(f"Ошибка при обработке файлов: {e}")


if __name__ == "__main__":
    main()
