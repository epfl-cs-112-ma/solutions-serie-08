import requests
import sys

def main() -> None:
    if len(sys.argv) > 1:
        library_name = sys.argv[1]
    else:
        library_name = "arcade" # some default, because why not?

    url = f"https://pypi.org/pypi/{library_name}/json"
    response = requests.get(url)

    if response.status_code != 200:
        print("The HTTP request did not complete successfully:")
        print(f"{response.status_code} {response.reason}")
    else:
        print(response.text)


if __name__ == "__main__":
    main()
