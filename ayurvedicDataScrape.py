import requests

cookies = {
    '64b89d05a4a7cf540e8cd068c2904eaf': 'cb909e6e644f285540b186469a77ef9a',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-GB,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': '64b89d05a4a7cf540e8cd068c2904eaf=cb909e6e644f285540b186469a77ef9a',
    'Origin': 'http://dgdagov.info',
    'Referer': 'http://dgdagov.info/index.php/registered-products/ayurvedic',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}
def fetchData1(n):
    data = {
        'sEcho': '2',
        'iColumns': '6',
        'sColumns': '',
        'iDisplayStart': f'{n*25}',
        'iDisplayLength': '25',
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
        'ManufacturerCategory': 'A',
    }

    response = requests.post(
        'http://dgdagov.info/administrator/components/com_jcode/source/serverProcessing.php',
        cookies=cookies,
        headers=headers,
        data=data,
        verify=False,
    )

    return response.json()['aaData']

fetchedData = []

from tqdm import tqdm
import json
for i in tqdm(range(207)):
    if(i==54):
        fetchedData.extend([[ "1351", "Bioharbs Ayurvedic", "HBP Nil","Tablet", "Rauwolfia", "AY-129-A-036"],[ "1352", "Bioharbs Ayurvedic", "Mytone Plus","Tablet", "Chinese Rhubarb (China Raucini)", "AY-129-A-037"],[ "1353", "Bioharbs Ayurvedic", "BioME","Tablet", "Artichoke", "AY-129-A-038"],[ "1354", "Bioharbs Ayurvedic", "Biovex","Tablet", "Cowhage", "AY-129-\A-039"],[ "1355", "Bioharbs Ayurvedic", "BioMove","Tablet", "Cat's Claw", "AY-129-A-041"],[ "1356", "Bioharbs Ayurvedic", "Biocalm","Tablet", "Belladonna", "AY-129-A-043"],[ "1357", "Bioharbs Ayurvedic", "Eribone","Tablet", "Devil's Claw", "AY-129-A-042"],[ "1358", "Bioharbs Ayurvedic", "Branogin","Tablet", "Ginkgo Biloba", "AY-129-A-044"],[ "1359", "Bioharbs Ayurvedic", "Amaru","Tablet", "Ashwagandha", "AY-129-A-045"],[ "1360", "Bioharbs Ayurvedic", "Diafree","Tablet", "Jambolan / Syzygium", "AY-129-A-046"],[ "1361", "Bioharbs Ayurvedic", "Licobye","Tablet", "Bengle Quince", "AY-129-A-047"],[ "1362", "Bioharbs Ayurvedic", "Kab","Tablet", "Kalamegh", "AY-129-A-048"],[ "1363", "Bioharbs Ayurvedic", "Dyoff","Tablet", "Kurchi", "AY-129-A-049"],[ "1364", "Bioharbs Ayurvedic", "Duob","Tablet", "Jayphal", "AY-129-A-050"],[ "1365", "Bioharbs Ayurvedic", "Liqu-joy","Powder", "Hwema Drink 2 gm/100 ml", "AY-129-A-007"],[ "1366", "Bioharbs Ayurvedic", "Bio Tulsi","Powder", "Sage (Bhui Tulsi)", "AY-129-A-008"],[ "1367", "Bioharbs Ayurvedic", "Bioplus","Liquid", "Bhimras", "AY-129-A-009"],[ "1368", "Bioharbs Ayurvedic", "Moho","Liquid", "Sanjivani Rasayan", "AY-129-A-010"],[ "1369", "Bioharbs Ayurvedic", "Lackme","Liquid", "Aswagandharista", "AY-129-A-011"],[ "1370", "Bioharbs Ayurvedic", "Himosev","Liquid", "Saribadyarista", "AY-129-A-012"],[ "1371", "Bioharbs Ayurvedic", "Biotine Plus","Liquid", "Dasamularista", "AY-129-A-013"],[ "1372", "Bioharbs Ayurvedic", "Bton Plus","Liquid", "Upasam", "AY-129-A-014"],[ "1373", "Bioharbs Ayurvedic", "Phalarista","Liquid", "Phalarista", "AY-129-A-015"],[ "1374", "Bioharbs Ayurvedic", "Biokuli","Liquid", "Chandanasav", "AY-129-A-016"],[ "1375", "Bioharbs Ayurvedic", "Hyliv","Liquid", "Kalameghasav", "AY-129-A-017"]])
    else:
        print(fetchData1(i))
        fetchedData.extend(fetchData1(i))

with open("ayurvedicDrugData.json", "w") as f:
    f.write(json.dumps(fetchedData))
