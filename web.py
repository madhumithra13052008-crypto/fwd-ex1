from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
<head>
    <title>TCP Protocol Table</title>
    <style>
        table {
            border-collapse: collapse;
            width: 90%;
            margin: 20px;
        }
        th {
            background-color: #4CAF50; /* Green header */
            color: white;
            padding: 10px;
        }
        td {
            background-color: #f9f9f9;
            padding: 10px;
            border: 1px solid #333;
        }
        tr:nth-child(even) td {
            background-color: #eaf4fc; /* Alternate row color */
        }
        tr:hover td {
            background-color: #d1e7dd; /* Hover effect */
        }
    </style>
</head>
<body>

    <h1 style="color:darkblue;">TCP Protocol Information</h1>

    <table>
        <tr>
            <th>Property</th>
            <th>Details</th>
        </tr>
        <tr>
            <td>Protocol Name</td>
            <td>TCP (Transmission Control Protocol)</td>
        </tr>
        <tr>
            <td>Type</td>
            <td>Connection-oriented protocol (requires connection before data transfer)</td>
        </tr>
        <tr>
            <td>Reliability</td>
            <td>Ensures reliable, ordered, and error-checked delivery of data</td>
        </tr>
        <tr>
            <td>Data Transfer</td>
            <td>Divides messages into segments and reassembles them in correct order</td>
        </tr>
        <tr>
            <td>Error Handling</td>
            <td>Uses acknowledgments (ACKs), checksums, and retransmissions</td>
        </tr>
        <tr>
            <td>Flow Control</td>
            <td>Adjusts the data rate between sender and receiver using sliding window</td>
        </tr>
        <tr>
            <td>Port Numbers</td>
            <td>Common ports include 80 (HTTP), 443 (HTTPS), 21 (FTP), 25 (SMTP)</td>
        </tr>
        <tr>
            <td>Uses</td>
            <td>Web browsing, file transfer, email, remote login, streaming with reliability</td>
        </tr>
        <tr>
            <td>OSI Model Layer</td>
            <td>Transport Layer</td>
        </tr>
    </table>

</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()