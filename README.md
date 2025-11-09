# Custom Pinokio script for n8n via Gepetto. 

## Uses Conda env with Node.js.

In Pinokio, start Gepetto (if not running, troubleshoot via logs—likely port 7860 conflict; stop others first if applicable - careful you save eferything before).

Gepetto UI: New Env → Paste the repo URL https://github.com/cocobeach/pinokio-n8n-custom → Select "Node.js + Conda" (if option; else "Custom").

Config: Env name "n8n", Port 5678, Auth as in script.json.

Install: Gepetto clones, runs script.json commands (~3-5min; watches for npm progress).

Start: Hits localhost:5678—login with admin/yourstrongpass.

Test & Troubleshoot:Success: n8n editor loads; create a test flow (e.g., HTTP to Wan2GP /predict).

Errors:"Conda not found": Ensure Pinokio's Conda is active (Pinokio Settings > Env > Base).
npm fails: Add "npm ci" to install script if cache issues.
Windows-specific (your log shows Win10): Use cmd /c prefix in scripts, e.g., "cmd /c npm install -g n8n".

Logs: Gepetto's console shows full output—grep for "n8n" to debug.


