"""REST API coding content module — REST API interview prep for nip SDET."""

from __future__ import annotations

from generator.models import NotebookSpec, PracticeProblem, TopicSection


def get_rest_api_spec() -> NotebookSpec:
    """Return a complete NotebookSpec for the REST API coding notebook."""
    return NotebookSpec(
        title="REST API Coding — Interview Prep",
        filename="04_rest_api_coding.ipynb",
        strategy_tips=_strategy_tips(),
        sections=_beginner_sections() + _mid_level_sections(),
        mock_test=_mock_test(),
        cheat_sheet=_cheat_sheet(),
    )


# ---------------------------------------------------------------------------
# Strategy tips
# ---------------------------------------------------------------------------

def _strategy_tips() -> str:
    return (
        "## Strategy Tips for the REST API Coding Section (25 minutes)\n\n"
        "**Read the Problem Fully:** Spend the first 1-2 minutes reading the "
        "entire problem statement. Pay close attention to the API endpoint "
        "structure, pagination details, and what the function must return.\n\n"
        "**Start with Brute Force:** Get a working solution first. For "
        "pagination problems, a simple loop that fetches all pages and "
        "aggregates results is correct and scores full marks.\n\n"
        "**Test Edge Cases:** Before submitting, consider: empty response "
        "lists, last page with fewer items, status codes other than 200, "
        "and deeply nested JSON keys.\n\n"
        "**Time Management (2-3 problems in 25 minutes):**\n"
        "- Problem 1 (easy): ~7 minutes\n"
        "- Problem 2 (medium): ~10 minutes\n"
        "- Problem 3 (harder): ~8 minutes\n"
        "- If stuck on pagination logic for more than 4 minutes, write a "
        "working single-page version first, then add the loop.\n\n"
        "**HackerRank REST API Patterns:**\n"
        "- Most problems give you a base URL and ask you to fetch paginated "
        "data, filter it, and return an aggregated result.\n"
        "- Always check `response.status_code == 200` before processing.\n"
        "- Use `response.json()` to parse the body — it returns a dict or list.\n"
        "- Pagination usually uses `?page=N` or `?offset=N&limit=M` query params.\n\n"
        "**Common Pitfalls:**\n"
        "- Forgetting to handle the last page (which may have fewer items)\n"
        "- Using `response.text` instead of `response.json()`\n"
        "- Not passing query parameters as a dict to `params=`\n"
        "- Hardcoding page numbers instead of looping until empty"
    )


# ---------------------------------------------------------------------------
# Beginner sections
# ---------------------------------------------------------------------------

def _beginner_sections() -> list[TopicSection]:
    return [
        _http_methods_status_codes(),
        _making_requests(),
        _parsing_json_responses(),
        _query_params_and_headers(),
    ]


def _http_methods_status_codes() -> TopicSection:
    explanation = (
        "### HTTP Methods and Status Codes\n\n"
        "REST APIs communicate over HTTP. Understanding the semantics of each "
        "HTTP method and what status codes mean is foundational.\n\n"
        "**HTTP Methods:**\n"
        "- `GET` — Retrieve a resource. Should be idempotent and safe (no side effects).\n"
        "- `POST` — Create a new resource. Body contains the new data.\n"
        "- `PUT` — Replace an existing resource entirely.\n"
        "- `PATCH` — Partially update an existing resource.\n"
        "- `DELETE` — Remove a resource.\n\n"
        "**Status Code Categories:**\n"
        "- `2xx` — Success: `200 OK`, `201 Created`, `204 No Content`\n"
        "- `3xx` — Redirection: `301 Moved Permanently`, `304 Not Modified`\n"
        "- `4xx` — Client Error: `400 Bad Request`, `401 Unauthorized`, "
        "`403 Forbidden`, `404 Not Found`, `429 Too Many Requests`\n"
        "- `5xx` — Server Error: `500 Internal Server Error`, `503 Service Unavailable`\n\n"
        "**Key distinction:** `401 Unauthorized` means not authenticated; "
        "`403 Forbidden` means authenticated but not permitted."
    )

    examples = [
        (
            "# --- HTTP method semantics with mock data ---\n"
            "# Simulating what each HTTP method does conceptually\n\n"
            "# Mock 'database' of users\n"
            "users_db = [\n"
            "    {'id': 1, 'name': 'Alice', 'role': 'admin'},\n"
            "    {'id': 2, 'name': 'Bob',   'role': 'viewer'},\n"
            "]\n\n"
            "def mock_get(user_id: int) -> dict:\n"
            "    \"\"\"GET /users/{id} — retrieve a user.\"\"\"\n"
            "    for u in users_db:\n"
            "        if u['id'] == user_id:\n"
            "            return {'status': 200, 'body': u}\n"
            "    return {'status': 404, 'body': {'error': 'Not found'}}\n\n"
            "def mock_post(name: str, role: str) -> dict:\n"
            "    \"\"\"POST /users — create a new user.\"\"\"\n"
            "    new_id = max(u['id'] for u in users_db) + 1\n"
            "    new_user = {'id': new_id, 'name': name, 'role': role}\n"
            "    users_db.append(new_user)\n"
            "    return {'status': 201, 'body': new_user}\n\n"
            "def mock_delete(user_id: int) -> dict:\n"
            "    \"\"\"DELETE /users/{id} — remove a user.\"\"\"\n"
            "    global users_db\n"
            "    before = len(users_db)\n"
            "    users_db = [u for u in users_db if u['id'] != user_id]\n"
            "    if len(users_db) < before:\n"
            "        return {'status': 204, 'body': None}\n"
            "    return {'status': 404, 'body': {'error': 'Not found'}}\n\n"
            "print(mock_get(1))       # {'status': 200, 'body': {'id': 1, ...}}\n"
            "print(mock_post('Carol', 'editor'))  # {'status': 201, ...}\n"
            "print(mock_delete(99))   # {'status': 404, ...}"
        ),
        (
            "# --- Status code handling pattern ---\n"
            "def handle_response(status_code: int, body: dict) -> str:\n"
            "    \"\"\"Interpret a response based on its status code.\"\"\"\n"
            "    if 200 <= status_code < 300:\n"
            "        return f'Success: {body}'\n"
            "    elif status_code == 401:\n"
            "        return 'Error: Not authenticated — check your credentials'\n"
            "    elif status_code == 403:\n"
            "        return 'Error: Forbidden — you lack permission'\n"
            "    elif status_code == 404:\n"
            "        return 'Error: Resource not found'\n"
            "    elif status_code == 429:\n"
            "        return 'Error: Rate limited — slow down requests'\n"
            "    elif status_code >= 500:\n"
            "        return f'Server error ({status_code}) — retry later'\n"
            "    return f'Unexpected status: {status_code}'\n\n"
            "print(handle_response(200, {'id': 1}))   # Success: ...\n"
            "print(handle_response(404, {}))           # Error: Resource not found\n"
            "print(handle_response(503, {}))           # Server error (503) ..."
        ),
    ]

    practice = [
        PracticeProblem(
            title="Categorize HTTP Status Codes",
            statement=(
                "Write a function that takes an HTTP status code (integer) "
                "and returns its category as a string: 'success', 'redirect', "
                "'client_error', 'server_error', or 'unknown'."
            ),
            function_signature="def categorize_status(code: int) -> str:",
            examples=[
                {"input": "200", "output": "'success'"},
                {"input": "404", "output": "'client_error'"},
                {"input": "503", "output": "'server_error'"},
                {"input": "301", "output": "'redirect'"},
            ],
            solution_code=(
                "def categorize_status(code: int) -> str:\n"
                "    \"\"\"Return the category of an HTTP status code.\"\"\"\n"
                "    if 200 <= code < 300:\n"
                "        return 'success'\n"
                "    elif 300 <= code < 400:\n"
                "        return 'redirect'\n"
                "    elif 400 <= code < 500:\n"
                "        return 'client_error'\n"
                "    elif 500 <= code < 600:\n"
                "        return 'server_error'\n"
                "    return 'unknown'"
            ),
            test_code=(
                "assert categorize_status(200) == 'success'\n"
                "assert categorize_status(201) == 'success'\n"
                "assert categorize_status(204) == 'success'\n"
                "assert categorize_status(301) == 'redirect'\n"
                "assert categorize_status(404) == 'client_error'\n"
                "assert categorize_status(401) == 'client_error'\n"
                "assert categorize_status(500) == 'server_error'\n"
                "assert categorize_status(503) == 'server_error'\n"
                "assert categorize_status(100) == 'unknown'\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Use range checks: 200 <= code < 300 for success, etc.",
                "Return 'unknown' as the fallback for anything outside 2xx-5xx.",
            ],
        ),
        PracticeProblem(
            title="Filter Successful Responses",
            statement=(
                "Given a list of API response dictionaries, each with a "
                "'url' (str) and 'status_code' (int), return a list of URLs "
                "that returned a successful response (2xx status codes)."
            ),
            function_signature=(
                "def successful_urls(responses: list[dict]) -> list[str]:"
            ),
            examples=[
                {
                    "input": (
                        "[{'url': '/api/users', 'status_code': 200}, "
                        "{'url': '/api/items', 'status_code': 404}, "
                        "{'url': '/api/data', 'status_code': 201}]"
                    ),
                    "output": "['/api/users', '/api/data']",
                },
            ],
            solution_code=(
                "def successful_urls(responses: list[dict]) -> list[str]:\n"
                "    \"\"\"Return URLs with 2xx status codes.\"\"\"\n"
                "    return [\n"
                "        r['url'] for r in responses\n"
                "        if 200 <= r['status_code'] < 300\n"
                "    ]"
            ),
            test_code=(
                "responses = [\n"
                "    {'url': '/api/users', 'status_code': 200},\n"
                "    {'url': '/api/items', 'status_code': 404},\n"
                "    {'url': '/api/data',  'status_code': 201},\n"
                "    {'url': '/api/admin', 'status_code': 403},\n"
                "]\n"
                "assert successful_urls(responses) == ['/api/users', '/api/data']\n"
                "assert successful_urls([]) == []\n"
                "assert successful_urls([{'url': '/x', 'status_code': 500}]) == []\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Use a list comprehension with a condition on status_code.",
                "2xx means 200 <= code < 300.",
            ],
        ),
        PracticeProblem(
            title="Count Errors by Category",
            statement=(
                "Given a list of status codes (integers), return a dictionary "
                "with counts for each error category: 'client_errors' (4xx) "
                "and 'server_errors' (5xx). Ignore 2xx and 3xx codes."
            ),
            function_signature=(
                "def count_errors(status_codes: list[int]) -> dict[str, int]:"
            ),
            examples=[
                {
                    "input": "[200, 404, 500, 403, 503, 201]",
                    "output": "{'client_errors': 2, 'server_errors': 2}",
                },
            ],
            solution_code=(
                "def count_errors(status_codes: list[int]) -> dict[str, int]:\n"
                "    \"\"\"Count 4xx and 5xx errors in a list of status codes.\"\"\"\n"
                "    result = {'client_errors': 0, 'server_errors': 0}\n"
                "    for code in status_codes:\n"
                "        if 400 <= code < 500:\n"
                "            result['client_errors'] += 1\n"
                "        elif 500 <= code < 600:\n"
                "            result['server_errors'] += 1\n"
                "    return result"
            ),
            test_code=(
                "assert count_errors([200, 404, 500, 403, 503, 201]) == {'client_errors': 2, 'server_errors': 2}\n"
                "assert count_errors([200, 201, 204]) == {'client_errors': 0, 'server_errors': 0}\n"
                "assert count_errors([]) == {'client_errors': 0, 'server_errors': 0}\n"
                "assert count_errors([400, 401, 403, 404]) == {'client_errors': 4, 'server_errors': 0}\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Initialize the result dict with zero counts.",
                "Use range checks inside a for loop.",
            ],
        ),
        PracticeProblem(
            title="Identify Idempotent Methods",
            statement=(
                "Write a function that takes an HTTP method string and returns "
                "True if the method is idempotent (calling it multiple times "
                "produces the same result), False otherwise. "
                "Idempotent methods: GET, HEAD, PUT, DELETE, OPTIONS. "
                "Non-idempotent: POST, PATCH."
            ),
            function_signature="def is_idempotent(method: str) -> bool:",
            examples=[
                {"input": "'GET'", "output": "True"},
                {"input": "'POST'", "output": "False"},
                {"input": "'DELETE'", "output": "True"},
            ],
            solution_code=(
                "def is_idempotent(method: str) -> bool:\n"
                "    \"\"\"Return True if the HTTP method is idempotent.\"\"\"\n"
                "    idempotent_methods = {'GET', 'HEAD', 'PUT', 'DELETE', 'OPTIONS'}\n"
                "    return method.upper() in idempotent_methods"
            ),
            test_code=(
                "assert is_idempotent('GET') == True\n"
                "assert is_idempotent('HEAD') == True\n"
                "assert is_idempotent('PUT') == True\n"
                "assert is_idempotent('DELETE') == True\n"
                "assert is_idempotent('OPTIONS') == True\n"
                "assert is_idempotent('POST') == False\n"
                "assert is_idempotent('PATCH') == False\n"
                "assert is_idempotent('get') == True  # case-insensitive\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Store idempotent methods in a set for O(1) lookup.",
                "Normalize with .upper() to handle lowercase input.",
            ],
        ),
    ]

    return TopicSection(
        title="HTTP Methods and Status Codes",
        difficulty="Beginner",
        explanation=explanation,
        examples=examples,
        practice=practice,
        key_takeaways=[
            "GET retrieves, POST creates, PUT replaces, PATCH updates, DELETE removes.",
            "2xx = success, 3xx = redirect, 4xx = client error, 5xx = server error.",
            "401 means unauthenticated; 403 means authenticated but forbidden.",
            "GET, PUT, DELETE are idempotent; POST and PATCH are not.",
            "Always check the status code before processing the response body.",
        ],
    )


