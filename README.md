# test1

## Setup
Obtain an [API Key from Alphavantage](https://www.alphavantage.co/support/#api-key) or from the prof (`ALPHAVANTAGE_API_KEY`).

Create a ".env" file and paste in the following contents:

    ```sh
    # this is the ".env" file...

    ALPHAVANTAGE_API_KEY="_________"
    ```


Create an activate an anaconda environment python

    ```sh
    conda create -n my-first-env python=3.10
    conda activate my-first-env
    ```

Install Packages:
    ```sh
    pip install -r requirements.txt
    ```
can also use a requirements.txt file to install all the packages 



## Usage 
running the python script 
```sh
python app/my_script.py
```

run the unemployment report 
```sh
python app/unemployment.py

ALPHAVANTAGE_API_KEY="abc123" python app/unemployment.py
```
