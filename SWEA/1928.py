import base64

T = int(input())
for test_case in range(1, T+1):
    encoded = input().strip()
    
    # Base64 디코딩
    decoded_bytes = base64.b64decode(encoded)
    
    # bytes -> str
    decoded_str = decoded_bytes.decode('utf-8')
    
    print(f"#{test_case} {decoded_str}")