def _making_requests() -> TopicSection:
    explanation = (
        "### Making Requests with the `requests` Library\n\n"
        "The `requests` library is the standard way to make HTTP calls in "
        "Python. It wraps the lower-level `urllib` with a clean, human-friendly API.\n\n"
        "**Installation:** `pip install requests`\n\n"
        "**Core functions:**\n"
        "```python\n"
        "import requests\n"
        "r = requests.get(url, params={}, headers={}, timeout=10)\n"
        "r = requests.post(url, json={}, headers={}, timeout=10)\n"
        "r = requests.put(url, json={}, timeout=10)\n"
        "r = requests.delete(url, timeout=10)\n"
        "```\n\n"
        "**Response object attributes:**\n"
        "- `r.status_code` — integer status code (200, 404, etc.)\n"
        "- `r.json()` — parse body as JSON (returns dict or list)\n"
        "- `r.text` — body as a string\n"
        "- `r.headers` — response headers dict\n"
        "- `r.ok` — True if status_code < 400\n\n"
        "**Always set a timeout** to avoid hanging indefinitely.\n\n"
        "**Public test APIs used in examples:**\n"
        "- `https://jsonplaceholder.typicode.com` — fake REST API for testing\n"
        "- `https://httpbin.org` — HTTP request/response testing service"
    )

    examples = [
        (
            "# --- requests.get with JSONPlaceholder (mock equivalent) ---\n"
            "# In a real environment you would call:\n"
            "#   import requests\n"
            "#   r = requests.get('https://jsonplaceholder.typicode.com/posts/1', timeout=10)\n"
            "#   post = r.json()\n\n"
            "# Mock equivalent for offline use:\n"
            "def mock_get_post(post_id: int) -> dict:\n"
            "    \"\"\"Simulate GET /posts/{id} from JSONPlaceholder.\"\"\"\n"
            "    mock_data = {\n"
            "        1: {'userId': 1, 'id': 1, 'title': 'sunt aut facere', 'body': 'quia et suscipit...'},\n"
            "        2: {'userId': 1, 'id': 2, 'title': 'qui est esse',    'body': 'est rerum tempore...'},\n"
            "    }\n"
            "    if post_id in mock_data:\n"
            "        return {'status_code': 200, 'json': mock_data[post_id]}\n"
            "    return {'status_code': 404, 'json': {}}\n\n"
            "response = mock_get_post(1)\n"
            "if response['status_code'] == 200:\n"
            "    post = response['json']\n"
            "    print(f\"Title: {post['title']}\")\n"
            "    print(f\"User ID: {post['userId']}\")"
        ),
        (
            "# --- POST request pattern (mock) ---\n"
            "# Real call:\n"
            "#   r = requests.post(\n"
            "#       'https://jsonplaceholder.typicode.com/posts',\n"
            "#       json={'title': 'foo', 'body': 'bar', 'userId': 1},\n"
            "#       timeout=10\n"
            "#   )\n\n"
            "def mock_post_create(payload: dict) -> dict:\n"
            "    \"\"\"Simulate POST /posts — JSONPlaceholder returns id=101 for new posts.\"\"\"\n"
            "    if not payload.get('title') or not payload.get('userId'):\n"
            "        return {'status_code': 400, 'json': {'error': 'Missing required fields'}}\n"
            "    created = {**payload, 'id': 101}\n"
            "    return {'status_code': 201, 'json': created}\n\n"
            "resp = mock_post_create({'title': 'New Post', 'body': 'Content', 'userId': 1})\n"
            "print(f\"Status: {resp['status_code']}\")  # 201\n"
            "print(f\"Created ID: {resp['json']['id']}\")  # 101\n\n"
            "# Always check status before using the body\n"
            "if resp['status_code'] in (200, 201):\n"
            "    print('Resource created successfully')"
        ),
    ]

    practice = [
        PracticeProblem(
            title="Extract Post Titles",
            statement=(
                "Given a list of post dictionaries (simulating a GET /posts "
                "response from JSONPlaceholder), return a list of all post "
                "titles. Each post dict has keys: 'id', 'userId', 'title', 'body'."
            ),
            function_signature=(
                "def extract_titles(posts: list[dict]) -> list[str]:"
            ),
            examples=[
                {
                    "input": (
                        "[{'id': 1, 'userId': 1, 'title': 'First Post', 'body': '...'}, "
                        "{'id': 2, 'userId': 1, 'title': 'Second Post', 'body': '...'}]"
                    ),
                    "output": "['First Post', 'Second Post']",
                },
            ],
            solution_code=(
                "def extract_titles(posts: list[dict]) -> list[str]:\n"
                "    \"\"\"Extract title from each post dict.\"\"\"\n"
                "    return [post['title'] for post in posts]"
            ),
            test_code=(
                "posts = [\n"
                "    {'id': 1, 'userId': 1, 'title': 'First Post',  'body': 'body1'},\n"
                "    {'id': 2, 'userId': 1, 'title': 'Second Post', 'body': 'body2'},\n"
                "    {'id': 3, 'userId': 2, 'title': 'Third Post',  'body': 'body3'},\n"
                "]\n"
                "assert extract_titles(posts) == ['First Post', 'Second Post', 'Third Post']\n"
                "assert extract_titles([]) == []\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Use a list comprehension: [post['title'] for post in posts].",
            ],
        ),
        PracticeProblem(
            title="Filter Posts by User",
            statement=(
                "Given a list of post dictionaries and a user_id, return "
                "only the posts belonging to that user. Each post has a "
                "'userId' field."
            ),
            function_signature=(
                "def posts_by_user(posts: list[dict], user_id: int) -> list[dict]:"
            ),
            examples=[
                {
                    "input": (
                        "[{'id': 1, 'userId': 1, 'title': 'A'}, "
                        "{'id': 2, 'userId': 2, 'title': 'B'}, "
                        "{'id': 3, 'userId': 1, 'title': 'C'}], 1"
                    ),
                    "output": "[{'id': 1, 'userId': 1, 'title': 'A'}, {'id': 3, 'userId': 1, 'title': 'C'}]",
                },
            ],
            solution_code=(
                "def posts_by_user(posts: list[dict], user_id: int) -> list[dict]:\n"
                "    \"\"\"Filter posts to only those belonging to user_id.\"\"\"\n"
                "    return [p for p in posts if p['userId'] == user_id]"
            ),
            test_code=(
                "posts = [\n"
                "    {'id': 1, 'userId': 1, 'title': 'A'},\n"
                "    {'id': 2, 'userId': 2, 'title': 'B'},\n"
                "    {'id': 3, 'userId': 1, 'title': 'C'},\n"
                "]\n"
                "result = posts_by_user(posts, 1)\n"
                "assert len(result) == 2\n"
                "assert all(p['userId'] == 1 for p in result)\n"
                "assert posts_by_user(posts, 99) == []\n"
                "assert posts_by_user([], 1) == []\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Use a list comprehension with a condition on p['userId'].",
            ],
        ),
        PracticeProblem(
            title="Build Request Summary",
            statement=(
                "Given a list of response dictionaries, each with 'method' "
                "(str), 'url' (str), and 'status_code' (int), return a "
                "summary dict with keys 'total', 'success' (2xx), and "
                "'failed' (4xx or 5xx)."
            ),
            function_signature=(
                "def request_summary(responses: list[dict]) -> dict[str, int]:"
            ),
            examples=[
                {
                    "input": (
                        "[{'method': 'GET', 'url': '/a', 'status_code': 200}, "
                        "{'method': 'POST', 'url': '/b', 'status_code': 201}, "
                        "{'method': 'GET', 'url': '/c', 'status_code': 404}]"
                    ),
                    "output": "{'total': 3, 'success': 2, 'failed': 1}",
                },
            ],
            solution_code=(
                "def request_summary(responses: list[dict]) -> dict[str, int]:\n"
                "    \"\"\"Summarize a list of HTTP responses.\"\"\"\n"
                "    total = len(responses)\n"
                "    success = sum(1 for r in responses if 200 <= r['status_code'] < 300)\n"
                "    failed = sum(1 for r in responses if r['status_code'] >= 400)\n"
                "    return {'total': total, 'success': success, 'failed': failed}"
            ),
            test_code=(
                "responses = [\n"
                "    {'method': 'GET',  'url': '/a', 'status_code': 200},\n"
                "    {'method': 'POST', 'url': '/b', 'status_code': 201},\n"
                "    {'method': 'GET',  'url': '/c', 'status_code': 404},\n"
                "    {'method': 'PUT',  'url': '/d', 'status_code': 500},\n"
                "]\n"
                "assert request_summary(responses) == {'total': 4, 'success': 2, 'failed': 2}\n"
                "assert request_summary([]) == {'total': 0, 'success': 0, 'failed': 0}\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Use sum() with a generator expression for counting.",
                "2xx: 200 <= code < 300; failed: code >= 400.",
            ],
        ),
        PracticeProblem(
            title="Find Slowest Endpoint",
            statement=(
                "Given a list of API call records, each with 'endpoint' (str) "
                "and 'response_time_ms' (float), return the endpoint with the "
                "highest average response time. If the list is empty, return None."
            ),
            function_signature=(
                "def slowest_endpoint(records: list[dict]) -> str | None:"
            ),
            examples=[
                {
                    "input": (
                        "[{'endpoint': '/api/users', 'response_time_ms': 120.0}, "
                        "{'endpoint': '/api/posts', 'response_time_ms': 340.0}, "
                        "{'endpoint': '/api/users', 'response_time_ms': 80.0}]"
                    ),
                    "output": "'/api/posts'",
                },
            ],
            solution_code=(
                "def slowest_endpoint(records: list[dict]) -> str | None:\n"
                "    \"\"\"Return the endpoint with the highest average response time.\"\"\"\n"
                "    if not records:\n"
                "        return None\n"
                "    totals: dict[str, list[float]] = {}\n"
                "    for r in records:\n"
                "        ep = r['endpoint']\n"
                "        totals.setdefault(ep, []).append(r['response_time_ms'])\n"
                "    averages = {ep: sum(times) / len(times) for ep, times in totals.items()}\n"
                "    return max(averages, key=averages.get)"
            ),
            test_code=(
                "records = [\n"
                "    {'endpoint': '/api/users', 'response_time_ms': 120.0},\n"
                "    {'endpoint': '/api/posts', 'response_time_ms': 340.0},\n"
                "    {'endpoint': '/api/users', 'response_time_ms': 80.0},\n"
                "]\n"
                "assert slowest_endpoint(records) == '/api/posts'\n"
                "assert slowest_endpoint([]) is None\n"
                "single = [{'endpoint': '/x', 'response_time_ms': 50.0}]\n"
                "assert slowest_endpoint(single) == '/x'\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Group response times by endpoint using a dict of lists.",
                "Compute averages, then use max() with a key function.",
            ],
        ),
    ]

    return TopicSection(
        title="Making Requests with the `requests` Library",
        difficulty="Beginner",
        explanation=explanation,
        examples=examples,
        practice=practice,
        key_takeaways=[
            "Use requests.get/post/put/delete with a timeout to avoid hanging.",
            "r.json() parses the response body; r.status_code gives the HTTP status.",
            "r.ok is True when status_code < 400 — a quick success check.",
            "Pass query parameters as a dict to params=, not in the URL string.",
            "JSONPlaceholder and httpbin.org are free public APIs for testing.",
        ],
    )


