import streamlit as st
import json
from grader import load_problem, load_test_cases, execute_user_code

# Load available problems
problems = {
    "problem1": "Modulo Operation Problem",
    "problem2": "Another Problem"
}

st.title("Grader Website")

st.sidebar.title("Select a Problem")
problem_id = st.sidebar.selectbox("Problem", list(problems.keys()), format_func=lambda x: problems[x])

problem = load_problem(problem_id)
test_cases = load_test_cases(problem_id)

st.header(problem["title"])
st.write(problem["description"])

user_code = st.text_area("Write your code here", height=200, value=f'{problem["function_definition"]}\n    pass')

if st.button("Submit"):
    with st.spinner("Grading..."):
        results = execute_user_code(user_code, problem["function_name"], test_cases)
        st.success("Grading complete!")

    st.write("## Results")
    for result in results:
        st.write(f"Input: {result['input']}")
        st.write(f"Expected Output: {result['expected']}")
        st.write(f"Your Output: {result['output']}")
        st.write(f"Passed: {'✅' if result['passed'] else '❌'}")
        st.write("---")

st.sidebar.write("### Constraints")
st.sidebar.write(problem["constraints"])
