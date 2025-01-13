import requests
from concurrent.futures import ThreadPoolExecutor

url = "https://ip.world"

# Headers tetap sama
headers = {
    'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36",
    'Accept': "text/x-component",
    'Accept-Encoding': "gzip, deflate, br, zstd",
    'sec-ch-ua': "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
    'next-router-state-tree': "%5B%22%22%2C%7B%22children%22%3A%5B%22(marketing)%22%2C%7B%22children%22%3A%5B%22landing%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2F%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
    'sec-ch-ua-mobile': "?1",
    'x-deployment-id': "dpl_tAaaD1e9C9txK3wxYUS6V6cbVgJF",
    'next-action': "b966fa1cf04bd64b272d456e7182f5d2d1c17116",
    'sec-ch-ua-platform': "\"Android\"",
    'origin': "https://ip.world",
    'sec-fetch-site': "same-origin",
    'sec-fetch-mode': "cors",
    'sec-fetch-dest': "empty",
    'referer': "https://ip.world/",
    'accept-language': "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
    'priority': "u=1, i"
}

# Fungsi untuk mengirim request
def send_request(i):
    if i % 2 == 1:  # Angka ganjil
        email = f"farissanke2+{(i // 2) + 1}@gmail.com"
    else:  # Angka genap
        email = f"eulakanaeru{(i // 2)}@gmail.com"

    payload = {
        '1_$ACTION_REF_1': '',
        '1_$ACTION_1:0': '{"id":"b966fa1cf04bd64b272d456e7182f5d2d1c17116","bound":"$@1"}',
        '1_$ACTION_1:1': '[{"success":false,"message":""}]',
        '1_$ACTION_KEY': 'k2945770830',
        '1_email': email,
        '0': '[{"success":false,"message":""},"$K1"]'
    }

    try:
        response = requests.post(url, data=payload, headers=headers)
        print(f"{i}: {email} -> {response.status_code}")

        if response.status_code != 200:
            print(f"Error for email {email}: {response.text}")

    except Exception as e:
        print(f"Failed for {email}: {e}")


# Main function to execute threads
if __name__ == "__main__":
    # Total iterasi: 1 hingga 1.000.000
    total_requests = 1000000
    thread_count = 4  # Jumlah thread

    with ThreadPoolExecutor(max_workers=thread_count) as executor:
        # Membagi pekerjaan untuk 4 thread
        executor.map(send_request, range(1, total_requests + 1))
