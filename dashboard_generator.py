# dashboard_generator.py
import json
import os

METADATA_DIR = "metadata"
MANIFEST_FILE = "manifest.json"
OUTPUT_HTML = "dashboard.html"

TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Polyglot Code Dashboard</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 0; padding: 0; background: #f0f2f5; color: #333; }
        header { background: #2c3e50; color: white; padding: 1rem 2rem; display: flex; justify-content: space-between; align-items: center; }
        h1 { margin: 0; font-size: 1.5rem; }
        .stats { font-size: 0.9rem; opacity: 0.8; }
        .container { display: flex; height: calc(100vh - 60px); }
        .sidebar { width: 300px; background: white; border-right: 1px solid #ddd; overflow-y: auto; }
        .file-list-item { padding: 10px 15px; border-bottom: 1px solid #eee; cursor: pointer; transition: background 0.2s; }
        .file-list-item:hover, .file-list-item.active { background: #e6f7ff; border-left: 4px solid #1890ff; }
        .file-name { font-weight: bold; display: block; margin-bottom: 4px; }
        .file-meta { font-size: 0.8em; color: #666; display: flex; justify-content: space-between; }
        .content { flex: 1; padding: 2rem; overflow-y: auto; display: flex; flex-direction: column; }
        #code-display { background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); white-space: pre-wrap; font-family: 'Consolas', 'Monaco', monospace; overflow-x: auto; flex: 1; }
        .hidden { display: none; }
        .empty-state { text-align: center; color: #888; margin-top: 20vh; }
        .badge { display: inline-block; padding: 2px 6px; border-radius: 4px; font-size: 0.75em; background: #eee; }
        .badge-lang { background: #e6f7ff; color: #0050b3; }
    </style>
</head>
<body>
    <header>
        <h1>PolyglotArchitect</h1>
        <div class="stats" id="stats">Loading...</div>
    </header>
    <div class="container">
        <div class="sidebar" id="file-list">
            <!-- List items -->
        </div>
        <div class="content">
            <div id="empty-state" class="empty-state">Select a file to view code</div>
            <pre id="code-display" class="hidden"></pre>
        </div>
    </div>

    <script>
        const data = __DATA__; // Injected Python Data

        function init() {
            const listEl = document.getElementById('file-list');
            const codeEl = document.getElementById('code-display');
            const emptyEl = document.getElementById('empty-state');
            const statsEl = document.getElementById('stats');

            if (!data || data.length === 0) {
                statsEl.textContent = "No files generated yet.";
                return;
            }

            statsEl.textContent = `${data.length} Files Generated`;

            // Sort by ID usually
            data.forEach((file, index) => {
                const item = document.createElement('div');
                item.className = 'file-list-item';
                item.innerHTML = `
                    <span class="file-name">${file.filename}</span>
                    <span class="file-meta">
                        <span class="badge badge-lang">${file.language}</span>
                        <span class="badge">${file.category || 'General'}</span>
                        <span>${file.lines_count} lines</span>
                    </span>
                `;
                item.onclick = () => {
                    // Update Active State
                    document.querySelectorAll('.file-list-item').forEach(el => el.classList.remove('active'));
                    item.classList.add('active');

                    // Show Code
                    emptyEl.classList.add('hidden');
                    codeEl.classList.remove('hidden');
                    // In a real app we might load content on demand, here we assume it's in the code_files dir relative.
                    // But wait, browsers can't fetch local files easily. 
                    // So we either inject the code (huge file) or assume relative path works if served?
                    // For static local file, relative link fetches might fail due to CORS.
                    // Let's inject a "preview" snippet or rely on the user running a local server.
                    // Or, simpler: We will embedding the code in the JSON for this dashboard if it's < 10MB total.
                    // 300 files * 100 lines * 50 chars = 1.5MB. Easy to embed.
                    
                    codeEl.textContent = file.code || "Code content not embedded. Please check the file directly.";
                };
                listEl.appendChild(item);
            });
        }
        
        init();
    </script>
</body>
</html>
"""

def generate_dashboard():
    # Read Manifest
    manifest_path = os.path.join(METADATA_DIR, MANIFEST_FILE)
    if not os.path.exists(manifest_path):
        print("No manifest found. Run the bot first.")
        return

    with open(manifest_path, 'r') as f:
        data = json.load(f)

    # Need to load the code content for embedding if not present in manifest
    # (Create_300_files saves code in files, but manifest might not have it depending on implementation)
    # Check file_creator.py: it writes 'code' to results list before dumping json. 
    # Yes, file_creator.py: "results.append(file_data)" and file_data has "code": code.
    # So manifest.json HAS the code. Perfect.

    html = TEMPLATE.replace("__DATA__", json.dumps(data))
    
    with open(OUTPUT_HTML, 'w', encoding='utf-8') as f:
        f.write(html)
        
    print(f"✅ Dashboard generated: {os.path.abspath(OUTPUT_HTML)}")

if __name__ == "__main__":
    generate_dashboard()
