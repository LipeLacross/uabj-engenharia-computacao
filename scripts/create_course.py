#!/usr/bin/env python3
from pathlib import Path
import re
import sys
import unicodedata

def slugify(text):
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return re.sub(r"-+", "-", text).strip("-")

if len(sys.argv) < 3:
    print("Uso: python create_course.py <periodo> <nome da disciplina>")
    sys.exit(1)

periodo = sys.argv[1]
nome = " ".join(sys.argv[2:])
curso_dir = Path("periodos") / periodo / slugify(nome)
curso_dir.mkdir(parents=True, exist_ok=True)

for pasta in ["resumos", "materiais", "listas-e-exercicios", "provas-e-avaliacoes", "projetos"]:
    p = curso_dir / pasta
    p.mkdir(exist_ok=True)
    (p / ".gitkeep").write_text("", encoding="utf-8")

(curso_dir / "README.md").write_text(f"# {nome}\n", encoding="utf-8")
print(f"Criado: {curso_dir}")
