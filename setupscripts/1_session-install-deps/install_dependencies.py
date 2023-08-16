print("install_dependencies.py")
!pip3 install --upgrade pip3
!pip3 install --no-cache-dir --log pip-req.log -r setupscripts/1_session-install-deps/requirements.txt
