print("install_dependencies.py")
!pip install --upgrade pip
!pip install --no-cache-dir --log pip-req.log -r setupscripts/1_session-install-deps/requirements.txt
