from datetime import datetime
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# Fake database
fake_database = {
    # Heavy breaches (5-6 breaches)
    "alex.king@gmail.com": [
        {"Name": "LinkedIn", "BreachDate": "2016-05-05", "Title": "LinkedIn Data Leak"},
        {"Name": "Dropbox", "BreachDate": "2012-07-01", "Title": "Dropbox Credential Exposure"},
        {"Name": "Yahoo", "BreachDate": "2014-08-01", "Title": "Yahoo Massive Data Breach"},
        {"Name": "Canva", "BreachDate": "2019-05-24", "Title": "Canva Data Breach"},
        {"Name": "Quora", "BreachDate": "2018-12-04", "Title": "Quora User Database Breach"}
    ],
    "maria.jones@gmail.com": [
        {"Name": "Facebook", "BreachDate": "2019-04-20", "Title": "Facebook Public Data Leak"},
        {"Name": "Adobe", "BreachDate": "2013-10-04", "Title": "Adobe Password Leak"},
        {"Name": "MySpace", "BreachDate": "2013-06-11", "Title": "MySpace Historical Data Leak"},
        {"Name": "Zynga", "BreachDate": "2019-09-12", "Title": "Zynga Gaming Accounts Breach"},
        {"Name": "Twitter", "BreachDate": "2020-07-15", "Title": "Twitter Data Leak"},
        {"Name": "Tumblr", "BreachDate": "2013-11-01", "Title": "Tumblr Password Exposure"}
    ],
    "steve.rogers@gmail.com": [
        {"Name": "Yahoo", "BreachDate": "2014-08-01", "Title": "Yahoo Massive Data Breach"},
        {"Name": "LinkedIn", "BreachDate": "2016-05-05", "Title": "LinkedIn Data Leak"},
        {"Name": "Adobe", "BreachDate": "2013-10-04", "Title": "Adobe Password Leak"},
        {"Name": "Dropbox", "BreachDate": "2012-07-01", "Title": "Dropbox Credential Exposure"},
        {"Name": "MyFitnessPal", "BreachDate": "2018-03-01", "Title": "MyFitnessPal Data Breach"}
    ],

    # Medium breaches (2-3 breaches)
    "jane.doe@gmail.com": [
        {"Name": "Canva", "BreachDate": "2019-05-24", "Title": "Canva Data Breach"},
        {"Name": "Quora", "BreachDate": "2018-12-04", "Title": "Quora User Database Breach"}
    ],
    "luke.skywalker@gmail.com": [
        {"Name": "Twitter", "BreachDate": "2020-07-15", "Title": "Twitter Data Leak"},
        {"Name": "LinkedIn", "BreachDate": "2016-05-05", "Title": "LinkedIn Data Leak"},
        {"Name": "Dropbox", "BreachDate": "2012-07-01", "Title": "Dropbox Credential Exposure"}
    ],
    "peter.parker@gmail.com": [
        {"Name": "Facebook", "BreachDate": "2019-04-20", "Title": "Facebook Public Data Leak"},
        {"Name": "Zynga", "BreachDate": "2019-09-12", "Title": "Zynga Gaming Accounts Breach"}
    ],
    "harry.potter@gmail.com": [
        {"Name": "MySpace", "BreachDate": "2013-06-11", "Title": "MySpace Historical Data Leak"},
        {"Name": "Tumblr", "BreachDate": "2013-11-01", "Title": "Tumblr Password Exposure"},
        {"Name": "Adobe", "BreachDate": "2013-10-04", "Title": "Adobe Password Leak"}
    ],
    "sara.connor@gmail.com": [
        {"Name": "Yahoo", "BreachDate": "2014-08-01", "Title": "Yahoo Massive Data Breach"},
        {"Name": "Dropbox", "BreachDate": "2012-07-01", "Title": "Dropbox Credential Exposure"}
    ],

    # Single breach accounts (light)
    "bruce.wayne@gmail.com": [
        {"Name": "Adobe", "BreachDate": "2013-10-04", "Title": "Adobe Password Leak"}
    ],
    "clark.kent@gmail.com": [
        {"Name": "Facebook", "BreachDate": "2019-04-20", "Title": "Facebook Public Data Leak"}
    ],
    "tony.stark@gmail.com": [
        {"Name": "LinkedIn", "BreachDate": "2016-05-05", "Title": "LinkedIn Data Leak"}
    ],
    "diana.prince@gmail.com": [
        {"Name": "Canva", "BreachDate": "2019-05-24", "Title": "Canva Data Breach"}
    ],
    "natasha.romanoff@gmail.com": [
        {"Name": "Quora", "BreachDate": "2018-12-04", "Title": "Quora User Database Breach"}
    ],
    "bruce.banner@gmail.com": [
        {"Name": "Dropbox", "BreachDate": "2012-07-01", "Title": "Dropbox Credential Exposure"}
    ],
    "wanda.maximoff@gmail.com": [
        {"Name": "Tumblr", "BreachDate": "2013-11-01", "Title": "Tumblr Password Exposure"}
    ],

    # More variety (rest to reach 30)
    "vision.ai@gmail.com": [
        {"Name": "Twitter", "BreachDate": "2020-07-15", "Title": "Twitter Data Leak"},
        {"Name": "LinkedIn", "BreachDate": "2016-05-05", "Title": "LinkedIn Data Leak"}
    ],
    "falcon.fly@gmail.com": [
        {"Name": "Adobe", "BreachDate": "2013-10-04", "Title": "Adobe Password Leak"},
        {"Name": "Dropbox", "BreachDate": "2012-07-01", "Title": "Dropbox Credential Exposure"},
        {"Name": "Yahoo", "BreachDate": "2014-08-01", "Title": "Yahoo Massive Data Breach"}
    ],
    "winter.soldier@gmail.com": [
        {"Name": "Facebook", "BreachDate": "2019-04-20", "Title": "Facebook Public Data Leak"}
    ],
    "shuri.tech@gmail.com": [
        {"Name": "Canva", "BreachDate": "2019-05-24", "Title": "Canva Data Breach"},
        {"Name": "Quora", "BreachDate": "2018-12-04", "Title": "Quora User Database Breach"}
    ],
    "okoye.guard@gmail.com": [
        {"Name": "MyFitnessPal", "BreachDate": "2018-03-01", "Title": "MyFitnessPal Data Breach"}
    ],
    "pepper.potts@gmail.com": [
        {"Name": "Yahoo", "BreachDate": "2014-08-01", "Title": "Yahoo Massive Data Breach"}
    ],
    "happy.hogan@gmail.com": [
        {"Name": "Tumblr", "BreachDate": "2013-11-01", "Title": "Tumblr Password Exposure"},
        {"Name": "Zynga", "BreachDate": "2019-09-12", "Title": "Zynga Gaming Accounts Breach"}
    ],
    "mj.watson@gmail.com": [
        {"Name": "Twitter", "BreachDate": "2020-07-15", "Title": "Twitter Data Leak"}
    ],
    "ned.leeds@gmail.com": [
        {"Name": "Dropbox", "BreachDate": "2012-07-01", "Title": "Dropbox Credential Exposure"}
    ],
    "may.parker@gmail.com": [
        {"Name": "Facebook", "BreachDate": "2019-04-20", "Title": "Facebook Public Data Leak"},
        {"Name": "LinkedIn", "BreachDate": "2016-05-05", "Title": "LinkedIn Data Leak"}
    ]
}

