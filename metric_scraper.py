import requests
from prometheus_client.parser import text_string_to_metric_families


def get_families():
    metrics = requests.get('http://18.206.191.172:9100/metrics').text
    families = []

    for family in text_string_to_metric_families(metrics):
        samples = []
        for sample in family.samples:
            samples.append({
                "name": sample[0],
                "labels": sample[1],
                "value": sample[2],
            })
        families.append({
            "name": family.name,
            "documentation": family.documentation,
            "unit": family.unit,
            "type": family.type,
            "samples": samples,
        })
    return families