def _parsing_json_responses() -> TopicSection:
    explanation = (
        "### Parsing JSON Responses\n\n"
        "JSON (JavaScript Object Notation) is the universal data format for "
        "REST APIs. Python's `json` module and the `requests` library make "
        "parsing straightforward.\n\n"
        "**Two ways to parse JSON:**\n"
        "```python\n"
        "import json\n"
        "# From a string:\n"
        "data = json.loads('{\"key\": \"value\"}')\n"
        "# From a requests response:\n"
        "data = response.json()\n"
        "```\n\n"
        "**Accessing nested data:**\n"
        "```python\n"
        "# Chained key access\n"
        "city = data['address']['city']\n"
        "# Safe access with .get()\n"
        "city = data.get('address', {}).get('city', 'unknown')\n"
        "```\n\n"
        "**Common patterns:**\n"
        "- `response.json()` returns a `dict` for object responses, `list` for arrays\n"
        "- Use `json.dumps(data, indent=2)` to pretty-print for debugging\n"
        "- Handle `json.JSONDecodeError` when the body might not be valid JSON\n\n"
        "**Error handling:**\n"
        "```python\n"
        "try:\n"
        "    data = response.json()\n"
        "except ValueError:  # json.JSONDecodeError is a subclass\n"
        "    data = {}\n"
        "```"
    )

    examples = [
        (
            "# --- Parsing nested JSON (mock data) ---\n"
            "import json\n\n"
            "# Simulated API response body (as you'd get from response.json())\n"
            "user_response = {\n"
            "    'id': 1,\n"
            "    'name': 'Leanne Graham',\n"
            "    'email': 'sincere@april.biz',\n"
            "    'address': {\n"
            "        'street': 'Kulas Light',\n"
            "        'city': 'Gwenborough',\n"
            "        'zipcode': '92998-3874',\n"
            "        'geo': {'lat': '-37.3159', 'lng': '81.1496'}\n"
            "    },\n"
            "    'company': {'name': 'Romaguera-Crona', 'catchPhrase': 'Multi-layered client-server neural-net'}\n"
            "}\n\n"
            "# Direct access\n"
            "print(user_response['name'])                    # 'Leanne Graham'\n"
            "print(user_response['address']['city'])         # 'Gwenborough'\n"
            "print(user_response['address']['geo']['lat'])   # '-37.3159'\n\n"
            "# Safe access with .get()\n"
            "phone = user_response.get('phone', 'N/A')       # 'N/A' (key missing)\n"
            "print(phone)\n\n"
            "# Pretty-print for debugging\n"
            "print(json.dumps(user_response['address'], indent=2))"
        ),
        (
            "# --- Extracting fields from a list of JSON objects ---\n"
            "posts = [\n"
            "    {'id': 1, 'userId': 1, 'title': 'Post One',   'body': 'Content A'},\n"
            "    {'id': 2, 'userId': 2, 'title': 'Post Two',   'body': 'Content B'},\n"
            "    {'id': 3, 'userId': 1, 'title': 'Post Three', 'body': 'Content C'},\n"
            "]\n\n"
            "# Extract all titles\n"
            "titles = [p['title'] for p in posts]\n"
            "print(titles)  # ['Post One', 'Post Two', 'Post Three']\n\n"
            "# Filter by userId and extract titles\n"
            "user1_titles = [p['title'] for p in posts if p['userId'] == 1]\n"
            "print(user1_titles)  # ['Post One', 'Post Three']\n\n"
            "# Build a lookup dict: id -> title\n"
            "id_to_title = {p['id']: p['title'] for p in posts}\n"
            "print(id_to_title[2])  # 'Post Two'"
        ),
    ]

    practice = [
        PracticeProblem(
            title="Extract Nested Field",
            statement=(
                "Given a list of user dictionaries (each with a nested "
                "'address' dict containing 'city'), return a list of city "
                "names. If a user has no 'address' or no 'city', use 'unknown'."
            ),
            function_signature=(
                "def extract_cities(users: list[dict]) -> list[str]:"
            ),
            examples=[
                {
                    "input": (
                        "[{'id': 1, 'name': 'Alice', 'address': {'city': 'Boston'}}, "
                        "{'id': 2, 'name': 'Bob', 'address': {'city': 'Austin'}}, "
                        "{'id': 3, 'name': 'Carol'}]"
                    ),
                    "output": "['Boston', 'Austin', 'unknown']",
                },
            ],
            solution_code=(
                "def extract_cities(users: list[dict]) -> list[str]:\n"
                "    \"\"\"Extract city from nested address, defaulting to 'unknown'.\"\"\"\n"
                "    return [\n"
                "        u.get('address', {}).get('city', 'unknown')\n"
                "        for u in users\n"
                "    ]"
            ),
            test_code=(
                "users = [\n"
                "    {'id': 1, 'name': 'Alice', 'address': {'city': 'Boston'}},\n"
                "    {'id': 2, 'name': 'Bob',   'address': {'city': 'Austin'}},\n"
                "    {'id': 3, 'name': 'Carol'},\n"
                "    {'id': 4, 'name': 'Dave',  'address': {}},\n"
                "]\n"
                "assert extract_cities(users) == ['Boston', 'Austin', 'unknown', 'unknown']\n"
                "assert extract_cities([]) == []\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Use .get('address', {}) to safely get the nested dict.",
                "Chain another .get('city', 'unknown') on the result.",
            ],
        ),
        PracticeProblem(
            title="Flatten API Response",
            statement=(
                "Given a JSON response dict with a 'data' key containing a "
                "list of items, and a 'meta' key with 'total' and 'page', "
                "return a flat dict with keys: 'items' (the list), 'total' "
                "(int), and 'page' (int)."
            ),
            function_signature=(
                "def flatten_response(response: dict) -> dict:"
            ),
            examples=[
                {
                    "input": (
                        "{'data': [{'id': 1}, {'id': 2}], "
                        "'meta': {'total': 50, 'page': 1}}"
                    ),
                    "output": "{'items': [{'id': 1}, {'id': 2}], 'total': 50, 'page': 1}",
                },
            ],
            solution_code=(
                "def flatten_response(response: dict) -> dict:\n"
                "    \"\"\"Flatten a paginated API response into a simple dict.\"\"\"\n"
                "    return {\n"
                "        'items': response.get('data', []),\n"
                "        'total': response.get('meta', {}).get('total', 0),\n"
                "        'page':  response.get('meta', {}).get('page', 1),\n"
                "    }"
            ),
            test_code=(
                "resp = {'data': [{'id': 1}, {'id': 2}], 'meta': {'total': 50, 'page': 1}}\n"
                "result = flatten_response(resp)\n"
                "assert result['items'] == [{'id': 1}, {'id': 2}]\n"
                "assert result['total'] == 50\n"
                "assert result['page'] == 1\n"
                "assert flatten_response({}) == {'items': [], 'total': 0, 'page': 1}\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Use .get() with defaults for missing keys.",
                "Access nested 'meta' with response.get('meta', {}).",
            ],
        ),
        PracticeProblem(
            title="Parse JSON String Safely",
            statement=(
                "Write a function that takes a JSON string and returns the "
                "parsed Python object. If the string is not valid JSON, "
                "return an empty dict {}."
            ),
            function_signature=(
                "def safe_parse_json(json_str: str) -> dict | list:"
            ),
            examples=[
                {"input": "'{\"key\": \"value\"}'", "output": "{'key': 'value'}"},
                {"input": "'not valid json'", "output": "{}"},
                {"input": "''", "output": "{}"},
            ],
            solution_code=(
                "import json\n\n"
                "def safe_parse_json(json_str: str) -> dict | list:\n"
                "    \"\"\"Parse a JSON string, returning {} on failure.\"\"\"\n"
                "    try:\n"
                "        return json.loads(json_str)\n"
                "    except (ValueError, TypeError):\n"
                "        return {}"
            ),
            test_code=(
                "import json\n"
                "assert safe_parse_json('{\"key\": \"value\"}') == {'key': 'value'}\n"
                "assert safe_parse_json('[1, 2, 3]') == [1, 2, 3]\n"
                "assert safe_parse_json('not valid json') == {}\n"
                "assert safe_parse_json('') == {}\n"
                "assert safe_parse_json('null') == {}\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Use json.loads() inside a try/except block.",
                "Catch ValueError (which includes json.JSONDecodeError) and TypeError.",
            ],
        ),
        PracticeProblem(
            title="Aggregate Scores from API Response",
            statement=(
                "Given a list of test result dicts (each with 'test_name' "
                "and 'score' as a float 0-100), return a dict with 'average' "
                "(rounded to 2 decimal places), 'max_score', and 'min_score'. "
                "Return {'average': 0, 'max_score': 0, 'min_score': 0} for empty input."
            ),
            function_signature=(
                "def aggregate_scores(results: list[dict]) -> dict:"
            ),
            examples=[
                {
                    "input": (
                        "[{'test_name': 'A', 'score': 90.0}, "
                        "{'test_name': 'B', 'score': 75.5}, "
                        "{'test_name': 'C', 'score': 88.0}]"
                    ),
                    "output": "{'average': 84.5, 'max_score': 90.0, 'min_score': 75.5}",
                },
            ],
            solution_code=(
                "def aggregate_scores(results: list[dict]) -> dict:\n"
                "    \"\"\"Compute average, max, and min scores from test results.\"\"\"\n"
                "    if not results:\n"
                "        return {'average': 0, 'max_score': 0, 'min_score': 0}\n"
                "    scores = [r['score'] for r in results]\n"
                "    return {\n"
                "        'average':   round(sum(scores) / len(scores), 2),\n"
                "        'max_score': max(scores),\n"
                "        'min_score': min(scores),\n"
                "    }"
            ),
            test_code=(
                "results = [\n"
                "    {'test_name': 'A', 'score': 90.0},\n"
                "    {'test_name': 'B', 'score': 75.5},\n"
                "    {'test_name': 'C', 'score': 88.0},\n"
                "]\n"
                "agg = aggregate_scores(results)\n"
                "assert agg['average'] == 84.5\n"
                "assert agg['max_score'] == 90.0\n"
                "assert agg['min_score'] == 75.5\n"
                "assert aggregate_scores([]) == {'average': 0, 'max_score': 0, 'min_score': 0}\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Extract scores into a list first, then use sum(), max(), min().",
                "Use round(value, 2) for the average.",
            ],
        ),
    ]

    return TopicSection(
        title="Parsing JSON Responses",
        difficulty="Beginner",
        explanation=explanation,
        examples=examples,
        practice=practice,
        key_takeaways=[
            "response.json() is the easiest way to parse a requests response body.",
            "json.loads() parses a JSON string; json.dumps() serializes to a string.",
            "Use .get('key', default) for safe access to avoid KeyError.",
            "Chain .get() calls for nested access: data.get('a', {}).get('b', 'default').",
            "Always handle json.JSONDecodeError (a subclass of ValueError) for robustness.",
        ],
    )


def _query_params_and_headers() -> TopicSection:
    explanation = (
        "### Query Parameters and Headers\n\n"
        "**Query parameters** are key-value pairs appended to a URL after `?`. "
        "They filter, sort, or paginate API results.\n\n"
        "```python\n"
        "# Don't build URLs manually:\n"
        "# url = 'https://api.example.com/posts?userId=1&_limit=5'  # fragile\n\n"
        "# Do use the params dict:\n"
        "params = {'userId': 1, '_limit': 5}\n"
        "r = requests.get('https://jsonplaceholder.typicode.com/posts', params=params)\n"
        "# requests builds: .../posts?userId=1&_limit=5\n"
        "```\n\n"
        "**Headers** carry metadata about the request: content type, auth tokens, "
        "API keys, and more.\n\n"
        "```python\n"
        "headers = {\n"
        "    'Content-Type': 'application/json',\n"
        "    'Accept': 'application/json',\n"
        "    'Authorization': 'Bearer <token>',\n"
        "    'X-API-Key': '<api_key>',\n"
        "}\n"
        "r = requests.get(url, headers=headers)\n"
        "```\n\n"
        "**Common headers:**\n"
        "- `Content-Type` — format of the request body\n"
        "- `Accept` — format the client wants in the response\n"
        "- `Authorization` — auth credentials (Bearer token, Basic auth)\n"
        "- `X-API-Key` — custom API key header (varies by service)"
    )

    examples = [
        (
            "# --- Query parameters (mock simulation) ---\n"
            "# Real call:\n"
            "#   r = requests.get(\n"
            "#       'https://jsonplaceholder.typicode.com/posts',\n"
            "#       params={'userId': 1, '_limit': 3},\n"
            "#       timeout=10\n"
            "#   )\n\n"
            "# Mock data simulating the filtered response\n"
            "ALL_POSTS = [\n"
            "    {'id': 1, 'userId': 1, 'title': 'Post A'},\n"
            "    {'id': 2, 'userId': 2, 'title': 'Post B'},\n"
            "    {'id': 3, 'userId': 1, 'title': 'Post C'},\n"
            "    {'id': 4, 'userId': 1, 'title': 'Post D'},\n"
            "    {'id': 5, 'userId': 3, 'title': 'Post E'},\n"
            "]\n\n"
            "def mock_get_posts(params: dict) -> list[dict]:\n"
            "    \"\"\"Simulate GET /posts with userId and _limit query params.\"\"\"\n"
            "    results = ALL_POSTS\n"
            "    if 'userId' in params:\n"
            "        results = [p for p in results if p['userId'] == params['userId']]\n"
            "    if '_limit' in params:\n"
            "        results = results[:params['_limit']]\n"
            "    return results\n\n"
            "filtered = mock_get_posts({'userId': 1, '_limit': 2})\n"
            "print(filtered)  # [{'id': 1, 'userId': 1, 'title': 'Post A'}, ...]"
        ),
        (
            "# --- Headers pattern ---\n"
            "def build_auth_headers(api_key: str, content_type: str = 'application/json') -> dict:\n"
            "    \"\"\"Build standard request headers with API key auth.\"\"\"\n"
            "    return {\n"
            "        'Content-Type': content_type,\n"
            "        'Accept': 'application/json',\n"
            "        'X-API-Key': api_key,\n"
            "    }\n\n"
            "headers = build_auth_headers('my-secret-key-123')\n"
            "print(headers)\n"
            "# {'Content-Type': 'application/json', 'Accept': 'application/json', 'X-API-Key': '...'}\n\n"
            "# Bearer token pattern\n"
            "def bearer_headers(token: str) -> dict:\n"
            "    return {\n"
            "        'Authorization': f'Bearer {token}',\n"
            "        'Content-Type': 'application/json',\n"
            "    }\n\n"
            "print(bearer_headers('eyJhbGciOiJIUzI1NiJ9...'))"
        ),
    ]

    practice = [
        PracticeProblem(
            title="Build Query String",
            statement=(
                "Write a function that takes a base URL and a dict of query "
                "parameters, and returns the full URL with query string. "
                "Parameters should be sorted alphabetically by key for "
                "deterministic output."
            ),
            function_signature=(
                "def build_url(base_url: str, params: dict) -> str:"
            ),
            examples=[
                {
                    "input": "'https://api.example.com/posts', {'userId': 1, '_limit': 5}",
                    "output": "'https://api.example.com/posts?_limit=5&userId=1'",
                },
                {
                    "input": "'https://api.example.com/posts', {}",
                    "output": "'https://api.example.com/posts'",
                },
            ],
            solution_code=(
                "def build_url(base_url: str, params: dict) -> str:\n"
                "    \"\"\"Build a URL with sorted query parameters.\"\"\"\n"
                "    if not params:\n"
                "        return base_url\n"
                "    query_string = '&'.join(\n"
                "        f'{k}={v}' for k, v in sorted(params.items())\n"
                "    )\n"
                "    return f'{base_url}?{query_string}'"
            ),
            test_code=(
                "assert build_url('https://api.example.com/posts', {'userId': 1, '_limit': 5}) == \\\n"
                "    'https://api.example.com/posts?_limit=5&userId=1'\n"
                "assert build_url('https://api.example.com/posts', {}) == \\\n"
                "    'https://api.example.com/posts'\n"
                "assert build_url('https://x.com/a', {'z': 3, 'a': 1}) == \\\n"
                "    'https://x.com/a?a=1&z=3'\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Sort params.items() for deterministic output.",
                "Use '&'.join() to combine key=value pairs.",
            ],
        ),
        PracticeProblem(
            title="Validate Required Headers",
            statement=(
                "Write a function that checks whether a headers dict contains "
                "all required headers. Return a list of missing header names "
                "(case-insensitive comparison). Return an empty list if all "
                "required headers are present."
            ),
            function_signature=(
                "def missing_headers(headers: dict, required: list[str]) -> list[str]:"
            ),
            examples=[
                {
                    "input": (
                        "{'Content-Type': 'application/json', 'Authorization': 'Bearer x'}, "
                        "['Content-Type', 'Authorization', 'X-API-Key']"
                    ),
                    "output": "['X-API-Key']",
                },
            ],
            solution_code=(
                "def missing_headers(headers: dict, required: list[str]) -> list[str]:\n"
                "    \"\"\"Return required headers not present in headers dict (case-insensitive).\"\"\"\n"
                "    lower_headers = {k.lower() for k in headers}\n"
                "    return [r for r in required if r.lower() not in lower_headers]"
            ),
            test_code=(
                "h = {'Content-Type': 'application/json', 'Authorization': 'Bearer x'}\n"
                "assert missing_headers(h, ['Content-Type', 'Authorization', 'X-API-Key']) == ['X-API-Key']\n"
                "assert missing_headers(h, ['Content-Type', 'Authorization']) == []\n"
                "assert missing_headers({}, ['Authorization']) == ['Authorization']\n"
                "# Case-insensitive\n"
                "assert missing_headers({'content-type': 'application/json'}, ['Content-Type']) == []\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Normalize both sides to lowercase for case-insensitive comparison.",
                "Use a set comprehension for the existing headers.",
            ],
        ),
    ]

    return TopicSection(
        title="Query Parameters and Headers",
        difficulty="Beginner",
        explanation=explanation,
        examples=examples,
        practice=practice,
        key_takeaways=[
            "Always pass query parameters as a dict to params= — never build URLs manually.",
            "Headers carry metadata: Content-Type, Accept, Authorization, X-API-Key.",
            "Use f'Bearer {token}' for Bearer token auth headers.",
            "requests URL-encodes params automatically, handling special characters.",
            "Check required headers before sending requests to catch config errors early.",
        ],
    )


# ---------------------------------------------------------------------------
# Mid-level sections
# ---------------------------------------------------------------------------

def _mid_level_sections() -> list[TopicSection]:
    return [
        _api_authentication(),
        _pagination_handling(),
        _error_handling_retry(),
        _nested_json_data(),
        _building_api_test_scripts(),
    ]


