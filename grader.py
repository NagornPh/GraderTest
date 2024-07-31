import json
import os

def load_problem(problem_id):
    base_path = os.path.dirname(__file__)
    problem_path = os.path.join(base_path, 'Problems', f'{problem_id}.json')
    if not os.path.exists(problem_path):
        raise FileNotFoundError(f'Problem file not found: {problem_path}')
    with open(problem_path, 'r') as f:
        return json.load(f)

def load_test_cases(problem_id):
    base_path = os.path.dirname(__file__)
    test_case_path = os.path.join(base_path, 'Problems', f'{problem_id}_test_cases.json')
    if not os.path.exists(test_case_path):
        raise FileNotFoundError(f'Test case file not found: {test_case_path}')
    with open(test_case_path, 'r') as f:
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
