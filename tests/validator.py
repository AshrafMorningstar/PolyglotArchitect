# validator.py
import json
import os

OUTPUT_DIR = "code_files"
METADATA_DIR = "metadata"
MANIFEST_FILE = "manifest.json"

def validate():
    # Assume running from root
    manifest_path = os.path.join(METADATA_DIR, MANIFEST_FILE)
    if not os.path.exists(manifest_path):
        # Try relative to tests/
        manifest_path = os.path.join("..", METADATA_DIR, MANIFEST_FILE)
    
    if not os.path.exists(manifest_path):
        print(f"Manifest not found at {manifest_path}")
        return

    with open(manifest_path, 'r') as f:
        data = json.load(f)

    # Resolve output dir
    output_path = OUTPUT_DIR
    if not os.path.exists(output_path):
        output_path = os.path.join("..", OUTPUT_DIR)

    print(f"Validating {len(data)} files...")
    
    stats = {
        "total": len(data),
        "valid_length": 0,
        "under_99_lines": [],
        "by_language": {}
    }
    
    for item in data:
        lang = item.get("language", "Unknown")
        stats["by_language"][lang] = stats["by_language"].get(lang, 0) + 1
        
        # Verify file actually exists
        if "rel_path" in item:
             filepath = os.path.join(output_path, item["rel_path"])
        else:
             filepath = os.path.join(output_path, item["filename"])
             
        if not os.path.exists(filepath):
            # Try checking if it's in a language folder named after the language
            lang_sub = os.path.join(output_path, lang.lower(), item["filename"])
            if os.path.exists(lang_sub):
                filepath = lang_sub
            else:
                print(f"❌ Missing file: {item['filename']}")
                continue
            
        # Count lines actually in file
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            lines = len(f.readlines())
            
        if lines >= 99:
            stats["valid_length"] += 1
        else:
            stats["under_99_lines"].append(f"{item['filename']} ({lines} lines)")
            
    print("-" * 40)
    print(f"Total Files: {stats['total']}")
    print(f"Files >= 99 lines: {stats['valid_length']}")
    print(f"Files < 99 lines: {len(stats['under_99_lines'])}")
    
    if stats["under_99_lines"]:
        print("\nFiles needing expansion:")
        for f in stats["under_99_lines"][:10]:
            print(f" - {f}")
            
    print("\nBreakdown by Language:")
    for lang, count in sorted(stats["by_language"].items(), key=lambda x: x[1], reverse=True):
        print(f"{lang}: {count}")

if __name__ == "__main__":
    validate()