def _api_authentication() -> TopicSection:
    explanation = (
        "### API Authentication\n\n"
        "Most production APIs require authentication. The three most common "
        "patterns are API keys, Bearer tokens (OAuth2/JWT), and Basic auth.\n\n"
        "**API Key (header or query param):**\n"
        "```python\n"
        "# Header-based (preferred)\n"
        "headers = {'X-API-Key': 'your-api-key'}\n"
        "r = requests.get(url, headers=headers)\n\n"
        "# Query param (less secure — key visible in logs)\n"
        "r = requests.get(url, params={'api_key': 'your-api-key'})\n"
        "```\n\n"
        "**Bearer Token (OAuth2/JWT):**\n"
        "```python\n"
        "headers = {'Authorization': f'Bearer {access_token}'}\n"
        "r = requests.get(url, headers=headers)\n"
        "```\n\n"
        "**Basic Auth:**\n"
        "```python\n"
        "from requests.auth import HTTPBasicAuth\n"
        "r = requests.get(url, auth=HTTPBasicAuth('username', 'password'))\n"
        "# Or shorthand:\n"
        "r = requests.get(url, auth=('username', 'password'))\n"
        "```\n\n"
        "**Redfish API (nip-relevant):** Redfish is a REST-based management "
        "API for server hardware (BMC/iDRAC). It uses Basic auth or session "
        "tokens and follows standard HTTP conventions.\n\n"
        "**Token refresh pattern:** When a token expires (401 response), "
        "re-authenticate and retry the original request."
    )

    examples = [
        (
            "# --- API Key and Bearer token patterns (mock) ---\n"
            "def make_authenticated_request(\n"
            "    url: str,\n"
            "    auth_type: str,\n"
            "    credential: str,\n"
            "    mock_responses: dict,\n"
            ") -> dict:\n"
            "    \"\"\"\n"
            "    Simulate an authenticated request.\n"
            "    auth_type: 'api_key' | 'bearer' | 'basic'\n"
            "    \"\"\"\n"
            "    if auth_type == 'api_key':\n"
            "        headers = {'X-API-Key': credential}\n"
            "    elif auth_type == 'bearer':\n"
            "        headers = {'Authorization': f'Bearer {credential}'}\n"
            "    else:\n"
            "        headers = {}\n\n"
            "    # Simulate: valid credentials return 200, invalid return 401\n"
            "    if credential == 'invalid':\n"
            "        return {'status_code': 401, 'body': {'error': 'Unauthorized'}}\n"
            "    return {'status_code': 200, 'body': mock_responses.get(url, {})}\n\n"
            "mock_data = {'/api/systems': [{'id': 'sys1', 'status': 'OK'}]}\n"
            "resp = make_authenticated_request('/api/systems', 'bearer', 'valid-token', mock_data)\n"
            "print(resp)  # {'status_code': 200, 'body': [{'id': 'sys1', ...}]}\n\n"
            "resp_bad = make_authenticated_request('/api/systems', 'bearer', 'invalid', mock_data)\n"
            "print(resp_bad)  # {'status_code': 401, ...}"
        ),
        (
            "# --- Redfish API interaction pattern (nip-relevant) ---\n"
            "# Redfish is a REST API for server hardware management (BMC/iDRAC).\n"
            "# It uses Basic auth and returns JSON following the DMTF Redfish schema.\n\n"
            "MOCK_REDFISH_SYSTEMS = {\n"
            "    '@odata.context': '/redfish/v1/$metadata#ComputerSystemCollection',\n"
            "    '@odata.id': '/redfish/v1/Systems',\n"
            "    'Members': [\n"
            "        {'@odata.id': '/redfish/v1/Systems/1'},\n"
            "        {'@odata.id': '/redfish/v1/Systems/2'},\n"
            "    ],\n"
            "    'Members@odata.count': 2,\n"
            "}\n\n"
            "MOCK_REDFISH_SYSTEM_1 = {\n"
            "    '@odata.id': '/redfish/v1/Systems/1',\n"
            "    'Id': '1',\n"
            "    'Name': 'Compute Node 1',\n"
            "    'Status': {'State': 'Enabled', 'Health': 'OK'},\n"
            "    'PowerState': 'On',\n"
            "    'ProcessorSummary': {'Count': 2, 'Model': 'Intel Xeon'},\n"
            "    'MemorySummary': {'TotalSystemMemoryGiB': 256},\n"
            "}\n\n"
            "def get_redfish_system_health(system_data: dict) -> str:\n"
            "    \"\"\"Extract health status from a Redfish System resource.\"\"\"\n"
            "    return system_data.get('Status', {}).get('Health', 'Unknown')\n\n"
            "def list_redfish_system_ids(collection: dict) -> list[str]:\n"
            "    \"\"\"Extract system IDs from a Redfish Systems collection.\"\"\"\n"
            "    return [\n"
            "        member['@odata.id'].split('/')[-1]\n"
            "        for member in collection.get('Members', [])\n"
            "    ]\n\n"
            "print(get_redfish_system_health(MOCK_REDFISH_SYSTEM_1))  # 'OK'\n"
            "print(list_redfish_system_ids(MOCK_REDFISH_SYSTEMS))     # ['1', '2']"
        ),
    ]

    practice = [
        PracticeProblem(
            title="Build Auth Headers",
            statement=(
                "Write a function that builds an Authorization header dict "
                "based on the auth type. Supported types: 'bearer' (returns "
                "{'Authorization': 'Bearer <token>'}), 'api_key' (returns "
                "{'X-API-Key': '<token>'}), 'basic' (returns "
                "{'Authorization': 'Basic <token>'}). Raise ValueError for "
                "unknown auth types."
            ),
            function_signature=(
                "def build_auth_header(auth_type: str, token: str) -> dict:"
            ),
            examples=[
                {"input": "'bearer', 'abc123'", "output": "{'Authorization': 'Bearer abc123'}"},
                {"input": "'api_key', 'xyz'", "output": "{'X-API-Key': 'xyz'}"},
            ],
            solution_code=(
                "def build_auth_header(auth_type: str, token: str) -> dict:\n"
                "    \"\"\"Build an auth header dict for the given auth type.\"\"\"\n"
                "    if auth_type == 'bearer':\n"
                "        return {'Authorization': f'Bearer {token}'}\n"
                "    elif auth_type == 'api_key':\n"
                "        return {'X-API-Key': token}\n"
                "    elif auth_type == 'basic':\n"
                "        return {'Authorization': f'Basic {token}'}\n"
                "    raise ValueError(f'Unknown auth type: {auth_type!r}')"
            ),
            test_code=(
                "assert build_auth_header('bearer', 'abc123') == {'Authorization': 'Bearer abc123'}\n"
                "assert build_auth_header('api_key', 'xyz') == {'X-API-Key': 'xyz'}\n"
                "assert build_auth_header('basic', 'dXNlcjpwYXNz') == {'Authorization': 'Basic dXNlcjpwYXNz'}\n"
                "try:\n"
                "    build_auth_header('oauth', 'token')\n"
                "    assert False, 'Should have raised ValueError'\n"
                "except ValueError:\n"
                "    pass\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Use if/elif for each auth type.",
                "Raise ValueError with a descriptive message for unknown types.",
            ],
        ),
        PracticeProblem(
            title="Handle Token Expiry",
            statement=(
                "Write a function that simulates token refresh logic. Given "
                "a response dict with 'status_code', if the status is 401, "
                "call the provided refresh_token() function (no args, returns "
                "a new token string) and return the new token. Otherwise "
                "return None (no refresh needed)."
            ),
            function_signature=(
                "def refresh_if_expired(response: dict, refresh_token) -> str | None:"
            ),
            examples=[
                {
                    "input": "{'status_code': 401, 'body': {}}, lambda: 'new-token-xyz'",
                    "output": "'new-token-xyz'",
                },
                {
                    "input": "{'status_code': 200, 'body': {'data': []}}, lambda: 'new-token'",
                    "output": "None",
                },
            ],
            solution_code=(
                "def refresh_if_expired(response: dict, refresh_token) -> str | None:\n"
                "    \"\"\"Call refresh_token() if response is 401, else return None.\"\"\"\n"
                "    if response.get('status_code') == 401:\n"
                "        return refresh_token()\n"
                "    return None"
            ),
            test_code=(
                "resp_401 = {'status_code': 401, 'body': {}}\n"
                "resp_200 = {'status_code': 200, 'body': {'data': []}}\n"
                "assert refresh_if_expired(resp_401, lambda: 'new-token-xyz') == 'new-token-xyz'\n"
                "assert refresh_if_expired(resp_200, lambda: 'new-token') is None\n"
                "assert refresh_if_expired(resp_401, lambda: 'refreshed') == 'refreshed'\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Check response['status_code'] == 401.",
                "Call refresh_token() (it's a callable passed as a parameter).",
            ],
        ),
        PracticeProblem(
            title="Extract Redfish System Health",
            statement=(
                "Given a list of Redfish System resource dicts (each with a "
                "nested 'Status' dict containing 'Health' and 'State'), "
                "return a list of dicts with 'id' (from the 'Id' field) and "
                "'health' (from Status.Health). Use 'Unknown' if Health is missing."
            ),
            function_signature=(
                "def extract_system_health(systems: list[dict]) -> list[dict]:"
            ),
            examples=[
                {
                    "input": (
                        "[{'Id': '1', 'Status': {'Health': 'OK', 'State': 'Enabled'}}, "
                        "{'Id': '2', 'Status': {'Health': 'Warning', 'State': 'Enabled'}}, "
                        "{'Id': '3'}]"
                    ),
                    "output": (
                        "[{'id': '1', 'health': 'OK'}, "
                        "{'id': '2', 'health': 'Warning'}, "
                        "{'id': '3', 'health': 'Unknown'}]"
                    ),
                },
            ],
            solution_code=(
                "def extract_system_health(systems: list[dict]) -> list[dict]:\n"
                "    \"\"\"Extract id and health from Redfish System resources.\"\"\"\n"
                "    return [\n"
                "        {\n"
                "            'id': s.get('Id', 'unknown'),\n"
                "            'health': s.get('Status', {}).get('Health', 'Unknown'),\n"
                "        }\n"
                "        for s in systems\n"
                "    ]"
            ),
            test_code=(
                "systems = [\n"
                "    {'Id': '1', 'Status': {'Health': 'OK',      'State': 'Enabled'}},\n"
                "    {'Id': '2', 'Status': {'Health': 'Warning', 'State': 'Enabled'}},\n"
                "    {'Id': '3'},\n"
                "]\n"
                "result = extract_system_health(systems)\n"
                "assert result[0] == {'id': '1', 'health': 'OK'}\n"
                "assert result[1] == {'id': '2', 'health': 'Warning'}\n"
                "assert result[2] == {'id': '3', 'health': 'Unknown'}\n"
                "assert extract_system_health([]) == []\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Use .get('Status', {}).get('Health', 'Unknown') for safe nested access.",
                "Build a list comprehension returning dicts.",
            ],
        ),
        PracticeProblem(
            title="Mask Sensitive Headers",
            statement=(
                "Write a function that takes a headers dict and returns a "
                "copy with sensitive header values replaced by '***'. "
                "Sensitive headers (case-insensitive): 'Authorization', "
                "'X-API-Key', 'X-Auth-Token'."
            ),
            function_signature=(
                "def mask_sensitive_headers(headers: dict) -> dict:"
            ),
            examples=[
                {
                    "input": (
                        "{'Content-Type': 'application/json', "
                        "'Authorization': 'Bearer secret', "
                        "'X-API-Key': 'my-key'}"
                    ),
                    "output": (
                        "{'Content-Type': 'application/json', "
                        "'Authorization': '***', "
                        "'X-API-Key': '***'}"
                    ),
                },
            ],
            solution_code=(
                "def mask_sensitive_headers(headers: dict) -> dict:\n"
                "    \"\"\"Return headers dict with sensitive values masked.\"\"\"\n"
                "    sensitive = {'authorization', 'x-api-key', 'x-auth-token'}\n"
                "    return {\n"
                "        k: '***' if k.lower() in sensitive else v\n"
                "        for k, v in headers.items()\n"
                "    }"
            ),
            test_code=(
                "h = {\n"
                "    'Content-Type': 'application/json',\n"
                "    'Authorization': 'Bearer secret',\n"
                "    'X-API-Key': 'my-key',\n"
                "    'Accept': 'application/json',\n"
                "}\n"
                "masked = mask_sensitive_headers(h)\n"
                "assert masked['Content-Type'] == 'application/json'\n"
                "assert masked['Authorization'] == '***'\n"
                "assert masked['X-API-Key'] == '***'\n"
                "assert masked['Accept'] == 'application/json'\n"
                "# Original unchanged\n"
                "assert h['Authorization'] == 'Bearer secret'\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Use a dict comprehension with a conditional expression.",
                "Normalize keys to lowercase for case-insensitive matching.",
            ],
        ),
    ]

    return TopicSection(
        title="API Authentication",
        difficulty="Mid-Level",
        explanation=explanation,
        examples=examples,
        practice=practice,
        key_takeaways=[
            "Bearer tokens go in the Authorization header: 'Bearer <token>'.",
            "API keys can be in headers (X-API-Key) or query params — prefer headers.",
            "Basic auth encodes 'username:password' in base64 in the Authorization header.",
            "Handle 401 responses by refreshing the token and retrying.",
            "Redfish uses Basic auth or session tokens for server hardware management APIs.",
        ],
    )


