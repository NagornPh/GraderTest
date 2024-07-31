import json

def load_problem(problem_id):
    with open(f'problems/{problem_id}.json', 'r') as f:
        return json.load(f)

def load_test_cases(problem_id):
    with open(f'test_cases/{problem_id}_test_cases.json', 'r') as f:
        return json.load(f)

def execute_user_code(user_code, func_name, test_cases):
    results = []
    exec_globals = {}
    exec(user_code, exec_globals)
    func = exec_globals[func_name]
    
    for case in test_cases:
        try:
            result = func(case["input"])
            passed = result == case["expected_output"]
            results.append({"input": case["input"], "expected": case["expected_output"], "output": result, "passed": passed})
        except Exception as e:
            results.append({"input": case["input"], "expected": case["expected_output"], "output": str(e), "passed": False})
    
    return results
