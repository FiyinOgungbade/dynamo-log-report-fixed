# Parse Access Log to JSON Summary

There is an Apache-style HTTP access log located at `/app/access.log`. Your task is to analyze this log and compile a summary of the traffic.

Save your findings in a JSON file with specific metric fields so that they can be automatically reviewed.

## Success Criteria
1. **File Location**: The compiled summary must be saved precisely at `/app/report.json`.
2. **Format**: The file must be structured as a valid, parsable JSON object.
3. **Content and Keys**: The JSON object must contain exactly the following three keys with their correctly calculated values based on the log:
   - `"total_requests"` (integer): The total number of request entries present in the log.
   - `"unique_ips"` (integer): The total number of unique client IP addresses (the first space-separated token of each log line).
   - `"top_path"` (string): The request resource path (e.g., `/index.html`) that was requested most frequently in the log.
