# Setup
- **Setup env in `~/.bashrc`**
    - **Must** change to your username.
```properties
export CONDA_PLUGINS_AUTO_ACCEPT_TOS=yes
export COMPUTER_VISION_CONDA=computer_vision
export AZUREML_USER="<USERNAME>"
export COMPUTER_VISION_REPO="/home/azureuser/cloudfiles/code/Users/$AZUREML_USER/opencv_yolo_supervision"
```

- **Create/activate Conda environment**
    - **Create:** `conda create -n $COMPUTER_VISION_CONDA python=3.11 -y`
    - **Activate:** 
        - `conda activate $COMPUTER_VISION_CONDA`
        - `pip install -r $COMPUTER_VISION_REPO/requirements.txt`

- **Register Kernal**
    - `python -m ipykernel install --user --name $COMPUTER_VISION_CONDA --display-name "Python ($COMPUTER_VISION_CONDA)"`
