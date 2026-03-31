log_file = "/var/log/nginx/access.log"

error_count = 0

with open(log_file, "r") as file:
    for line in file:
        if "404" in line or "500" in line:
            error_count += 1

print(f"Total error requests: {error_count}")

if error_count > 5:
    print("WARNING: High number of errors detected!")