def generate_report(email, breaches):
    lines = [f"Data Breach Report for {email}", "="*40]
    for b in breaches:
        lines.append(f"{b['Name']} - {b['BreachDate']} - {b['Title']}")
    # Summary
    dates = [datetime.strptime(b['BreachDate'], "%Y-%m-%d") for b in breaches]
    lines.append("\nSummary:")
    lines.append(f"Total breaches: {len(breaches)}")
    lines.append(f"First breach: {min(dates).date()}")
    lines.append(f"Most recent breach: {max(dates).date()}")
    return "\n".join(lines)

def save_report(report, email):
    filename = f"breach_report_{email.replace('@','_')}.txt"
    with open(filename, "w") as f:
        f.write(report)
    print(Fore.CYAN + f"\nReport saved as {filename}")

def get_severity(count):
    if count <= 1:
        return "LOW"
    elif 2 <= count <= 3:
        return "MEDIUM"
    else:
        return "HIGH"

def check_breaches(email):
    breaches = fake_database.get(email, [])
    if breaches:
        count = len(breaches)
        severity = get_severity(count)
        print(Fore.RED + f"\nOh no! {email} was found in {count} breaches.")
        print(Fore.MAGENTA + f"Severity: {severity}\n")

        for b in breaches:
            print(Fore.YELLOW + f"- {b['Name']} ({b['BreachDate']}): {b['Title']}")

        report = generate_report(email, breaches)
        report += f"\n\nSeverity Level: {severity}"

        choice = input(Fore.GREEN + "\nDo you want to save a detailed report? (y/n): ")
        if choice.lower() == 'y':
            save_report(report, email)
    else:
        print(Fore.GREEN + f"\nGood news! No breaches found for {email}.")

if __name__ == "__main__":
    print(Fore.CYAN + Style.BRIGHT + "\n=== PERSONAL DATA BREACH CHECKER ===")
    email = input(Fore.WHITE + "\nEnter email to check: ").strip()
    check_breaches(email)
    print(Fore.CYAN + "\nThank you for using the Data Breach Checker.\n")
