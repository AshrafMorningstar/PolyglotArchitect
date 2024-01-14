# file_creator.py
import json
import os
import time
from bot_config import CATEGORIES, CATEGORY_QUOTAS, PROGRAM_TYPES
from generator import generate_code_file

OUTPUT_DIR = "code_files"
METADATA_DIR = "metadata"
MANIFEST_FILE = "../metadata/manifest.json" 

def create_300_files():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    if not os.path.exists(METADATA_DIR):
        os.makedirs(METADATA_DIR)
        
    results = []
    # Load existing manifest
    manifest_path = os.path.join(METADATA_DIR, "manifest.json")
    if os.path.exists(manifest_path):
        with open(manifest_path, 'r') as f:
            try:
                results = json.load(f)
            except json.JSONDecodeError:
                results = []
    
    # Calculate generated counts
    generated_count = len(results)
    
    print(f"Starting generation. Goal: 300 files.")

    for category, languages_dict in CATEGORIES.items():
        quota = CATEGORY_QUOTAS.get(category, 0)
        langs_list = list(languages_dict.keys())
        
        if not langs_list:
            continue
            
        print(f"--- Category: {category} (Quota: {quota}) ---")
        
        files_per_lang = quota // len(langs_list)
        remainder = quota % len(langs_list)
        
        files_created_in_category = 0
        
        for idx, lang in enumerate(langs_list):
            target_for_this_lang = files_per_lang + (1 if idx < remainder else 0)
            
            lang_config = languages_dict[lang]
            ext = lang_config["ext"]
            run_cmd = lang_config["run"]
            
            # Create subdirectory
            lang_dir = os.path.join(OUTPUT_DIR, lang.lower())
            if not os.path.exists(lang_dir):
                os.makedirs(lang_dir)

            for i in range(target_for_this_lang):
                program_type = PROGRAM_TYPES[i % len(PROGRAM_TYPES)]
                
                safe_program = program_type.replace(' ', '_').lower()
                safe_lang = lang.lower()
                
                filename = f"{safe_program}{ext}" 
                if target_for_this_lang > len(PROGRAM_TYPES):
                     filename = f"{safe_program}_{i}{ext}"
                
                rel_filepath = os.path.join(lang.lower(), filename)
                abs_filepath = os.path.join(OUTPUT_DIR, rel_filepath)
                
                if any(r.get('rel_path') == rel_filepath for r in results) or os.path.exists(abs_filepath):
                    print(f"Skipping {rel_filepath} (Exists)")
                    files_created_in_category += 1
                    continue
                
                print(f"Generating {lang} [{i+1}/{target_for_this_lang}]: {program_type}...")
                code = generate_code_file(lang, program_type)
                
                if not code:
                     print("Generaton failed.")
                     continue
                
                with open(abs_filepath, 'w', encoding='utf-8') as f:
                    f.write(code)
                
                lines_count = len(code.split('\n'))
                
                meta = {
                    "id": len(results) + 1,
                    "category": category,
                    "language": lang,
                    "program_type": program_type,
                    "filename": filename,
                    "rel_path": rel_filepath, 
                    "lines_count": lines_count,
                    "run_cmd": run_cmd
                }
                
                results.append(meta)
                generated_count += 1
                files_created_in_category += 1
                
                with open(manifest_path, 'w') as f:
                    json.dump(results, f, indent=2)
                    
                time.sleep(0.5)

    print("Batch generation complete.")
