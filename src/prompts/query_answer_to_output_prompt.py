query_result = """You are an expert SQLite analyst. A query you wrote did not work. Fix it.

DATABASE SCHEMA
{schema}

QUESTION
{question}

PREVIOUS ATTEMPTS (all of these failed, do not repeat them)
{attempts}

WHAT WENT WRONG WITH THE LAST ATTEMPT
{problem}

RULES
1. Use ONLY tables and columns from the schema above.
2. Write exactly ONE read-only SELECT statement.
3. If the problem is "no rows", check the filter values against the sample rows in the schema.
4. Return ONLY the corrected SQL. No explanation, no markdown fences.

CORRECTED SQL:
"""