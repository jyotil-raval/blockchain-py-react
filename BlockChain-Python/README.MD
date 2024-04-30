**Install All Packages with specific version**
```
pip3 install -r requirements.txt
```

**Create new virtual Environment**
```
python3 -m venv blockchain-env
```

**Activate the Virtual Environment Command**
```
source blockchain-env/bin/activate
```

**Run Test Cases**

Make sure, Virtual Environment is running before running testacies
```
python3 -m pytest Backend/Tests
```


**Run The Code**

Suppose we are running *Backend/Blockchain/block.py* file
```
python3 -m Backend.Blockchain.block
```