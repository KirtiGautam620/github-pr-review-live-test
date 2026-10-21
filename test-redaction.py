# Synthetic test data only — NOT real credentials

# Test 1: Private-key body redaction
PRIVATE_KEY_TEST = """-----BEGIN PRIVATE KEY-----
FAKE_PRIVATE_KEY_BODY_CANARY_1234567890
THIS_IS_NOT_VALID_BASE64_OR_A_REAL_PRIVATE_KEY
-----END PRIVATE KEY-----"""

# Test 2: Long Google-shaped value redaction
GOOGLE_KEY_TEST = "AIzaSyD_FAKE_TEST_ONLY_NOT_A_REAL_GOOGLE_CREDENTIAL_1234567890"
