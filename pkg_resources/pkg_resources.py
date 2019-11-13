import uio

c = {}

def resource_stream(package, resource):
    if package not in c:
        try:
            if package:
                p = __import__(package + ".R", None, None, True)
            else:
                p = __import__("R")
            c[package] = p.R
        except ImportError:
            if package:
                p = __import__(package)
                d = p.__path__
                c[package] = d + "/"
            else:
                d = ""
                c[package] = ""
#            if d[0] != "/":
#                import uos
#                d = uos.getcwd() + "/" + d

    p = c[package]
    if isinstance(p, dict):
        return uio.BytesIO(p[resource])
    return open(p + resource, "rb")
