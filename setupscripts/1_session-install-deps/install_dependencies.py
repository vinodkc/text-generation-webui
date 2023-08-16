print("install_dependencies.py")
!pip install --upgrade pip setuptools==59.8.0 wheel
!pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
!pip install --no-cache-dir --log pip-req.log -r requirements.txt
