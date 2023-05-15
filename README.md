# cBioPortal Performance Tester

This is a very simply Python script to test the performance of web API endpoints.

## To install

Create a virtual environment and install dependencies:

	python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

Then, run like so:

    python perf.py --base_url=https://www.cbioportal.org --end_point=clinical_bins --num_tries=3
    
The above will use test performance of the clinical_bins endpoint ten times
on the public portal.

It will then output performance stats like so:

    Performance of each run:
    1399.28 ms
    1332.10 ms
    1734.17 ms
    1638.40 ms
    1304.46 ms
    1508.83 ms
    1406.20 ms
    1175.83 ms
    1408.60 ms
    1482.15 ms
    Average:  1439.00 ms

## To add new End Points

Right now, the performance tester only tests the clinical bins endpoint.  But,
you can easily add new endpoints by modifying the code.