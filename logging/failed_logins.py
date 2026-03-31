auth_log = "/var/log/auth.log"

failed_logins = 0

with open(auth_log, "r") as file:
    for line in file:
        if "Failed password" in line:
            failed_logins += 1

print(f"Failed SSH login attempts: {failed_logins}")