def _pagination_handling() -> TopicSection:
    explanation = (
        "### Pagination Handling\n\n"
        "APIs rarely return all results in one response. Pagination limits "
        "response size and protects server resources. You must loop to collect "
        "all data.\n\n"
        "**Three common pagination styles:**\n\n"
        "1. **Page-based:** `?page=1&per_page=20` — increment page until empty\n"
        "```python\n"
        "page = 1\n"
        "all_items = []\n"
        "while True:\n"
        "    r = requests.get(url, params={'page': page, 'per_page': 20})\n"
        "    items = r.json()\n"
        "    if not items:\n"
        "        break\n"
        "    all_items.extend(items)\n"
        "    page += 1\n"
        "```\n\n"
        "2. **Offset-based:** `?offset=0&limit=20` — increment offset by limit\n"
        "```python\n"
        "offset, limit = 0, 20\n"
        "all_items = []\n"
        "while True:\n"
        "    r = requests.get(url, params={'offset': offset, 'limit': limit})\n"
        "    items = r.json()\n"
        "    if not items:\n"
        "        break\n"
        "    all_items.extend(items)\n"
        "    offset += limit\n"
        "```\n\n"
        "3. **Cursor-based:** Response includes a `next_cursor` or `next` URL\n"
        "```python\n"
        "cursor = None\n"
        "all_items = []\n"
        "while True:\n"
        "    params = {'cursor': cursor} if cursor else {}\n"
        "    data = requests.get(url, params=params).json()\n"
        "    all_items.extend(data['items'])\n"
        "    cursor = data.get('next_cursor')\n"
        "    if not cursor:\n"
        "        break\n"
        "```\n\n"
        "**HackerRank pattern:** Most HackerRank REST API problems use "
        "page-based pagination. The loop terminates when the response is "
        "an empty list or when `page > total_pages`."
    )

    examples = [
        (
            "# --- Page-based pagination (mock) ---\n"
            "# Simulates a paginated API with 7 total items, 3 per page\n"
            "ALL_USERS = [\n"
            "    {'id': i, 'name': f'User {i}', 'active': i % 2 == 0}\n"
            "    for i in range(1, 8)\n"
            "]\n\n"
            "def mock_paginated_api(page: int, per_page: int = 3) -> list[dict]:\n"
            "    \"\"\"Simulate GET /users?page=N&per_page=3.\"\"\"\n"
            "    start = (page - 1) * per_page\n"
            "    return ALL_USERS[start:start + per_page]\n\n"
            "def fetch_all_users() -> list[dict]:\n"
            "    \"\"\"Fetch all users across all pages.\"\"\"\n"
            "    all_users = []\n"
            "    page = 1\n"
            "    while True:\n"
            "        users = mock_paginated_api(page)\n"
            "        if not users:\n"
            "            break\n"
            "        all_users.extend(users)\n"
            "        page += 1\n"
            "    return all_users\n\n"
            "all_users = fetch_all_users()\n"
            "print(f'Total users fetched: {len(all_users)}')  # 7\n"
            "print([u['id'] for u in all_users])              # [1, 2, 3, 4, 5, 6, 7]"
        ),
        (
            "# --- Offset-based pagination with filtering (mock) ---\n"
            "POSTS = [\n"
            "    {'id': i, 'userId': (i % 3) + 1, 'title': f'Post {i}', 'views': i * 10}\n"
            "    for i in range(1, 16)\n"
            "]\n\n"
            "def mock_posts_api(offset: int, limit: int = 5) -> list[dict]:\n"
            "    \"\"\"Simulate GET /posts?offset=N&limit=5.\"\"\"\n"
            "    return POSTS[offset:offset + limit]\n\n"
            "def fetch_all_posts_paginated(limit: int = 5) -> list[dict]:\n"
            "    \"\"\"Collect all posts using offset pagination.\"\"\"\n"
            "    all_posts = []\n"
            "    offset = 0\n"
            "    while True:\n"
            "        batch = mock_posts_api(offset, limit)\n"
            "        if not batch:\n"
            "            break\n"
            "        all_posts.extend(batch)\n"
            "        offset += limit\n"
            "    return all_posts\n\n"
            "all_posts = fetch_all_posts_paginated()\n"
            "print(f'Total posts: {len(all_posts)}')  # 15\n\n"
            "# Aggregate: total views across all posts\n"
            "total_views = sum(p['views'] for p in all_posts)\n"
            "print(f'Total views: {total_views}')"
        ),
    ]

    practice = [
        PracticeProblem(
            title="Fetch All Pages",
            statement=(
                "Given a function `get_page(page: int) -> list[dict]` that "
                "returns a page of items (empty list on last page), write a "
                "function that collects all items across all pages and returns "
                "them as a single list."
            ),
            function_signature=(
                "def fetch_all(get_page) -> list[dict]:"
            ),
            examples=[
                {
                    "input": "get_page that returns [1,2,3] for page 1, [4,5] for page 2, [] for page 3",
                    "output": "[1, 2, 3, 4, 5]",
                },
            ],
            solution_code=(
                "def fetch_all(get_page) -> list[dict]:\n"
                "    \"\"\"Collect all items from a paginated API.\"\"\"\n"
                "    all_items = []\n"
                "    page = 1\n"
                "    while True:\n"
                "        items = get_page(page)\n"
                "        if not items:\n"
                "            break\n"
                "        all_items.extend(items)\n"
                "        page += 1\n"
                "    return all_items"
            ),
            test_code=(
                "pages = {1: [1, 2, 3], 2: [4, 5], 3: []}\n"
                "def get_page(p): return pages.get(p, [])\n"
                "assert fetch_all(get_page) == [1, 2, 3, 4, 5]\n\n"
                "# Empty first page\n"
                "assert fetch_all(lambda p: []) == []\n\n"
                "# Single page\n"
                "single = {1: ['a', 'b'], 2: []}\n"
                "assert fetch_all(lambda p: single.get(p, [])) == ['a', 'b']\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Start with page=1 and loop until get_page returns an empty list.",
                "Use list.extend() to add each page's items to the accumulator.",
            ],
        ),
        PracticeProblem(
            title="Filter Across Paginated Results",
            statement=(
                "Given a list of pages (each page is a list of user dicts "
                "with 'id', 'name', 'active'), return a list of names of "
                "all active users across all pages."
            ),
            function_signature=(
                "def active_users_from_pages(pages: list[list[dict]]) -> list[str]:"
            ),
            examples=[
                {
                    "input": (
                        "[[{'id': 1, 'name': 'Alice', 'active': True}, "
                        "{'id': 2, 'name': 'Bob', 'active': False}], "
                        "[{'id': 3, 'name': 'Carol', 'active': True}]]"
                    ),
                    "output": "['Alice', 'Carol']",
                },
            ],
            solution_code=(
                "def active_users_from_pages(pages: list[list[dict]]) -> list[str]:\n"
                "    \"\"\"Collect names of active users across all pages.\"\"\"\n"
                "    return [\n"
                "        user['name']\n"
                "        for page in pages\n"
                "        for user in page\n"
                "        if user.get('active')\n"
                "    ]"
            ),
            test_code=(
                "pages = [\n"
                "    [{'id': 1, 'name': 'Alice', 'active': True},\n"
                "     {'id': 2, 'name': 'Bob',   'active': False}],\n"
                "    [{'id': 3, 'name': 'Carol', 'active': True},\n"
                "     {'id': 4, 'name': 'Dave',  'active': False}],\n"
                "]\n"
                "assert active_users_from_pages(pages) == ['Alice', 'Carol']\n"
                "assert active_users_from_pages([]) == []\n"
                "assert active_users_from_pages([[{'id': 1, 'name': 'X', 'active': False}]]) == []\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Use a nested list comprehension: for page in pages, for user in page.",
                "Add an if condition to filter active users.",
            ],
        ),
        PracticeProblem(
            title="Aggregate Paginated Totals",
            statement=(
                "Given a function `get_page(page: int) -> dict` that returns "
                "{'items': [...], 'total_pages': N}, write a function that "
                "fetches all pages and returns the total count of items."
            ),
            function_signature=(
                "def count_all_items(get_page) -> int:"
            ),
            examples=[
                {
                    "input": "get_page returning 3 items on page 1, 2 items on page 2, total_pages=2",
                    "output": "5",
                },
            ],
            solution_code=(
                "def count_all_items(get_page) -> int:\n"
                "    \"\"\"Count total items across all pages.\"\"\"\n"
                "    total = 0\n"
                "    page = 1\n"
                "    while True:\n"
                "        data = get_page(page)\n"
                "        items = data.get('items', [])\n"
                "        total += len(items)\n"
                "        if page >= data.get('total_pages', 1):\n"
                "            break\n"
                "        page += 1\n"
                "    return total"
            ),
            test_code=(
                "def make_api(pages_data):\n"
                "    total = len(pages_data)\n"
                "    def get_page(p):\n"
                "        return {'items': pages_data[p - 1], 'total_pages': total}\n"
                "    return get_page\n\n"
                "api = make_api([[1, 2, 3], [4, 5]])\n"
                "assert count_all_items(api) == 5\n\n"
                "api_single = make_api([[10, 20]])\n"
                "assert count_all_items(api_single) == 2\n\n"
                "api_empty = make_api([[]])\n"
                "assert count_all_items(api_empty) == 0\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Check page >= total_pages to know when to stop.",
                "Accumulate len(items) each iteration.",
            ],
        ),
        PracticeProblem(
            title="Find Item Across Pages",
            statement=(
                "Given a list of pages (each a list of dicts with 'id' and "
                "'value'), and a target id, return the 'value' of the item "
                "with that id. Return None if not found."
            ),
            function_signature=(
                "def find_across_pages(pages: list[list[dict]], target_id: int) -> object:"
            ),
            examples=[
                {
                    "input": (
                        "[[{'id': 1, 'value': 'a'}, {'id': 2, 'value': 'b'}], "
                        "[{'id': 3, 'value': 'c'}]], 2"
                    ),
                    "output": "'b'",
                },
                {
                    "input": "[[{'id': 1, 'value': 'a'}]], 99",
                    "output": "None",
                },
            ],
            solution_code=(
                "def find_across_pages(pages: list[list[dict]], target_id: int) -> object:\n"
                "    \"\"\"Search for an item by id across all pages.\"\"\"\n"
                "    for page in pages:\n"
                "        for item in page:\n"
                "            if item['id'] == target_id:\n"
                "                return item['value']\n"
                "    return None"
            ),
            test_code=(
                "pages = [\n"
                "    [{'id': 1, 'value': 'a'}, {'id': 2, 'value': 'b'}],\n"
                "    [{'id': 3, 'value': 'c'}],\n"
                "]\n"
                "assert find_across_pages(pages, 2) == 'b'\n"
                "assert find_across_pages(pages, 3) == 'c'\n"
                "assert find_across_pages(pages, 99) is None\n"
                "assert find_across_pages([], 1) is None\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Use nested for loops: for page in pages, for item in page.",
                "Return early when found; return None after all pages exhausted.",
            ],
        ),
    ]

    return TopicSection(
        title="Pagination Handling",
        difficulty="Mid-Level",
        explanation=explanation,
        examples=examples,
        practice=practice,
        key_takeaways=[
            "Always loop to collect all pages — never assume one response has everything.",
            "Page-based: increment page until empty list. Offset-based: increment offset by limit.",
            "Cursor-based pagination uses a token from the response to fetch the next page.",
            "Use list.extend() (not append) to add a page's items to the accumulator.",
            "HackerRank REST problems almost always involve pagination — master this pattern.",
        ],
    )


