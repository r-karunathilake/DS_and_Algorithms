def checkSpamEmails(emails: list[str], spam_words: list[str]) -> list[str]:
    spam_words = [spam.lower() for spam in spam_words]

    result = []
    for email in emails:
        count = 0
        for word in email.split():
            # break early
            if count >= 2:
                break

            if word.lower() not in spam_words: 
                continue 
            count += 1

        if count >= 2:
            result.append("spam")
        else:
            result.append("not spam")

    return result

import unittest
###############################################################################
###############                  TEST CASES                     ###############
###############################################################################

class TestSpamEmail(unittest.TestCase):
    def test_one(self):
        email_subjects = ["This is spam spam", "click for free"]
        spam_words = ["spam", "free"]
        expected_result = ["spam", "not spam"]
        self.assertEqual(checkSpamEmails(email_subjects, spam_words), expected_result)

if __name__ == "__main__":
    unittest.main() 
