'''
https://www.ssa.gov/oact/babynames/limits.html 에서 National data를 다운로드하여 makemore/names 디렉토리에 저장한 후, 
이 스크립트를 실행하여 2000년 이후의 이름 데이터를 names.txt 파일로 생성하였음
파일 사이즈로 인해 github에는 업로드하지 않았음
'''


import csv
from pathlib import Path
 
BASE_DIR = Path(__file__).resolve().parent
NAMES_DIR = BASE_DIR / "names"
OUTPUT_FILE = BASE_DIR / "names.txt"


def create_names_file() -> int:
    names = list()
    source_files = sorted(
        source_file
        for source_file in NAMES_DIR.glob("yob*.txt")
        if source_file.stem.removeprefix("yob").isdigit()
        and int(source_file.stem.removeprefix("yob")) >= 2000
    )

    if not source_files:
        raise FileNotFoundError(f"이름 데이터 파일을 찾을 수 없습니다: {NAMES_DIR}")

    for source_file in source_files:
        with source_file.open(encoding="utf-8", newline="") as file:
            for row in csv.reader(file):
                if row and row[0].strip():
                    names.append(row[0].strip().lower())

    sorted_names = sorted(names)
    OUTPUT_FILE.write_text("\n".join(sorted_names) + "\n", encoding="utf-8")
    return len(sorted_names)


if __name__ == "__main__":
    name_count = create_names_file()
    print(f"완료: 총 {name_count}개의 고유한 이름이 {OUTPUT_FILE}에 저장되었습니다.")