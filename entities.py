# entities.py
import re
from typing import Optional

def normalize_text(text: str) -> str:
    t = text.lower()
    t = re.sub(r"[\n\t]+", " ", t)
    t = re.sub(r"[^a-z0-9- _.:/]+", " ", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t

def find_between_markers(text: str, marker_list) -> Optional[str]:
    for marker in marker_list:
        if marker in text:
            pattern = re.escape(marker) + r"\s+([a-z0-9-_.]+)"
            m = re.search(pattern, text)
            if m:
                return m.group(1)
    return None

def extract_instance_type(text: str, instance_patterns) -> Optional[str]:
    tokens = text.split()
    for tok in tokens:
        for pat in instance_patterns:
            if tok.startswith(pat):
                return tok
    for tok in tokens:
        if re.match(r"^[a-z0-9]+\.[a-z0-9]+$", tok):
            return tok
    return None

def extract_region_for_cloud(text: str, cloud: Optional[str], region_table) -> Optional[str]:
    if cloud and cloud in region_table:
        for r in region_table[cloud]:
            if r in text:
                return r
    for _, regions in region_table.items():
        for r in regions:
            if r in text:
                return r
    tokens = text.split()
    for tok in tokens:
        if re.match(r"[a-z]{2,}-[a-z]+-\d", tok):
            return tok
    return None

def safe_split_words(text: str):
    return text.split()
