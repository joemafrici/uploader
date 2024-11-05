import re
from pathlib import Path
import unicodedata

def sanitize_filename(filename: str) -> str:
    """
    Sanitize filename
    :param filename:
    :return:
    """
    filename = unicodedata.normalize("NFKD", filename)

    # remove any directory components
    filename = Path(filename).name

    # remove non-ASCII, and some special characters, convert spaces to underscore
    filename = re.sub(r"[^\x00-\x7F]+", "", filename)
    filename = re.sub(r"\s+", "_", filename)
    filename = re.sub(r"[^\w.-]", "", filename)

    filename = filename.lstrip(".")

    if not filename:
        filename = "unnamed_file"

    return filename
