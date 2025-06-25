
import requests

def main():
    print("Main Agent is running.")
    # Thực hiện các tác vụ hoặc gửi request tới các node khác
    try:
        response = requests.get("http://localhost:5001/ping")
        print("Received from node:", response.text)
    except Exception as e:
        print("Failed to connect to other node:", e)

if __name__ == "__main__":
    main()
