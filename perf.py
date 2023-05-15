import requests
import pprint
from timeit import default_timer as timer
import statistics
import click
import emoji


def create_data_bin_counts_json(attribute_list, study_id_list):
    """Create JSON Payload for the Clinical Data Bin Counts End Point."""
    json_attributes = []
    for attribute in attribute_list:
        json_attribute = {
            "attributeId": attribute,
            "disableLogScale": False,
            "showNA": True,
        }
        json_attributes.append(json_attribute)
    json = {}
    json["attributes"] = json_attributes
    json["studyViewFilter"] = {"studyIds": study_id_list}
    return json


def connect(url, json, num_runs):
    """Connect to endpoint with specified JSON Payload."""
    print("Connecting to:  " + url)
    print("With JSON Payload:")
    pprint.pprint(json)
    print(f"Total number of runs:  {num_runs}")
    experiments = []
    for i in range(num_runs):
        start_time = timer()
        r = requests.post(url, json=json)
        end_time = timer()
        print(f"Received status code {r.status_code}")
        print("Received JSON Response")
        pprint.pprint(r.json())
        time_elapsed = (end_time - start_time) * 1000
        experiments.append(time_elapsed)
    print("Performance of each run:")
    for experiment in experiments:
        print(f"{experiment:.2f} ms")
    avg = statistics.mean(experiments)
    print(f"Average:  {avg:.2f} ms")


@click.command()
@click.option(
    "--base_url", default="https://www.cbioportal.org", help="Base URL of cBioPortal."
)
@click.option("--num_tries", default=5, help="Number of tries.")
@click.option("--end_point", default="clinical_bins", help="End Point to Test")
def performance(base_url, num_tries, end_point):
    print(emoji.emojize('cBioPortal Performance Testing :wave:', language='alias'))
    if end_point == "clinical_bins":
        CLINICAL_DATA_BIN_COUNTS_URL = (
            f"{base_url}/api/clinical-data-bin-counts/fetch?dataBinMethod=STATIC"
        )
        json = create_data_bin_counts_json(
            ["AGE", "MUTATION_COUNT"], ["msk_impact_2017", "msk_met_2021", "msk_ch_2020"]
        )
        connect(CLINICAL_DATA_BIN_COUNTS_URL, json, num_tries)

if __name__ == '__main__':
    performance()