import streamlit as st
from datetime import datetime

# --- Fake database with sample emails ---
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

# --- Helper functions ---
def get_severity(count):
    if count <= 1:
        return "LOW", "green"
    elif 2 <= count <= 3:
        return "MEDIUM", "orange"
    else:
        return "HIGH", "red"

# --- Streamlit UI ---
st.set_page_config(page_title="Personal Data Breach Checker", page_icon="🔐")

st.title("🔐 Personal Data Breach Checker")
st.write("Enter an email address to see if it appears in known data breaches (simulated dataset).")

email = st.text_input("Email address")

if st.button("Check Breaches"):
    breaches = fake_database.get(email.strip(), [])
    if breaches:
        count = len(breaches)
        severity, color = get_severity(count)

        st.markdown(f"### {count} breaches found")
        st.markdown(f"**Severity:** <span style='color:{color}'>{severity}</span>", unsafe_allow_html=True)

        st.write("---")
        for b in breaches:
            st.write(f"**{b['Name']}** ({b['BreachDate']}): {b['Title']}")

        # Summary
        dates = [datetime.strptime(b['BreachDate'], "%Y-%m-%d") for b in breaches]
        st.write("---")
        st.subheader("Summary")
        st.write(f"First breach: {min(dates).date()}")
        st.write(f"Most recent breach: {max(dates).date()}")
    else:
        st.success("Good news! No breaches found for this email.")
