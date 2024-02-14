import requests
import json

cookies = {
    '64b89d05a4a7cf540e8cd068c2904eaf': '5a7e58c35f6d5828cf0cc237cd66fbd3',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-GB,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': '64b89d05a4a7cf540e8cd068c2904eaf=5a7e58c35f6d5828cf0cc237cd66fbd3',
    'Origin': 'http://dgdagov.info',
    'Referer': 'http://dgdagov.info/index.php/registered-products/unani',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

def fetchData(n):
    data = {
        'sEcho': '2',
        'iColumns': '6',
        'sColumns': '',
        'iDisplayStart': f'{n*100}',
        'iDisplayLength': '100',
        'mDataProp_0': '0',
        'mDataProp_1': '1',
        'mDataProp_2': '2',
        'mDataProp_3': '3',
        'mDataProp_4': '4',
        'mDataProp_5': '5',
        'sSearch': '',
        'bRegex': 'false',
        'sSearch_0': '',
        'bRegex_0': 'false',
        'bSearchable_0': 'true',
        'sSearch_1': '',
        'bRegex_1': 'false',
        'bSearchable_1': 'true',
        'sSearch_2': '',
        'bRegex_2': 'false',
        'bSearchable_2': 'true',
        'sSearch_3': '',
        'bRegex_3': 'false',
        'bSearchable_3': 'true',
        'sSearch_4': '',
        'bRegex_4': 'false',
        'bSearchable_4': 'true',
        'sSearch_5': '',
        'bRegex_5': 'false',
        'bSearchable_5': 'true',
        'iSortCol_0': '2',
        'sSortDir_0': 'asc',
        'iSortingCols': '1',
        'bSortable_0': 'false',
        'bSortable_1': 'true',
        'bSortable_2': 'true',
        'bSortable_3': 'true',
        'bSortable_4': 'true',
        'bSortable_5': 'false',
        'action': 'getDrugOthersCompanyDatabaseData',
        'FilterAll': '4',
        'FilterItem': '',
        'ManufacturerCategory': 'U',
    }

    response = requests.post(
        'http://dgdagov.info/administrator/components/com_jcode/source/serverProcessing.php',
        cookies=cookies,
        headers=headers,
        data=data,
        verify=False,
    )
    response_content = response.text
    
    # Preprocessing the content to escape problematic characters
    escaped_content = response_content.replace('\\', '\\\\')
    
    # Parsing JSON content
    try:
        parsed_response = json.loads(escaped_content)
        return parsed_response['aaData']
    except json.JSONDecodeError as e:
        return print("JSON Decode Error:", e)
        

fetchedData = []

from tqdm import tqdm
for i in tqdm(range(84)):
    # print(fetchData(i))
    fetchedData.extend(fetchData(i))

with open("unaniDrugData.json", "w") as f:
    f.write(json.dumps(fetchedData))