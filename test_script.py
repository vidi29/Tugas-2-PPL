import os

def test_index_file_exists():
    assert os.path.exists("index.html"), "File index.html tidak ditemukan!"

def test_content_in_index():
    with open("index.html", "r", encoding="utf-8") as f:
        content = f.read()
    assert "NIM" in content, "Konten 'NIM' tidak ditemukan di halaman!"
    assert "Nama" in content, "Konten 'Nama' tidak ditemukan di halaman!"