def _error_handling_retry() -> TopicSection:
    explanation = (
        "### Error Handling and Retry Logic\n\n"
        "Robust API clients handle failures gracefully. Network issues, "
        "rate limits, and transient server errors are common in production.\n\n"
        "**Status code checking:**\n"
        "```python\n"
        "r = requests.get(url, timeout=10)\n"
        "r.raise_for_status()  # raises HTTPError for 4xx/5xx\n"
        "# Or manually:\n"
        "if r.status_code != 200:\n"
        "    raise ValueError(f'API error: {r.status_code}')\n"
        "```\n\n"
        "**Timeout handling:**\n"
        "```python\n"
        "try:\n"
        "    r = requests.get(url, timeout=5)\n"
        "except requests.Timeout:\n"
        "    print('Request timed out')\n"
        "except requests.ConnectionError:\n"
        "    print('Network error')\n"
        "```\n\n"
        "**Exponential backoff retry:**\n"
        "```python\n"
        "import time\n\n"
        "def get_with_retry(url, max_retries=3, backoff=1.0):\n"
        "    for attempt in range(max_retries):\n"
        "        r = requests.get(url, timeout=10)\n"
        "        if r.status_code == 200:\n"
        "            return r.json()\n"
        "        if r.status_code == 429:  # rate limited\n"
        "            time.sleep(backoff * (2 ** attempt))\n"
        "        else:\n"
        "            break  # non-retryable error\n"
        "    raise RuntimeError(f'Failed after {max_retries} attempts')\n"
        "```\n\n"
        "**Retryable vs non-retryable errors:**\n"
        "- Retry: `429 Too Many Requests`, `503 Service Unavailable`, network timeouts\n"
        "- Don't retry: `400 Bad Request`, `401 Unauthorized`, `403 Forbidden`, `404 Not Found`"
    )

    examples = [
        (
            "# --- Retry with exponential backoff (mock) ---\n"
            "import time\n\n"
            "def get_with_retry(\n"
            "    fetch_fn,          # callable(attempt) -> dict with 'status_code'\n"
            "    max_retries: int = 3,\n"
            "    base_delay: float = 0.0,  # 0 for tests; use 1.0 in production\n"
            ") -> dict:\n"
            "    \"\"\"\n"
            "    Retry a request with exponential backoff on 429/5xx errors.\n"
            "    Returns the response dict on success.\n"
            "    Raises RuntimeError after max_retries exhausted.\n"
            "    \"\"\"\n"
            "    retryable = {429, 500, 502, 503, 504}\n"
            "    for attempt in range(max_retries):\n"
            "        response = fetch_fn(attempt)\n"
            "        code = response['status_code']\n"
            "        if code == 200:\n"
            "            return response\n"
            "        if code in retryable:\n"
            "            delay = base_delay * (2 ** attempt)\n"
            "            if delay > 0:\n"
            "                time.sleep(delay)\n"
            "            continue\n"
            "        # Non-retryable (4xx except 429)\n"
            "        raise ValueError(f'Non-retryable error: {code}')\n"
            "    raise RuntimeError(f'Failed after {max_retries} attempts')\n\n"
            "# Simulate: fails twice with 503, then succeeds\n"
            "call_count = [0]\n"
            "def flaky_api(attempt):\n"
            "    call_count[0] += 1\n"
            "    if call_count[0] < 3:\n"
            "        return {'status_code': 503, 'body': {}}\n"
            "    return {'status_code': 200, 'body': {'data': 'success'}}\n\n"
            "result = get_with_retry(flaky_api, max_retries=3, base_delay=0)\n"
            "print(result)          # {'status_code': 200, 'body': {'data': 'success'}}\n"
            "print(call_count[0])   # 3"
        ),
        (
            "# --- Comprehensive error handling pattern ---\n"
            "def safe_api_call(fetch_fn, url: str) -> dict | None:\n"
            "    \"\"\"\n"
            "    Make an API call with full error handling.\n"
            "    Returns parsed JSON on success, None on failure.\n"
            "    \"\"\"\n"
            "    try:\n"
            "        response = fetch_fn(url)\n"
            "        status = response.get('status_code', 0)\n\n"
            "        if status == 200:\n"
            "            return response.get('body')\n"
            "        elif status == 401:\n"
            "            print(f'Authentication failed for {url}')\n"
            "        elif status == 403:\n"
            "            print(f'Access forbidden: {url}')\n"
            "        elif status == 404:\n"
            "            print(f'Resource not found: {url}')\n"
            "        elif status == 429:\n"
            "            print(f'Rate limited — slow down requests to {url}')\n"
            "        elif status >= 500:\n"
            "            print(f'Server error {status} for {url}')\n"
            "        return None\n"
            "    except Exception as e:\n"
            "        print(f'Request failed: {e}')\n"
            "        return None\n\n"
            "# Test it\n"
            "def mock_fetch(url):\n"
            "    return {'status_code': 200, 'body': {'result': 42}}\n\n"
            "data = safe_api_call(mock_fetch, '/api/data')\n"
            "print(data)  # {'result': 42}"
        ),
    ]

    practice = [
        PracticeProblem(
            title="Retry Until Success",
            statement=(
                "Write a function that calls `fetch()` (no args, returns a "
                "dict with 'status_code') up to `max_retries` times. Return "
                "the response dict when status_code is 200. If all attempts "
                "fail, return the last response dict."
            ),
            function_signature=(
                "def retry_until_success(fetch, max_retries: int = 3) -> dict:"
            ),
            examples=[
                {
                    "input": "fetch that fails twice then returns 200, max_retries=3",
                    "output": "{'status_code': 200, 'body': 'ok'}",
                },
            ],
            solution_code=(
                "def retry_until_success(fetch, max_retries: int = 3) -> dict:\n"
                "    \"\"\"Retry fetch() up to max_retries times, return first 200 or last response.\"\"\"\n"
                "    response = {'status_code': 0}\n"
                "    for _ in range(max_retries):\n"
                "        response = fetch()\n"
                "        if response.get('status_code') == 200:\n"
                "            return response\n"
                "    return response"
            ),
            test_code=(
                "# Succeeds on 3rd attempt\n"
                "attempts = [0]\n"
                "def flaky():\n"
                "    attempts[0] += 1\n"
                "    if attempts[0] < 3:\n"
                "        return {'status_code': 503}\n"
                "    return {'status_code': 200, 'body': 'ok'}\n\n"
                "result = retry_until_success(flaky, max_retries=3)\n"
                "assert result['status_code'] == 200\n\n"
                "# Always fails — returns last response\n"
                "always_fail = lambda: {'status_code': 500}\n"
                "result2 = retry_until_success(always_fail, max_retries=2)\n"
                "assert result2['status_code'] == 500\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Loop max_retries times, return early on status 200.",
                "Keep track of the last response to return if all attempts fail.",
            ],
        ),
        PracticeProblem(
            title="Classify Retryable Errors",
            statement=(
                "Write a function that takes a status code and returns True "
                "if the error is retryable, False otherwise. Retryable codes: "
                "429, 500, 502, 503, 504. All other codes are not retryable."
            ),
            function_signature="def is_retryable(status_code: int) -> bool:",
            examples=[
                {"input": "429", "output": "True"},
                {"input": "503", "output": "True"},
                {"input": "404", "output": "False"},
                {"input": "200", "output": "False"},
            ],
            solution_code=(
                "def is_retryable(status_code: int) -> bool:\n"
                "    \"\"\"Return True if the status code indicates a retryable error.\"\"\"\n"
                "    return status_code in {429, 500, 502, 503, 504}"
            ),
            test_code=(
                "assert is_retryable(429) == True\n"
                "assert is_retryable(500) == True\n"
                "assert is_retryable(502) == True\n"
                "assert is_retryable(503) == True\n"
                "assert is_retryable(504) == True\n"
                "assert is_retryable(200) == False\n"
                "assert is_retryable(404) == False\n"
                "assert is_retryable(401) == False\n"
                "assert is_retryable(403) == False\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Use a set for O(1) membership testing.",
            ],
        ),
        PracticeProblem(
            title="Compute Backoff Delay",
            statement=(
                "Write a function that computes the exponential backoff delay "
                "in seconds for a given attempt number (0-indexed). Formula: "
                "`base * (2 ** attempt)`. Cap the result at `max_delay` seconds."
            ),
            function_signature=(
                "def backoff_delay(attempt: int, base: float = 1.0, max_delay: float = 60.0) -> float:"
            ),
            examples=[
                {"input": "0, base=1.0", "output": "1.0"},
                {"input": "3, base=1.0", "output": "8.0"},
                {"input": "10, base=1.0, max_delay=60.0", "output": "60.0"},
            ],
            solution_code=(
                "def backoff_delay(attempt: int, base: float = 1.0, max_delay: float = 60.0) -> float:\n"
                "    \"\"\"Compute exponential backoff delay, capped at max_delay.\"\"\"\n"
                "    return min(base * (2 ** attempt), max_delay)"
            ),
            test_code=(
                "assert backoff_delay(0) == 1.0\n"
                "assert backoff_delay(1) == 2.0\n"
                "assert backoff_delay(2) == 4.0\n"
                "assert backoff_delay(3) == 8.0\n"
                "assert backoff_delay(10) == 60.0  # capped\n"
                "assert backoff_delay(0, base=0.5) == 0.5\n"
                "assert backoff_delay(3, base=2.0, max_delay=10.0) == 10.0  # capped\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Use min() to cap the result at max_delay.",
                "Formula: base * (2 ** attempt).",
            ],
        ),
        PracticeProblem(
            title="Parse Error Response",
            statement=(
                "Given an API error response dict with 'status_code' and "
                "optionally 'error' (str) and 'message' (str), return a "
                "human-readable error string in the format: "
                "'HTTP {code}: {error} - {message}'. Use 'Unknown Error' "
                "if 'error' is missing, and 'No details' if 'message' is missing."
            ),
            function_signature=(
                "def format_error(response: dict) -> str:"
            ),
            examples=[
                {
                    "input": "{'status_code': 404, 'error': 'Not Found', 'message': 'User does not exist'}",
                    "output": "'HTTP 404: Not Found - User does not exist'",
                },
                {
                    "input": "{'status_code': 500}",
                    "output": "'HTTP 500: Unknown Error - No details'",
                },
            ],
            solution_code=(
                "def format_error(response: dict) -> str:\n"
                "    \"\"\"Format an API error response as a human-readable string.\"\"\"\n"
                "    code = response.get('status_code', 0)\n"
                "    error = response.get('error', 'Unknown Error')\n"
                "    message = response.get('message', 'No details')\n"
                "    return f'HTTP {code}: {error} - {message}'"
            ),
            test_code=(
                "r1 = {'status_code': 404, 'error': 'Not Found', 'message': 'User does not exist'}\n"
                "assert format_error(r1) == 'HTTP 404: Not Found - User does not exist'\n\n"
                "r2 = {'status_code': 500}\n"
                "assert format_error(r2) == 'HTTP 500: Unknown Error - No details'\n\n"
                "r3 = {'status_code': 401, 'error': 'Unauthorized'}\n"
                "assert format_error(r3) == 'HTTP 401: Unauthorized - No details'\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Use .get() with default values for optional fields.",
                "Use an f-string to format the output.",
            ],
        ),
    ]

    return TopicSection(
        title="Error Handling and Retry Logic",
        difficulty="Mid-Level",
        explanation=explanation,
        examples=examples,
        practice=practice,
        key_takeaways=[
            "Always set a timeout on requests to avoid hanging indefinitely.",
            "Retryable errors: 429, 500, 502, 503, 504. Non-retryable: 400, 401, 403, 404.",
            "Exponential backoff: delay = base * 2^attempt — prevents overwhelming the server.",
            "Use raise_for_status() for concise error checking, or check status_code manually.",
            "Catch requests.Timeout and requests.ConnectionError for network-level failures.",
        ],
    )


def _nested_json_data() -> TopicSection:
    explanation = (
        "### Nested JSON Data\n\n"
        "Real-world API responses are often deeply nested. Mastering "
        "techniques for safe access, flattening, and field extraction "
        "is essential.\n\n"
        "**Deep access patterns:**\n"
        "```python\n"
        "# Chained access (raises KeyError if any key missing)\n"
        "city = data['user']['address']['city']\n\n"
        "# Safe chained access\n"
        "city = data.get('user', {}).get('address', {}).get('city', 'N/A')\n\n"
        "# Using a helper for arbitrary depth\n"
        "def deep_get(d, *keys, default=None):\n"
        "    for key in keys:\n"
        "        if not isinstance(d, dict):\n"
        "            return default\n"
        "        d = d.get(key, default)\n"
        "    return d\n\n"
        "city = deep_get(data, 'user', 'address', 'city', default='N/A')\n"
        "```\n\n"
        "**Flattening nested structures:**\n"
        "```python\n"
        "# Flatten a list of lists\n"
        "flat = [item for sublist in nested for item in sublist]\n\n"
        "# Flatten a dict of lists\n"
        "all_items = [item for items in d.values() for item in items]\n"
        "```\n\n"
        "**Extracting fields from nested arrays:**\n"
        "```python\n"
        "# Get all tag names from posts with nested tags list\n"
        "all_tags = [tag for post in posts for tag in post.get('tags', [])]\n"
        "```"
    )

    examples = [
        (
            "# --- Deep access helper ---\n"
            "def deep_get(d: dict, *keys, default=None):\n"
            "    \"\"\"Safely access nested dict keys.\"\"\"\n"
            "    for key in keys:\n"
            "        if not isinstance(d, dict):\n"
            "            return default\n"
            "        d = d.get(key, default)\n"
            "        if d is default:\n"
            "            return default\n"
            "    return d\n\n"
            "# Complex nested response (e.g., from a CI/CD API)\n"
            "build_response = {\n"
            "    'build': {\n"
            "        'id': 'build-42',\n"
            "        'status': 'failed',\n"
            "        'stages': [\n"
            "            {'name': 'compile', 'result': 'passed', 'duration_s': 12},\n"
            "            {'name': 'test',    'result': 'failed', 'duration_s': 45},\n"
            "            {'name': 'deploy',  'result': 'skipped','duration_s': 0},\n"
            "        ],\n"
            "        'metadata': {\n"
            "            'triggered_by': 'push',\n"
            "            'branch': 'main',\n"
            "            'commit': {'sha': 'abc123', 'author': 'alice'},\n"
            "        },\n"
            "    }\n"
            "}\n\n"
            "print(deep_get(build_response, 'build', 'status'))              # 'failed'\n"
            "print(deep_get(build_response, 'build', 'metadata', 'branch'))  # 'main'\n"
            "print(deep_get(build_response, 'build', 'metadata', 'commit', 'author'))  # 'alice'\n"
            "print(deep_get(build_response, 'build', 'missing_key', default='N/A'))    # 'N/A'\n\n"
            "# Extract failed stages\n"
            "stages = build_response['build']['stages']\n"
            "failed = [s['name'] for s in stages if s['result'] == 'failed']\n"
            "print(failed)  # ['test']"
        ),
        (
            "# --- Flattening nested arrays ---\n"
            "# API response: users with multiple roles\n"
            "users_with_roles = [\n"
            "    {'id': 1, 'name': 'Alice', 'roles': ['admin', 'developer']},\n"
            "    {'id': 2, 'name': 'Bob',   'roles': ['viewer']},\n"
            "    {'id': 3, 'name': 'Carol', 'roles': ['developer', 'tester']},\n"
            "]\n\n"
            "# All unique roles across all users\n"
            "all_roles = list({role for user in users_with_roles for role in user['roles']})\n"
            "print(sorted(all_roles))  # ['admin', 'developer', 'tester', 'viewer']\n\n"
            "# Users who have the 'developer' role\n"
            "devs = [u['name'] for u in users_with_roles if 'developer' in u['roles']]\n"
            "print(devs)  # ['Alice', 'Carol']\n\n"
            "# Flatten: list of (user_name, role) pairs\n"
            "pairs = [(u['name'], role) for u in users_with_roles for role in u['roles']]\n"
            "print(pairs[:3])  # [('Alice', 'admin'), ('Alice', 'developer'), ('Bob', 'viewer')]"
        ),
    ]

    practice = [
        PracticeProblem(
            title="Deep Get Utility",
            statement=(
                "Implement a `deep_get(d, *keys, default=None)` function that "
                "safely traverses a nested dict using the provided keys. "
                "Return `default` if any key is missing or if an intermediate "
                "value is not a dict."
            ),
            function_signature=(
                "def deep_get(d: dict, *keys, default=None):"
            ),
            examples=[
                {
                    "input": "{'a': {'b': {'c': 42}}}, 'a', 'b', 'c'",
                    "output": "42",
                },
                {
                    "input": "{'a': {'b': 1}}, 'a', 'x', default='missing'",
                    "output": "'missing'",
                },
            ],
            solution_code=(
                "def deep_get(d: dict, *keys, default=None):\n"
                "    \"\"\"Safely traverse nested dicts, returning default if any key is missing.\"\"\"\n"
                "    current = d\n"
                "    for key in keys:\n"
                "        if not isinstance(current, dict):\n"
                "            return default\n"
                "        current = current.get(key, default)\n"
                "        if current is default:\n"
                "            return default\n"
                "    return current"
            ),
            test_code=(
                "assert deep_get({'a': {'b': {'c': 42}}}, 'a', 'b', 'c') == 42\n"
                "assert deep_get({'a': {'b': 1}}, 'a', 'x', default='missing') == 'missing'\n"
                "assert deep_get({}, 'a', default=0) == 0\n"
                "assert deep_get({'a': None}, 'a', 'b', default='N/A') == 'N/A'\n"
                "assert deep_get({'x': 5}, 'x') == 5\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Iterate through keys, updating current at each step.",
                "Check isinstance(current, dict) before calling .get().",
            ],
        ),
        PracticeProblem(
            title="Extract All Tags",
            statement=(
                "Given a list of article dicts, each with a 'tags' key "
                "containing a list of strings, return a sorted list of all "
                "unique tags across all articles."
            ),
            function_signature=(
                "def all_unique_tags(articles: list[dict]) -> list[str]:"
            ),
            examples=[
                {
                    "input": (
                        "[{'title': 'A', 'tags': ['python', 'api']}, "
                        "{'title': 'B', 'tags': ['api', 'rest']}, "
                        "{'title': 'C', 'tags': ['python']}]"
                    ),
                    "output": "['api', 'python', 'rest']",
                },
            ],
            solution_code=(
                "def all_unique_tags(articles: list[dict]) -> list[str]:\n"
                "    \"\"\"Return sorted unique tags from all articles.\"\"\"\n"
                "    return sorted({tag for a in articles for tag in a.get('tags', [])})"
            ),
            test_code=(
                "articles = [\n"
                "    {'title': 'A', 'tags': ['python', 'api']},\n"
                "    {'title': 'B', 'tags': ['api', 'rest']},\n"
                "    {'title': 'C', 'tags': ['python']},\n"
                "]\n"
                "assert all_unique_tags(articles) == ['api', 'python', 'rest']\n"
                "assert all_unique_tags([]) == []\n"
                "assert all_unique_tags([{'title': 'X'}]) == []  # no tags key\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Use a set comprehension with nested iteration.",
                "Use .get('tags', []) to handle missing tags key.",
            ],
        ),
    ]

    return TopicSection(
        title="Nested JSON Data",
        difficulty="Mid-Level",
        explanation=explanation,
        examples=examples,
        practice=practice,
        key_takeaways=[
            "Use .get('key', {}) chaining for safe nested access without KeyError.",
            "A deep_get() helper simplifies access to arbitrary-depth nested keys.",
            "Flatten nested lists with: [item for sublist in nested for item in sublist].",
            "Use set comprehensions to collect unique values from nested arrays.",
            "Always use .get('key', []) when accessing list fields that may be absent.",
        ],
    )


