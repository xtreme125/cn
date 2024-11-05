import socket


# Function to resolve URL to IP address
def url_to_ip(url):
    try:
        ip_address = socket.gethostbyname(url)
        return f"The IP address of {url} is: {ip_address}"
    except socket.gaierror:
        return f"Unable to resolve {url}"


# Function to resolve IP address to URL
def ip_to_url(ip):
    try:
        url = socket.gethostbyaddr(ip)
        return f"The URL for IP address {ip} is: {url[0]}"
    except socket.herror:
        return f"Unable to resolve {ip}"


# Main function to take input and call the respective function
def main():
    print("DNS Lookup Tool")
    print("1. Lookup URL to IP")
    print("2. Lookup IP to URL")

    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        url = input("Enter the URL (without http/https): ")
        print(url_to_ip(url))
    elif choice == '2':
        ip = input("Enter the IP address: ")
        print(ip_to_url(ip))
    else:
        print("Invalid choice. Please choose 1 or 2.")


if __name__ == "__main__":
    main()

