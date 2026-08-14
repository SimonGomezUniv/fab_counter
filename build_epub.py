from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parent
OUT_DIR = ROOT / "dist"
OUT_DIR.mkdir(exist_ok=True)
EPUB_PATH = OUT_DIR / "fab_life_counter.epub"


def build_epub():
    oebps = ROOT / "_epub"
    oebps.mkdir(exist_ok=True)

    meta = oebps / "META-INF"
    meta.mkdir(exist_ok=True)

    (oebps / "style.css").write_text(
        """
        @page {
            margin: 0.6in;
        }

        body {
            font-family: Georgia, "Times New Roman", serif;
            background: #f5f0e8;
            color: #111;
            margin: 0;
        }

        .page {
            width: 100%;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            padding: 0.5in 0.4in;
            box-sizing: border-box;
        }

        .title {
            text-align: center;
            font-size: 2.2em;
            font-weight: bold;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            margin-bottom: 0.3in;
        }

        .board {
            display: flex;
            flex-direction: column;
            gap: 0.5in;
        }

        .player {
            border: 3px solid #111;
            border-radius: 1.2rem;
            padding: 0.35in 0.3in;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 0.25in;
        }

        .name {
            font-size: 1.6em;
            letter-spacing: 0.12em;
            text-transform: uppercase;
            font-weight: bold;
        }

        .life {
            font-size: 6em;
            line-height: 1;
            font-weight: 700;
            letter-spacing: -0.08em;
        }

        .controls {
            display: flex;
            justify-content: space-between;
            width: 100%;
            font-size: 1.4em;
            font-weight: bold;
        }

        .controls span {
            display: inline-block;
            width: 32%;
            text-align: center;
            border: 2px solid #111;
            border-radius: 999px;
            padding: 0.12in 0.18in;
        }
        """,
        encoding="utf-8",
    )

    book_html = """<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <title>FAB Life Counter</title>
    <link rel="stylesheet" href="style.css" type="text/css" />
  </head>
  <body>
    <div class="page">
      <div class="title">Flesh and Blood</div>
      <div class="board">
        <div class="player">
          <div class="name">Joueur 1</div>
          <div class="life">20</div>
          <div class="controls">
            <span>−1</span>
            <span>+1</span>
          </div>
        </div>

        <div class="player">
          <div class="name">Joueur 2</div>
          <div class="life">20</div>
          <div class="controls">
            <span>−1</span>
            <span>+1</span>
          </div>
        </div>
      </div>
    </div>
  </body>
</html>
"""

    (oebps / "book.xhtml").write_text(book_html, encoding="utf-8")

    container_xml = """<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles>
    <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
  </rootfiles>
</container>
"""
    (meta / "container.xml").write_text(container_xml, encoding="utf-8")

    content_opf = """<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" unique-identifier="BookId" version="3.0">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:identifier id="BookId">fab-life-counter</dc:identifier>
    <dc:title>FAB Life Counter</dc:title>
    <dc:language>fr</dc:language>
    <dc:creator>Copilot</dc:creator>
    <dc:description>Compteur de vie de Flesh and Blood en version statique pour lecture Kindle.</dc:description>
    <meta property="dcterms:modified">2026-08-14T00:00:00Z</meta>
  </metadata>
  <manifest>
    <item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>
    <item id="css" href="style.css" media-type="text/css"/>
    <item id="book" href="book.xhtml" media-type="application/xhtml+xml" properties="nav"/>
  </manifest>
  <spine toc="ncx">
    <itemref idref="book"/>
  </spine>
</package>
"""
    (oebps / "content.opf").write_text(content_opf, encoding="utf-8")

    toc_ncx = """<?xml version="1.0" encoding="UTF-8"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
  <head>
    <meta name="dtb:uid" content="fab-life-counter"/>
    <meta name="dtb:depth" content="1"/>
    <meta name="dtb:totalPageCount" content="0"/>
    <meta name="dtb:maxPageNumber" content="0"/>
  </head>
  <docTitle>
    <text>FAB Life Counter</text>
  </docTitle>
  <navMap>
    <navPoint id="navpoint-1" playOrder="1">
      <navLabel><text>FAB Life Counter</text></navLabel>
      <content src="book.xhtml"/>
    </navPoint>
  </navMap>
</ncx>
"""
    (oebps / "toc.ncx").write_text(toc_ncx, encoding="utf-8")

    with zipfile.ZipFile(EPUB_PATH, "w") as zf:
        zf.writestr("mimetype", "application/epub+zip", compress_type=zipfile.ZIP_STORED)

        for file_path in sorted([meta / "container.xml", oebps / "content.opf", oebps / "toc.ncx", oebps / "style.css", oebps / "book.xhtml"]):
            arcname = str(file_path.relative_to(ROOT)).replace("\\", "/")
            if arcname.startswith("_epub/"):
                arcname = arcname.replace("_epub/", "OEBPS/", 1)
            if arcname.startswith("_epub/META-INF/"):
                arcname = arcname.replace("_epub/META-INF/", "META-INF/", 1)
            zf.write(file_path, arcname, compress_type=zipfile.ZIP_DEFLATED)

    print(f"EPUB generated: {EPUB_PATH}")


if __name__ == "__main__":
    build_epub()
