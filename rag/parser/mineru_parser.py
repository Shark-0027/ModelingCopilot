import subprocess
import os


def parse_pdf(pdf_path, output_dir):

    os.makedirs(output_dir, exist_ok=True)

    command = [
        "mineru",
        "-p",
        pdf_path,
        "-o",
        output_dir
    ]

    subprocess.run(command, check=True)

    print("MinerU 解析完成")