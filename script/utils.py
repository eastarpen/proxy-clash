import re

def is_server_valid(server:"ipv4 or domain") -> "is server string valid":
    domainPattern = r'\b((?=[a-z0-9-]{1,63}\.)(xn--)?[a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{2,63}\b'
    ipv4Pattern = r'^(((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)(\.(?!$)|$)){4})$'
    return None != re.match(domainPattern, server) or None != re.match(ipv4Pattern, server)
