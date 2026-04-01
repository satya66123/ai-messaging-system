def should_reply(email: str):
    email = email.lower()

    # 🚨 Critical alerts (security / account access)
    critical_keywords = [
        "security", "alert", "exposed",
        "token", "breach", "github",
        "warning", "access", "permission",
        "login", "account"
    ]

    if any(word in email for word in critical_keywords):
        return True, "Critical: Security/Access Alert"

    # ❌ Skip unwanted
    skip_keywords = [
        "otp", "verification code",
        "unsubscribe", "offer", "promotion"
    ]

    if any(word in email for word in skip_keywords):
        return False, "Skipped: system email"

    # ✅ Work-related
    important_keywords = [
        "project", "update", "meeting",
        "deadline", "client", "issue"
    ]

    if any(word in email for word in important_keywords):
        return True, "Important: Work"

    return False, "Not relevant"