import re

data = """ 
) """

# Extract email addresses using a regular expression
emails = re.findall(r'\S+@\S+', data)

# Extract phone numbers using a regular expression
phone_numbers = re.findall(r'\+?\d{10,12}|\(\d{3}\)\s*\d{3}[-\s]*\d{4}', data)

# Extract links using a regular expression
links = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', data)

# Remove duplicates from each list
unique_emails = list(set(emails))
unique_phone_numbers = list(set(phone_numbers))
unique_links = list(set(links))

# Filter out email addresses that are not valid
valid_emails = [email for email in unique_emails if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email)]

# Print the filtered email addresses
print("Email Addresses:")
for email in valid_emails:
    print(email)

# Print the extracted phone numbers
print("\nPhone Numbers:")
for phone in unique_phone_numbers:
    print(phone)

# Print the extracted links
print("\nLinks:")
for link in unique_links:
    print(link)
