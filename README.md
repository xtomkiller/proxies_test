# proxies_test tool 
The proxies tool is a script that helps you check the validity of a list of proxies. It verifies whether the proxies are working or not by making HTTP requests to a target website (in this case, "https://www.google.com"). This tool can be useful in scenarios where you need to ensure that your proxies are functional before using them for any purpose.
## Here's how the tool works:

    It reads the list of proxies from a file called "proxies.txt".
    It iterates through each proxy in the list and sends an HTTP request to the target website using that proxy.
    If the request is successful (HTTP status code 200), it considers the proxy as working and adds it to the "proxies_verify.txt" file.
    If the request fails or encounters an error, it considers the proxy as not working.
    After checking all the proxies, it displays the following information:
        Total proxies to check: The number of proxies read from the file.
        Total proxies checked: The number of proxies that were checked.
        Verified proxies: The number of proxies that were found to be working and saved in the "proxies_verify.txt" file.
        Not working proxies: The number of proxies that were found to be not working.
    If there are any verified proxies, it notifies that the verified proxies have been saved in the "proxies_verify.txt" file.

The tool allows you to quickly ide
# Requirement & setup this tool 
$ 
$ pip install requests termcolor
