import pymupdf4llm

# Convert PDF to Markdown
md_text = pymupdf4llm.to_markdown("data/janka-farmacia-otazky-01-02.pdf")

# Save to file
with open("data/janka-farmacia-otazky-01-02.md", "w", encoding="utf-8") as f:
    f.write(md_text)

print("✅ PDF converted to Markdown")