def _building_api_test_scripts() -> TopicSection:
    explanation = (
        "### Building API Test Scripts\n\n"
        "API test scripts validate that endpoints behave correctly. "
        "They combine HTTP calls with assertions to catch regressions.\n\n"
        "**Core test patterns:**\n"
        "```python\n"
        "def test_get_user():\n"
        "    response = requests.get(f'{BASE_URL}/users/1', timeout=10)\n"
        "    assert response.status_code == 200\n"
        "    data = response.json()\n"
        "    assert 'id' in data\n"
        "    assert data['id'] == 1\n"
        "```\n\n"
        "**Mock responses for offline testing:**\n"
        "```python\n"
        "from unittest.mock import patch, Mock\n\n"
        "def test_with_mock():\n"
        "    mock_resp = Mock()\n"
        "    mock_resp.status_code = 200\n"
        "    mock_resp.json.return_value = {'id': 1, 'name': 'Alice'}\n"
        "    with patch('requests.get', return_value=mock_resp):\n"
        "        result = my_api_function()\n"
        "    assert result['name'] == 'Alice'\n"
        "```\n\n"
        "**nip-relevant patterns:**\n"
        "- **Redfish API test:** Validate server health endpoints\n"
        "- **CI/CD webhook handler:** Process build event payloads\n"
        "- **Test result reporting client:** POST results to a reporting API\n\n"
        "**HackerRank REST API patterns:**\n"
        "- Fetch all pages, filter by a condition, return count or list\n"
        "- Aggregate a numeric field (sum, average, max) across all pages\n"
        "- Join data from two endpoints (e.g., users + posts)"
    )

    examples = [
        (
            "# --- CI/CD webhook handler pattern (nip-relevant) ---\n"
            "# A webhook handler receives POST requests from CI/CD systems\n"
            "# (e.g., Jenkins, GitHub Actions) when build events occur.\n\n"
            "def handle_webhook_payload(payload: dict) -> dict:\n"
            "    \"\"\"\n"
            "    Process a CI/CD webhook payload.\n"
            "    Returns a summary dict with build status and key metadata.\n"
            "    \"\"\"\n"
            "    event_type = payload.get('event', 'unknown')\n"
            "    build = payload.get('build', {})\n\n"
            "    summary = {\n"
            "        'event': event_type,\n"
            "        'build_id': build.get('id'),\n"
            "        'status': build.get('status', 'unknown'),\n"
            "        'branch': build.get('ref', 'unknown'),\n"
            "        'duration_s': build.get('duration', 0),\n"
            "        'failed_stages': [\n"
            "            s['name'] for s in build.get('stages', [])\n"
            "            if s.get('result') == 'failed'\n"
            "        ],\n"
            "    }\n"
            "    return summary\n\n"
            "# Simulate a Jenkins/GitHub Actions webhook payload\n"
            "webhook_payload = {\n"
            "    'event': 'build_complete',\n"
            "    'build': {\n"
            "        'id': 'build-99',\n"
            "        'status': 'failed',\n"
            "        'ref': 'feature/new-driver',\n"
            "        'duration': 127,\n"
            "        'stages': [\n"
            "            {'name': 'lint',    'result': 'passed'},\n"
            "            {'name': 'test',    'result': 'failed'},\n"
            "            {'name': 'package', 'result': 'skipped'},\n"
            "        ],\n"
            "    }\n"
            "}\n\n"
            "result = handle_webhook_payload(webhook_payload)\n"
            "print(result['status'])         # 'failed'\n"
            "print(result['failed_stages'])  # ['test']"
        ),
        (
            "# --- Test result reporting API client (nip-relevant) ---\n"
            "# Posts test results to a reporting API (e.g., TestRail, custom dashboard)\n\n"
            "def format_test_results_payload(suite_name: str, results: list[dict]) -> dict:\n"
            "    \"\"\"\n"
            "    Build a payload for posting test results to a reporting API.\n"
            "    Each result dict has: 'name', 'status' ('pass'/'fail'), 'duration_ms'.\n"
            "    \"\"\"\n"
            "    passed = [r for r in results if r['status'] == 'pass']\n"
            "    failed = [r for r in results if r['status'] == 'fail']\n"
            "    return {\n"
            "        'suite': suite_name,\n"
            "        'total': len(results),\n"
            "        'passed': len(passed),\n"
            "        'failed': len(failed),\n"
            "        'pass_rate': round(len(passed) / len(results) * 100, 1) if results else 0.0,\n"
            "        'results': results,\n"
            "    }\n\n"
            "test_run = [\n"
            "    {'name': 'test_boot',    'status': 'pass', 'duration_ms': 1200},\n"
            "    {'name': 'test_network', 'status': 'fail', 'duration_ms': 3400},\n"
            "    {'name': 'test_storage', 'status': 'pass', 'duration_ms': 890},\n"
            "]\n\n"
            "payload = format_test_results_payload('HW Validation Suite', test_run)\n"
            "print(f\"Suite: {payload['suite']}\")\n"
            "print(f\"Pass rate: {payload['pass_rate']}%\")  # 66.7%"
        ),
    ]

    practice = [
        PracticeProblem(
            title="Validate API Response Schema",
            statement=(
                "Write a function that validates an API response dict against "
                "a list of required keys. Return a list of missing keys. "
                "Return an empty list if all required keys are present."
            ),
            function_signature=(
                "def validate_schema(response: dict, required_keys: list[str]) -> list[str]:"
            ),
            examples=[
                {
                    "input": "{'id': 1, 'name': 'Alice'}, ['id', 'name', 'email']",
                    "output": "['email']",
                },
                {
                    "input": "{'id': 1, 'name': 'Alice', 'email': 'a@b.com'}, ['id', 'name', 'email']",
                    "output": "[]",
                },
            ],
            solution_code=(
                "def validate_schema(response: dict, required_keys: list[str]) -> list[str]:\n"
                "    \"\"\"Return list of required keys missing from response.\"\"\"\n"
                "    return [k for k in required_keys if k not in response]"
            ),
            test_code=(
                "assert validate_schema({'id': 1, 'name': 'Alice'}, ['id', 'name', 'email']) == ['email']\n"
                "assert validate_schema({'id': 1, 'name': 'Alice', 'email': 'a@b.com'}, ['id', 'name', 'email']) == []\n"
                "assert validate_schema({}, ['id', 'name']) == ['id', 'name']\n"
                "assert validate_schema({'x': 1}, []) == []\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Use a list comprehension: [k for k in required_keys if k not in response].",
            ],
        ),
        PracticeProblem(
            title="Build Test Result Report",
            statement=(
                "Given a list of test result dicts (each with 'name', "
                "'status' ('pass'/'fail'/'skip'), and 'duration_ms'), "
                "return a summary dict with 'total', 'passed', 'failed', "
                "'skipped', and 'pass_rate' (float, percentage rounded to 1 decimal). "
                "pass_rate = passed / (passed + failed) * 100, or 0.0 if no pass/fail."
            ),
            function_signature=(
                "def build_report(results: list[dict]) -> dict:"
            ),
            examples=[
                {
                    "input": (
                        "[{'name': 'A', 'status': 'pass', 'duration_ms': 100}, "
                        "{'name': 'B', 'status': 'fail', 'duration_ms': 200}, "
                        "{'name': 'C', 'status': 'skip', 'duration_ms': 0}]"
                    ),
                    "output": "{'total': 3, 'passed': 1, 'failed': 1, 'skipped': 1, 'pass_rate': 50.0}",
                },
            ],
            solution_code=(
                "def build_report(results: list[dict]) -> dict:\n"
                "    \"\"\"Build a test result summary report.\"\"\"\n"
                "    passed  = sum(1 for r in results if r['status'] == 'pass')\n"
                "    failed  = sum(1 for r in results if r['status'] == 'fail')\n"
                "    skipped = sum(1 for r in results if r['status'] == 'skip')\n"
                "    denominator = passed + failed\n"
                "    pass_rate = round(passed / denominator * 100, 1) if denominator else 0.0\n"
                "    return {\n"
                "        'total':     len(results),\n"
                "        'passed':    passed,\n"
                "        'failed':    failed,\n"
                "        'skipped':   skipped,\n"
                "        'pass_rate': pass_rate,\n"
                "    }"
            ),
            test_code=(
                "results = [\n"
                "    {'name': 'A', 'status': 'pass', 'duration_ms': 100},\n"
                "    {'name': 'B', 'status': 'fail', 'duration_ms': 200},\n"
                "    {'name': 'C', 'status': 'skip', 'duration_ms': 0},\n"
                "]\n"
                "report = build_report(results)\n"
                "assert report['total'] == 3\n"
                "assert report['passed'] == 1\n"
                "assert report['failed'] == 1\n"
                "assert report['skipped'] == 1\n"
                "assert report['pass_rate'] == 50.0\n"
                "assert build_report([])['pass_rate'] == 0.0\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Use sum() with generator expressions to count each status.",
                "Guard against division by zero when computing pass_rate.",
            ],
        ),
        PracticeProblem(
            title="Redfish API — Query Server Health Across a Fleet",
            statement=(
                "**NVIDIA SDET context:** Redfish is the REST API for server "
                "hardware management (BMC/iDRAC/iLO). It follows standard HTTP "
                "conventions and returns JSON.\n\n"
                "Given a list of Redfish System resource dicts (simulating "
                "GET /redfish/v1/Systems/{id} responses), write a function "
                "`fleet_health_summary(systems)` that returns a dict with:\n"
                "- `'total'`: total system count\n"
                "- `'healthy'`: count where Status.Health == 'OK'\n"
                "- `'degraded'`: count where Status.Health == 'Warning'\n"
                "- `'critical'`: count where Status.Health == 'Critical'\n"
                "- `'powered_on'`: count where PowerState == 'On'\n"
                "- `'unhealthy_ids'`: list of system IDs where Health != 'OK'"
            ),
            function_signature="def fleet_health_summary(systems: list[dict]) -> dict:",
            examples=[
                {
                    "input": (
                        "[{'Id': 'sys1', 'PowerState': 'On', 'Status': {'Health': 'OK'}}, "
                        "{'Id': 'sys2', 'PowerState': 'On', 'Status': {'Health': 'Warning'}}, "
                        "{'Id': 'sys3', 'PowerState': 'Off', 'Status': {'Health': 'Critical'}}]"
                    ),
                    "output": "{'total': 3, 'healthy': 1, 'degraded': 1, 'critical': 1, 'powered_on': 2, 'unhealthy_ids': ['sys2', 'sys3']}",
                },
            ],
            solution_code=(
                "def fleet_health_summary(systems: list[dict]) -> dict:\n"
                "    \"\"\"Summarise Redfish system health across a server fleet.\"\"\"\n"
                "    summary = {'total': len(systems), 'healthy': 0, 'degraded': 0,\n"
                "               'critical': 0, 'powered_on': 0, 'unhealthy_ids': []}\n"
                "    for s in systems:\n"
                "        health = s.get('Status', {}).get('Health', 'Unknown')\n"
                "        if health == 'OK':\n"
                "            summary['healthy'] += 1\n"
                "        elif health == 'Warning':\n"
                "            summary['degraded'] += 1\n"
                "            summary['unhealthy_ids'].append(s.get('Id', 'unknown'))\n"
                "        else:\n"
                "            summary['critical'] += 1\n"
                "            summary['unhealthy_ids'].append(s.get('Id', 'unknown'))\n"
                "        if s.get('PowerState') == 'On':\n"
                "            summary['powered_on'] += 1\n"
                "    return summary"
            ),
            test_code=(
                "systems = [\n"
                "    {'Id': 'sys1', 'PowerState': 'On',  'Status': {'Health': 'OK'}},\n"
                "    {'Id': 'sys2', 'PowerState': 'On',  'Status': {'Health': 'Warning'}},\n"
                "    {'Id': 'sys3', 'PowerState': 'Off', 'Status': {'Health': 'Critical'}},\n"
                "    {'Id': 'sys4', 'PowerState': 'On',  'Status': {'Health': 'OK'}},\n"
                "]\n"
                "result = fleet_health_summary(systems)\n"
                "assert result['total'] == 4\n"
                "assert result['healthy'] == 2\n"
                "assert result['degraded'] == 1\n"
                "assert result['critical'] == 1\n"
                "assert result['powered_on'] == 3\n"
                "assert set(result['unhealthy_ids']) == {'sys2', 'sys3'}\n"
                "assert fleet_health_summary([])['total'] == 0\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Use .get('Status', {}).get('Health', 'Unknown') for safe nested access.",
                "Append to unhealthy_ids for both Warning and Critical health states.",
            ],
        ),
    ]

    return TopicSection(
        title="Building API Test Scripts",
        difficulty="Mid-Level",
        explanation=explanation,
        examples=examples,
        practice=practice,
        key_takeaways=[
            "API test scripts combine HTTP calls with assertions to validate behavior.",
            "Use mock data or unittest.mock.patch for offline/unit testing.",
            "CI/CD webhook handlers parse build event payloads and extract key fields.",
            "Test result reporting clients format and POST results to dashboards.",
            "HackerRank REST problems: fetch all pages, filter/aggregate, return result.",
        ],
    )


# ---------------------------------------------------------------------------
# Mock test
# ---------------------------------------------------------------------------

