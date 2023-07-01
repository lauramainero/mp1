num_email = int(input())

n_email = []

for email in range(num_email):
    email = input()

    if '@' not in email:
        n_email.append(email)
  
print(len(n_email))