# 2.8. Writing a Regular Expression for Multiline Patterns

# Problem
# You’re trying to match a block of text using a regular expression, but you need the match
# to span multiple lines.

# Solution
# This problem typically arises in patterns that use the dot (.) to match any character but
# forget to account for the fact that it doesn’t match newlines. For example, suppose you
# are trying to match C-style comments: