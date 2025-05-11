import requests

payload = {
    "name": "Mradul Hetawal",
    "regNo": "0827CS221169",
    "email": "mradulhetawal220864@acropolis.in"
}

gen_url = "https://bfhldevapigw.healthrx.co.in/hiring/generateWebhook/PYTHON"
response = requests.post(gen_url, json=payload)
response_data = response.json()

webhookURL = response_data.get('webhook')
accessToken = response_data.get('accessToken')

print("Webhook URL:", webhookURL)
print("Access Token:", accessToken)

SQL_QUERY = """
SELECT 
    p.AMOUNT AS SALARY,
    CONCAT(e.FIRST_NAME, ' ', e.LAST_NAME) AS NAME,
    FLOOR(DATEDIFF(CURDATE(), e.DOB) / 365) AS AGE,
    d.DEPARTMENT_NAME
FROM PAYMENTS p
JOIN EMPLOYEE e ON p.EMP_ID = e.EMP_ID
JOIN DEPARTMENT d ON e.DEPARTMENT = d.DEPARTMENT_ID
WHERE DAY(p.PAYMENT_TIME) != 1
ORDER BY p.AMOUNT DESC
LIMIT 1;
"""

headers = {
    "Authorization": accessToken,
    "Content-Type": "application/json"
}

body = {
    "finalQuery": SQL_QUERY.strip()
}

response = requests.post(webhookURL, headers=headers, json=body)

print("Status Code:", response.status_code)
try:
    print("Response:", response.json())
except:
    print("Non-JSON response received.")
