import hashlib


def crack_sha1_hash(hash, use_salts=False):

    with open("top-10000-passwords.txt", "r") as password_file:
        passwords = [line.strip() for line in password_file]

    if use_salts:

        with open("known-salts.txt", "r") as salt_file:
            salts = [line.strip() for line in salt_file]

        for password in passwords:

            password_hash = hashlib.sha1(
                password.encode("utf-8")
            ).hexdigest()

            if password_hash == hash:
                return password

            for salt in salts:

                salted_front = hashlib.sha1(
                    (salt + password).encode("utf-8")
                ).hexdigest()

                if salted_front == hash:
                    return password

                salted_back = hashlib.sha1(
                    (password + salt).encode("utf-8")
                ).hexdigest()

                if salted_back == hash:
                    return password

    else:

        for password in passwords:

            password_hash = hashlib.sha1(
                password.encode("utf-8")
            ).hexdigest()

            if password_hash == hash:
                return password

    return "PASSWORD NOT IN DATABASE"
