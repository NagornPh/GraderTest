import streamlit as st
import os
import subprocess
from tempfile import NamedTemporaryFile

# Problem configurations
PROBLEMS = {
    "Pointing": {
        "description_file": "Problems/Pointing/Pointing.pdf",
        "folder": "Problems/Pointing"
    },
    "Stonks": {
        "description_file": "Problems/Stonks/Stonks.pdf",
        "folder": "Problems/Stonks"
    }
}

def run_cpp_code(cpp_code, input_data):
    # Write the code to a temporary file
    with NamedTemporaryFile(delete=False, suffix=".cpp") as cpp_file:
        cpp_file.write(cpp_code.encode('utf-8'))
        cpp_file_path = cpp_file.name

    # Compile the C++ code
    exe_file_path = cpp_file_path.replace('.cpp', '')
    compile_process = subprocess.run(['g++', cpp_file_path, '-o', exe_file_path], capture_output=True, text=True)
    
    if compile_process.returncode != 0:
        return compile_process.stderr, None

    # Run the compiled code with input_data
    run_process = subprocess.run([exe_file_path], input=input_data, capture_output=True, text=True)

    # Clean up the temporary files
    os.remove(cpp_file_path)
    os.remove(exe_file_path)

    return None, run_process.stdout.strip()

def grade_problem(problem_folder, cpp_code):
    results = []

    for i in range(1, 11):
        input_file = os.path.join(problem_folder, f"{i}.in")
        output_file = os.path.join(problem_folder, f"{i}.out")

        with open(input_file, 'r') as f:
            input_data = f.read()

        with open(output_file, 'r') as f:
            expected_output = f.read().strip()

        error, user_output = run_cpp_code(cpp_code, input_data)
        
        if error:
            results.append((i, False, error))
        else:
            passed = user_output == expected_output
            results.append((i, passed, user_output, expected_output))
    
    return results

# Streamlit app
st.title("Grader Website")

tab1, tab2 = st.tabs(["Pointing", "Stonks"])

def display_results(results):
    num_passed = sum(result[1] for result in results)
    score = num_passed * 10
    percentage_score = (num_passed / 10) * 100

    st.markdown(f"## Results", unsafe_allow_html=True)
    st.markdown(f"**Score: {score} / 100**", unsafe_allow_html=True)
    st.markdown(f"**Percentage: {percentage_score:.2f}%**", unsafe_allow_html=True)
    
    st.markdown("### Detailed Results", unsafe_allow_html=True)
    for idx, result in enumerate(results):
        if result[1]:
            st.write(f"**Test case {result[0]}:** ✅ Passed")
        else:
            st.write(f"**Test case {result[0]}:** ❌ Failed")
            st.write(f"**Expected:** {result[3]}")
            st.write(f"**Got:** {result[2]}")

with tab1:
    st.header("Pointing Problem")
    
    with open(PROBLEMS["Pointing"]["description_file"], "rb") as f:
        pointing_description = f.read()
    
    st.download_button(
        label="Download Pointing Problem Statement",
        data=pointing_description,
        file_name="Pointing.pdf",
        mime="application/pdf"
    )

    cpp_code = st.text_area("Paste your C++ code here", height=300)
    uploaded_file = st.file_uploader("Or upload a C++ file", type=["cpp"], key="pointing_upload")

    if uploaded_file is not None:
        cpp_code = uploaded_file.read().decode("utf-8")

    if st.button("Submit Code", key="pointing_submit"):
        if not cpp_code:
            st.warning("Please provide your C++ code.")
        else:
            with st.spinner("Grading..."):
                results = grade_problem(PROBLEMS["Pointing"]["folder"], cpp_code)
            st.success("Grading complete!")
            display_results(results)

with tab2:
    st.header("Stonks Problem")
    
    with open(PROBLEMS["Stonks"]["description_file"], "rb") as f:
        stonks_description = f.read()
    
    st.download_button(
        label="Download Stonks Problem Statement",
        data=stonks_description,
        file_name="Stonks.pdf",
        mime="application/pdf"
    )

    cpp_code = st.text_area("Paste your C++ code here", height=300, key="stonks_code")
    uploaded_file = st.file_uploader("Or upload a C++ file", type=["cpp"], key="stonks_upload")

    if uploaded_file is not None:
        cpp_code = uploaded_file.read().decode("utf-8")

    if st.button("Submit Code", key="stonks_submit"):
        if not cpp_code:
            st.warning("Please provide your C++ code.")
        else:
            with st.spinner("Grading..."):
                results = grade_problem(PROBLEMS["Stonks"]["folder"], cpp_code)
            st.success("Grading complete!")
            display_results(results)