def _mock_test() -> list[PracticeProblem]:
    return [
        PracticeProblem(
            title="Fetch and Filter Paginated Users",
            statement=(
                "**Timed Problem — target: ~8 minutes**\n\n"
                "You are given a function `get_page(page: int) -> list[dict]` "
                "that returns a page of user dicts. Each user has 'id' (int), "
                "'name' (str), 'active' (bool), and 'score' (float). "
                "The function returns an empty list when there are no more pages.\n\n"
                "Write a function `top_active_users(get_page, n: int) -> list[str]` "
                "that fetches ALL pages, filters to active users only, and "
                "returns the names of the top `n` users by score (highest first)."
            ),
            function_signature=(
                "def top_active_users(get_page, n: int) -> list[str]:"
            ),
            examples=[
                {
                    "input": (
                        "get_page returning pages of users, n=2"
                    ),
                    "output": "['Alice', 'Carol']  # top 2 active users by score",
                },
            ],
            solution_code=(
                "def top_active_users(get_page, n: int) -> list[str]:\n"
                "    \"\"\"Fetch all pages, filter active users, return top n by score.\"\"\"\n"
                "    all_users = []\n"
                "    page = 1\n"
                "    while True:\n"
                "        users = get_page(page)\n"
                "        if not users:\n"
                "            break\n"
                "        all_users.extend(users)\n"
                "        page += 1\n"
                "    active = [u for u in all_users if u.get('active')]\n"
                "    active.sort(key=lambda u: u['score'], reverse=True)\n"
                "    return [u['name'] for u in active[:n]]"
            ),
            test_code=(
                "pages_data = [\n"
                "    [\n"
                "        {'id': 1, 'name': 'Alice', 'active': True,  'score': 95.0},\n"
                "        {'id': 2, 'name': 'Bob',   'active': False, 'score': 88.0},\n"
                "    ],\n"
                "    [\n"
                "        {'id': 3, 'name': 'Carol', 'active': True,  'score': 91.0},\n"
                "        {'id': 4, 'name': 'Dave',  'active': True,  'score': 72.0},\n"
                "    ],\n"
                "    [],  # end of pages\n"
                "]\n"
                "def get_page(p): return pages_data[p - 1] if p <= len(pages_data) else []\n\n"
                "assert top_active_users(get_page, 2) == ['Alice', 'Carol']\n"
                "assert top_active_users(get_page, 1) == ['Alice']\n"
                "assert top_active_users(get_page, 10) == ['Alice', 'Carol', 'Dave']\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Step 1: Fetch all pages with a while loop (break on empty list).",
                "Step 2: Filter to active=True users.",
                "Step 3: Sort by score descending, slice to n, extract names.",
            ],
        ),
        PracticeProblem(
            title="Aggregate API Metrics Across Pages",
            statement=(
                "**Timed Problem — target: ~9 minutes**\n\n"
                "You are given a function `get_metrics_page(page: int) -> list[dict]` "
                "that returns pages of API call records. Each record has "
                "'endpoint' (str), 'status_code' (int), and 'response_time_ms' (float). "
                "Returns empty list when done.\n\n"
                "Write `api_summary(get_metrics_page) -> dict` that fetches all "
                "pages and returns:\n"
                "- `'total_calls'`: total number of records\n"
                "- `'error_rate'`: percentage of calls with status >= 400 (rounded to 1 decimal)\n"
                "- `'avg_response_ms'`: average response time in ms (rounded to 1 decimal)\n"
                "- `'slowest_endpoint'`: endpoint with highest average response time\n\n"
                "Return `{'total_calls': 0, 'error_rate': 0.0, 'avg_response_ms': 0.0, "
                "'slowest_endpoint': None}` for empty data."
            ),
            function_signature=(
                "def api_summary(get_metrics_page) -> dict:"
            ),
            examples=[
                {
                    "input": "get_metrics_page returning 2 pages of records",
                    "output": "{'total_calls': 4, 'error_rate': 25.0, 'avg_response_ms': 175.0, 'slowest_endpoint': '/api/data'}",
                },
            ],
            solution_code=(
                "def api_summary(get_metrics_page) -> dict:\n"
                "    \"\"\"Aggregate API metrics across all pages.\"\"\"\n"
                "    all_records = []\n"
                "    page = 1\n"
                "    while True:\n"
                "        records = get_metrics_page(page)\n"
                "        if not records:\n"
                "            break\n"
                "        all_records.extend(records)\n"
                "        page += 1\n\n"
                "    if not all_records:\n"
                "        return {'total_calls': 0, 'error_rate': 0.0,\n"
                "                'avg_response_ms': 0.0, 'slowest_endpoint': None}\n\n"
                "    total = len(all_records)\n"
                "    errors = sum(1 for r in all_records if r['status_code'] >= 400)\n"
                "    error_rate = round(errors / total * 100, 1)\n"
                "    avg_rt = round(sum(r['response_time_ms'] for r in all_records) / total, 1)\n\n"
                "    # Slowest endpoint by average response time\n"
                "    ep_times: dict[str, list[float]] = {}\n"
                "    for r in all_records:\n"
                "        ep_times.setdefault(r['endpoint'], []).append(r['response_time_ms'])\n"
                "    ep_avgs = {ep: sum(ts) / len(ts) for ep, ts in ep_times.items()}\n"
                "    slowest = max(ep_avgs, key=ep_avgs.get)\n\n"
                "    return {\n"
                "        'total_calls': total,\n"
                "        'error_rate': error_rate,\n"
                "        'avg_response_ms': avg_rt,\n"
                "        'slowest_endpoint': slowest,\n"
                "    }"
            ),
            test_code=(
                "pages = [\n"
                "    [\n"
                "        {'endpoint': '/api/users', 'status_code': 200, 'response_time_ms': 100.0},\n"
                "        {'endpoint': '/api/data',  'status_code': 200, 'response_time_ms': 300.0},\n"
                "    ],\n"
                "    [\n"
                "        {'endpoint': '/api/users', 'status_code': 404, 'response_time_ms': 50.0},\n"
                "        {'endpoint': '/api/data',  'status_code': 200, 'response_time_ms': 250.0},\n"
                "    ],\n"
                "    [],\n"
                "]\n"
                "def get_page(p): return pages[p - 1] if p <= len(pages) else []\n\n"
                "result = api_summary(get_page)\n"
                "assert result['total_calls'] == 4\n"
                "assert result['error_rate'] == 25.0\n"
                "assert result['avg_response_ms'] == 175.0\n"
                "assert result['slowest_endpoint'] == '/api/data'\n"
                "assert api_summary(lambda p: [])['total_calls'] == 0\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Step 1: Collect all records with a pagination loop.",
                "Step 2: Count errors (status >= 400) and compute error_rate.",
                "Step 3: Compute avg_response_ms across all records.",
                "Step 4: Group response times by endpoint, compute averages, find max.",
            ],
        ),
        PracticeProblem(
            title="Join Users and Posts from Paginated APIs",
            statement=(
                "**Timed Problem — target: ~8 minutes**\n\n"
                "You have two data sources (simulated as lists):\n"
                "- `users`: list of dicts with 'id' and 'name'\n"
                "- `posts`: list of dicts with 'id', 'userId', and 'title'\n\n"
                "Write `user_post_counts(users, posts) -> list[dict]` that "
                "returns a list of dicts with 'name' and 'post_count' for "
                "each user, sorted by post_count descending. Users with 0 "
                "posts should be included."
            ),
            function_signature=(
                "def user_post_counts(users: list[dict], posts: list[dict]) -> list[dict]:"
            ),
            examples=[
                {
                    "input": (
                        "users=[{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}], "
                        "posts=[{'id': 1, 'userId': 1, 'title': 'A'}, "
                        "{'id': 2, 'userId': 1, 'title': 'B'}, "
                        "{'id': 3, 'userId': 2, 'title': 'C'}]"
                    ),
                    "output": "[{'name': 'Alice', 'post_count': 2}, {'name': 'Bob', 'post_count': 1}]",
                },
            ],
            solution_code=(
                "def user_post_counts(users: list[dict], posts: list[dict]) -> list[dict]:\n"
                "    \"\"\"Return users with their post counts, sorted by count descending.\"\"\"\n"
                "    # Build a count map: userId -> count\n"
                "    counts: dict[int, int] = {}\n"
                "    for post in posts:\n"
                "        uid = post['userId']\n"
                "        counts[uid] = counts.get(uid, 0) + 1\n\n"
                "    result = [\n"
                "        {'name': u['name'], 'post_count': counts.get(u['id'], 0)}\n"
                "        for u in users\n"
                "    ]\n"
                "    result.sort(key=lambda x: x['post_count'], reverse=True)\n"
                "    return result"
            ),
            test_code=(
                "users = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}, {'id': 3, 'name': 'Carol'}]\n"
                "posts = [\n"
                "    {'id': 1, 'userId': 1, 'title': 'A'},\n"
                "    {'id': 2, 'userId': 1, 'title': 'B'},\n"
                "    {'id': 3, 'userId': 2, 'title': 'C'},\n"
                "]\n"
                "result = user_post_counts(users, posts)\n"
                "assert result[0] == {'name': 'Alice', 'post_count': 2}\n"
                "assert result[1] == {'name': 'Bob',   'post_count': 1}\n"
                "assert result[2] == {'name': 'Carol', 'post_count': 0}\n"
                "assert user_post_counts([], []) == []\n"
                "print('All tests passed!')"
            ),
            hints=[
                "Build a userId -> count dict from the posts list.",
                "Use counts.get(user_id, 0) to handle users with no posts.",
                "Sort the result list by post_count descending.",
            ],
        ),
    ]


# ---------------------------------------------------------------------------
# Cheat sheet
# ---------------------------------------------------------------------------

def _cheat_sheet() -> str:
    return (
        "## REST API Coding — Quick Reference Cheat Sheet\n\n"
        "---\n\n"
        "### HTTP Status Codes\n\n"
        "| Code | Name | Meaning |\n"
        "|------|------|---------|\n"
        "| 200  | OK | Request succeeded |\n"
        "| 201  | Created | Resource created (POST) |\n"
        "| 204  | No Content | Success, no body (DELETE) |\n"
        "| 301  | Moved Permanently | Redirect |\n"
        "| 304  | Not Modified | Cached response still valid |\n"
        "| 400  | Bad Request | Invalid request syntax/params |\n"
        "| 401  | Unauthorized | Not authenticated |\n"
        "| 403  | Forbidden | Authenticated but not permitted |\n"
        "| 404  | Not Found | Resource doesn't exist |\n"
        "| 429  | Too Many Requests | Rate limited — back off |\n"
        "| 500  | Internal Server Error | Server-side bug |\n"
        "| 502  | Bad Gateway | Upstream server error |\n"
        "| 503  | Service Unavailable | Server overloaded/down |\n"
        "| 504  | Gateway Timeout | Upstream timeout |\n\n"
        "---\n\n"
        "### Common `requests` Patterns\n\n"
        "```python\n"
        "import requests\n\n"
        "# GET with query params\n"
        "r = requests.get(url, params={'page': 1, 'limit': 20}, timeout=10)\n\n"
        "# POST with JSON body\n"
        "r = requests.post(url, json={'key': 'value'}, timeout=10)\n\n"
        "# PUT (replace resource)\n"
        "r = requests.put(url, json={'key': 'new_value'}, timeout=10)\n\n"
        "# DELETE\n"
        "r = requests.delete(url, timeout=10)\n\n"
        "# With auth headers\n"
        "headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}\n"
        "r = requests.get(url, headers=headers, timeout=10)\n\n"
        "# Check response\n"
        "if r.status_code == 200:\n"
        "    data = r.json()   # dict or list\n"
        "r.raise_for_status()  # raises HTTPError for 4xx/5xx\n"
        "```\n\n"
        "---\n\n"
        "### JSON Handling\n\n"
        "```python\n"
        "import json\n\n"
        "# Parse JSON string\n"
        "data = json.loads(json_string)\n\n"
        "# Serialize to JSON string\n"
        "s = json.dumps(data, indent=2)\n\n"
        "# Safe nested access\n"
        "val = data.get('key', {}).get('nested', 'default')\n\n"
        "# Deep get helper\n"
        "def deep_get(d, *keys, default=None):\n"
        "    for k in keys:\n"
        "        if not isinstance(d, dict): return default\n"
        "        d = d.get(k, default)\n"
        "        if d is default: return default\n"
        "    return d\n"
        "```\n\n"
        "---\n\n"
        "### Pagination Patterns\n\n"
        "```python\n"
        "# Page-based (most common in HackerRank)\n"
        "all_items, page = [], 1\n"
        "while True:\n"
        "    items = get_page(page)   # returns [] on last page\n"
        "    if not items: break\n"
        "    all_items.extend(items)\n"
        "    page += 1\n\n"
        "# Offset-based\n"
        "all_items, offset, limit = [], 0, 20\n"
        "while True:\n"
        "    items = get_items(offset=offset, limit=limit)\n"
        "    if not items: break\n"
        "    all_items.extend(items)\n"
        "    offset += limit\n\n"
        "# Cursor-based\n"
        "all_items, cursor = [], None\n"
        "while True:\n"
        "    data = get_data(cursor=cursor)\n"
        "    all_items.extend(data['items'])\n"
        "    cursor = data.get('next_cursor')\n"
        "    if not cursor: break\n"
        "```\n\n"
        "---\n\n"
        "### Common HackerRank REST API Patterns\n\n"
        "**Pattern 1: Filter paginated results**\n"
        "```python\n"
        "# Fetch all pages, filter by condition, return matching items\n"
        "def get_active_users(get_page):\n"
        "    all_users, page = [], 1\n"
        "    while True:\n"
        "        users = get_page(page)\n"
        "        if not users: break\n"
        "        all_users.extend(users)\n"
        "        page += 1\n"
        "    return [u for u in all_users if u.get('active')]\n"
        "```\n\n"
        "**Pattern 2: Aggregate across all pages**\n"
        "```python\n"
        "# Fetch all pages, compute sum/average/max\n"
        "def total_score(get_page):\n"
        "    total, page = 0, 1\n"
        "    while True:\n"
        "        items = get_page(page)\n"
        "        if not items: break\n"
        "        total += sum(item['score'] for item in items)\n"
        "        page += 1\n"
        "    return total\n"
        "```\n\n"
        "**Pattern 3: Join two endpoints**\n"
        "```python\n"
        "# Build lookup from one endpoint, enrich with another\n"
        "user_map = {u['id']: u['name'] for u in fetch_all_users()}\n"
        "posts = fetch_all_posts()\n"
        "enriched = [{**p, 'author': user_map.get(p['userId'], 'Unknown')} for p in posts]\n"
        "```\n\n"
        "**Pattern 4: Top-N from paginated data**\n"
        "```python\n"
        "# Fetch all, sort, slice\n"
        "all_items = fetch_all_pages(get_page)\n"
        "top_n = sorted(all_items, key=lambda x: x['score'], reverse=True)[:n]\n"
        "```\n\n"
        "---\n\n"
        "### Authentication Quick Reference\n\n"
        "```python\n"
        "# Bearer token\n"
        "headers = {'Authorization': f'Bearer {token}'}\n\n"
        "# API key in header\n"
        "headers = {'X-API-Key': api_key}\n\n"
        "# Basic auth\n"
        "import requests\n"
        "r = requests.get(url, auth=('username', 'password'))\n\n"
        "# Redfish (Basic auth)\n"
        "r = requests.get(\n"
        "    'https://bmc-host/redfish/v1/Systems',\n"
        "    auth=('admin', 'password'),\n"
        "    verify=False,  # self-signed cert in lab\n"
        "    timeout=10\n"
        ")\n"
        "```\n\n"
        "---\n\n"
        "### Error Handling Template\n\n"
        "```python\n"
        "def safe_get(url, headers=None, params=None, max_retries=3):\n"
        "    retryable = {429, 500, 502, 503, 504}\n"
        "    for attempt in range(max_retries):\n"
        "        try:\n"
        "            r = requests.get(url, headers=headers, params=params, timeout=10)\n"
        "            if r.status_code == 200:\n"
        "                return r.json()\n"
        "            if r.status_code not in retryable:\n"
        "                raise ValueError(f'HTTP {r.status_code}')\n"
        "        except requests.Timeout:\n"
        "            pass  # retry on timeout\n"
        "    raise RuntimeError(f'Failed after {max_retries} attempts')\n"
        "```"
    )
