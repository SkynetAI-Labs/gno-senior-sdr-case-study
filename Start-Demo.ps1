param([int]$Port=8503)
$ErrorActionPreference='Stop'
Set-Location $PSScriptRoot
python -m streamlit run streamlit_app.py --server.port $Port --server.headless true
