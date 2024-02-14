import requests

cookies = {
    '64b89d05a4a7cf540e8cd068c2904eaf': '44190b199262df0c9a99c16e70e941ab',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-GB,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': '64b89d05a4a7cf540e8cd068c2904eaf=44190b199262df0c9a99c16e70e941ab',
    'Origin': 'http://dgdagov.info',
    'Referer': 'http://dgdagov.info/index.php/registered-products/allopathic',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

def fetchData(n):
    data = {
        'sEcho': '2',
        'iColumns': '9',
        'sColumns': '',
        'iDisplayStart': f'{n*100}',
        'iDisplayLength': '100',
        'mDataProp_0': '0',
        'mDataProp_1': '1',
        'mDataProp_2': '2',
        'mDataProp_3': '3',
        'mDataProp_4': '4',
        'mDataProp_5': '5',
        'mDataProp_6': '6',
        'mDataProp_7': '7',
        'mDataProp_8': '8',
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
        'sSearch_6': '',
        'bRegex_6': 'false',
        'bSearchable_6': 'true',
        'sSearch_7': '',
        'bRegex_7': 'false',
        'bSearchable_7': 'true',
        'sSearch_8': '',
        'bRegex_8': 'false',
        'bSearchable_8': 'true',
        'iSortCol_0': '1',
        'sSortDir_0': 'asc',
        'iSortingCols': '1',
        'bSortable_0': 'false',
        'bSortable_1': 'true',
        'bSortable_2': 'true',
        'bSortable_3': 'true',
        'bSortable_4': 'true',
        'bSortable_5': 'true',
        'bSortable_6': 'false',
        'bSortable_7': 'true',
        'bSortable_8': 'false',
        'action': 'getDrugCompanyDatabaseData',
        'FilterAll': '4',
        'FilterItem': '',
    }

    response = requests.post(
        'http://dgdagov.info/administrator/components/com_jcode/source/serverProcessing.php',
        cookies=cookies,
        headers=headers,
        data=data,
        verify=False,
    )
    return response.json()['aaData']

data = []

from tqdm import tqdm
import json
for i in tqdm(range(351)):
    print(fetchData(i))
    data.extend(fetchData(i))

with open("allopathicDrugData.json", "w") as f:
    f.write(json.dumps(data))
