# music-brain
---
A project to research the relationship between music and brain activity.

## 1. initializing

### 1.1 downloading packages

Download the dependencies for openneuro.
```
cd openneuro
npm install
cd ..
```

Create a Python virtual environment.
```
virtualenv -p python3 venv
source venv/bin/activate
pip3 install -r requirements.txt
```

### 1.2 logging into openneuro

For the first time, login to openneuro.
```
openneuro/node_modules/.bin/openneuro login
```

This needs to be run only once. The login info is stored in ~/.openneuro.

### 1.3 downloading data

Because the data sets are large, they are not stored in git. For the first time, run the following command to download them into the current directory.

```
./download.sh
```

## 2. running

Run the Python code to plot the data.
```
./run.py
```
